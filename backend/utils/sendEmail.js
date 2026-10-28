
const nodemailer = require("nodemailer");
const Notification = require("../models/Notification");

const sendEmail = async ({
  to,
  subject,
  text,
  html,
  recipientId,
  recipientName = "User",
  notificationType = "citizen_advisory",
  disasterId,
}) => {
  let notificationRecord = null;

  // Validate recipient
  if (!to) {
    console.error("[Email Error] Recipient email is missing.");

    return {
      success: false,
      deliveryStatus: "failed",
      error: "Recipient email is missing",
    };
  }

  // 1. Save the notification in MongoDB
  try {
    notificationRecord = await Notification.create({
      recipient: recipientId || null,
      recipientEmail: to,
      recipientName,
      subject,
      messageText: text || "",
      messageHtml: html || text || "",
      notificationType,
      disasterId: disasterId || null,
      deliveryStatus: "pending",
    });

    console.log(
      "[Notification] Saved to database:",
      notificationRecord._id
    );
  } catch (dbError) {
    console.error(
      "[Notification Database Error]:",
      dbError.message
    );
  }

  // 2. Read Gmail credentials from backend .env
  const email = process.env.EMAIL;
  const password = process.env.EMAIL_PASSWORD;

  // 3. Send a real email through Gmail
  if (
    email &&
    password &&
    email !== "your-email@gmail.com" &&
    password !== "your_16_character_gmail_app_password"
  ) {
    let transporter;

    try {
      transporter = nodemailer.createTransport({
        service: "gmail",
        auth: {
          user: email,
          pass: password,
        },
        connectionTimeout: 10000,
        greetingTimeout: 10000,
        socketTimeout: 20000,
      });

      // Verify the SMTP connection and credentials
      await transporter.verify();

      console.log("[Email] Gmail SMTP connection successful.");

      const info = await transporter.sendMail({
        from: `"DisasterConnect AI" <${email}>`,
        to,
        subject,
        text: text || "",
        html: html || undefined,
      });

      console.log(
        `[Email] SMTP accepted message for ${to}. Message ID: ${info.messageId}`
      );

      if (notificationRecord) {
        notificationRecord.deliveryStatus = "sent_smtp";
        notificationRecord.smtpMessageId = info.messageId;
        await notificationRecord.save();
      }

      return {
        success: true,
        deliveryStatus: "sent_smtp",
        messageId: info.messageId,
        notificationId: notificationRecord?._id,
      };
    } catch (smtpError) {
      console.error(
        "[Gmail SMTP Error]:",
        smtpError.message
      );

      if (notificationRecord) {
        try {
          notificationRecord.deliveryStatus = "failed_smtp";
          await notificationRecord.save();
        } catch (saveError) {
          console.error(
            "[Notification Update Error]:",
            saveError.message
          );
        }
      }

      return {
        success: false,
        deliveryStatus: "failed_smtp",
        error: smtpError.message,
        notificationId: notificationRecord?._id,
      };
    } finally {
      if (transporter) {
        transporter.close();
      }
    }
  }

  // 4. Credentials missing: save in-app notification only
  console.error(
    "[Email Error] EMAIL or EMAIL_PASSWORD is missing or still a placeholder in backend .env."
  );

  return {
    success: false,
    deliveryStatus: "delivered_in_app",
    error: "Gmail credentials are not configured",
    notificationId: notificationRecord?._id,
  };
};

module.exports = sendEmail;
