const express = require("express");
const router = express.Router();

const upload = require("../config/multer");

const {
  createDisaster,
  getAllDisasters,
  updateDisasterStatus,
  deleteDisaster,
  assignVolunteer,
  getVolunteerDisasters,
} = require("../controllers/disasterControllers");

// Create Disaster with Image
router.post("/", upload.single("image"), createDisaster);
router.get("/volunteer/:id", getVolunteerDisasters);
// Get All Disasters
router.get("/", getAllDisasters);

// Update Status
router.put("/:id", updateDisasterStatus);

// Delete Disaster
router.delete("/:id", deleteDisaster);
router.put("/:id/assign", assignVolunteer);
module.exports = router;