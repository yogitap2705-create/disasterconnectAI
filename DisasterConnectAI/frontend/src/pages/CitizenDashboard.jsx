import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import API from "../services/api";
import { FaCheckCircle, FaRobot, FaShieldAlt, FaTimes } from "react-icons/fa";

function CitizenDashboard() {
  const user = JSON.parse(localStorage.getItem("user") || "null");

  const [reports, setReports] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    if (user?._id) {
      fetchReports();
    }
  }, [user?._id]);

  const fetchReports = async () => {
    try {
      const res = await API.get("/disasters");

      const myReports = res.data.filter(
        (d) => d.reportedBy?._id === user?._id
      );

      setReports(myReports);
    } catch (error) {
      console.log(error);
    }
  };

  const filteredReports = reports.filter(
    (d) =>
      d.disasterType
        .toLowerCase()
        .includes(search.toLowerCase()) ||
      d.location
        .toLowerCase()
        .includes(search.toLowerCase())
  );

  const [selectedAIPlan, setSelectedAIPlan] = useState(null);

  return (
    <>
      <Navbar />

      <div style={styles.container}>
        <h1 style={styles.heading}>
          Welcome, {user?.fullName || "Citizen"}
        </h1>

        <div style={styles.stats}>
          <div style={styles.card}>
            <h2>{reports.length}</h2>
            <p>Total Reports</p>
          </div>

          <div style={styles.card}>
            <h2>
              {reports.filter((r) => r.status === "Pending").length}
            </h2>
            <p>Pending</p>
          </div>

          <div style={styles.card}>
            <h2>
              {reports.filter((r) => r.status === "In Progress" || r.status === "Assigned").length}
            </h2>
            <p>In Progress / Assigned</p>
          </div>

          <div style={styles.card}>
            <h2>
              {reports.filter((r) => r.status === "Resolved").length}
            </h2>
            <p>Resolved</p>
          </div>
        </div>

        <input
          type="text"
          placeholder="Search by disaster or location..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          style={styles.search}
        />

        <table
          style={styles.table}
          border="1"
          cellPadding="10"
        >
          <thead>
            <tr>
              <th>Disaster & Priority</th>
              <th>Location</th>
              <th>Description</th>
              <th>Assigned Volunteer</th>
              <th>Image</th>
              <th>Status</th>
              <th>AI Advisory</th>
            </tr>
          </thead>

          <tbody>
            {filteredReports.map((report) => (
              <tr key={report._id}>
                <td>
                  <strong>{report.disasterType}</strong>
                  <div style={{ marginTop: "4px" }}>
                    <span
                      style={{
                        backgroundColor:
                          (report.aiRiskScore || 5) >= 8
                            ? "#d90429"
                            : (report.aiRiskScore || 5) >= 6
                            ? "#f77f00"
                            : "#2b8a3e",
                        color: "white",
                        padding: "2px 7px",
                        borderRadius: "10px",
                        fontSize: "11px",
                        fontWeight: "700",
                      }}
                    >
                      Risk: {report.aiRiskScore || 5}/10
                    </span>
                  </div>
                </td>

                <td>{report.location}</td>

                <td>{report.description}</td>

                <td>
                  {report.assignedVolunteer ? (
                    <span
                      style={{
                        backgroundColor: "#e8f5e9",
                        color: "#2e7d32",
                        padding: "4px 8px",
                        borderRadius: "6px",
                        fontSize: "12px",
                        fontWeight: "bold",
                        display: "inline-block",
                      }}
                    >
                      <FaCheckCircle size={11} style={{ marginRight: 4 }} />
                      {report.assignedVolunteer.fullName}
                    </span>
                  ) : (
                    <span style={{ color: "#888", fontSize: "12px" }}>
                      Awaiting Volunteer
                    </span>
                  )}
                </td>

                <td>
                  {report.image ? (
                    <img
                      src={`http://localhost:5000/uploads/${report.image}`}
                      alt="Disaster"
                      width="120"
                      height="80"
                      style={{
                        objectFit: "cover",
                        borderRadius: "10px",
                      }}
                    />
                  ) : (
                    "No Image"
                  )}
                </td>

                <td>
                  <span
                    style={{
                      padding: "8px 15px",
                      borderRadius: "20px",
                      color: "white",
                      fontWeight: "bold",
                      fontSize: "12px",
                      display: "inline-block",
                      backgroundColor:
                        report.status === "Pending"
                          ? "#f39c12"
                          : report.status === "In Progress" || report.status === "Assigned"
                          ? "#3498db"
                          : "#2ecc71",
                    }}
                  >
                    {report.status}
                  </span>
                </td>

                <td>
                  <button
                    onClick={() => setSelectedAIPlan(report)}
                    style={{
                      backgroundColor: "#800020",
                      color: "white",
                      border: "none",
                      padding: "6px 10px",
                      borderRadius: "6px",
                      cursor: "pointer",
                      display: "inline-flex",
                      alignItems: "center",
                      gap: "5px",
                    }}
                  >
                    <FaRobot /> View AI Plan
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {/* AI Action Plan Modal */}
        {selectedAIPlan && (
          <div
            style={{
              position: "fixed",
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              backgroundColor: "rgba(0, 0, 0, 0.6)",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              zIndex: 1000,
              padding: "20px",
            }}
          >
            <div
              style={{
                backgroundColor: "#fff",
                borderRadius: "14px",
                padding: "24px 28px",
                maxWidth: "600px",
                width: "100%",
                maxHeight: "85vh",
                overflowY: "auto",
                boxShadow: "0 10px 30px rgba(0,0,0,0.25)",
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", borderBottom: "1px solid #eee", paddingBottom: "10px" }}>
                <h2 style={{ margin: 0, color: "#800020", fontSize: "20px", display: "inline-flex", alignItems: "center", gap: "8px" }}>
                  <FaShieldAlt /> AI Survival Action Plan
                </h2>
                <button
                  onClick={() => setSelectedAIPlan(null)}
                  style={{ background: "none", border: "none", fontSize: "16px", cursor: "pointer", color: "#888" }}
                >
                  <FaTimes />
                </button>
              </div>

              <div style={{ margin: "14px 0", padding: "10px 14px", backgroundColor: "#fff5f5", borderLeft: "4px solid #800020", borderRadius: "4px" }}>
                <strong style={{ color: "#800020", fontSize: "13px" }}>Threat Assessment:</strong>
                <p style={{ margin: "4px 0 0 0", fontSize: "13.5px" }}>
                  {selectedAIPlan.aiThreatAssessment || "Active emergency incident. Follow safety protocols below."}
                </p>
              </div>

              {selectedAIPlan.aiActionPlan && selectedAIPlan.aiActionPlan.length > 0 && (
                <div style={{ marginBottom: "16px" }}>
                  <h4 style={{ color: "#800020", margin: "0 0 8px 0" }}>What You Must Do:</h4>
                  <ol style={{ margin: 0, paddingLeft: "20px", fontSize: "13.5px" }}>
                    {selectedAIPlan.aiActionPlan.map((s, idx) => (
                      <li key={idx} style={{ marginBottom: "6px" }}>{s}</li>
                    ))}
                  </ol>
                </div>
              )}

              {selectedAIPlan.aiRecommendedSupplies && selectedAIPlan.aiRecommendedSupplies.length > 0 && (
                <div style={{ marginBottom: "16px" }}>
                  <strong style={{ fontSize: "12px", color: "#666" }}>Recommended Emergency Supplies:</strong>
                  <div style={{ display: "flex", flexWrap: "wrap", gap: "6px", marginTop: "6px" }}>
                    {selectedAIPlan.aiRecommendedSupplies.map((item, idx) => (
                      <span key={idx} style={{ backgroundColor: "#e9ecef", padding: "3px 8px", borderRadius: "10px", fontSize: "12px" }}>
                        • {item}
                      </span>
                    ))}
                  </div>
                </div>
              )}

              <button
                onClick={() => setSelectedAIPlan(null)}
                style={{
                  width: "100%",
                  backgroundColor: "#800020",
                  color: "#fff",
                  border: "none",
                  padding: "10px",
                  borderRadius: "8px",
                  fontWeight: "bold",
                  cursor: "pointer",
                }}
              >
                Close Plan
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
    padding: "35px",
    background: "#F8F8F8",
    minHeight: "100vh",
  },

  heading: {
    color: "#800020",
    marginBottom: "30px",
    textAlign: "center",
    fontSize: "35px",
  },

  stats: {
    display: "flex",
    justifyContent: "space-between",
    gap: "20px",
    marginBottom: "30px",
    flexWrap: "wrap",
  },

  card: {
    flex: 1,
    minWidth: "200px",
    background: "white",
    padding: "20px",
    borderRadius: "15px",
    textAlign: "center",
    boxShadow: "0 5px 12px rgba(0,0,0,0.1)",
  },

  search: {
    width: "100%",
    padding: "15px",
    borderRadius: "10px",
    border: "1px solid lightgray",
    marginBottom: "25px",
    fontSize: "16px",
  },

  table: {
    width: "100%",
    borderCollapse: "collapse",
    background: "white",
    boxShadow: "0 5px 15px rgba(0,0,0,0.1)",
    borderRadius: "15px",
    overflow: "hidden",
  },

};

export default CitizenDashboard;