const express = require("express");
const router = express.Router();
const {
  getShelters,
  createShelter,
  updateOccupancy,
} = require("../controllers/shelterController");

router.get("/", getShelters);
router.post("/", createShelter);
router.put("/:id/occupancy", updateOccupancy);

module.exports = router;
