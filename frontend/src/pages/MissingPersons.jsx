import { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import API from "../services/api";
import {
  FaUserFriends,
  FaSearch,
  FaPlusCircle,
  FaMapMarkerAlt,
  FaPhoneAlt,
  FaCheckCircle,
  FaTimes,
  FaClock,
} from "react-icons/fa";

const DISTRICTS = [
  "All",
  "Pune",
  "Mumbai",
  "Thane",
  "Nashik",
  "Nagpur",
  "Chhatrapati Sambhajinagar",
  "Solapur",
  "Kolhapur",
  "Satara",
  "Ahmednagar",
  "Raigad",
  "Ratnagiri",
];

function MissingPersons() {
  const [records, setRecords] = useState([]);
  const [district, setDistrict] = useState("All");
  const [statusFilter, setStatusFilter] = useState("All");
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);

  const [formData, setFormData] = useState({
    fullName: "",
    age: "",
    gender: "Male",
    district: "Pune",
    lastSeenLocation: "",
    contactPhone: "",
    reporterName: "",
    description: "",
  });

  useEffect(() => {
    fetchRecords();
  }, [district, statusFilter]);

  const fetchRecords = async () => {
    try {
      setLoading(true);
      let query = [];
      if (district !== "All") query.push(`district=${district}`);
      if (statusFilter !== "All") query.push(`status=${statusFilter}`);
      const queryString = query.length > 0 ? `?${query.join("&")}` : "";

      const res = await API.get(`/missing-persons${queryString}`);
      setRecords(res.data);
    } catch (error) {
      console.error("Failed to load missing persons:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleCreate = async (e) => {
    e.preventDefault();
    try {
      await API.post("/missing-persons", formData);
      alert("Notice logged into statewide reunification registry.");
      setShowModal(false);
      setFormData({
        fullName: "",
        age: "",
        gender: "Male",
        district: "Pune",
        lastSeenLocation: "",
        contactPhone: "",
        reporterName: "",
        description: "",
      });
      fetchRecords();
    } catch (error) {
      alert("Failed to submit notice: " + (error.response?.data?.message || error.message));
    }
  };

  const handleMarkLocated = async (id) => {
    const confirm = window.confirm("Mark this individual as Located Safe / Reunited?");
    if (!confirm) return;

    try {
      await API.put(`/missing-persons/${id}/status`, {
        status: "Located Safe",
        notes: "Confirmed safe and reunited by family.",
      });
      fetchRecords();
    } catch (error) {
      alert("Failed to update status.");
    }
  };

  const filteredRecords = records.filter((r) => {
    const q = search.toLowerCase();
    return (
      r.fullName.toLowerCase().includes(q) ||
      r.lastSeenLocation.toLowerCase().includes(q) ||
      r.description.toLowerCase().includes(q)
    );
  });

  return (
    <>
      <Navbar />

      <div style={styles.container}>
        {/* Header */}
        <div style={styles.header}>
          <div>
            <div style={styles.badge}>
              <FaUserFriends style={{ marginRight: 6 }} />
              STATEWIDE REUNIFICATION DESK
            </div>
            <h1 style={styles.title}>Missing Persons & Family Registry</h1>
            <p style={styles.subtitle}>
              Centralized tracing database to report and search for individuals separated during natural disasters across Maharashtra.
            </p>
          </div>

          <button onClick={() => setShowModal(true)} style={styles.reportBtn}>
            <FaPlusCircle style={{ marginRight: 8 }} /> Log Missing Notice
          </button>
        </div>

        {/* Filter Bar */}
        <div style={styles.filterBar}>
          <div style={styles.searchBox}>
            <FaSearch color="#64748b" style={{ marginRight: 10 }} />
            <input
              type="text"
              placeholder="Search by full name, location, or physical traits..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              style={styles.searchInput}
            />
          </div>

          <div style={{ display: "flex", gap: "10px", flexWrap: "wrap" }}>
            <select
              value={district}
              onChange={(e) => setDistrict(e.target.value)}
              style={styles.select}
            >
              {DISTRICTS.map((d) => (
                <option key={d} value={d}>
                  {d === "All" ? "All Districts" : `${d} District`}
                </option>
              ))}
            </select>

            <select
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value)}
              style={styles.select}
            >
              <option value="All">All Statuses</option>
              <option value="Searching">Searching (Active)</option>
              <option value="Located Safe">Located Safe</option>
              <option value="In Relief Shelter">In Relief Shelter</option>
            </select>
          </div>
        </div>

        {/* Records Grid */}
        {loading ? (
          <div style={{ textAlign: "center", padding: "60px", color: "#64748b" }}>
            Querying reunification registry...
          </div>
        ) : filteredRecords.length === 0 ? (
          <div style={styles.emptyCard}>
            <h3>No records matching your search</h3>
            <p>You can lodge an urgent missing person report using the button above.</p>
          </div>
        ) : (
          <div style={styles.grid}>
            {filteredRecords.map((r) => {
              const isFound = r.status === "Located Safe";

              return (
                <div key={r._id} style={styles.personCard}>
                  <div style={styles.cardTop}>
                    <div>
                      <span style={styles.districtBadge}>{r.district} District</span>
                      <h3 style={styles.name}>{r.fullName}</h3>
                      <div style={styles.ageGender}>
                        Age: <strong>{r.age}</strong> • Gender: <strong>{r.gender}</strong>
                      </div>
                    </div>

                    <span
                      style={{
                        ...styles.statusTag,
                        backgroundColor: isFound ? "#dcfce7" : "#fee2e2",
                        color: isFound ? "#166534" : "#991b1b",
                      }}
                    >
                      {r.status}
                    </span>
                  </div>

                  <div style={styles.detailRow}>
                    <FaMapMarkerAlt color="#800020" size={13} style={{ marginTop: 2, marginRight: 6 }} />
                    <span style={{ fontSize: "13px", color: "#334155" }}>
                      <strong>Last Seen:</strong> {r.lastSeenLocation}
                    </span>
                  </div>

                  <div style={styles.detailRow}>
                    <FaClock color="#64748b" size={12} style={{ marginTop: 2, marginRight: 6 }} />
                    <span style={{ fontSize: "12px", color: "#64748b" }}>
                      Reported: {new Date(r.createdAt).toLocaleDateString()}
                    </span>
                  </div>

                  <p style={styles.descriptionText}>{r.description}</p>

                  <div style={styles.cardBottom}>
                    <div>
                      <small style={{ color: "#64748b", display: "block" }}>
                        Contact: {r.reporterName}
                      </small>
                      <a href={`tel:${r.contactPhone}`} style={styles.phoneLink}>
                        <FaPhoneAlt size={10} style={{ marginRight: 4 }} />
                        {r.contactPhone}
                      </a>
                    </div>

                    {!isFound && (
                      <button
                        onClick={() => handleMarkLocated(r._id)}
                        style={styles.markFoundBtn}
                      >
                        <FaCheckCircle style={{ marginRight: 4 }} /> Mark Safe
                      </button>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        )}

        {/* Modal to Log Missing Person Notice */}
        {showModal && (
          <div style={styles.modalOverlay}>
            <div style={styles.modal}>
              <div style={styles.modalHeader}>
                <h3 style={{ margin: 0, color: "#800020" }}>Log Missing Person Notice</h3>
                <button onClick={() => setShowModal(false)} style={styles.closeBtn}>
                  <FaTimes />
                </button>
              </div>

              <form onSubmit={handleCreate} style={{ marginTop: 16 }}>
                <div style={styles.inputGroup}>
                  <label style={styles.label}>Full Name of Missing Person *</label>
                  <input
                    type="text"
                    name="fullName"
                    value={formData.fullName}
                    onChange={handleChange}
                    style={styles.input}
                    required
                  />
                </div>

                <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Age *</label>
                    <input
                      type="number"
                      name="age"
                      value={formData.age}
                      onChange={handleChange}
                      style={styles.input}
                      required
                    />
                  </div>

                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Gender *</label>
                    <select
                      name="gender"
                      value={formData.gender}
                      onChange={handleChange}
                      style={styles.input}
                    >
                      <option>Male</option>
                      <option>Female</option>
                      <option>Other</option>
                    </select>
                  </div>
                </div>

                <div style={styles.inputGroup}>
                  <label style={styles.label}>District *</label>
                  <select
                    name="district"
                    value={formData.district}
                    onChange={handleChange}
                    style={styles.input}
                  >
                    {DISTRICTS.filter((d) => d !== "All").map((d) => (
                      <option key={d} value={d}>
                        {d} District
                      </option>
                    ))}
                  </select>
                </div>

                <div style={styles.inputGroup}>
                  <label style={styles.label}>Last Seen Location / Landmark *</label>
                  <input
                    type="text"
                    name="lastSeenLocation"
                    placeholder="E.g., Near Deccan Gymkhana Bus Stop, Pune"
                    value={formData.lastSeenLocation}
                    onChange={handleChange}
                    style={styles.input}
                    required
                  />
                </div>

                <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Your Name (Reporter) *</label>
                    <input
                      type="text"
                      name="reporterName"
                      value={formData.reporterName}
                      onChange={handleChange}
                      style={styles.input}
                      required
                    />
                  </div>

                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Emergency Contact Phone *</label>
                    <input
                      type="tel"
                      name="contactPhone"
                      value={formData.contactPhone}
                      onChange={handleChange}
                      style={styles.input}
                      required
                    />
                  </div>
                </div>

                <div style={styles.inputGroup}>
                  <label style={styles.label}>Physical Description, Clothing & Identifiers *</label>
                  <textarea
                    name="description"
                    rows="3"
                    placeholder="Height, clothes worn, eyeglasses, visible marks, bag carried..."
                    value={formData.description}
                    onChange={handleChange}
                    style={{ ...styles.input, height: "auto" }}
                    required
                  />
                </div>

                <button type="submit" style={styles.submitBtn}>
                  Register Notice
                </button>
              </form>
            </div>
          </div>
        )}
      </div>

      <Footer />
    </>
  );
}

const styles = {
  container: {
    padding: "40px 30px",
    background: "#f8fafc",
    minHeight: "90vh",
    maxWidth: "1350px",
    margin: "0 auto",
  },

  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    marginBottom: "28px",
    flexWrap: "wrap",
    gap: "16px",
  },

  badge: {
    display: "inline-flex",
    alignItems: "center",
    backgroundColor: "#fff1f2",
    color: "#800020",
    padding: "4px 12px",
    borderRadius: "12px",
    fontSize: "11px",
    fontWeight: "800",
    letterSpacing: "0.8px",
    marginBottom: "8px",
  },

  title: {
    fontSize: "32px",
    fontWeight: "800",
    color: "#0f172a",
    margin: "0 0 8px 0",
  },

  subtitle: {
    color: "#475569",
    fontSize: "14.5px",
    maxWidth: "750px",
    lineHeight: "1.5",
    margin: 0,
  },

  reportBtn: {
    backgroundColor: "#800020",
    color: "#ffffff",
    padding: "12px 20px",
    borderRadius: "10px",
    border: "none",
    fontWeight: "700",
    fontSize: "14px",
    cursor: "pointer",
    display: "inline-flex",
    alignItems: "center",
    boxShadow: "0 3px 10px rgba(128,0,32,0.25)",
  },

  filterBar: {
    display: "flex",
    gap: "14px",
    flexWrap: "wrap",
    marginBottom: "26px",
    background: "#ffffff",
    padding: "14px",
    borderRadius: "12px",
    border: "1px solid #e2e8f0",
  },

  searchBox: {
    flex: 1,
    minWidth: "260px",
    display: "flex",
    alignItems: "center",
    background: "#f1f5f9",
    borderRadius: "8px",
    padding: "10px 14px",
  },

  searchInput: {
    flex: 1,
    border: "none",
    background: "transparent",
    outline: "none",
    fontSize: "14px",
  },

  select: {
    padding: "10px 14px",
    borderRadius: "8px",
    border: "1px solid #cbd5e1",
    fontSize: "13.5px",
    background: "#ffffff",
    cursor: "pointer",
    minWidth: "160px",
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(360px, 1fr))",
    gap: "20px",
  },

  personCard: {
    background: "#ffffff",
    border: "1px solid #e2e8f0",
    borderRadius: "14px",
    padding: "22px",
    boxShadow: "0 3px 10px rgba(0,0,0,0.03)",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
  },

  cardTop: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    marginBottom: "10px",
  },

  districtBadge: {
    fontSize: "11px",
    fontWeight: "700",
    color: "#800020",
    textTransform: "uppercase",
  },

  name: {
    fontSize: "17px",
    fontWeight: "800",
    color: "#0f172a",
    margin: "4px 0 2px 0",
  },

  ageGender: {
    fontSize: "12px",
    color: "#64748b",
  },

  statusTag: {
    padding: "4px 8px",
    borderRadius: "8px",
    fontSize: "11px",
    fontWeight: "700",
    whiteSpace: "nowrap",
  },

  detailRow: {
    display: "flex",
    alignItems: "flex-start",
    marginTop: "6px",
  },

  descriptionText: {
    fontSize: "13px",
    color: "#475569",
    lineHeight: "1.45",
    backgroundColor: "#f8fafc",
    padding: "10px",
    borderRadius: "8px",
    margin: "12px 0",
  },

  cardBottom: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    paddingTop: "12px",
    borderTop: "1px solid #f1f5f9",
  },

  phoneLink: {
    color: "#0d6efd",
    fontSize: "12.5px",
    fontWeight: "700",
    textDecoration: "none",
    display: "inline-flex",
    alignItems: "center",
  },

  markFoundBtn: {
    backgroundColor: "#16a34a",
    color: "#ffffff",
    border: "none",
    padding: "6px 12px",
    borderRadius: "6px",
    fontSize: "11.5px",
    fontWeight: "700",
    cursor: "pointer",
    display: "inline-flex",
    alignItems: "center",
  },

  emptyCard: {
    textAlign: "center",
    padding: "50px",
    backgroundColor: "#fff",
    borderRadius: "14px",
    border: "1px solid #e2e8f0",
    color: "#64748b",
  },

  modalOverlay: {
    position: "fixed",
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: "rgba(0,0,0,0.6)",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    zIndex: 1100,
    padding: "20px",
  },

  modal: {
    backgroundColor: "#ffffff",
    borderRadius: "16px",
    padding: "24px 28px",
    maxWidth: "540px",
    width: "100%",
    maxHeight: "90vh",
    overflowY: "auto",
  },

  modalHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    borderBottom: "1px solid #e2e8f0",
    paddingBottom: "12px",
  },

  closeBtn: {
    background: "transparent",
    border: "none",
    fontSize: "16px",
    cursor: "pointer",
    color: "#64748b",
  },

  inputGroup: {
    marginBottom: "12px",
  },

  label: {
    display: "block",
    fontSize: "12px",
    fontWeight: "700",
    color: "#334155",
    marginBottom: "5px",
  },

  input: {
    width: "100%",
    padding: "10px 12px",
    borderRadius: "8px",
    border: "1px solid #cbd5e1",
    fontSize: "13.5px",
    boxSizing: "border-box",
  },

  submitBtn: {
    width: "100%",
    backgroundColor: "#800020",
    color: "#ffffff",
    border: "none",
    padding: "12px",
    borderRadius: "10px",
    fontSize: "14px",
    fontWeight: "700",
    cursor: "pointer",
    marginTop: "12px",
  },
};

export default MissingPersons;
