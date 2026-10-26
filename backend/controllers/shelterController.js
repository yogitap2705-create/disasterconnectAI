const Shelter = require("../models/Shelter");

// Default initial seed data if collection is empty
const DEFAULT_SHELTERS = [
  {
    name: "Balewadi Sports Complex Emergency Relief Camp",
    district: "Pune",
    address: "National Games Park, Mahalunge, Balewadi, Pune 411045",
    capacity: 1200,
    occupancy: 420,
    contactPerson: "Col. S. Patil (Retd.)",
    contactPhone: "+91 98220 11442",
    hasMedicalUnit: true,
    hasCleanWater: true,
    hasFoodSupplies: true,
    status: "Active",
    latitude: 18.5744,
    longitude: 73.7744,
  },
  {
    name: "Shivaji Nagar Multi-Purpose Relief Center",
    district: "Pune",
    address: "Near Congress Bhavan, Shivaji Nagar, Pune 411005",
    capacity: 650,
    occupancy: 180,
    contactPerson: "Dr. Anjali Deshmukh",
    contactPhone: "+91 94225 88910",
    hasMedicalUnit: true,
    hasCleanWater: true,
    hasFoodSupplies: true,
    status: "Active",
    latitude: 18.5308,
    longitude: 73.8475,
  },
  {
    name: "Bandra Kurla Emergency Transition Shelter",
    district: "Mumbai",
    address: "MMRDA Grounds, BKC Complex, Bandra East, Mumbai 400051",
    capacity: 2500,
    occupancy: 890,
    contactPerson: "Capt. Rajesh Varma",
    contactPhone: "+91 98200 44123",
    hasMedicalUnit: true,
    hasCleanWater: true,
    hasFoodSupplies: true,
    status: "Active",
    latitude: 19.0657,
    longitude: 72.8687,
  },
  {
    name: "Thane Town Hall Civil Defense Shelter",
    district: "Thane",
    address: "Station Road, Near Talao Pali, Thane West 400601",
    capacity: 800,
    occupancy: 210,
    contactPerson: "Insp. Vikram Shinde",
    contactPhone: "+91 98199 55667",
    hasMedicalUnit: true,
    hasCleanWater: true,
    hasFoodSupplies: true,
    status: "Active",
    latitude: 19.186,
    longitude: 72.9759,
  },
  {
    name: "Nashik Golf Club Pavilion Relief Hub",
    district: "Nashik",
    address: "Trimbak Road, Near Civil Hospital, Nashik 422002",
    capacity: 900,
    occupancy: 140,
    contactPerson: "Dr. Sandeep Kulkarni",
    contactPhone: "+91 94231 66789",
    hasMedicalUnit: true,
    hasCleanWater: true,
    hasFoodSupplies: true,
    status: "Active",
    latitude: 19.9975,
    longitude: 73.7898,
  },
  {
    name: "Nagpur Reshimbagh Indoor Stadium Camp",
    district: "Nagpur",
    address: "Reshimbagh Road, Great Nag Road, Nagpur 440009",
    capacity: 1500,
    occupancy: 310,
    contactPerson: "Maj. Dilip Gaikwad",
    contactPhone: "+91 98230 77124",
    hasMedicalUnit: true,
    hasCleanWater: true,
    hasFoodSupplies: true,
    status: "Active",
    latitude: 21.135,
    longitude: 79.105,
  },
];

// ==========================================
// Get All Shelters (with District filter)
// ==========================================
exports.getShelters = async (req, res) => {
  try {
    const { district } = req.query;

    let count = await Shelter.countDocuments();
    if (count === 0) {
      await Shelter.insertMany(DEFAULT_SHELTERS);
    }

    const query = {};
    if (district && district !== "All") {
      query.district = new RegExp(`^${district}$`, "i");
    }

    const shelters = await Shelter.find(query).sort({ status: 1, capacity: -1 });
    res.status(200).json(shelters);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// ==========================================
// Add New Shelter
// ==========================================
exports.createShelter = async (req, res) => {
  try {
    const shelter = await Shelter.create(req.body);
    res.status(201).json({
      message: "Emergency Shelter Registered Successfully",
      shelter,
    });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// ==========================================
// Update Shelter Occupancy / Status
// ==========================================
exports.updateOccupancy = async (req, res) => {
  try {
    const { id } = req.params;
    const { occupancy, status } = req.body;

    const shelter = await Shelter.findByIdAndUpdate(
      id,
      {
        ...(occupancy !== undefined && { occupancy }),
        ...(status && { status }),
      },
      { new: true }
    );

    if (!shelter) {
      return res.status(404).json({ message: "Shelter not found" });
    }

    res.status(200).json({
      message: "Shelter data updated successfully",
      shelter,
    });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
