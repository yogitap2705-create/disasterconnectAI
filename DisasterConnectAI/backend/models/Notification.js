const mongoose = require("mongoose");

const notificationSchema = new mongoose.Schema(
  {
    recipient: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
    },
    recipientEmail: {
      type: String,
      required: true,
    },
    recipientName: {
      type: String,
      default: "Recipient",
    },
    subject: {
      type: String,
      required: true,
    },
    messageText: {
      type: String,
      default: "",
    },
    messageHtml: {
      type: String,
      default: "",
    },
    notificationType: {
      type: String,
      enum: [
        "volunteer_assignment",
        "citizen_advisory",
        "incident_resolution",
        "system_broadcast",
      ],
      default: "volunteer_assignment",
    },
    disasterId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Disaster",
    },
    deliveryStatus: {
      type: String,
      enum: ["delivered_in_app", "sent_smtp", "failed_smtp", "ethereal_preview"],
      default: "delivered_in_app",
    },
    smtpMessageId: {
      type: String,
      default: "",
    },
    previewUrl: {
      type: String,
      default: "",
    },
    read: {
      type: Boolean,
      default: false,
    },
    acknowledged: {
      type: Boolean,
      default: false,
    },
    acknowledgedAt: {
      type: Date,
    },
    createdAt: {
      type: Date,
      default: Date.now,
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model("Notification", notificationSchema);
