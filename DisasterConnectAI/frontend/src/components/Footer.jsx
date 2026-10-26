import { Link } from "react-router-dom";
import { FaShieldAlt, FaPhoneAlt, FaMapMarkedAlt, FaCampground, FaBookMedical } from "react-icons/fa";

function Footer() {
  return (
    <footer style={styles.footer}>
      <div style={styles.container}>
        {/* Col 1: Brand & Mission */}
        <div style={styles.col}>
          <div style={styles.brandRow}>
            <FaShieldAlt size={18} color="#ffccd5" style={{ marginRight: 8 }} />
            <span style={styles.brandText}>DisasterConnect AI</span>
          </div>
          <p style={styles.desc}>
            Enterprise emergency disaster intelligence and district-wide resource mobilization framework for Maharashtra Civil Defense and community first responders.
          </p>
          <div style={styles.tagline}>
            AI Neural Triage • District-Smart Dispatch • Zero-Loss In-App Comms
          </div>
        </div>

        {/* Col 2: Navigation Links */}
        <div style={styles.col}>
          <h4 style={styles.colHeading}>Emergency Operations</h4>
          <ul style={styles.list}>
            <li>
              <Link to="/report" style={styles.link}>Lodge Disaster Report</Link>
            </li>
            <li>
              <Link to="/map" style={styles.link}>Statewide GIS Threat Map</Link>
            </li>
            <li>
              <Link to="/shelters" style={styles.link}>Relief Camps & Shelters</Link>
            </li>
            <li>
              <Link to="/missing-persons" style={styles.link}>Family Tracing Registry</Link>
            </li>
            <li>
              <Link to="/safety-protocols" style={styles.link}>Standard Operating Procedures</Link>
            </li>
          </ul>
        </div>

        {/* Col 3: Helplines */}
        <div style={styles.col}>
          <h4 style={styles.colHeading}>Centralized Helplines</h4>
          <ul style={styles.list}>
            <li style={styles.hotlineItem}>
              <span>Unified Police & Emergency:</span>
              <a href="tel:112" style={styles.phone}>112</a>
            </li>
            <li style={styles.hotlineItem}>
              <span>Disaster Medical Ambulance:</span>
              <a href="tel:108" style={styles.phone}>108</a>
            </li>
            <li style={styles.hotlineItem}>
              <span>Fire Rescue & Hazmat:</span>
              <a href="tel:101" style={styles.phone}>101</a>
            </li>
            <li style={styles.hotlineItem}>
              <span>NDRF Apex Command:</span>
              <a href="tel:1078" style={styles.phone}>1078</a>
            </li>
            <li style={styles.hotlineItem}>
              <span>District Disaster Control:</span>
              <a href="tel:1077" style={styles.phone}>1077</a>
            </li>
          </ul>
        </div>

        {/* Col 4: Portals */}
        <div style={styles.col}>
          <h4 style={styles.colHeading}>Authorized Portals</h4>
          <ul style={styles.list}>
            <li>
              <Link to="/admin" style={styles.link}>District Command Administration</Link>
            </li>
            <li>
              <Link to="/volunteer" style={styles.link}>Volunteer Field Operations</Link>
            </li>
            <li>
              <Link to="/volunteer/inbox" style={styles.link}>Tactical Communications Inbox</Link>
            </li>
            <li>
              <Link to="/citizen" style={styles.link}>Citizen Incident Tracker</Link>
            </li>
            <li>
              <Link to="/chatbot" style={styles.link}>AI Emergency Decision Advisor</Link>
            </li>
          </ul>
        </div>
      </div>

      <div style={styles.bottomBar}>
        <div>
          DisasterConnect AI Operations Platform | Engineered for High-Reliability Emergency Management
        </div>
        <div style={{ color: "#64748b", marginTop: 4 }}>
          All rights reserved. Secure TLS / MongoDB Resilient Deployment.
        </div>
      </div>
    </footer>
  );
}

const styles = {
  footer: {
    background: "#090d16",
    color: "#e2e8f0",
    padding: "50px 30px 24px 30px",
    marginTop: "60px",
    borderTop: "1px solid #1e293b",
    fontSize: "13.5px",
  },

  container: {
    maxWidth: "1300px",
    margin: "0 auto",
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))",
    gap: "36px",
    marginBottom: "40px",
  },

  col: {
    display: "flex",
    flexDirection: "column",
  },

  brandRow: {
    display: "flex",
    alignItems: "center",
    marginBottom: "12px",
  },

  brandText: {
    fontSize: "18px",
    fontWeight: "800",
    color: "#ffffff",
    letterSpacing: "0.5px",
  },

  desc: {
    color: "#94a3b8",
    lineHeight: "1.6",
    margin: "0 0 14px 0",
    fontSize: "13px",
  },

  tagline: {
    fontSize: "11px",
    fontWeight: "700",
    color: "#cbd5e1",
    letterSpacing: "0.5px",
    textTransform: "uppercase",
  },

  colHeading: {
    color: "#ffffff",
    fontSize: "14.5px",
    fontWeight: "700",
    margin: "0 0 14px 0",
    letterSpacing: "0.5px",
    textTransform: "uppercase",
  },

  list: {
    listStyle: "none",
    padding: 0,
    margin: 0,
    display: "flex",
    flexDirection: "column",
    gap: "9px",
  },

  link: {
    color: "#94a3b8",
    textDecoration: "none",
    transition: "color 0.15s ease",
    fontSize: "13px",
  },

  hotlineItem: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    fontSize: "12.5px",
    color: "#94a3b8",
  },

  phone: {
    color: "#38bdf8",
    fontWeight: "700",
    textDecoration: "none",
    marginLeft: "8px",
  },

  bottomBar: {
    borderTop: "1px solid #1e293b",
    paddingTop: "20px",
    textAlign: "center",
    color: "#94a3b8",
    fontSize: "12.5px",
  },
};

export default Footer;