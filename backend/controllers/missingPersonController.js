const MissingPerson = require("../models/MissingPerson");

// Initial sample seed if empty
const DEFAULT_MISSING_PERSONS = [
  {
    fullName: "Rohan Suresh Shinde",
    age: 14,
    gender: "Male",
    district: "Pune",
    lastSeenLocation: "Near Baba Bhide Bridge, Deccan Gymkhana, Pune",
    lastSeenDate: new Date(Date.now() - 36 * 3600 * 1000),
    contactPhone: "+91 98223 99182",
    reporterName: "Suresh Shinde (Father)",
    description: "Wearing blue school uniform shirt and black shorts. Height 5ft 2in. Was separated during sudden river flash flood.",
    status: "Searching",
    notes: "Reported to Deccan Police Station. Search team notified.",
  },
  {
    fullName: "Kavita Ramesh Patil",
    age: 68,
    gender: "Female",
    district: "Nashik",
    lastSeenLocation: "Ramkund Ghat, Panchavati, Nashik",
    lastSeenDate: new Date(Date.now() - 20 * 3600 * 1000),
    contactPhone: "+91 94221 44556",
    reporterName: "Amol Patil (Son)",
    description: "Wearing green cotton saree, wears reading spectacles. Has mild hearing difficulty.",
    status: "Located Safe",
    notes: "Safely located by SDRF squad at Panchavati Relief Camp. Family in contact.",
  },
  {
    fullName: "Deepak Narayan Joshi",
    age: 34,
    gender: "Male",
    district: "Mumbai",
    lastSeenLocation: "Near Kurla Railway Station West, Mumbai",
    lastSeenDate: new Date(Date.now() - 14 * 3600 * 1000),
    contactPhone: "+91 98190 22345",
    reporterName: "Sunita Joshi (Wife)",
    description: "Wearing grey polo t-shirt, blue denim jeans. Carrying black backpack with office laptop.",
    status: "Searching",
    notes: "Last phone ping recorded near Kurla West at 7:30 PM.",
  },
];

// ==========================================
// Get Missing Persons (Filter by district, status, search)
// ==========================================
exports.getMissingPersons = async (req, res) => {
  try {
    const { district, status, search } = req.query;

    let count = await MissingPerson.countDocuments();
    if (count === 0) {
      await MissingPerson.insertMany(DEFAULT_MISSING_PERSONS);
    }

    const query = {};
    if (district && district !== "All") {
      query.district = new RegExp(`^${district}$`, "i");
    }
    if (status && status !== "All") {
      query.status = status;
    }
    if (search && search.trim()) {
      query.$or = [
        { fullName: new RegExp(search.trim(), "i") },
        { lastSeenLocation: new RegExp(search.trim(), "i") },
        { description: new RegExp(search.trim(), "i") },
      ];
    }

    const records = await MissingPerson.find(query).sort({ createdAt: -1 });
    res.status(200).json(records);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// ==========================================
// Report New Missing Person
// ==========================================
exports.createMissingPerson = async (req, res) => {
  try {
    const record = await MissingPerson.create(req.body);
    res.status(201).json({
      message: "Missing person notice logged into statewide registry",
      record,
    });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// ==========================================
// Update Status (e.g., Mark as Located Safe)
// ==========================================
exports.updateMissingPersonStatus = async (req, res) => {
  try {
    const { id } = req.params;
    const { status, notes } = req.body;

    const record = await MissingPerson.findByIdAndUpdate(
      id,
      {
        status,
        ...(notes && { notes }),
      },
      { new: true }
    );

    if (!record) {
      return res.status(404).json({ message: "Record not found" });
    }

    res.status(200).json({
      message: "Registry record updated successfully",
      record,
    });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
