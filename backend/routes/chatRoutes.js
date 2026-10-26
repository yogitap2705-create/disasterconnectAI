const express = require("express");
const router = express.Router();

const { chatWithAI, enhanceDescription } = require("../controllers/chatController");

router.post("/", chatWithAI);
router.post("/enhance", enhanceDescription);

module.exports = router;