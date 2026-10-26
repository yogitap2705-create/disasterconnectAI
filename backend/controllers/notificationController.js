const Notification = require("../models/Notification");
const User = require("../models/users");

// ==========================================
// Get Notifications for Volunteer or User
// ==========================================
exports.getVolunteerNotifications = async (req, res) => {
  try {
    const { volunteerId } = req.params;

    // Find notifications either matching the recipient ObjectId OR matching their email
    let userEmail = "";
    if (volunteerId) {
      const user = await User.findById(volunteerId);
      if (user) {
        userEmail = user.email;
      }
    }

    const query = {
      $or: [
        { recipient: volunteerId },
        ...(userEmail ? [{ recipientEmail: userEmail }] : []),
      ],
    };

    const notifications = await Notification.find(query)
      .populate("disasterId", "disasterType location severity aiRiskScore status")
      .sort({ createdAt: -1 });

    res.status(200).json(notifications);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// ==========================================
// Get All System Notifications (Admin / Debug)
// ==========================================
exports.getAllNotifications = async (req, res) => {
  try {
    const notifications = await Notification.find()
      .populate("disasterId", "disasterType location severity")
      .populate("recipient", "fullName email role district")
      .sort({ createdAt: -1 })
      .limit(100);

    res.status(200).json(notifications);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// ==========================================
// Mark Notification as Acknowledged by Volunteer
// ==========================================
exports.acknowledgeNotification = async (req, res) => {
  try {
    const { id } = req.params;
    const notification = await Notification.findByIdAndUpdate(
      id,
      {
        read: true,
        acknowledged: true,
        acknowledgedAt: new Date(),
      },
      { new: true }
    );

    if (!notification) {
      return res.status(404).json({ message: "Notification not found" });
    }

    res.status(200).json({
      message: "Mission briefing acknowledged successfully",
      notification,
    });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
