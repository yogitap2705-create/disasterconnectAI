import { useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import hero3D from "../assets/hero_3d.jpg";
import {
  FaMapMarkedAlt,
  FaRobot,
  FaUsers,
  FaShieldAlt,
  FaBolt,
  FaSatellite,
  FaEnvelopeOpenText,
  FaHeartbeat,
  FaPlayCircle,
  FaPhoneAlt,
  FaExclamationTriangle,
  FaUserShield,
  FaWater,
  FaFire,
  FaWind,
} from "react-icons/fa";

const SIMULATION_SCENARIOS = {
  flood: {
    title: "Pune Mula-Mutha Flash Flood",
    district: "Pune",
    type: "Flood",
    severity: "High",
    riskScore: 8.8,
    radius: "3.5 km Evacuation Perimeter",
    volunteersNeeded: "24 First Responders (Water Rescue + Medical)",
    supplies: ["Inflatable Life Rafts", "High-Beam Searchlights", "Water Purification Tablets", "Emergency Rations"],
    aiAdvisory: "Mula-Mutha river crossed danger mark by 1.8m. AI advises immediate vertical evacuation to RCC structures above 2nd floor. De-energize low-lying electrical substations.",
  },
  fire: {
    title: "Nashik Industrial Park Chemical Blaze",
    district: "Nashik",
    type: "Fire",
    severity: "High",
    riskScore: 9.2,
    radius: "2.0 km Toxic Smoke Zone",
    volunteersNeeded: "16 Hazmat & Fire Support Volunteers",
    supplies: ["N95 / Chemical Respirators", "Burn Trauma Kits", "Foam Extinguishers", "Evacuation Buses"],
    aiAdvisory: "Class-B industrial fire with toxic hydrocarbon vapor plumes moving southwest at 14 km/h. Shelter in place with sealed windows within 1km or evacuate perpendicular to wind.",
  },
  cyclone: {
    title: "Raigad Coastal Cyclone Storm Surge",
    district: "Raigad",
    type: "Cyclone",
    severity: "High",
    riskScore: 8.4,
    radius: "12.0 km Coastal Buffer",
    volunteersNeeded: "30 Coastal Relief Volunteers",
    supplies: ["Satellite Radios", "Tarpaulin Sheets", "First Aid Trauma Kits", "Canned Foods"],
    aiAdvisory: "Gale-force winds at 85 km/h with 2.5m surge predicted in next 3 hours. Fishermen alerted. Activate coastal cyclone shelters and preposition emergency relief packs.",
  },
};

function Home() {
  const [selectedScenarioKey, setSelectedScenarioKey] = useState("flood");
  const [isSimulating, setIsSimulating] = useState(false);
  const [simulationResult, setSimulationResult] = useState(SIMULATION_SCENARIOS.flood);

  const handleRunSimulation = (key) => {
    setSelectedScenarioKey(key);
    setIsSimulating(true);
    setTimeout(() => {
      setSimulationResult(SIMULATION_SCENARIOS[key]);
      setIsSimulating(false);
    }, 600);
  };

  return (
    <>
      <Navbar />

      {/* 3D Hero Section */}
      <section style={styles.heroSection}>
        <div style={styles.heroGrid}>
          {/* Left Hero Column */}
          <div style={styles.heroTextCol}>
            <div style={styles.heroBadge}>
              <FaBolt style={{ color: "#ffd166", marginRight: 6 }} />
              NEXT-GEN AI CRISIS COMMAND & DISTRICT DISPATCH
            </div>

            <h1 style={styles.heroTitle}>
              Real-Time Disaster Defense & <span style={styles.highlightText}>Intelligent Response</span>
            </h1>

            <p style={styles.heroDesc}>
              Empowering citizens, field volunteers, and emergency administrators with instant AI threat triage, automated email advisory dispatch, and district-based relief mobilization across Maharashtra.
            </p>

            <div style={styles.heroActionBtns}>
              <Link to="/report" style={styles.primaryCtaBtn}>
                <FaExclamationTriangle style={{ marginRight: 8 }} /> Report Disaster Now
              </Link>

              <Link to="/login" style={styles.secondaryCtaBtn}>
                <FaUserShield style={{ marginRight: 8 }} /> Admin & Volunteer Login
              </Link>
            </div>

            {/* Live Metrics Row */}
            <div style={styles.telemetryRow}>
              <div style={styles.telemetryItem}>
                <span style={styles.telemetryDot} />
                <span>AI Neural Triage: <strong>ONLINE</strong></span>
              </div>
              <div style={styles.telemetryItem}>
                <span style={{ ...styles.telemetryDot, background: "#06d6a0" }} />
                <span>District Grid: <strong>36 DISTRICTS ACTIVE</strong></span>
              </div>
              <div style={styles.telemetryItem}>
                <span style={{ ...styles.telemetryDot, background: "#118ab2" }} />
                <span>Automated Email: <strong>CONNECTED</strong></span>
              </div>
            </div>
          </div>

          {/* Right Hero Column: 3D Command Center Visual Card */}
          <div style={styles.heroVisualCol}>
            <div style={styles.visual3DCard}>
              <div style={styles.visualBadge}>
                <FaSatellite style={{ marginRight: 6 }} />
                3D Command Center Live Hologram
              </div>
              <img
                src={hero3D}
                alt="3D Disaster Command Center"
                style={styles.hero3DImage}
              />
              <div style={styles.visualCardOverlay}>
                <div style={styles.radarCard}>
                  <div style={styles.radarPing} />
                  <div>
                    <strong style={{ fontSize: "12px", color: "#fff", display: "block" }}>
                      AI DISASTER RADAR
                    </strong>
                    <small style={{ color: "#e0e0e0", fontSize: "11px" }}>
                      Scanning 36 Maharashtra Districts
                    </small>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Interactive 3D Emergency Scenario Simulator */}
      <section style={styles.simulatorSection}>
        <div style={styles.simulatorContainer}>
          <div style={{ textAlign: "center", marginBottom: "28px" }}>
            <span style={styles.sectionPill}>INTERACTIVE AI DEMONSTRATOR</span>
            <h2 style={styles.sectionHeading}>
              Test Our AI Emergency Decision Engine
            </h2>
            <p style={styles.sectionSubtitle}>
              Select a real-world disaster scenario to see how DisasterConnect AI calculates risk, models impact, and generates tactical volunteer assignments in real time.
            </p>
          </div>

          {/* Scenario Selector Pills */}
          <div style={styles.scenarioButtonRow}>
            <button
              onClick={() => handleRunSimulation("flood")}
              style={{
                ...styles.scenarioTabBtn,
                ...(selectedScenarioKey === "flood" ? styles.scenarioTabActive : {}),
                display: "inline-flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <FaWater /> Pune Flash Flood
            </button>

            <button
              onClick={() => handleRunSimulation("fire")}
              style={{
                ...styles.scenarioTabBtn,
                ...(selectedScenarioKey === "fire" ? styles.scenarioTabActive : {}),
                display: "inline-flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <FaFire /> Nashik Chemical Fire
            </button>

            <button
              onClick={() => handleRunSimulation("cyclone")}
              style={{
                ...styles.scenarioTabBtn,
                ...(selectedScenarioKey === "cyclone" ? styles.scenarioTabActive : {}),
                display: "inline-flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <FaWind /> Raigad Cyclone Warning
            </button>
          </div>

          {/* Live Simulated AI Telemetry Dashboard */}
          <div style={styles.simulationCard}>
            {isSimulating ? (
              <div style={{ padding: "50px", textAlign: "center" }}>
                <FaRobot size={36} color="#800020" style={{ animation: "pulse 1s infinite" }} />
                <h3 style={{ marginTop: "14px", color: "#800020" }}>
                  Calculating AI Decision Matrix & District Telemetry...
                </h3>
              </div>
            ) : (
              <div style={styles.simCardInner}>
                <div style={styles.simHeader}>
                  <div>
                    <h3 style={{ margin: "0 0 4px 0", color: "#800020", fontSize: "22px" }}>
                      {simulationResult.title}
                    </h3>
                    <span style={{ fontSize: "13px", color: "#666" }}>
                      District: <strong>{simulationResult.district}</strong> • Hazard: <strong>{simulationResult.type}</strong>
                    </span>
                  </div>

                  <div style={styles.riskBadgeLarge}>
                    <div style={{ fontSize: "11px", textTransform: "uppercase", letterSpacing: "1px" }}>AI Risk Score</div>
                    <div style={{ fontSize: "26px", fontWeight: "900" }}>{simulationResult.riskScore} / 10</div>
                    <small>Critical Severity</small>
                  </div>
                </div>

                {/* Key Metrics Grid */}
                <div style={styles.simMetricsGrid}>
                  <div style={styles.simMetricBox}>
                    <FaShieldAlt color="#800020" size={18} />
                    <div style={{ fontSize: "11px", color: "#777", textTransform: "uppercase" }}>Safety Perimeter</div>
                    <strong style={{ fontSize: "14px", color: "#222" }}>{simulationResult.radius}</strong>
                  </div>

                  <div style={styles.simMetricBox}>
                    <FaUsers color="#800020" size={18} />
                    <div style={{ fontSize: "11px", color: "#777", textTransform: "uppercase" }}>Volunteer Mobilization</div>
                    <strong style={{ fontSize: "14px", color: "#222" }}>{simulationResult.volunteersNeeded}</strong>
                  </div>

                  <div style={styles.simMetricBox}>
                    <FaEnvelopeOpenText color="#800020" size={18} />
                    <div style={{ fontSize: "11px", color: "#777", textTransform: "uppercase" }}>Email Advisory</div>
                    <strong style={{ fontSize: "14px", color: "#27ae60" }}>Auto-Dispatched to Citizens</strong>
                  </div>
                </div>

                {/* AI Tactical Advisory */}
                <div style={styles.advisoryBox}>
                  <strong style={{ color: "#800020", fontSize: "13px", textTransform: "uppercase", display: "flex", alignItems: "center", gap: "6px" }}>
                    <FaRobot /> AI Tactical Response Directive:
                  </strong>
                  <p style={{ margin: "8px 0 0 0", fontSize: "14px", color: "#2b2d42", lineHeight: "1.5" }}>
                    {simulationResult.aiAdvisory}
                  </p>
                </div>

                {/* Recommended Supplies */}
                <div style={{ marginTop: "16px" }}>
                  <small style={{ fontWeight: "700", color: "#555", textTransform: "uppercase", fontSize: "11.5px" }}>
                    Recommended Emergency Equipment Dispatched to Volunteers:
                  </small>
                  <div style={{ display: "flex", flexWrap: "wrap", gap: "8px", marginTop: "8px" }}>
                    {simulationResult.supplies.map((s, idx) => (
                      <span key={idx} style={styles.supplyPill}>
                        • {s}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </section>

      {/* 4 Pillars of Advanced Capabilities */}
      <section style={styles.pillarsSection}>
        <div style={{ textAlign: "center", marginBottom: "40px" }}>
          <span style={styles.sectionPill}>FULL-SPECTRUM PLATFORM</span>
          <h2 style={styles.sectionHeading}>
            Comprehensive Crisis Management Architecture
          </h2>
        </div>

        <div style={styles.cardsGrid}>
          <div style={styles.card}>
            <div style={styles.iconCircle}>
              <FaMapMarkedAlt size={26} color="#800020" />
            </div>
            <h3 style={styles.cardTitle}>Live Interactive GIS Map</h3>
            <p style={styles.cardDesc}>
              Real-time interactive Leaflet mapping plotting coordinates across all 36 Maharashtra districts with severity heatmap clustering.
            </p>
          </div>

          <div style={styles.card}>
            <div style={styles.iconCircle}>
              <FaRobot size={26} color="#800020" />
            </div>
            <h3 style={styles.cardTitle}>Neural AI Triage & Advisory</h3>
            <p style={styles.cardDesc}>
              Groq LLaMA-3.3 high-speed inference engine generates instant risk scores, customized survival steps, and automated field briefings.
            </p>
          </div>

          <div style={styles.card}>
            <div style={styles.iconCircle}>
              <FaUsers size={26} color="#800020" />
            </div>
            <h3 style={styles.cardTitle}>District-Smart Volunteer Dispatch</h3>
            <p style={styles.cardDesc}>
              Admins assign verified volunteers matched to their exact home district, emergency skill sets, and active phone contacts.
            </p>
          </div>

          <div style={styles.card}>
            <div style={styles.iconCircle}>
              <FaEnvelopeOpenText size={26} color="#800020" />
            </div>
            <h3 style={styles.cardTitle}>Automated Email Alerts</h3>
            <p style={styles.cardDesc}>
              Nodemailer dispatches formatted AI survival advisories to citizens upon reporting, mission orders to volunteers, and resolution notices.
            </p>
          </div>
        </div>
      </section>

      {/* Emergency Hotlines Statewide Bar */}
      <section style={styles.hotlineSection}>
        <div style={styles.hotlineContainer}>
          <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
            <FaPhoneAlt size={24} color="#ffd166" />
            <div>
              <h3 style={{ margin: 0, color: "#fff", fontSize: "18px" }}>
                National & Maharashtra Emergency Hotlines
              </h3>
              <small style={{ color: "#ddd" }}>Toll-free 24/7 centralized dispatch</small>
            </div>
          </div>

          <div style={styles.hotlinesGrid}>
            <div style={styles.hotlineChip}>
              <span>All Emergency:</span> <strong>112</strong>
            </div>
            <div style={styles.hotlineChip}>
              <span>Ambulance:</span> <strong>108</strong>
            </div>
            <div style={styles.hotlineChip}>
              <span>Fire Rescue:</span> <strong>101</strong>
            </div>
            <div style={styles.hotlineChip}>
              <span>Disaster Relief:</span> <strong>1078</strong>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </>
  );
}

const styles = {
  heroSection: {
    background: "linear-gradient(135deg, #4a0011 0%, #800020 50%, #2b000a 100%)",
    color: "#ffffff",
    padding: "60px 40px 70px 40px",
    minHeight: "86vh",
    display: "flex",
    alignItems: "center",
  },

  heroGrid: {
    maxWidth: "1280px",
    margin: "0 auto",
    display: "grid",
    gridTemplateColumns: "1.1fr 0.9fr",
    gap: "50px",
    alignItems: "center",
  },

  heroTextCol: {
    display: "flex",
    flexDirection: "column",
    gap: "18px",
  },

  heroBadge: {
    alignSelf: "flex-start",
    backgroundColor: "rgba(255, 255, 255, 0.12)",
    backdropFilter: "blur(8px)",
    border: "1px solid rgba(255, 255, 255, 0.2)",
    padding: "6px 14px",
    borderRadius: "20px",
    fontSize: "12px",
    fontWeight: "700",
    letterSpacing: "0.8px",
    display: "inline-flex",
    alignItems: "center",
  },

  heroTitle: {
    fontSize: "48px",
    fontWeight: "900",
    lineHeight: "1.15",
    margin: 0,
    letterSpacing: "-0.5px",
  },

  highlightText: {
    color: "#ffc2d1",
    textDecoration: "underline",
    textDecorationColor: "#ff758f",
  },

  heroDesc: {
    fontSize: "16px",
    lineHeight: "1.6",
    color: "#f1f3f5",
    margin: 0,
    maxWidth: "600px",
  },

  heroActionBtns: {
    display: "flex",
    gap: "16px",
    flexWrap: "wrap",
    marginTop: "8px",
  },

  primaryCtaBtn: {
    backgroundColor: "#ffffff",
    color: "#800020",
    padding: "14px 28px",
    borderRadius: "10px",
    textDecoration: "none",
    fontWeight: "800",
    fontSize: "15px",
    display: "inline-flex",
    alignItems: "center",
    boxShadow: "0 8px 20px rgba(0,0,0,0.25)",
    transition: "transform 0.2s ease",
  },

  secondaryCtaBtn: {
    backgroundColor: "transparent",
    color: "#ffffff",
    padding: "14px 28px",
    borderRadius: "10px",
    textDecoration: "none",
    fontWeight: "700",
    fontSize: "15px",
    border: "2px solid rgba(255,255,255,0.8)",
    display: "inline-flex",
    alignItems: "center",
  },

  telemetryRow: {
    display: "flex",
    gap: "20px",
    flexWrap: "wrap",
    marginTop: "14px",
    paddingTop: "18px",
    borderTop: "1px solid rgba(255, 255, 255, 0.15)",
    fontSize: "12px",
    color: "#e0e0e0",
  },

  telemetryItem: {
    display: "flex",
    alignItems: "center",
    gap: "8px",
  },

  telemetryDot: {
    width: "8px",
    height: "8px",
    borderRadius: "50%",
    backgroundColor: "#ffd166",
    display: "inline-block",
    boxShadow: "0 0 8px currentColor",
  },

  heroVisualCol: {
    display: "flex",
    justifyContent: "center",
  },

  visual3DCard: {
    position: "relative",
    borderRadius: "20px",
    overflow: "hidden",
    boxShadow: "0 25px 60px rgba(0, 0, 0, 0.5)",
    border: "2px solid rgba(255, 255, 255, 0.2)",
    background: "#1a0006",
    transform: "perspective(1000px) rotateY(-4deg) rotateX(2deg)",
    transition: "transform 0.4s ease",
    maxWidth: "520px",
    width: "100%",
  },

  visualBadge: {
    position: "absolute",
    top: "14px",
    left: "14px",
    backgroundColor: "rgba(0, 0, 0, 0.75)",
    backdropFilter: "blur(6px)",
    color: "#fff",
    padding: "5px 12px",
    borderRadius: "12px",
    fontSize: "11px",
    fontWeight: "700",
    zIndex: 2,
    border: "1px solid rgba(255, 255, 255, 0.2)",
    display: "flex",
    alignItems: "center",
  },

  hero3DImage: {
    width: "100%",
    height: "360px",
    objectFit: "cover",
    display: "block",
  },

  visualCardOverlay: {
    position: "absolute",
    bottom: "14px",
    left: "14px",
    right: "14px",
    zIndex: 2,
  },

  radarCard: {
    backgroundColor: "rgba(20, 0, 5, 0.85)",
    backdropFilter: "blur(8px)",
    border: "1px solid rgba(255, 255, 255, 0.2)",
    borderRadius: "12px",
    padding: "10px 14px",
    display: "flex",
    alignItems: "center",
    gap: "12px",
  },

  radarPing: {
    width: "14px",
    height: "14px",
    borderRadius: "50%",
    backgroundColor: "#d90429",
    boxShadow: "0 0 12px #d90429",
  },

  simulatorSection: {
    padding: "70px 30px",
    backgroundColor: "#ffffff",
  },

  simulatorContainer: {
    maxWidth: "1050px",
    margin: "0 auto",
  },

  sectionPill: {
    display: "inline-block",
    backgroundColor: "#fff0f2",
    color: "#800020",
    padding: "4px 14px",
    borderRadius: "14px",
    fontSize: "11px",
    fontWeight: "800",
    letterSpacing: "1px",
    marginBottom: "10px",
  },

  sectionHeading: {
    fontSize: "34px",
    fontWeight: "800",
    color: "#800020",
    margin: "0 0 10px 0",
  },

  sectionSubtitle: {
    fontSize: "15px",
    color: "#666",
    maxWidth: "650px",
    margin: "0 auto",
    lineHeight: "1.5",
  },

  scenarioButtonRow: {
    display: "flex",
    justifyContent: "center",
    gap: "12px",
    flexWrap: "wrap",
    marginBottom: "24px",
  },

  scenarioTabBtn: {
    padding: "10px 20px",
    borderRadius: "10px",
    border: "1px solid #dee2e6",
    backgroundColor: "#f8f9fa",
    color: "#495057",
    fontWeight: "700",
    fontSize: "14px",
    cursor: "pointer",
    transition: "all 0.2s ease",
  },

  scenarioTabActive: {
    backgroundColor: "#800020",
    color: "#ffffff",
    borderColor: "#800020",
    boxShadow: "0 4px 12px rgba(128,0,32,0.25)",
  },

  simulationCard: {
    backgroundColor: "#ffffff",
    border: "1px solid #e2e8f0",
    borderRadius: "18px",
    boxShadow: "0 10px 30px rgba(0,0,0,0.08)",
    overflow: "hidden",
  },

  simCardInner: {
    padding: "30px",
  },

  simHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    borderBottom: "1px solid #edf2f7",
    paddingBottom: "18px",
    marginBottom: "20px",
    flexWrap: "wrap",
    gap: "16px",
  },

  riskBadgeLarge: {
    backgroundColor: "#d90429",
    color: "#ffffff",
    padding: "10px 18px",
    borderRadius: "14px",
    textAlign: "center",
    boxShadow: "0 4px 12px rgba(217,4,41,0.3)",
  },

  simMetricsGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))",
    gap: "16px",
    marginBottom: "20px",
  },

  simMetricBox: {
    backgroundColor: "#f8fafc",
    border: "1px solid #e2e8f0",
    borderRadius: "12px",
    padding: "14px 16px",
    display: "flex",
    flexDirection: "column",
    gap: "6px",
  },

  advisoryBox: {
    backgroundColor: "#fff5f5",
    borderLeft: "4px solid #800020",
    borderRadius: "8px",
    padding: "16px",
    marginBottom: "16px",
  },

  supplyPill: {
    backgroundColor: "#e2e8f0",
    color: "#334155",
    padding: "4px 10px",
    borderRadius: "12px",
    fontSize: "12px",
    fontWeight: "600",
  },

  pillarsSection: {
    padding: "70px 40px",
    backgroundColor: "#f8f9fa",
  },

  cardsGrid: {
    maxWidth: "1200px",
    margin: "0 auto",
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
    gap: "24px",
  },

  card: {
    backgroundColor: "#ffffff",
    borderRadius: "16px",
    padding: "30px 24px",
    boxShadow: "0 4px 16px rgba(0,0,0,0.06)",
    border: "1px solid #edf2f7",
    textAlign: "center",
  },

  iconCircle: {
    width: "60px",
    height: "60px",
    borderRadius: "50%",
    backgroundColor: "#fff0f2",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    margin: "0 auto 18px auto",
  },

  cardTitle: {
    fontSize: "18px",
    fontWeight: "700",
    color: "#800020",
    marginBottom: "10px",
  },

  cardDesc: {
    fontSize: "13.5px",
    color: "#666",
    lineHeight: "1.55",
    margin: 0,
  },

  hotlineSection: {
    backgroundColor: "#800020",
    padding: "24px 30px",
  },

  hotlineContainer: {
    maxWidth: "1200px",
    margin: "0 auto",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    flexWrap: "wrap",
    gap: "20px",
  },

  hotlinesGrid: {
    display: "flex",
    gap: "12px",
    flexWrap: "wrap",
  },

  hotlineChip: {
    backgroundColor: "rgba(255, 255, 255, 0.15)",
    border: "1px solid rgba(255, 255, 255, 0.3)",
    padding: "6px 14px",
    borderRadius: "20px",
    color: "#ffffff",
    fontSize: "13px",
  },
};

export default Home;