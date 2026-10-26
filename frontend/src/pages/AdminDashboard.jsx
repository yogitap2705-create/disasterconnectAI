import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Analytics from "../components/Analytics";
import API from "../services/api";
import RecentActivity from "../components/RecentActivity";
import generatePDF from "../utils/generatePDF";
import {
  FaMapMarkerAlt,
  FaShieldAlt,
  FaUserCheck,
  FaFilePdf,
  FaSyncAlt,
  FaPhoneAlt,
  FaTools,
  FaBolt,
  FaSearch,
  FaRobot,
  FaExclamationTriangle,
  FaCheckCircle,
  FaTimes,
} from "react-icons/fa";

const MAHARASHTRA_DISTRICTS = [
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
  "Amravati",
  "Nanded",
  "Jalgaon",
  "Akola",
  "Latur",
  "Dhule",
  "Sangli",
  "Chandrapur",
  "Parbhani",
  "Raigad",
  "Ratnagiri",
  "Sindhudurg",
  "Palghar",
  "Wardha",
];

function AdminDashboard() {
  const [disasters, setDisasters] = useState([]);
  const [volunteers, setVolunteers] = useState([]);
  const [search, setSearch] = useState("");
  const [statusFilter, setStatusFilter] = useState("All");
  const [districtFilter, setDistrictFilter] = useState("All");
  const [selectedDisasterForAI, setSelectedDisasterForAI] = useState(null);
  const [isRefreshing, setIsRefreshing] = useState(false);

  useEffect(() => {
    fetchDisasters();
    fetchVolunteers();
  }, []);

  const fetchDisasters = async () => {
    try {
      setIsRefreshing(true);
      const res = await API.get("/disasters");
      setDisasters(res.data);
    } catch (error) {
      console.error("Error fetching disasters:", error);
    } finally {
      setIsRefreshing(false);
    }
  };

  const fetchVolunteers = async () => {
    try {
      const res = await API.get("/auth/volunteers");
      setVolunteers(res.data);
    } catch (error) {
      console.error("Error fetching volunteers:", error);
    }
  };

  const updateStatus = async (id, status) => {
    try {
      await API.put(`/disasters/${id}`, { status });
      fetchDisasters();
    } catch (error) {
      console.error(error);
    }
  };

  const deleteReport = async (id) => {
    const confirmDelete = window.confirm("Delete this disaster report?");
    if (!confirmDelete) return;

    try {
      await API.delete(`/disasters/${id}`);
      fetchDisasters();
    } catch (error) {
      console.error(error);
    }
  };

  const assignVolunteer = async (disasterId, volunteerId) => {
    if (!volunteerId) return;

    try {
      await API.put(`/disasters/${disasterId}/assign`, {
        volunteerId,
      });
      alert(
        "Volunteer successfully assigned & AI tactical mission briefing dispatched via email!"
      );
      fetchDisasters();
    } catch (error) {
      console.error(error);
      alert("Failed to assign volunteer.");
    }
  };

  // Auto-assign nearest matching volunteer for a disaster's district
  const autoAssignDistrictVolunteer = (disaster) => {
    const disasterDist = (disaster.district || "Pune").toLowerCase();
    const matchingVol = volunteers.find(
      (v) => (v.district || "Pune").toLowerCase() === disasterDist
    );

    if (matchingVol) {
      assignVolunteer(disaster._id, matchingVol._id);
    } else if (volunteers.length > 0) {
      // Fallback to first available volunteer
      assignVolunteer(disaster._id, volunteers[0]._id);
    } else {
      alert("No active volunteers registered in the system yet.");
    }
  };

  const filteredDisasters = disasters.filter((d) => {
    const matchesSearch =
      d.disasterType.toLowerCase().includes(search.toLowerCase()) ||
      d.location.toLowerCase().includes(search.toLowerCase()) ||
      (d.district || "").toLowerCase().includes(search.toLowerCase()) ||
      (d.reportedBy?.fullName || "").toLowerCase().includes(search.toLowerCase());

    const matchesStatus =
      statusFilter === "All" || d.status === statusFilter;

    const matchesDistrict =
      districtFilter === "All" ||
      (d.district && d.district.toLowerCase() === districtFilter.toLowerCase()) ||
      (!d.district && districtFilter === "Pune");

    return matchesSearch && matchesStatus && matchesDistrict;
  });

  return (
    <>
      <Navbar />

      <div style={styles.container}>
        {/* Command Center Header */}
        <div style={styles.headerBar}>
          <div>
            <div style={styles.badge}>
              <FaShieldAlt style={{ marginRight: 6 }} />
              EMERGENCY COMMAND CENTER & DISTRICT DISPATCH
            </div>
            <h1 style={styles.commandTitle}>Disaster Intelligence Administration</h1>
            <p style={styles.commandSub}>
              Assign relief volunteers by district, monitor AI triage risk scores, and manage statewide response.
            </p>
          </div>

          <div style={{ display: "flex", gap: "10px", alignItems: "center" }}>
            <button
              onClick={fetchDisasters}
              disabled={isRefreshing}
              style={styles.refreshBtn}
              title="Refresh live feeds"
            >
              <FaSyncAlt
                style={{
                  marginRight: "6px",
                  animation: isRefreshing ? "spin 1s linear infinite" : "none",
                }}
              />
              {isRefreshing ? "Refreshing..." : "Refresh"}
            </button>

            <button
              onClick={() => generatePDF(disasters)}
              style={styles.downloadPdfBtn}
            >
              <FaFilePdf style={{ marginRight: "6px" }} /> Download Incident PDF
            </button>
          </div>
        </div>

        {/* Analytics Statistics Cards */}
        <div style={styles.stats}>
          <div style={styles.statCard}>
            <div style={{ fontSize: "28px", fontWeight: "800", color: "#800020" }}>
              {disasters.length}
            </div>
            <div style={styles.statLabel}>Total Incident Reports</div>
          </div>

          <div style={styles.statCard}>
            <div style={{ fontSize: "28px", fontWeight: "800", color: "#e67e22" }}>
              {disasters.filter((d) => d.status === "Pending").length}
            </div>
            <div style={styles.statLabel}>Pending Triage</div>
          </div>

          <div style={styles.statCard}>
            <div style={{ fontSize: "28px", fontWeight: "800", color: "#2980b9" }}>
              {disasters.filter((d) => d.status === "In Progress" || d.status === "Assigned").length}
            </div>
            <div style={styles.statLabel}>Missions Dispatched</div>
          </div>

          <div style={styles.statCard}>
            <div style={{ fontSize: "28px", fontWeight: "800", color: "#27ae60" }}>
              {disasters.filter((d) => d.status === "Resolved").length}
            </div>
            <div style={styles.statLabel}>Incidents Resolved</div>
          </div>

          <div style={styles.statCard}>
            <div style={{ fontSize: "28px", fontWeight: "800", color: "#8e44ad" }}>
              {volunteers.length}
            </div>
            <div style={styles.statLabel}>Registered Volunteers</div>
          </div>
        </div>

        {/* Analytics Chart Components */}
        <Analytics disasters={disasters} />
        <RecentActivity disasters={disasters} />

        {/* District & Incident Search / Filter Bar */}
        <div style={styles.filterSection}>
          <div style={styles.filterTitle}>
            <span style={{ display: "inline-flex", alignItems: "center", gap: "6px" }}>
              <FaBolt /> Real-Time District Dispatch & Volunteer Assignment
            </span>
            <small style={{ color: "#666", fontWeight: "normal" }}>
              Showing {filteredDisasters.length} of {disasters.length} total reports
            </small>
          </div>

          <div style={styles.searchBarRow}>
            {/* Search Input */}
            <div style={styles.searchInputWrap}>
              <FaSearch color="#800020" style={{ marginRight: "8px" }} />
              <input
                type="text"
                placeholder="Search by disaster type, location, citizen, or district..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                style={styles.searchInput}
              />
            </div>

            {/* District Selector Filter */}
            <div style={{ display: "flex", alignItems: "center", gap: "6px" }}>
              <FaMapMarkerAlt color="#800020" />
              <select
                value={districtFilter}
                onChange={(e) => setDistrictFilter(e.target.value)}
                style={styles.filterSelect}
              >
                <option value="All">All Maharashtra Districts</option>
                {MAHARASHTRA_DISTRICTS.map((d) => (
                  <option key={d} value={d}>
                    District: {d}
                  </option>
                ))}
              </select>
            </div>

            {/* Status Selector Filter */}
            <select
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value)}
              style={styles.filterSelect}
            >
              <option value="All">All Incident Statuses</option>
              <option value="Pending">Pending</option>
              <option value="Assigned">Assigned</option>
              <option value="In Progress">In Progress</option>
              <option value="Resolved">Resolved</option>
            </select>
          </div>
        </div>

        {/* Master Disasters Table with District-Smart Volunteer Assignment */}
        <div style={{ overflowX: "auto" }}>
          <table style={styles.table} border="1" cellPadding="12">
            <thead>
              <tr style={styles.tableHeaderRow}>
                <th style={{ width: "16%" }}>Disaster & AI Risk</th>
                <th style={{ width: "18%" }}>District & Location</th>
                <th style={{ width: "12%" }}>Evidence Photo</th>
                <th style={{ width: "14%" }}>Reported By</th>
                <th style={{ width: "10%" }}>Current Status</th>
                <th style={{ width: "20%" }}>District Volunteer Assignment</th>
                <th style={{ width: "10%" }}>Actions</th>
              </tr>
            </thead>

            <tbody>
              {filteredDisasters.length === 0 ? (
                <tr>
                  <td colSpan="7" style={{ textAlign: "center", padding: "30px", color: "#888" }}>
                    No disaster incidents match your search or district filter.
                  </td>
                </tr>
              ) : (
                filteredDisasters.map((d) => {
                  const incidentDistrict = (d.district || "Pune").toLowerCase();
                  const matchingVolunteers = volunteers.filter(
                    (v) => (v.district || "Pune").toLowerCase() === incidentDistrict
                  );
                  const otherVolunteers = volunteers.filter(
                    (v) => (v.district || "Pune").toLowerCase() !== incidentDistrict
                  );

                  return (
                    <tr key={d._id} style={{ background: "#fff" }}>
                      {/* Disaster & AI Risk */}
                      <td>
                        <strong style={{ fontSize: "15px", color: "#212529" }}>
                          {d.disasterType}
                        </strong>
                        <div style={{ marginTop: "4px", display: "flex", alignItems: "center", gap: "6px", flexWrap: "wrap" }}>
                          <span
                            style={{
                              backgroundColor:
                                (d.aiRiskScore || 5) >= 8
                                  ? "#d90429"
                                  : (d.aiRiskScore || 5) >= 6
                                  ? "#f77f00"
                                  : "#2b8a3e",
                              color: "white",
                              padding: "2px 7px",
                              borderRadius: "10px",
                              fontSize: "11px",
                              fontWeight: "700",
                            }}
                          >
                            AI Risk: {d.aiRiskScore || 5}/10
                          </span>
                          <span style={{ fontSize: "11px", color: "#666" }}>
                            {d.severity} Priority
                          </span>
                        </div>
                        <button
                          style={styles.aiBriefBtn}
                          onClick={() => setSelectedDisasterForAI(d)}
                        >
                          <span style={{ display: "inline-flex", alignItems: "center", gap: "5px" }}>
                            <FaRobot /> View AI Plan
                          </span>
                        </button>
                      </td>

                      {/* District & Location */}
                      <td>
                        <div style={styles.districtBadge}>
                          <FaMapMarkerAlt style={{ marginRight: 4 }} />
                          {d.district || "Pune"} District
                        </div>
                        <div style={{ marginTop: "4px", fontSize: "13.5px", color: "#333", fontWeight: "500" }}>
                          {d.location}
                        </div>
                        {d.latitude && d.longitude && (
                          <small style={{ color: "#777", display: "block", marginTop: "2px", fontSize: "11px" }}>
                            GPS: {d.latitude.toFixed(4)}, {d.longitude.toFixed(4)}
                          </small>
                        )}
                      </td>

                      {/* Photo */}
                      <td>
                        {d.image ? (
                          <img
                            src={`http://localhost:5000/uploads/${d.image}`}
                            alt="Disaster"
                            width="110"
                            height="75"
                            style={{
                              objectFit: "cover",
                              borderRadius: "8px",
                              border: "1px solid #dee2e6",
                            }}
                          />
                        ) : (
                          <span style={{ color: "#aaa", fontSize: "12px", fontStyle: "italic" }}>
                            No Image
                          </span>
                        )}
                      </td>

                      {/* Reporter Info */}
                      <td>
                        <strong>{d.reportedBy?.fullName || "Anonymous Citizen"}</strong>
                        <div style={{ color: "#666", fontSize: "12px", marginTop: "2px" }}>
                          {d.reportedBy?.email}
                        </div>
                        {d.reportedBy?.phone && (
                          <div style={{ color: "#0d6efd", fontSize: "11.5px", marginTop: "2px" }}>
                            <FaPhoneAlt size={10} style={{ marginRight: 3 }} /> {d.reportedBy.phone}
                          </div>
                        )}
                      </td>

                      {/* Status */}
                      <td>
                        <span
                          style={{
                            background:
                              d.status === "Pending"
                                ? "#f39c12"
                                : d.status === "Assigned"
                                ? "#0288d1"
                                : d.status === "In Progress"
                                ? "#3498db"
                                : "#27ae60",
                            color: "white",
                            padding: "5px 10px",
                            borderRadius: "15px",
                            fontWeight: "bold",
                            fontSize: "11.5px",
                            display: "inline-block",
                          }}
                        >
                          {d.status}
                        </span>
                      </td>

                      {/* District Volunteer Assignment */}
                      <td>
                        {d.assignedVolunteer ? (
                          <div style={{ marginBottom: "6px" }}>
                            <div
                              style={{
                                backgroundColor: "#e8f5e9",
                                border: "1px solid #c8e6c9",
                                color: "#2e7d32",
                                padding: "6px 10px",
                                borderRadius: "6px",
                                fontSize: "12.5px",
                                fontWeight: "bold",
                              }}
                            >
                              <FaUserCheck style={{ marginRight: 4 }} />
                              {d.assignedVolunteer.fullName}
                              <div style={{ fontSize: "11px", fontWeight: "normal", color: "#1b5e20", marginTop: "2px" }}>
                                District: <strong>{d.assignedVolunteer.district || d.district || "Pune"}</strong>
                                {d.assignedVolunteer.skills ? ` • ${d.assignedVolunteer.skills}` : ""}
                              </div>
                              {d.assignedVolunteer.phone && (
                                <div style={{ fontSize: "11px", color: "#2e7d32", marginTop: "2px", display: "flex", alignItems: "center", gap: "4px" }}>
                                  <FaPhoneAlt size={10} /> {d.assignedVolunteer.phone}
                                </div>
                              )}
                            </div>
                            <small style={{ display: "block", color: "#888", marginTop: "4px" }}>
                              Reassign to another volunteer:
                            </small>
                          </div>
                        ) : (
                          <div style={{ marginBottom: "6px" }}>
                            <div
                              style={{
                                backgroundColor: "#fff3cd",
                                border: "1px solid #ffeeba",
                                color: "#856404",
                                padding: "4px 8px",
                                borderRadius: "6px",
                                fontSize: "11.5px",
                                fontWeight: "bold",
                                display: "inline-flex",
                                alignItems: "center",
                                gap: "5px",
                                marginBottom: "4px",
                              }}
                            >
                              <FaExclamationTriangle size={11} /> Unassigned
                            </div>

                            {/* 1-Click Auto Dispatch Nearest District Volunteer */}
                            <button
                              type="button"
                              onClick={() => autoAssignDistrictVolunteer(d)}
                              style={styles.autoAssignBtn}
                              title="Instantly assign first available volunteer from this district"
                            >
                              <FaBolt style={{ marginRight: 4 }} />
                              1-Click District Dispatch
                            </button>
                          </div>
                        )}

                        {/* District-Categorized Volunteer Dropdown */}
                        <select
                          defaultValue=""
                          onChange={(e) => assignVolunteer(d._id, e.target.value)}
                          style={styles.dropdown}
                        >
                          <option value="">-- Choose District Volunteer --</option>
                          {matchingVolunteers.length > 0 && (
                            <optgroup label={`Matching District: ${d.district || "Pune"} (${matchingVolunteers.length} available)`}>
                              {matchingVolunteers.map((v) => (
                                <option key={v._id} value={v._id}>
                                  {v.fullName} [{v.district || "Pune"}] {v.skills ? `- ${v.skills}` : ""}
                                </option>
                              ))}
                            </optgroup>
                          )}
                          <optgroup label="Volunteers from Other Districts">
                            {otherVolunteers.map((v) => (
                              <option key={v._id} value={v._id}>
                                {v.fullName} [{v.district || "General"}] {v.skills ? `- ${v.skills}` : ""}
                              </option>
                            ))}
                          </optgroup>
                        </select>
                      </td>

                      {/* Actions */}
                      <td>
                        <div style={{ display: "flex", flexDirection: "column", gap: "5px" }}>
                          <button
                            style={styles.progressBtn}
                            onClick={() => updateStatus(d._id, "In Progress")}
                          >
                            In Progress
                          </button>

                          <button
                            style={styles.resolveBtn}
                            onClick={() => updateStatus(d._id, "Resolved")}
                          >
                            Resolve
                          </button>

                          <button
                            style={styles.deleteBtn}
                            onClick={() => deleteReport(d._id)}
                          >
                            Delete
                          </button>
                        </div>
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>

        {/* AI Action Plan & Briefing Modal */}
        {selectedDisasterForAI && (
          <div style={styles.modalOverlay}>
            <div style={styles.modalContent}>
              <div style={styles.modalHeader}>
                <h3 style={{ margin: 0, color: "#800020", display: "inline-flex", alignItems: "center", gap: "8px" }}>
                  <FaRobot /> AI Disaster Action Plan & Field Briefing
                </h3>
                <button
                  style={styles.modalCloseBtn}
                  onClick={() => setSelectedDisasterForAI(null)}
                >
                  <FaTimes />
                </button>
              </div>

              <div style={{ display: "flex", gap: "10px", margin: "14px 0", flexWrap: "wrap", alignItems: "center" }}>
                <span style={{ fontWeight: "bold", fontSize: "16px" }}>
                  {selectedDisasterForAI.disasterType}
                </span>
                <span style={{ fontSize: "13px", color: "#666", display: "inline-flex", alignItems: "center", gap: "4px" }}>
                  <FaMapMarkerAlt /> {selectedDisasterForAI.location} ({selectedDisasterForAI.district || "Pune"} District)
                </span>
                <span
                  style={{
                    backgroundColor:
                      (selectedDisasterForAI.aiRiskScore || 5) >= 8
                        ? "#d90429"
                        : "#f77f00",
                    color: "white",
                    padding: "2px 8px",
                    borderRadius: "10px",
                    fontSize: "12px",
                    fontWeight: "bold",
                  }}
                >
                  Risk: {selectedDisasterForAI.aiRiskScore || 5} / 10
                </span>
              </div>

              {selectedDisasterForAI.aiThreatAssessment && (
                <div style={{ marginBottom: "14px" }}>
                  <h4 style={{ color: "#800020", margin: "0 0 6px 0", fontSize: "14px" }}>
                    Threat Assessment:
                  </h4>
                  <p style={{ margin: 0, fontSize: "13.5px", lineHeight: "1.5" }}>
                    {selectedDisasterForAI.aiThreatAssessment}
                  </p>
                </div>
              )}

              {selectedDisasterForAI.aiActionPlan && selectedDisasterForAI.aiActionPlan.length > 0 && (
                <div style={{ marginBottom: "14px" }}>
                  <h4 style={{ color: "#800020", margin: "0 0 6px 0", fontSize: "14px" }}>
                    Citizen Immediate Action Plan (Dispatched via Email):
                  </h4>
                  <ol style={{ margin: 0, paddingLeft: "20px", fontSize: "13px" }}>
                    {selectedDisasterForAI.aiActionPlan.map((step, idx) => (
                      <li key={idx} style={{ marginBottom: "4px" }}>
                        {step}
                      </li>
                    ))}
                  </ol>
                </div>
              )}

              {selectedDisasterForAI.aiVolunteerBriefing && (
                <div
                  style={{
                    marginBottom: "14px",
                    backgroundColor: "#fff5f5",
                    borderLeft: "4px solid #800020",
                    padding: "10px 14px",
                    borderRadius: "4px",
                  }}
                >
                  <h4 style={{ color: "#800020", margin: "0 0 6px 0", fontSize: "14px" }}>
                    Volunteer Tactical Field Briefing (Sent upon Assignment):
                  </h4>
                  <p style={{ margin: 0, fontSize: "13px", lineHeight: "1.5" }}>
                    {selectedDisasterForAI.aiVolunteerBriefing}
                  </p>
                </div>
              )}

              {selectedDisasterForAI.aiRecommendedSupplies &&
                selectedDisasterForAI.aiRecommendedSupplies.length > 0 && (
                  <div style={{ marginBottom: "16px" }}>
                    <h4 style={{ color: "#495057", margin: "0 0 6px 0", fontSize: "13px" }}>
                      Recommended Equipment / Supplies:
                    </h4>
                    <div style={{ display: "flex", flexWrap: "wrap", gap: "6px" }}>
                      {selectedDisasterForAI.aiRecommendedSupplies.map((s, idx) => (
                        <span
                          key={idx}
                          style={{
                            backgroundColor: "#e2e8f0",
                            padding: "3px 8px",
                            borderRadius: "10px",
                            fontSize: "11.5px",
                          }}
                        >
                          • {s}
                        </span>
                      ))}
                    </div>
                  </div>
                )}

              <button
                style={styles.modalDoneBtn}
                onClick={() => setSelectedDisasterForAI(null)}
              >
                Close Advisory
              </button>
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
    padding: "30px 24px",
    background: "#f4f6f9",
    minHeight: "100vh",
  },

  headerBar: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    marginBottom: "24px",
    flexWrap: "wrap",
    gap: "16px",
  },

  badge: {
    display: "inline-block",
    padding: "4px 12px",
    backgroundColor: "#fff0f2",
    color: "#800020",
    borderRadius: "12px",
    fontSize: "11px",
    fontWeight: "800",
    letterSpacing: "0.8px",
    marginBottom: "6px",
  },

  commandTitle: {
    color: "#800020",
    fontSize: "28px",
    fontWeight: "800",
    margin: "0 0 6px 0",
  },

  commandSub: {
    margin: 0,
    color: "#666",
    fontSize: "14px",
  },

  refreshBtn: {
    background: "#ffffff",
    color: "#800020",
    border: "1px solid #800020",
    padding: "10px 18px",
    borderRadius: "8px",
    cursor: "pointer",
    fontSize: "14px",
    fontWeight: "600",
    display: "flex",
    alignItems: "center",
  },

  downloadPdfBtn: {
    background: "#800020",
    color: "white",
    border: "none",
    padding: "10px 18px",
    borderRadius: "8px",
    cursor: "pointer",
    fontSize: "14px",
    fontWeight: "bold",
    display: "flex",
    alignItems: "center",
    boxShadow: "0 2px 6px rgba(128,0,32,0.3)",
  },

  stats: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit,minmax(200px,1fr))",
    gap: "18px",
    marginBottom: "24px",
  },

  statCard: {
    background: "#fff",
    borderRadius: "14px",
    padding: "20px 24px",
    textAlign: "center",
    boxShadow: "0 4px 14px rgba(0,0,0,0.06)",
    border: "1px solid #edf2f7",
  },

  statLabel: {
    fontSize: "13px",
    color: "#718096",
    marginTop: "6px",
    fontWeight: "600",
  },

  filterSection: {
    backgroundColor: "#ffffff",
    borderRadius: "14px",
    padding: "18px 22px",
    marginBottom: "20px",
    boxShadow: "0 4px 14px rgba(0,0,0,0.06)",
    border: "1px solid #edf2f7",
  },

  filterTitle: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    fontSize: "16px",
    fontWeight: "700",
    color: "#800020",
    marginBottom: "14px",
    flexWrap: "wrap",
    gap: "8px",
  },

  searchBarRow: {
    display: "flex",
    gap: "14px",
    flexWrap: "wrap",
  },

  searchInputWrap: {
    flex: 1,
    minWidth: "260px",
    display: "flex",
    alignItems: "center",
    border: "1px solid #cbd5e1",
    borderRadius: "8px",
    padding: "10px 14px",
    background: "#f8fafc",
  },

  searchInput: {
    flex: 1,
    border: "none",
    background: "transparent",
    outline: "none",
    fontSize: "14px",
  },

  filterSelect: {
    padding: "10px 14px",
    borderRadius: "8px",
    border: "1px solid #cbd5e1",
    fontSize: "13.5px",
    background: "#ffffff",
    cursor: "pointer",
    minWidth: "190px",
  },

  table: {
    width: "100%",
    background: "white",
    borderCollapse: "collapse",
    borderRadius: "12px",
    overflow: "hidden",
    boxShadow: "0 4px 14px rgba(0,0,0,0.06)",
    borderColor: "#edf2f7",
  },

  tableHeaderRow: {
    background: "linear-gradient(135deg, #800020, #5c0013)",
    color: "white",
    fontSize: "13px",
    textAlign: "left",
  },

  districtBadge: {
    display: "inline-flex",
    alignItems: "center",
    backgroundColor: "#fbebee",
    color: "#800020",
    padding: "3px 8px",
    borderRadius: "6px",
    fontSize: "11.5px",
    fontWeight: "700",
  },

  autoAssignBtn: {
    backgroundColor: "#800020",
    color: "#fff",
    border: "none",
    padding: "5px 9px",
    borderRadius: "6px",
    fontSize: "11px",
    fontWeight: "700",
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
    marginTop: "4px",
    boxShadow: "0 2px 5px rgba(128,0,32,0.25)",
  },

  dropdown: {
    width: "100%",
    padding: "8px",
    borderRadius: "6px",
    border: "1px solid #cbd5e1",
    fontSize: "12px",
    background: "#fff",
    marginTop: "4px",
  },

  progressBtn: {
    background: "#0d6efd",
    color: "white",
    border: "none",
    padding: "6px 10px",
    borderRadius: "5px",
    cursor: "pointer",
    fontSize: "11px",
    fontWeight: "600",
  },

  resolveBtn: {
    background: "#198754",
    color: "white",
    border: "none",
    padding: "6px 10px",
    borderRadius: "5px",
    cursor: "pointer",
    fontSize: "11px",
    fontWeight: "600",
  },

  deleteBtn: {
    background: "#dc3545",
    color: "white",
    border: "none",
    padding: "6px 10px",
    borderRadius: "5px",
    cursor: "pointer",
    fontSize: "11px",
    fontWeight: "600",
  },

  aiBriefBtn: {
    marginTop: "6px",
    background: "#fff0f0",
    color: "#800020",
    border: "1px solid #800020",
    padding: "4px 8px",
    borderRadius: "6px",
    fontSize: "11px",
    fontWeight: "bold",
    cursor: "pointer",
    display: "inline-block",
  },

  modalOverlay: {
    position: "fixed",
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: "rgba(0, 0, 0, 0.65)",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    zIndex: 1000,
    padding: "20px",
  },

  modalContent: {
    backgroundColor: "#ffffff",
    borderRadius: "14px",
    padding: "24px 28px",
    maxWidth: "650px",
    width: "100%",
    maxHeight: "85vh",
    overflowY: "auto",
    boxShadow: "0 10px 30px rgba(0, 0, 0, 0.25)",
  },

  modalHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    borderBottom: "1px solid #e9ecef",
    paddingBottom: "12px",
  },

  modalCloseBtn: {
    background: "transparent",
    border: "none",
    fontSize: "18px",
    cursor: "pointer",
    color: "#868e96",
  },

  modalDoneBtn: {
    width: "100%",
    backgroundColor: "#800020",
    color: "#ffffff",
    border: "none",
    padding: "10px",
    borderRadius: "8px",
    fontSize: "14px",
    fontWeight: "bold",
    cursor: "pointer",
    marginTop: "10px",
  },
};

export default AdminDashboard;