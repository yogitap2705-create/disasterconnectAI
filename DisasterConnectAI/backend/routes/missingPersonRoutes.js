const express = require("express");
const router = express.Router();
const {
  getMissingPersons,
  createMissingPerson,
  updateMissingPersonStatus,
} = require("../controllers/missingPersonController");

router.get("/", getMissingPersons);
router.post("/", createMissingPerson);
router.put("/:id/status", updateMissingPersonStatus);

module.exports = router;
