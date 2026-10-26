import { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import API from "../services/api";
import {
  FaMapMarkerAlt,
  FaExclamationTriangle,
  FaImage,
  FaClipboardList,
  FaCrosshairs,
  FaCheckCircle,
  FaTimes,
  FaMapMarkedAlt,
  FaBolt,
  FaShieldAlt,
  FaEnvelope,
  FaRobot,
  FaBoxes,
  FaMagic,
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

function ReportDisaster() {
  const navigate = useNavigate();
  const user = JSON.parse(localStorage.getItem("user") || "null");

  const [image, setImage] = useState(null);
  const [coords, setCoords] = useState(null);
  const [geoLoading, setGeoLoading] = useState(false);
  const [geoError, setGeoError] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [submittedReport, setSubmittedReport] = useState(null);

  const [formData, setFormData] = useState({
    disasterType: "",
    district: "Pune",
    location: "",
    description: "",
  });

  const [enhancing, setEnhancing] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleEnhanceDescription = async () => {
    if (!formData.description || !formData.description.trim()) {
      alert("Please enter a few words describing the disaster first.");
      return;
    }
    setEnhancing(true);
    try {
      const res = await API.post("/chat/enhance", {
        description: formData.description,
        disasterType: formData.disasterType,
        location: formData.location,
      });
      if (res.data?.enhancedDescription) {
        setFormData((prev) => ({
          ...prev,
          description: res.data.enhancedDescription,
        }));
      }
    } catch {
      alert("Could not enhance description at this time.");
    } finally {
      setEnhancing(false);
    }
  };

  // Compute live severity preview
  const getCalculatedSeverity = () => {
    const text = (formData.description || "").toLowerCase();
    const type = (formData.disasterType || "").toLowerCase();

    if (
      text.includes("dead") ||
      text.includes("death") ||
      text.includes("trapped") ||
      text.includes("collapsed") ||
      text.includes("major") ||
      text.includes("severe") ||
      text.includes("sos") ||
      type.includes("sos")
    ) {
      return { level: "High", color: "#d90429", label: "Critical Priority" };
    }

    if (
      text.includes("injured") ||
      text.includes("flood") ||
      text.includes("fire") ||
      text.includes("earthquake") ||
      text.includes("cyclone") ||
      type === "fire" ||
      type === "flood" ||
      type === "earthquake"
    ) {
      return { level: "Medium", color: "#f77f00", label: "Medium Priority" };
    }

    return { level: "Low", color: "#2b8a3e", label: "Standard Priority" };
  };

  // One-Tap Geolocation detection
  const handleDetectLocation = () => {
    if (!navigator.geolocation) {
      setGeoError("Geolocation is not supported by your browser.");
      return;
    }

    setGeoLoading(true);
    setGeoError("");

    navigator.geolocation.getCurrentPosition(
      async (position) => {
        const lat = position.coords.latitude;
        const lng = position.coords.longitude;
        setCoords({ lat, lng });

        // Try reverse geocoding to human-readable address
        try {
          const res = await fetch(
            `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}&zoom=16&addressdetails=1`,
            { headers: { "User-Agent": "DisasterConnectAI/1.0" } }
          );
          const data = await res.json();
          if (data && data.display_name) {
            setFormData((prev) => ({
              ...prev,
              location: data.display_name.split(",").slice(0, 4).join(", "),
            }));
          } else {
            setFormData((prev) => ({
              ...prev,
              location: prev.location || `GPS Location (${lat.toFixed(4)}, ${lng.toFixed(4)})`,
            }));
          }
        } catch {
          setFormData((prev) => ({
            ...prev,
            location: prev.location || `GPS Coordinates: ${lat.toFixed(4)}, ${lng.toFixed(4)}`,
          }));
        } finally {
          setGeoLoading(false);
        }
      },
      (error) => {
        setGeoLoading(false);
        switch (error.code) {
          case error.PERMISSION_DENIED:
            setGeoError("Location permission denied. Please allow location access or type manually.");
            break;
          case error.POSITION_UNAVAILABLE:
            setGeoError("Location info unavailable. Please enter your location manually.");
            break;
          case error.TIMEOUT:
            setGeoError("Location request timed out. Please try again.");
            break;
          default:
            setGeoError("Could not retrieve GPS location.");
        }
      },
      { enableHighAccuracy: true, timeout: 10000, maximumAge: 0 }
    );
  };

  // Quick Emergency SOS trigger
  const handleTriggerSOS = () => {
    handleDetectLocation();
    setFormData({
      disasterType: "Emergency / SOS",
      location: formData.location || "Detecting GPS coordinates...",
      description:
        "[URGENT SOS DISTRESS ALERT] Critical assistance requested immediately at this location. Life-safety hazard in progress.",
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!user) {
      alert("Please log in to submit a disaster report.");
      navigate("/login");
      return;
    }

    setSubmitting(true);

    try {
      const data = new FormData();
      data.append("disasterType", formData.disasterType);
      data.append("district", formData.district || "Pune");
      data.append("location", formData.location);
      data.append("description", formData.description);
      data.append("reportedBy", user._id);

      if (coords) {
        data.append("latitude", coords.lat);
        data.append("longitude", coords.lng);
      }

      if (image) {
        data.append("image", image);
      }

      const res = await API.post("/disasters", data);

      setSubmittedReport(res.data.disaster || true);
      setFormData({
        disasterType: "",
        district: "Pune",
        location: "",
        description: "",
      });
      setImage(null);
      setCoords(null);
    } catch (error) {
      alert(error.response?.data?.message || "Failed to submit report. Please try again.");
    } finally {
      setSubmitting(false);
    }
  };

  const severity = getCalculatedSeverity();

  return (
    <>
      <Navbar />

      <div style={styles.container}>
        <div style={styles.card}>
          {/* Header */}
          <div style={styles.headerArea}>
            <span style={styles.badge}>Live Incident Intake</span>
            <h1 style={styles.title}>
              <span style={{ display: "inline-flex", alignItems: "center", gap: "8px" }}>
                <FaExclamationTriangle color="#d90429" /> Report a Disaster
              </span>
            </h1>
            <p style={styles.subtitle}>
              Submit incident details immediately to dispatch emergency volunteers and plot coordinates on the live response map.
            </p>
          </div>

          {/* SOS Quick Button */}
          <div style={styles.sosBanner}>
            <div style={styles.sosText}>
              <FaBolt size={18} color="#d90429" />
              <div>
                <strong>Life-Threatening Emergency?</strong>
                <p style={{ margin: "2px 0 0 0", fontSize: "12px", color: "#666" }}>
                  One-tap SOS fills high-priority tags and captures your GPS location instantly.
                </p>
              </div>
            </div>
            <button
              type="button"
              style={styles.sosButton}
              onClick={handleTriggerSOS}
            >
              <span style={{ display: "inline-flex", alignItems: "center", gap: "6px" }}>
                <FaBolt /> Instant SOS
              </span>
            </button>
          </div>

          {/* AI Emergency Advisory & Action Plan Card */}
          {submittedReport && (
            <div style={styles.aiAdvisoryCard}>
              <div style={styles.aiAdvisoryHeader}>
                <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
                  <FaCheckCircle size={22} color="#2b8a3e" />
                  <div>
                    <h3 style={{ margin: 0, color: "#2b8a3e", fontSize: "18px" }}>
                      Report Submitted & AI Advisory Generated
                    </h3>
                    <p style={{ margin: "2px 0 0 0", fontSize: "12.5px", color: "#495057" }}>
                      Incident reference ID: #{typeof submittedReport === "object" ? submittedReport._id?.slice(-6) : "NEW"}
                    </p>
                  </div>
                </div>
                <button
                  style={styles.closeSuccessBtn}
                  onClick={() => setSubmittedReport(null)}
                  title="Close advisory"
                >
                  <FaTimes size={16} />
                </button>
              </div>

              {/* Email Sent Banner */}
              <div style={styles.emailNotifBanner}>
                <span style={{ display: "inline-flex", alignItems: "center", gap: "6px" }}>
                  <FaEnvelope /> <strong>Email Dispatched:</strong> An incident confirmation and copy of this AI Action Plan has been sent to your registered email.
                </span>
              </div>

              {/* AI Threat Assessment */}
              {submittedReport.aiThreatAssessment && (
                <div style={styles.aiAssessmentBox}>
                  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "6px" }}>
                    <strong style={{ color: "#800020", fontSize: "13px", textTransform: "uppercase", letterSpacing: "0.5px", display: "inline-flex", alignItems: "center", gap: "6px" }}>
                      <FaRobot /> AI Threat Assessment
                    </strong>
                    <span style={{
                      backgroundColor: (submittedReport.aiRiskScore || 7) >= 8 ? "#d90429" : "#f77f00",
                      color: "#ffffff",
                      fontSize: "11px",
                      fontWeight: "700",
                      padding: "2px 8px",
                      borderRadius: "10px",
                    }}>
                      Risk Score: {submittedReport.aiRiskScore || 7} / 10
                    </span>
                  </div>
                  <p style={{ margin: 0, fontSize: "14px", color: "#212529", lineHeight: "1.5" }}>
                    {submittedReport.aiThreatAssessment}
                  </p>
                </div>
              )}

              {/* AI Action Plan Steps */}
              {submittedReport.aiActionPlan && submittedReport.aiActionPlan.length > 0 && (
                <div style={styles.actionPlanSection}>
                  <h4 style={{ margin: "0 0 10px 0", color: "#800020", fontSize: "15px", display: "flex", alignItems: "center", gap: "6px" }}>
                    <FaShieldAlt /> What You Must Do Right Now (AI Action Steps):
                  </h4>
                  <ol style={{ margin: 0, paddingLeft: "20px", display: "flex", flexDirection: "column", gap: "8px" }}>
                    {submittedReport.aiActionPlan.map((step, idx) => (
                      <li key={idx} style={{ fontSize: "13.5px", color: "#343a40", lineHeight: "1.5" }}>
                        {step}
                      </li>
                    ))}
                  </ol>
                </div>
              )}

              {/* Recommended Emergency Supplies */}
              {submittedReport.aiRecommendedSupplies && submittedReport.aiRecommendedSupplies.length > 0 && (
                <div style={styles.suppliesSection}>
                  <strong style={{ fontSize: "12px", color: "#6c757d", textTransform: "uppercase", display: "inline-flex", alignItems: "center", gap: "6px" }}>
                    <FaBoxes /> Recommended Supplies to Gather:
                  </strong>
                  <div style={{ display: "flex", flexWrap: "wrap", gap: "6px", marginTop: "6px" }}>
                    {submittedReport.aiRecommendedSupplies.map((item, idx) => (
                      <span key={idx} style={styles.supplyBadge}>
                        • {item}
                      </span>
                    ))}
                  </div>
                </div>
              )}

              {/* Action Buttons */}
              <div style={styles.advisoryActions}>
                <Link to="/map" style={styles.successLink}>
                  <FaMapMarkedAlt style={{ marginRight: "6px" }} /> View on Live Map
                </Link>
                <Link to="/myreports" style={styles.successSecondaryLink}>
                  View in My Reports
                </Link>
                <button
                  type="button"
                  style={styles.newReportBtn}
                  onClick={() => setSubmittedReport(null)}
                >
                  Report Another Incident
                </button>
              </div>
            </div>
          )}

          <form onSubmit={handleSubmit}>
            {/* Disaster Type */}
            <label style={styles.label}>Disaster Type *</label>
            <div style={styles.inputBox}>
              <FaExclamationTriangle color="#800020" />
              <select
                name="disasterType"
                value={formData.disasterType}
                onChange={handleChange}
                style={styles.input}
                required
              >
                <option value="">Select Disaster Type</option>
                <option value="Flood">Flood</option>
                <option value="Fire">Fire / Wildfire</option>
                <option value="Earthquake">Earthquake</option>
                <option value="Landslide">Landslide</option>
                <option value="Cyclone">Cyclone / Severe Storm</option>
                <option value="Road Accident">Major Road / Transit Accident</option>
                <option value="Building Collapse">Building / Bridge Collapse</option>
                <option value="Emergency / SOS">Emergency / SOS Distress</option>
                <option value="Other">Other Hazard</option>
              </select>
            </div>

            {/* District Selection */}
            <label style={styles.label}>District (Maharashtra) *</label>
            <div style={styles.inputBox}>
              <FaMapMarkerAlt color="#800020" />
              <select
                name="district"
                value={formData.district}
                onChange={handleChange}
                style={styles.input}
                required
              >
                {MAHARASHTRA_DISTRICTS.map((d) => (
                  <option key={d} value={d}>
                    {d} District
                  </option>
                ))}
              </select>
            </div>

            {/* Location with GPS Auto-Detect */}
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <label style={styles.label}>Incident Location / Street / Landmark *</label>
              <button
                type="button"
                style={styles.geoBtn}
                onClick={handleDetectLocation}
                disabled={geoLoading}
              >
                <FaCrosshairs
                  size={12}
                  style={{
                    marginRight: "6px",
                    animation: geoLoading ? "spin 1s linear infinite" : "none",
                  }}
                />
                {geoLoading ? "Acquiring GPS..." : "Auto-Detect My GPS Location"}
              </button>
            </div>

            <div style={styles.inputBox}>
              <FaMapMarkerAlt color="#800020" />
              <input
                type="text"
                name="location"
                placeholder="Enter city, landmark, or street address..."
                value={formData.location}
                onChange={handleChange}
                style={styles.input}
                required
              />
            </div>

            {/* GPS Status Indicator */}
            {coords && (
              <div style={styles.coordsBadge}>
                <FaCheckCircle size={12} color="#2b8a3e" style={{ marginRight: "6px" }} />
                <span>
                  GPS Lat: <strong>{coords.lat.toFixed(5)}</strong>, Lng:{" "}
                  <strong>{coords.lng.toFixed(5)}</strong> captured
                </span>
              </div>
            )}
            {geoError && <div style={styles.geoErrorText}>{geoError}</div>}

            {/* Description */}
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <label style={styles.label}>Incident Description & Severity Details *</label>
              <button
                type="button"
                onClick={handleEnhanceDescription}
                disabled={enhancing || !formData.description.trim()}
                style={{
                  background: "transparent",
                  border: "none",
                  color: "#800020",
                  fontSize: "12px",
                  fontWeight: "700",
                  cursor: formData.description.trim() ? "pointer" : "not-allowed",
                  opacity: formData.description.trim() ? 1 : 0.6,
                  display: "inline-flex",
                  alignItems: "center",
                  padding: "2px 0",
                }}
              >
                <span style={{ display: "inline-flex", alignItems: "center", gap: "5px" }}>
                  <FaMagic /> {enhancing ? "AI Structuring..." : "AI Polish & Structure"}
                </span>
              </button>
            </div>
            <div style={styles.inputBox}>
              <FaClipboardList color="#800020" style={{ alignSelf: "flex-start", marginTop: "4px" }} />
              <textarea
                rows="4"
                name="description"
                placeholder="Detail the emergency (e.g., number of people affected, structural damage, trapped victims, immediate hazards)..."
                value={formData.description}
                onChange={handleChange}
                style={styles.textarea}
                required
              />
            </div>

            {/* Dynamic Severity Preview Meter */}
            <div style={styles.severityMeter}>
              <div style={styles.severityLabel}>
                <FaShieldAlt size={13} color={severity.color} style={{ marginRight: "6px" }} />
                <span>Assessed Response Priority:</span>
              </div>
              <span
                style={{
                  ...styles.severityPill,
                  backgroundColor: severity.color,
                }}
              >
                {severity.level} — {severity.label}
              </span>
            </div>

            {/* Image Upload */}
            <label style={styles.label}>Attach Incident Photo (Optional)</label>
            <div style={styles.uploadBox}>
              <FaImage size={28} color="#800020" style={{ marginBottom: "8px" }} />
              <p style={{ margin: "0 0 10px 0", fontSize: "13px", color: "#666" }}>
                Add live photos to help emergency response teams evaluate damage
              </p>
              <input
                type="file"
                accept="image/*"
                onChange={(e) => setImage(e.target.files[0])}
                style={{ fontSize: "13px" }}
              />
            </div>

            {image && (
              <div style={styles.previewContainer}>
                <img
                  src={URL.createObjectURL(image)}
                  alt="Incident Preview"
                  style={styles.preview}
                />
                <button
                  type="button"
                  style={styles.removeImageBtn}
                  onClick={() => setImage(null)}
                >
                  <FaTimes size={12} style={{ marginRight: "4px" }} /> Remove Photo
                </button>
              </div>
            )}

            {/* Submit Button */}
            <button
              type="submit"
              style={{
                ...styles.button,
                opacity: submitting ? 0.7 : 1,
                cursor: submitting ? "not-allowed" : "pointer",
              }}
              disabled={submitting}
            >
              {submitting ? "Submitting Emergency Report..." : "Submit Disaster Report"}
            </button>
          </form>
        </div>
      </div>

      <Footer />
    </>
  );
}

const styles = {
  container: {
    minHeight: "calc(100vh - 140px)",
    background: "#f4f5f7",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    padding: "36px 16px",
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
  },
  card: {
    width: "100%",
    maxWidth: "680px",
    background: "#ffffff",
    padding: "36px 32px",
    borderRadius: "18px",
    boxShadow: "0 10px 30px rgba(0,0,0,0.08)",
    border: "1px solid #e5e7eb",
  },
  headerArea: {
    textAlign: "center",
    marginBottom: "24px",
  },
  badge: {
    display: "inline-block",
    backgroundColor: "#fff0f0",
    color: "#800020",
    fontSize: "12px",
    fontWeight: "700",
    padding: "4px 12px",
    borderRadius: "20px",
    textTransform: "uppercase",
    letterSpacing: "0.5px",
    marginBottom: "8px",
    border: "1px solid #ffd4d4",
  },
  title: {
    color: "#800020",
    margin: "0 0 8px 0",
    fontSize: "26px",
    fontWeight: "800",
  },
  subtitle: {
    color: "#6c757d",
    fontSize: "14px",
    lineHeight: "1.5",
    margin: 0,
  },
  sosBanner: {
    backgroundColor: "#fff5f5",
    border: "1px solid #ffc9c9",
    borderRadius: "12px",
    padding: "12px 16px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "24px",
    flexWrap: "wrap",
    gap: "12px",
  },
  sosText: {
    display: "flex",
    alignItems: "center",
    gap: "12px",
  },
  sosButton: {
    backgroundColor: "#d90429",
    color: "#ffffff",
    border: "none",
    padding: "8px 16px",
    borderRadius: "8px",
    fontSize: "13px",
    fontWeight: "700",
    cursor: "pointer",
    boxShadow: "0 2px 6px rgba(217, 4, 41, 0.3)",
    transition: "transform 0.1s",
  },
  successBox: {
    backgroundColor: "#ebfbee",
    border: "1px solid #b2f2bb",
    borderRadius: "12px",
    padding: "16px 20px",
    display: "flex",
    alignItems: "flex-start",
    marginBottom: "24px",
    position: "relative",
  },
  aiAdvisoryCard: {
    backgroundColor: "#ffffff",
    border: "2px solid #800020",
    borderRadius: "14px",
    padding: "20px 22px",
    marginBottom: "24px",
    boxShadow: "0 6px 20px rgba(128, 0, 32, 0.12)",
  },
  aiAdvisoryHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    borderBottom: "1px solid #f1f3f5",
    paddingBottom: "12px",
    marginBottom: "12px",
  },
  emailNotifBanner: {
    backgroundColor: "#e8f4fd",
    border: "1px solid #bee3f8",
    color: "#2b6cb0",
    borderRadius: "8px",
    padding: "8px 12px",
    fontSize: "12.5px",
    marginBottom: "14px",
  },
  aiAssessmentBox: {
    backgroundColor: "#fff5f5",
    borderLeft: "4px solid #800020",
    padding: "12px 14px",
    borderRadius: "6px",
    marginBottom: "16px",
  },
  actionPlanSection: {
    backgroundColor: "#f8f9fa",
    border: "1px solid #e9ecef",
    borderRadius: "10px",
    padding: "14px 16px",
    marginBottom: "14px",
  },
  suppliesSection: {
    marginBottom: "18px",
    padding: "8px 4px",
  },
  supplyBadge: {
    backgroundColor: "#e2e8f0",
    color: "#334155",
    fontSize: "12px",
    fontWeight: "600",
    padding: "4px 10px",
    borderRadius: "14px",
  },
  advisoryActions: {
    display: "flex",
    flexWrap: "wrap",
    gap: "10px",
    alignItems: "center",
    paddingTop: "10px",
    borderTop: "1px solid #f1f3f5",
  },
  newReportBtn: {
    backgroundColor: "#f1f3f5",
    color: "#495057",
    border: "1px solid #ced4da",
    padding: "6px 14px",
    borderRadius: "6px",
    fontSize: "12.5px",
    fontWeight: "600",
    cursor: "pointer",
  },
  successLink: {
    backgroundColor: "#800020",
    color: "#ffffff",
    textDecoration: "none",
    padding: "6px 14px",
    borderRadius: "6px",
    fontSize: "12.5px",
    fontWeight: "600",
    display: "inline-flex",
    alignItems: "center",
  },
  successSecondaryLink: {
    backgroundColor: "#ffffff",
    color: "#800020",
    border: "1px solid #800020",
    textDecoration: "none",
    padding: "6px 14px",
    borderRadius: "6px",
    fontSize: "12.5px",
    fontWeight: "600",
  },
  closeSuccessBtn: {
    background: "transparent",
    border: "none",
    color: "#868e96",
    cursor: "pointer",
    padding: "4px",
  },
  label: {
    display: "block",
    fontSize: "13px",
    fontWeight: "600",
    color: "#343a40",
    marginBottom: "6px",
  },
  geoBtn: {
    background: "transparent",
    border: "none",
    color: "#800020",
    fontSize: "12.5px",
    fontWeight: "600",
    cursor: "pointer",
    display: "inline-flex",
    alignItems: "center",
    padding: "2px 0",
  },
  coordsBadge: {
    backgroundColor: "#e8f5e9",
    color: "#2e7d32",
    padding: "6px 12px",
    borderRadius: "6px",
    fontSize: "12px",
    display: "inline-flex",
    alignItems: "center",
    marginBottom: "16px",
    border: "1px solid #c8e6c9",
  },
  geoErrorText: {
    color: "#d90429",
    fontSize: "12px",
    marginBottom: "14px",
  },
  inputBox: {
    display: "flex",
    alignItems: "center",
    gap: "10px",
    border: "1px solid #ced4da",
    borderRadius: "10px",
    padding: "10px 14px",
    marginBottom: "18px",
    backgroundColor: "#ffffff",
    transition: "border-color 0.2s",
  },
  input: {
    flex: 1,
    border: "none",
    outline: "none",
    fontSize: "14.5px",
    background: "transparent",
    fontFamily: "inherit",
    color: "#212529",
  },
  textarea: {
    flex: 1,
    border: "none",
    outline: "none",
    resize: "vertical",
    fontSize: "14px",
    background: "transparent",
    fontFamily: "inherit",
    lineHeight: "1.5",
    color: "#212529",
  },
  severityMeter: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    backgroundColor: "#f8f9fa",
    border: "1px solid #e9ecef",
    padding: "10px 14px",
    borderRadius: "10px",
    marginBottom: "20px",
  },
  severityLabel: {
    display: "flex",
    alignItems: "center",
    fontSize: "12.5px",
    fontWeight: "600",
    color: "#495057",
  },
  severityPill: {
    color: "#ffffff",
    fontSize: "11.5px",
    fontWeight: "700",
    padding: "3px 10px",
    borderRadius: "12px",
  },
  uploadBox: {
    border: "2px dashed #800020",
    padding: "20px",
    textAlign: "center",
    borderRadius: "12px",
    marginBottom: "18px",
    backgroundColor: "#fdf8f8",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  previewContainer: {
    position: "relative",
    marginBottom: "20px",
  },
  preview: {
    width: "100%",
    maxHeight: "260px",
    objectFit: "cover",
    borderRadius: "12px",
    display: "block",
  },
  removeImageBtn: {
    position: "absolute",
    top: "10px",
    right: "10px",
    backgroundColor: "rgba(0, 0, 0, 0.7)",
    color: "#ffffff",
    border: "none",
    padding: "6px 12px",
    borderRadius: "6px",
    fontSize: "11.5px",
    cursor: "pointer",
    display: "inline-flex",
    alignItems: "center",
  },
  button: {
    width: "100%",
    padding: "14px",
    background: "#800020",
    color: "#ffffff",
    border: "none",
    borderRadius: "10px",
    fontSize: "16px",
    fontWeight: "700",
    cursor: "pointer",
    boxShadow: "0 4px 12px rgba(128, 0, 32, 0.25)",
    transition: "background 0.2s, transform 0.1s",
  },
};

export default ReportDisaster;