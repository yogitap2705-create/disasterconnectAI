const mongoose = require("mongoose");

const shelterSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
    },
    district: {
      type: String,
      required: true,
      default: "Pune",
    },
    address: {
      type: String,
      required: true,
    },
    capacity: {
      type: Number,
      required: true,
      default: 200,
    },
    occupancy: {
      type: Number,
      default: 0,
    },
    contactPerson: {
      type: String,
      default: "Camp In-Charge",
    },
    contactPhone: {
      type: String,
      default: "112",
    },
    hasMedicalUnit: {
      type: Boolean,
      default: true,
    },
    hasCleanWater: {
      type: Boolean,
      default: true,
    },
    hasFoodSupplies: {
      type: Boolean,
      default: true,
    },
    status: {
      type: String,
      enum: ["Active", "Full", "Standby"],
      default: "Active",
    },
    latitude: {
      type: Number,
      default: 18.5204,
    },
    longitude: {
      type: Number,
      default: 73.8567,
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model("Shelter", shelterSchema);
