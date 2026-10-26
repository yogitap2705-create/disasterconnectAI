const mongoose = require("mongoose");

const missingPersonSchema = new mongoose.Schema(
  {
    fullName: {
      type: String,
      required: true,
    },
    age: {
      type: Number,
      required: true,
    },
    gender: {
      type: String,
      enum: ["Male", "Female", "Other", "Unknown"],
      default: "Unknown",
    },
    district: {
      type: String,
      required: true,
      default: "Pune",
    },
    lastSeenLocation: {
      type: String,
      required: true,
    },
    lastSeenDate: {
      type: Date,
      default: Date.now,
    },
    contactPhone: {
      type: String,
      required: true,
    },
    reporterName: {
      type: String,
      default: "Citizen",
    },
    description: {
      type: String,
      required: true,
    },
    photo: {
      type: String,
      default: "",
    },
    status: {
      type: String,
      enum: ["Searching", "Located Safe", "In Relief Shelter"],
      default: "Searching",
    },
    notes: {
      type: String,
      default: "",
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model("MissingPerson", missingPersonSchema);
