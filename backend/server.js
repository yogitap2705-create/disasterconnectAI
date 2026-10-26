const dotenv = require("dotenv");
dotenv.config();
const express = require("express");
const cors = require("cors");
const connectDB = require("./config/db");
const authRoutes = require("./routes/authRoutes");
const disasterRoutes = require("./routes/disasterRoutes");
const chatRoutes = require("./routes/chatRoutes");
const notificationRoutes = require("./routes/notificationRoutes");
const shelterRoutes = require("./routes/shelterRoutes");
const missingPersonRoutes = require("./routes/missingPersonRoutes");
const path = require("path");

connectDB();

const app = express();

app.use(cors());
app.use(express.json());
app.use("/uploads", express.static(path.join(__dirname, "uploads")));

app.use("/api/auth", authRoutes);
app.use("/api/disasters", disasterRoutes);
app.use("/api/chat", chatRoutes);
app.use("/api/notifications", notificationRoutes);
app.use("/api/shelters", shelterRoutes);
app.use("/api/missing-persons", missingPersonRoutes);

app.get("/", (req, res) => {
  res.send("DisasterConnect AI Enterprise Backend Active");
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`[Server] DisasterConnect AI running on http://localhost:${PORT}`);
});