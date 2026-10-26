import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import API from "../services/api";
import {
  FaInbox,
  FaCheckCircle,
  FaExternalLinkAlt,
  FaClock,
  FaEnvelopeOpenText,
  FaInfoCircle,
  FaExclamationTriangle,
  FaSyncAlt,
  FaFileAlt,
} from "react-icons/fa";

function VolunteerInbox() {
  const user = JSON.parse(localStorage.getItem("user") || "null");
  const [notifications, setNotifications] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedMsg, setSelectedMsg] = useState(null);

  useEffect(() => {
    if (user?._id) {
      fetchNotifications();
    }
  }, [user?._id]);

  const fetchNotifications = async () => {
    try {
      setLoading(true);
      const res = await API.get(`/notifications/volunteer/${user._id}`);
      setNotifications(res.data);
      if (res.data.length > 0 && !selectedMsg) {
        setSelectedMsg(res.data[0]);
      }
    } catch (error) {
      console.error("Failed to load notifications:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleAcknowledge = async (id) => {
    try {
      await API.put(`/notifications/${id}/acknowledge`);
      alert("Mission briefing successfully acknowledged.");
      fetchNotifications();
    } catch (error) {
      alert("Failed to acknowledge order.");
    }
  };

  if (!user) {
    return (
      <>
        <Navbar />
        <div style={styles.loginNotice}>
          <h2>Volunteer Session Required</h2>
          <p>Please log in with your volunteer account to access your official dispatch transmissions.</p>
          <Link to="/login" style={styles.loginBtn}>
            Go to Login
          </Link>
        </div>
        <Footer />
      </>
    );
  }

  return (
    <>
      <Navbar />

      <div style={styles.container}>
        {/* Header */}
        <div style={styles.header}>
          <div>
            <div style={styles.badge}>
              <FaInbox style={{ marginRight: 6 }} />
              SECURE DISPATCH TRANSMISSION CENTER
            </div>
            <h1 style={styles.title}>Volunteer Tactical Communications</h1>
            <p style={styles.subtitle}>
              Official mission orders, incident assignments, and AI tactical briefings dispatched by Emergency Command.
            </p>
          </div>

          <div style={{ display: "flex", gap: "10px" }}>
            <button onClick={fetchNotifications} style={styles.refreshBtn}>
              <FaSyncAlt style={{ marginRight: 6 }} /> Refresh In-App Inbox
            </button>
            <Link to="/volunteer" style={styles.dashboardBtn}>
              Mission Operations
            </Link>
          </div>
        </div>

        {/* Email Diagnostic Banner */}
        <div style={styles.diagnosticBanner}>
          <FaInfoCircle size={20} color="#0284c7" style={{ marginTop: 2, marginRight: 12, flexShrink: 0 }} />
          <div>
            <strong style={{ color: "#0369a1", fontSize: "13.5px" }}>
              Transmission Delivery Diagnostic & Verification:
            </strong>
            <p style={{ margin: "4px 0 0 0", fontSize: "12.5px", color: "#334155", lineHeight: "1.5" }}>
              All disaster assignments are permanently recorded in this <strong>In-App Dispatch Center</strong> with guaranteed zero-loss delivery. To also receive messages in your real Gmail inbox, enter your 16-character Google App Password in <code>backend/.env</code>.
            </p>
          </div>
        </div>

        {/* Split View: List on Left, Message Detail on Right */}
        {loading ? (
          <div style={{ textAlign: "center", padding: "60px", color: "#64748b" }}>
            Querying secure message dispatch logs...
          </div>
        ) : notifications.length === 0 ? (
          <div style={styles.emptyCard}>
            <FaEnvelopeOpenText size={36} color="#94a3b8" />
            <h3 style={{ margin: "14px 0 6px 0", color: "#0f172a" }}>No Dispatch Messages Received Yet</h3>
            <p style={{ margin: 0, color: "#64748b", fontSize: "13.5px" }}>
              When command assigns you an incident in your district, the tactical mission order will appear here immediately.
            </p>
          </div>
        ) : (
          <div style={styles.splitGrid}>
            {/* Left: Message List */}
            <div style={styles.msgListCol}>
              <div style={styles.listHeader}>
                <span>Dispatched Transmissions ({notifications.length})</span>
              </div>
              <div style={styles.msgScrollArea}>
                {notifications.map((msg) => {
                  const isSelected = selectedMsg?._id === msg._id;

                  return (
                    <div
                      key={msg._id}
                      onClick={() => setSelectedMsg(msg)}
                      style={{
                        ...styles.msgItem,
                        ...(isSelected ? styles.msgItemActive : {}),
                      }}
                    >
                      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 4 }}>
                        <span style={styles.msgTypeBadge}>
                          {msg.notificationType === "volunteer_assignment"
                            ? "Emergency Order"
                            : "Incident Notice"}
                        </span>
                        <small style={{ color: "#64748b", fontSize: "11px" }}>
                          {new Date(msg.createdAt).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}
                        </small>
                      </div>

                      <strong style={styles.msgSubject}>
                        {msg.subject.replace(/\[.*?\]\s*/g, "")}
                      </strong>

                      <p style={styles.msgSnippet}>
                        {msg.messageText.slice(0, 75)}...
                      </p>

                      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginTop: 6 }}>
                        <span
                          style={{
                            ...styles.statusTag,
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

                        {msg.acknowledged && (
                          <span style={{ fontSize: "11px", color: "#16a34a", fontWeight: "700" }}>
                            <FaCheckCircle size={10} style={{ marginRight: 2 }} /> Acknowledged
                          </span>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Right: Message Detail */}
            <div style={styles.detailCol}>
              {selectedMsg ? (
                <div>
                  <div style={styles.detailHead}>
                    <div>
                      <div style={{ display: "flex", gap: "8px", alignItems: "center", marginBottom: "6px" }}>
                        <span style={styles.detailTypeTag}>OFFICIAL DISPATCH TRANSMISSION</span>
                        <span style={{ fontSize: "12px", color: "#64748b" }}>
                          ID: #{selectedMsg._id.slice(-8)}
                        </span>
                      </div>
                      <h2 style={styles.detailSubject}>{selectedMsg.subject}</h2>
                    </div>

                    {!selectedMsg.acknowledged && (
                      <button
                        onClick={() => handleAcknowledge(selectedMsg._id)}
                        style={styles.ackBtn}
                      >
                        <FaCheckCircle style={{ marginRight: 6 }} /> Acknowledge Order
                      </button>
                    )}
                  </div>

                  <div style={styles.metaRow}>
                    <div>
                      <small style={{ color: "#64748b", display: "block" }}>Recipient:</small>
                      <strong>{selectedMsg.recipientName} ({selectedMsg.recipientEmail})</strong>
                    </div>
                    <div>
                      <small style={{ color: "#64748b", display: "block" }}>Dispatched At:</small>
                      <span>
                        <FaClock size={11} style={{ marginRight: 4 }} />
                        {new Date(selectedMsg.createdAt).toLocaleString()}
                      </span>
                    </div>
                    <div>
                      <small style={{ color: "#64748b", display: "block" }}>Delivery Channel:</small>
                      <span style={{ fontWeight: "600", color: "#0369a1" }}>
                        {selectedMsg.deliveryStatus.toUpperCase()}
                      </span>
                    </div>
                  </div>

                  {/* Ethereal Clickable Preview if Available */}
                  {selectedMsg.previewUrl && (
                    <div style={styles.etherealBanner}>
                      <span>Live Browser Email Preview Generated:</span>
                      <a
                        href={selectedMsg.previewUrl}
                        target="_blank"
                        rel="noreferrer"
                        style={styles.previewLink}
                      >
                        <FaExternalLinkAlt style={{ marginRight: 4 }} /> Open Email in Browser
                      </a>
                    </div>
                  )}

                  {/* Formatted Message Body */}
                  <div style={styles.messageBodyWrap}>
                    <div style={styles.bodyLabel}>
                      <FaFileAlt style={{ marginRight: 6 }} /> Transmission Content:
                    </div>
                    <div
                      style={styles.messageHtmlBox}
                      dangerouslySetInnerHTML={{
                        __html: selectedMsg.messageHtml || selectedMsg.messageText.replace(/\n/g, "<br/>"),
                      }}
                    />
                  </div>
                </div>
              ) : (
                <div style={{ textAlign: "center", padding: "60px", color: "#94a3b8" }}>
                  Select a message from the left to read full mission orders.
                </div>
              )}
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
    padding: "36px 30px",
    background: "#f8fafc",
    minHeight: "90vh",
    maxWidth: "1350px",
    margin: "0 auto",
  },

  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    marginBottom: "20px",
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
    marginBottom: "6px",
  },

  title: {
    fontSize: "30px",
    fontWeight: "800",
    color: "#0f172a",
    margin: "0 0 6px 0",
  },

  subtitle: {
    color: "#475569",
    fontSize: "14px",
    maxWidth: "750px",
    lineHeight: "1.5",
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

  dashboardBtn: {
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

  diagnosticBanner: {
    backgroundColor: "#f0f9ff",
    border: "1px solid #bae6fd",
    borderRadius: "12px",
    padding: "14px 18px",
    display: "flex",
    alignItems: "flex-start",
    marginBottom: "24px",
  },

  splitGrid: {
    display: "grid",
    gridTemplateColumns: "380px 1fr",
    gap: "20px",
    background: "#ffffff",
    border: "1px solid #e2e8f0",
    borderRadius: "16px",
    overflow: "hidden",
    boxShadow: "0 4px 16px rgba(0,0,0,0.04)",
    minHeight: "650px",
  },

  msgListCol: {
    borderRight: "1px solid #e2e8f0",
    background: "#fafafa",
    display: "flex",
    flexDirection: "column",
  },

  listHeader: {
    padding: "14px 18px",
    borderBottom: "1px solid #e2e8f0",
    fontSize: "13px",
    fontWeight: "700",
    color: "#334155",
  },

  msgScrollArea: {
    overflowY: "auto",
    flex: 1,
    maxHeight: "700px",
  },

  msgItem: {
    padding: "14px 18px",
    borderBottom: "1px solid #f1f5f9",
    cursor: "pointer",
    transition: "background 0.15s ease",
  },

  msgItemActive: {
    backgroundColor: "#fff1f2",
    borderLeft: "4px solid #800020",
  },

  msgTypeBadge: {
    fontSize: "10.5px",
    fontWeight: "700",
    color: "#800020",
    textTransform: "uppercase",
  },

  msgSubject: {
    fontSize: "13.5px",
    color: "#0f172a",
    display: "block",
    lineHeight: "1.35",
    marginBottom: "4px",
  },

  msgSnippet: {
    margin: 0,
    fontSize: "12px",
    color: "#64748b",
    lineHeight: "1.4",
  },

  statusTag: {
    fontSize: "10.5px",
    fontWeight: "700",
    padding: "2px 6px",
    borderRadius: "6px",
  },

  detailCol: {
    padding: "24px",
    overflowY: "auto",
    maxHeight: "750px",
  },

  detailHead: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    borderBottom: "1px solid #e2e8f0",
    paddingBottom: "14px",
    marginBottom: "16px",
    gap: "16px",
  },

  detailTypeTag: {
    fontSize: "11px",
    fontWeight: "700",
    backgroundColor: "#f1f5f9",
    color: "#475569",
    padding: "2px 6px",
    borderRadius: "4px",
  },

  detailSubject: {
    fontSize: "20px",
    fontWeight: "800",
    color: "#0f172a",
    margin: 0,
    lineHeight: "1.3",
  },

  ackBtn: {
    backgroundColor: "#16a34a",
    color: "#ffffff",
    border: "none",
    padding: "8px 14px",
    borderRadius: "8px",
    fontSize: "12.5px",
    fontWeight: "700",
    cursor: "pointer",
    display: "inline-flex",
    alignItems: "center",
    whiteSpace: "nowrap",
  },

  metaRow: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))",
    gap: "12px",
    backgroundColor: "#f8fafc",
    padding: "12px 16px",
    borderRadius: "10px",
    fontSize: "12.5px",
    marginBottom: "16px",
  },

  etherealBanner: {
    backgroundColor: "#faf5ff",
    border: "1px solid #e9d5ff",
    borderRadius: "8px",
    padding: "10px 14px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    fontSize: "12.5px",
    marginBottom: "16px",
    color: "#6b21a8",
  },

  previewLink: {
    color: "#7e22ce",
    fontWeight: "700",
    textDecoration: "underline",
    display: "inline-flex",
    alignItems: "center",
  },

  messageBodyWrap: {
    marginTop: "16px",
  },

  bodyLabel: {
    fontSize: "12px",
    fontWeight: "700",
    color: "#64748b",
    marginBottom: "8px",
    display: "flex",
    alignItems: "center",
    textTransform: "uppercase",
  },

  messageHtmlBox: {
    backgroundColor: "#ffffff",
    border: "1px solid #e2e8f0",
    borderRadius: "12px",
    padding: "20px",
    fontSize: "14px",
    lineHeight: "1.6",
    color: "#1e293b",
  },

  emptyCard: {
    textAlign: "center",
    padding: "70px 20px",
    backgroundColor: "#ffffff",
    borderRadius: "16px",
    border: "1px solid #e2e8f0",
  },

  loginNotice: {
    textAlign: "center",
    padding: "80px 20px",
    maxWidth: "500px",
    margin: "0 auto",
  },

  loginBtn: {
    display: "inline-block",
    marginTop: "16px",
    backgroundColor: "#800020",
    color: "#ffffff",
    padding: "12px 24px",
    borderRadius: "8px",
    textDecoration: "none",
    fontWeight: "700",
  },
};

export default VolunteerInbox;
