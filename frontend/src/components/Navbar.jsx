import { Link, useNavigate } from "react-router-dom";
import {
  FaHome,
  FaMapMarkedAlt,
  FaRobot,
  FaClipboardList,
  FaSignOutAlt,
  FaUserShield,
  FaShieldAlt,
  FaCampground,
  FaPhoneAlt,
  FaUserFriends,
  FaBookMedical,
  FaInbox,
} from "react-icons/fa";

function Navbar() {
  const navigate = useNavigate();
  const user = JSON.parse(localStorage.getItem("user") || "null");

  const logout = () => {
    localStorage.removeItem("user");
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <nav style={styles.navbar}>
      <Link to="/" style={styles.brand}>
        <FaShieldAlt style={{ marginRight: 8, color: "#ffccd5" }} />
        <span>DisasterConnect AI</span>
      </Link>

      <div style={styles.links}>
        <Link style={styles.link} to="/">
          <FaHome size={14} /> Home
        </Link>

        <Link style={styles.link} to="/report">
          <FaClipboardList size={14} /> Report
        </Link>

        <Link style={styles.link} to="/map">
          <FaMapMarkedAlt size={14} /> Live Map
        </Link>

        <Link style={styles.link} to="/shelters">
          <FaCampground size={14} /> Shelters
        </Link>

        <Link style={styles.link} to="/directory">
          <FaPhoneAlt size={13} /> Helplines
        </Link>

        <Link style={styles.link} to="/missing-persons">
          <FaUserFriends size={14} /> Tracing
        </Link>

        <Link style={styles.link} to="/safety-protocols">
          <FaBookMedical size={14} /> Protocols
        </Link>

        <Link style={styles.link} to="/chatbot">
          <FaRobot size={14} /> AI Advisor
        </Link>

        {user?.role === "admin" && (
          <Link style={styles.dashboardLink} to="/admin">
            Command Center
          </Link>
        )}

        {user?.role === "volunteer" && (
          <>
            <Link style={styles.dashboardLink} to="/volunteer">
              Missions
            </Link>
            <Link style={styles.inboxLink} to="/volunteer/inbox" title="Dispatch Communications">
              <FaInbox size={13} style={{ marginRight: 4 }} /> Inbox
            </Link>
          </>
        )}

        {user?.role === "citizen" && (
          <Link style={styles.dashboardLink} to="/citizen">
            My Dashboard
          </Link>
        )}

        {user ? (
          <button onClick={logout} style={styles.logout}>
            <FaSignOutAlt /> Logout
          </button>
        ) : (
          <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
            <Link style={styles.link} to="/login">
              Login
            </Link>

            <Link style={styles.register} to="/register">
              Register
            </Link>

            <Link style={styles.adminBtn} to="/login" title="Emergency Command Access">
              <FaUserShield size={13} /> Admin
            </Link>
          </div>
        )}
      </div>
    </nav>
  );
}

const styles = {
  navbar: {
    background: "#800020",
    color: "white",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "12px 30px",
    position: "sticky",
    top: 0,
    zIndex: 1000,
    boxShadow: "0 4px 14px rgba(0,0,0,0.25)",
    borderBottom: "1px solid rgba(255,255,255,0.12)",
    flexWrap: "wrap",
    gap: "12px",
  },

  brand: {
    fontSize: "22px",
    fontWeight: "800",
    letterSpacing: "0.5px",
    color: "#ffffff",
    textDecoration: "none",
    display: "flex",
    alignItems: "center",
  },

  links: {
    display: "flex",
    alignItems: "center",
    gap: "14px",
    flexWrap: "wrap",
  },

  link: {
    color: "#f8fafc",
    textDecoration: "none",
    display: "flex",
    alignItems: "center",
    gap: "5px",
    fontSize: "13.5px",
    fontWeight: "500",
    padding: "6px 8px",
    borderRadius: "6px",
    transition: "background 0.2s ease",
  },

  dashboardLink: {
    color: "#ffffff",
    backgroundColor: "rgba(255,255,255,0.18)",
    padding: "6px 12px",
    borderRadius: "6px",
    textDecoration: "none",
    fontSize: "13px",
    fontWeight: "700",
  },

  inboxLink: {
    color: "#ffffff",
    backgroundColor: "#0d6efd",
    padding: "6px 12px",
    borderRadius: "6px",
    textDecoration: "none",
    fontSize: "13px",
    fontWeight: "700",
    display: "inline-flex",
    alignItems: "center",
  },

  register: {
    background: "#ffffff",
    color: "#800020",
    padding: "7px 14px",
    borderRadius: "6px",
    textDecoration: "none",
    fontWeight: "700",
    fontSize: "13px",
  },

  logout: {
    background: "#ffffff",
    color: "#800020",
    border: "none",
    padding: "7px 14px",
    borderRadius: "6px",
    cursor: "pointer",
    fontWeight: "700",
    fontSize: "13px",
    display: "flex",
    alignItems: "center",
    gap: "5px",
  },

  adminBtn: {
    background: "#ffd1dc",
    color: "#800020",
    padding: "7px 12px",
    borderRadius: "6px",
    textDecoration: "none",
    fontWeight: "700",
    fontSize: "13px",
    display: "flex",
    alignItems: "center",
    gap: "5px",
    boxShadow: "0 2px 6px rgba(0,0,0,0.15)",
  },
};

export default Navbar;