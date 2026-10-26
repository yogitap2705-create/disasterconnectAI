const express = require("express");
const router = express.Router();
const {
  getVolunteerNotifications,
  getAllNotifications,
  acknowledgeNotification,
} = require("../controllers/notificationController");

router.get("/volunteer/:volunteerId", getVolunteerNotifications);
router.get("/all", getAllNotifications);
router.put("/:id/acknowledge", acknowledgeNotification);

module.exports = router;
