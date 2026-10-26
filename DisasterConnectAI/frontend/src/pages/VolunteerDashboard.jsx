import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import API from "../services/api";
import {
  FaShieldAlt,
  FaMapMarkerAlt,
  FaCheckCircle,
  FaClock,
  FaInbox,
  FaSyncAlt,
  FaPlay,
  FaCheck,
  FaFileAlt,
  FaInfoCircle,
  FaExternalLinkAlt,
} from "react-icons/fa";

function VolunteerDashboard() {
  const user = JSON.parse(localStorage.getItem("user") || "null");

  const [disasters, setDisasters] = useState([]);
  const [notifications, setNotifications] = useState([]);
  const [activeTab, setActiveTab] = useState("missions");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (user?._id) {
      fetchAssignedDisasters();
      fetchNotifications();
    }
  }, [user?._id]);

  const fetchAssignedDisasters = async () => {
    try {
      setLoading(true);
      if (!user?._id) return;
      const res = await API.get(
        `/disasters/volunteer/${user._id}`
      );
      setDisasters(res.data);
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  };

  const fetchNotifications = async () => {
    try {
      if (!user?._id) return;
      const res = await API.get(`/notifications/volunteer/${user._id}`);
      setNotifications(res.data);
    } catch (error) {
      console.error(error);
    }
  };
    const updateStatus = async (id, status) => {
    try {
      let resolutionNotes = "";
      if (status === "Resolved") {
        const input = window.prompt(
          "Enter brief resolution notes for the reporting citizen and command center (e.g. 'All residents safely evacuated, medical aid rendered'):",
          "Relief operations successfully concluded."
        );
        if (input === null) return; // User cancelled
        resolutionNotes = input.trim();
      }

      await API.put(`/disasters/${id}`, {
        status,
        resolutionNotes,
      });

      alert(
        status === "Resolved"
          ? "Mission marked Resolved. Notification dispatched to reporter."
          : `Status updated to ${status}`
      );
      fetchAssignedDisasters();

    } catch (error) {
      console.log(error);
      alert("Failed to update status.");
    }
  };

  const handleAcknowledge = async (id) => {
    try {
      await API.put(`/notifications/${id}/acknowledge`);
      fetchNotifications();
      alert("Mission order acknowledged.");
    } catch (err) {
      console.error(err);
    }
  };

  const unacknowledgedCount = notifications.filter((n) => !n.acknowledged).length;

  return (
    <>
      <Navbar />

      <div style={styles.container}>
        {/* Header */}
        <div style={styles.headerBar}>
          <div>
            <div style={styles.badgeTop}>
              <FaShieldAlt style={{ marginRight: 6 }} />
              VOLUNTEER FIELD OPERATIONS CONSOLE
            </div>
            <h1 style={styles.heading}>Field Operations & Mission Dispatch</h1>
            <p style={styles.subtitle}>
              Responder: <strong>{user.fullName}</strong> • District: <strong>{user.district || "Pune"}</strong> • Specialization: <strong>{user.skills?.[0] || "Emergency Response"}</strong>
            </p>
          </div>

          <div style={{ display: "flex", gap: "10px", alignItems: "center" }}>
            <button
              onClick={() => {
                fetchAssignedDisasters();
                fetchNotifications();
              }}
              style={styles.refreshBtn}
            >
              <FaSyncAlt style={{ marginRight: 6 }} /> Refresh
            </button>
            <Link to="/volunteer/inbox" style={styles.inboxBtn}>
              <FaInbox style={{ marginRight: 6 }} /> Dispatch Comms
              {unacknowledgedCount > 0 && (
                <span style={styles.unreadBadge}>{unacknowledgedCount}</span>
              )}
            </Link>
          </div>
        </div>

        {/* Tab Selection */}
        <div style={styles.tabContainer}>
          <button
            onClick={() => setActiveTab("missions")}
            style={{
              ...styles.tabBtn,
              ...(activeTab === "missions" ? styles.tabBtnActive : {}),
            }}
          >
            Assigned Emergency Missions ({disasters.length})
          </button>

          <button
            onClick={() => setActiveTab("comms")}
            style={{
              ...styles.tabBtn,
              ...(activeTab === "comms" ? styles.tabBtnActive : {}),
            }}
          >
            Official Dispatch Transmissions ({notifications.length})
            {unacknowledgedCount > 0 && (
              <span style={styles.tabAlertPill}>{unacknowledgedCount} New</span>
            )}
          </button>
        </div>

        {/* TAB 1: Assigned Emergency Missions */}
        {activeTab === "missions" && (
          <div>
            {loading ? (
              <div style={{ textAlign: "center", padding: "60px", color: "#64748b" }}>
                Loading assigned missions...
              </div>
            ) : disasters.length === 0 ? (
              <div style={styles.emptyBox}>
                <FaShieldAlt size={38} color="#94a3b8" />
                <h3 style={{ margin: "14px 0 6px 0", color: "#0f172a" }}>No Active Missions Assigned</h3>
                <p style={{ margin: 0, color: "#64748b", fontSize: "14px" }}>
                  You currently have no pending disaster deployments assigned by District Command. You will receive an immediate in-app order and email dispatch when assigned.
                </p>
              </div>
            ) : (
              <div style={styles.grid}>
                {disasters.map((d) => (
                  <div key={d._id} style={styles.card}>
                    <div style={styles.cardHead}>
                      <div>
                        <span style={styles.districtBadge}>
                          <FaMapMarkerAlt style={{ marginRight: 4 }} />
                          {d.district || "Pune"} District
                        </span>
                        <h2 style={styles.title}>{d.disasterType}</h2>
                      </div>
                      <span
                        style={{
                          backgroundColor:
                            (d.aiRiskScore || 5) >= 8
                              ? "#dc2626"
                              : (d.aiRiskScore || 5) >= 6
                              ? "#ea580c"
                              : "#16a34a",
                          color: "white",
                          padding: "3px 8px",
                          borderRadius: "6px",
                          fontSize: "11px",
                          fontWeight: "700",
                        }}
                      >
                        Risk: {d.aiRiskScore || 5}/10 ({d.severity})
                      </span>
                    </div>

                    {d.image && (
                      <img
                        src={`http://localhost:5000/uploads/${d.image}`}
                        alt="Disaster Scene"
                        style={styles.cardImage}
                      />
                    )}

                    <p style={{ margin: "6px 0", fontSize: "13.5px" }}>
                      <strong>Location:</strong> {d.location}
                    </p>

                    <p style={{ margin: "6px 0", fontSize: "13px", color: "#475569" }}>
                      <strong>Description:</strong> {d.description}
                    </p>

                    <p style={{ margin: "6px 0", fontSize: "12.5px", color: "#64748b" }}>
                      <strong>Reported By:</strong> {d.reportedBy?.fullName || "Citizen"} ({d.reportedBy?.email})
                    </p>

                    {/* AI Tactical Field Briefing */}
                    {d.aiVolunteerBriefing && (
                      <div style={styles.briefingBox}>
                        <div style={styles.briefingTitle}>
                          <FaFileAlt style={{ marginRight: 6 }} /> AI Tactical Field Briefing:
                        </div>
                        <p style={{ margin: "4px 0 0 0", fontSize: "13px", color: "#1e293b", lineHeight: "1.45" }}>
                          {d.aiVolunteerBriefing}
                        </p>
                      </div>
                    )}

                    {/* Recommended Field Gear */}
                    {d.aiRecommendedSupplies && d.aiRecommendedSupplies.length > 0 && (
                      <div style={{ marginBottom: "12px" }}>
                        <small style={{ fontWeight: "700", color: "#475569", fontSize: "11px", textTransform: "uppercase" }}>
                          Recommended Field Gear:
                        </small>
                        <div style={{ display: "flex", flexWrap: "wrap", gap: "5px", marginTop: "4px" }}>
                          {d.aiRecommendedSupplies.map((item, idx) => (
                            <span key={idx} style={styles.supplyBadge}>
                              {item}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}

                    {/* Resolution Notes */}
                    {d.resolutionNotes && (
                      <div style={styles.resolutionBox}>
                        <strong style={{ fontSize: "12px", color: "#166534" }}>Resolution Summary:</strong>
                        <p style={{ margin: "2px 0 0 0", fontSize: "12.5px", color: "#14532d" }}>
                          {d.resolutionNotes}
                        </p>
                      </div>
                    )}

                    <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", margin: "10px 0" }}>
                      <span style={{ fontSize: "13px", fontWeight: "600", color: "#475569" }}>Status:</span>
                      <span
                        style={{
                          ...styles.badge,
                          backgroundColor:
                            d.status === "Pending"
                              ? "#f59e0b"
                              : d.status === "Assigned"
                              ? "#0284c7"
                              : d.status === "In Progress"
                              ? "#2563eb"
                              : "#16a34a",
                        }}
                      >
                        {d.status}
                      </span>
                    </div>

                    <div style={{ display: "flex", gap: "8px", marginTop: "12px" }}>
                      {d.status !== "In Progress" && d.status !== "Resolved" && (
                        <button
                          style={styles.progressBtn}
                          onClick={() => updateStatus(d._id, "In Progress")}
                        >
                          <FaPlay size={10} style={{ marginRight: 6 }} /> Start Relief Work
                        </button>
                      )}

                      {d.status !== "Resolved" && (
                        <button
                          style={styles.resolveBtn}
                          onClick={() => updateStatus(d._id, "Resolved")}
                        >
                          <FaCheck size={11} style={{ marginRight: 6 }} /> Mark Resolved
                        </button>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {/* TAB 2: Official Dispatch Transmissions */}
        {activeTab === "comms" && (
          <div>
            <div style={styles.commsIntroCard}>
              <FaInfoCircle size={18} color="#0284c7" style={{ marginRight: 10, flexShrink: 0 }} />
              <div>
                <strong style={{ color: "#0369a1", fontSize: "13.5px" }}>
                  Official Emergency Communications System
                </strong>
                <p style={{ margin: "4px 0 0 0", fontSize: "12.5px", color: "#334155", lineHeight: "1.5" }}>
                  Every mission dispatched to you by District Command is logged here with zero data loss. If external SMTP is blocked or not configured in <code>backend/.env</code>, you can review the full briefing, orders, and browser preview here.
                </p>
              </div>
            </div>

            {notifications.length === 0 ? (
              <div style={styles.emptyBox}>
                <FaInbox size={36} color="#94a3b8" />
                <h3 style={{ margin: "14px 0 6px 0", color: "#0f172a" }}>No Communications Logged</h3>
                <p style={{ margin: 0, color: "#64748b", fontSize: "13.5px" }}>
                  Your dispatch comms history will appear here once incident assignments are made.
                </p>
              </div>
            ) : (
              <div style={styles.notifList}>
                {notifications.map((msg) => (
                  <div key={msg._id} style={styles.notifCard}>
                    <div style={styles.notifHead}>
                      <div>
                        <div style={{ display: "flex", gap: "8px", alignItems: "center", marginBottom: "4px" }}>
                          <span style={styles.notifTypeTag}>OFFICIAL ORDER</span>
                          <span style={{ fontSize: "11px", color: "#64748b" }}>
                            Ref: #{msg._id.slice(-6)}
                          </span>
                        </div>
                        <h3 style={styles.notifSubject}>{msg.subject}</h3>
                        <small style={{ color: "#64748b" }}>
                          <FaClock size={10} style={{ marginRight: 4 }} />
                          {new Date(msg.createdAt).toLocaleString()}
                        </small>
                      </div>

                      <div style={{ textAlign: "right" }}>
                        <span
                          style={{
                            ...styles.channelTag,
                            backgroundColor:
                              msg.deliveryStatus === "sent_smtp"
                                ? "#dcfce7"
                                : msg.deliveryStatus === "ethereal_preview"
                                ? "#ede9fe"
                                : "#e0f2fe",
                            color:
                              msg.deliveryStatus === "sent_smtp"
                                ? "#166534"
                                : msg.deliveryStatus === "ethereal_preview"
                                ? "#6d28d9"
                                : "#0369a1",
                          }}
                        >
                          {msg.deliveryStatus === "sent_smtp"
                            ? "Sent via SMTP"
                            : msg.deliveryStatus === "ethereal_preview"
                            ? "Ethereal Preview"
                            : "Delivered In-App"}
                        </span>

                        <div style={{ marginTop: 8 }}>
                          {msg.acknowledged ? (
                            <span style={{ color: "#16a34a", fontSize: "12px", fontWeight: "700" }}>
                              <FaCheckCircle style={{ marginRight: 4 }} /> Acknowledged
                            </span>
                          ) : (
                            <button
                              onClick={() => handleAcknowledge(msg._id)}
                              style={styles.ackSmallBtn}
                            >
                              <FaCheck size={10} style={{ marginRight: 4 }} /> Acknowledge Order
                            </button>
                          )}
                        </div>
                      </div>
                    </div>

                    {msg.previewUrl && (
                      <div style={{ margin: "10px 0" }}>
                        <a
                          href={msg.previewUrl}
                          target="_blank"
                          rel="noreferrer"
                          style={styles.etherealLink}
                        >
                          <FaExternalLinkAlt size={11} style={{ marginRight: 4 }} /> View Formatted HTML Email in Browser
                        </a>
                      </div>
                    )}

                    <div
                      style={styles.notifHtmlBody}
                      dangerouslySetInnerHTML={{
                        __html: msg.messageHtml || msg.messageText.replace(/\n/g, "<br/>"),
                      }}
                    />
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
      </div>

      <Footer />
    </>
  );
}const styles = {
  container: {
    minHeight: "90vh",
    background: "#f8fafc",
    padding: "36px 30px",
    maxWidth: "1350px",
    margin: "0 auto",
  },

  headerBar: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    marginBottom: "20px",
    flexWrap: "wrap",
    gap: "16px",
  },

  badgeTop: {
    display: "inline-flex",
    alignItems: "center",
    backgroundColor: "#fff1f2",
    color: "#800020",
    padding: "4px 12px",
    borderRadius: "12px",
    fontSize: "11px",
    fontWeight: "800",
    letterSpacing: "0.8px",
    marginBottom: "6px",
  },

  heading: {
    color: "#0f172a",
    margin: "0 0 6px 0",
    fontSize: "30px",
    fontWeight: "800",
  },

  subtitle: {
    color: "#475569",
    fontSize: "13.5px",
    margin: 0,
  },

  refreshBtn: {
    backgroundColor: "#ffffff",
    border: "1px solid #cbd5e1",
    color: "#334155",
    padding: "9px 16px",
    borderRadius: "8px",
    fontSize: "13px",
    fontWeight: "600",
    cursor: "pointer",
    display: "inline-flex",
    alignItems: "center",
  },

  inboxBtn: {
    backgroundColor: "#800020",
    color: "#ffffff",
    padding: "9px 16px",
    borderRadius: "8px",
    fontSize: "13px",
    fontWeight: "700",
    textDecoration: "none",
    display: "inline-flex",
    alignItems: "center",
  },

  unreadBadge: {
    backgroundColor: "#ef4444",
    color: "#fff",
    fontSize: "11px",
    fontWeight: "800",
    padding: "2px 6px",
    borderRadius: "10px",
    marginLeft: "6px",
  },

  tabContainer: {
    display: "flex",
    gap: "10px",
    marginBottom: "24px",
    borderBottom: "1px solid #e2e8f0",
    paddingBottom: "10px",
  },

  tabBtn: {
    padding: "10px 18px",
    borderRadius: "8px",
    border: "1px solid transparent",
    backgroundColor: "#f1f5f9",
    color: "#475569",
    fontWeight: "700",
    fontSize: "13.5px",
    cursor: "pointer",
    display: "inline-flex",
    alignItems: "center",
  },

  tabBtnActive: {
    backgroundColor: "#800020",
    color: "#ffffff",
  },

  tabAlertPill: {
    backgroundColor: "#ef4444",
    color: "#ffffff",
    fontSize: "11px",
    padding: "2px 6px",
    borderRadius: "8px",
    marginLeft: "8px",
  },

  emptyBox: {
    background: "white",
    padding: "60px 20px",
    borderRadius: "14px",
    textAlign: "center",
    border: "1px solid #e2e8f0",
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit,minmax(340px,1fr))",
    gap: "22px",
  },

  card: {
    background: "white",
    padding: "22px",
    borderRadius: "14px",
    border: "1px solid #e2e8f0",
    boxShadow: "0 3px 10px rgba(0,0,0,.03)",
  },

  cardHead: {
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
    display: "inline-flex",
    alignItems: "center",
  },

  title: {
    color: "#0f172a",
    fontSize: "18px",
    fontWeight: "800",
    margin: "4px 0 0 0",
  },

  cardImage: {
    width: "100%",
    height: "160px",
    objectFit: "cover",
    borderRadius: "8px",
    marginBottom: "12px",
    border: "1px solid #f1f5f9",
  },

  briefingBox: {
    backgroundColor: "#fff1f2",
    borderLeft: "4px solid #800020",
    padding: "10px 12px",
    borderRadius: "6px",
    margin: "12px 0",
  },

  briefingTitle: {
    color: "#800020",
    fontSize: "11.5px",
    fontWeight: "800",
    textTransform: "uppercase",
    display: "flex",
    alignItems: "center",
  },

  supplyBadge: {
    backgroundColor: "#f1f5f9",
    color: "#334155",
    fontSize: "11px",
    fontWeight: "600",
    padding: "2px 7px",
    borderRadius: "6px",
    border: "1px solid #e2e8f0",
  },

  resolutionBox: {
    backgroundColor: "#f0fdf4",
    border: "1px solid #bbf7d0",
    padding: "8px 12px",
    borderRadius: "6px",
    marginBottom: "12px",
  },

  badge: {
    color: "white",
    padding: "4px 10px",
    borderRadius: "6px",
    fontWeight: "700",
    fontSize: "11.5px",
  },

  progressBtn: {
    flex: 1,
    background: "#2563eb",
    color: "white",
    border: "none",
    padding: "10px",
    borderRadius: "8px",
    cursor: "pointer",
    fontSize: "12px",
    fontWeight: "700",
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
  },

  resolveBtn: {
    flex: 1,
    background: "#16a34a",
    color: "white",
    border: "none",
    padding: "10px",
    borderRadius: "8px",
    cursor: "pointer",
    fontSize: "12px",
    fontWeight: "700",
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
  },

  commsIntroCard: {
    backgroundColor: "#f0f9ff",
    border: "1px solid #bae6fd",
    borderRadius: "12px",
    padding: "14px 18px",
    display: "flex",
    alignItems: "flex-start",
    marginBottom: "20px",
  },

  notifList: {
    display: "flex",
    flexDirection: "column",
    gap: "16px",
  },

  notifCard: {
    background: "#ffffff",
    border: "1px solid #e2e8f0",
    borderRadius: "14px",
    padding: "20px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.03)",
  },

  notifHead: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    borderBottom: "1px solid #f1f5f9",
    paddingBottom: "12px",
    marginBottom: "12px",
    gap: "14px",
    flexWrap: "wrap",
  },

  notifTypeTag: {
    fontSize: "10.5px",
    fontWeight: "800",
    backgroundColor: "#fff1f2",
    color: "#800020",
    padding: "2px 6px",
    borderRadius: "4px",
  },

  notifSubject: {
    fontSize: "16px",
    fontWeight: "800",
    color: "#0f172a",
    margin: "4px 0",
  },

  channelTag: {
    fontSize: "11px",
    fontWeight: "700",
    padding: "3px 8px",
    borderRadius: "6px",
    display: "inline-block",
  },

  ackSmallBtn: {
    backgroundColor: "#16a34a",
    color: "#ffffff",
    border: "none",
    padding: "5px 10px",
    borderRadius: "6px",
    fontSize: "11px",
    fontWeight: "700",
    cursor: "pointer",
    display: "inline-flex",
    alignItems: "center",
  },

  etherealLink: {
    color: "#7e22ce",
    fontSize: "12px",
    fontWeight: "700",
    textDecoration: "underline",
    display: "inline-flex",
    alignItems: "center",
  },

  notifHtmlBody: {
    backgroundColor: "#fafafa",
    border: "1px solid #f1f5f9",
    borderRadius: "8px",
    padding: "14px",
    fontSize: "13.5px",
    lineHeight: "1.5",
    color: "#1e293b",
  },

  loginCard: {
    textAlign: "center",
    padding: "80px 20px",
    maxWidth: "500px",
    margin: "0 auto",
  },

  loginBtn: {
    display: "inline-block",
    marginTop: "14px",
    backgroundColor: "#800020",
    color: "#ffffff",
    padding: "10px 20px",
    borderRadius: "8px",
    textDecoration: "none",
    fontWeight: "700",
  },
};

export default VolunteerDashboard;