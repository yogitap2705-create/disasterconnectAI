const mongoose = require("mongoose");

const disasterSchema = new mongoose.Schema(
  {
    disasterType: {
      type: String,
      required: true,
    },
    severity: {
      type: String,
      enum: ["Low", "Medium", "High"],
      default: "Low",
    },
    location: {
      type: String,
      required: true,
    },
    district: {
      type: String,
      default: "Pune",
    },
    latitude: {
      type: Number,
    },
    longitude: {
      type: Number,
    },
    description: {
      type: String,
      required: true,
    },
    image: {
      type: String,
      default: "",
    },
    reportedBy: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
    },
    assignedVolunteer: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
    },
    assignedAt: {
      type: Date,
    },
    status: {
      type: String,
      enum: ["Pending", "Assigned", "In Progress", "Resolved"],
      default: "Pending",
    },
    resolutionNotes: {
      type: String,
      default: "",
    },
    resolvedAt: {
      type: Date,
    },

    // AI Analysis & Decision Support
    aiRiskScore: {
      type: Number,
      min: 1,
      max: 10,
      default: 5,
    },
    aiThreatAssessment: {
      type: String,
      default: "",
    },
    aiActionPlan: {
      type: [String],
      default: [],
    },
    aiRecommendedSupplies: {
      type: [String],
      default: [],
    },
    aiVolunteerBriefing: {
      type: String,
      default: "",
    },

    createdAt: {
      type: Date,
      default: Date.now,
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model("Disaster", disasterSchema);