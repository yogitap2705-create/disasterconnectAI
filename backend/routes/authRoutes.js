const express = require("express");
const router = express.Router();

const {
  register,
  getVolunteers,
  login,
} = require("../controllers/authController");

router.post("/register", register);
router.post("/login", login);
router.get("/volunteers", getVolunteers);
// If you added another route, include it here.
// For example:
// router.get("/users", someFunction);

module.exports = router;