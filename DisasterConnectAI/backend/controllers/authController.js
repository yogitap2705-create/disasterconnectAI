const User = require("../models/users");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const sendEmail = require("../utils/sendEmail");

// Register
exports.register = async (req, res) => {
  try {
    const { fullName, email, password, role, district, phone, skills } = req.body;

    const existingUser = await User.findOne({ email });

    if (existingUser) {
      return res.status(400).json({
        message: "User already exists",
      });
    }

    const hashedPassword = await bcrypt.hash(password, 10);

    const user = await User.create({
      fullName,
      email,
      password: hashedPassword,
      role: role || "citizen",
      district: district || "Pune",
      phone: phone || "",
      skills: Array.isArray(skills) ? skills : [skills || "Emergency First Responder"],
    });

    // Send welcome email (asynchronous & non-blocking)
    sendEmail({
      to: user.email,
      subject: "Welcome to DisasterConnect AI",
      text: `Hello ${user.fullName},\n\nWelcome to DisasterConnect AI! You have registered as a ${user.role} (District: ${user.district}).\n\nStay safe and connected.\n\nDisasterConnect AI Team`,
      html: `
        <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden;">
          <div style="background-color: #800020; color: #ffffff; padding: 18px 24px;">
            <h2 style="margin: 0;">DisasterConnect AI</h2>
          </div>
          <div style="padding: 24px;">
            <p>Hello <strong>${user.fullName}</strong>,</p>
            <p>Welcome to <strong>DisasterConnect AI</strong>! Your account has been registered successfully as a <strong>${user.role}</strong> (District: <strong>${user.district}</strong>).</p>
            <p>You can now report disasters, view real-time incident maps, and coordinate life-saving relief.</p>
            <p style="margin-top: 24px; font-size: 13px; color: #777;">Stay safe,<br/>— DisasterConnect AI Team</p>
          </div>
        </div>
      `,
    }).catch((err) => console.error("Welcome email error:", err.message));

    res.status(201).json({
      message: "Registration Successful",
      user,
    });
  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

// Login
exports.login = async (req, res) => {
  try {
    const { email, password } = req.body;

    let user = await User.findOne({ email });

    // Auto-provision Admin account on first attempt if demo admin is requested
    if (!user && (email === "admin@disasterconnect.ai" || email === "admin@emergency.gov.in")) {
      const hashedPassword = await bcrypt.hash(password || "admin123", 10);
      user = await User.create({
        fullName: "Command Center Administrator",
        email: email,
        password: hashedPassword,
        role: "admin",
        district: "All Maharashtra",
      });
    }

    if (!user) {
      return res.status(400).json({
        message: "User not found with this email",
      });
    }

    const isMatch = await bcrypt.compare(password, user.password);

    if (!isMatch) {
      return res.status(400).json({
        message: "Invalid Password",
      });
    }

    const token = jwt.sign(
      {
        id: user._id,
        role: user.role,
      },
      process.env.JWT_SECRET || "disasterconnect_secret",
      {
        expiresIn: "7d",
      }
    );

    res.status(200).json({
      message: "Login Successful",
      token,
      user,
    });

  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

// Get All Users
exports.getAllUsers = async (req, res) => {
  try {
    const users = await User.find().select("-password");
    res.status(200).json(users);
  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

// Get Volunteers (with District, Phone, Skills)
exports.getVolunteers = async (req, res) => {
  try {
    const volunteers = await User.find(
      { role: "volunteer" },
      "fullName email district phone skills"
    );
    res.status(200).json(volunteers);
  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};