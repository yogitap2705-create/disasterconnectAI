import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import API from "../services/api";
import { FaEnvelope, FaLock, FaUserShield, FaUserFriends, FaHandsHelping, FaBolt } from "react-icons/fa";

function Login() {
  const navigate = useNavigate();

  const [activeRole, setActiveRole] = useState("citizen"); // "citizen" | "volunteer" | "admin"
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
  const [isLoading, setIsLoading] = useState(false);

  const handleRoleTabClick = (role) => {
    setActiveRole(role);
    if (role === "admin") {
      setFormData({
        email: "admin@disasterconnect.ai",
        password: "admin123",
      });
    } else {
      setFormData({
        email: "",
        password: "",
      });
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const executeLogin = async (credentials) => {
    setIsLoading(true);
    try {
      const res = await API.post("/auth/login", credentials);

      localStorage.setItem("user", JSON.stringify(res.data.user));
      localStorage.setItem("token", res.data.token);

      const userRole = res.data.user.role;
      if (userRole === "admin") {
        navigate("/admin");
      } else if (userRole === "volunteer") {
        navigate("/volunteer");
      } else {
        navigate("/citizen");
      }
    } catch (error) {
      alert(error.response?.data?.message || "Login Failed. Please verify credentials.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    executeLogin(formData);
  };

  // 1-Click Instant Admin Login
  const handleAdminQuickLogin = () => {
    executeLogin({
      email: "admin@disasterconnect.ai",
      password: "admin123",
    });
  };

  return (
    <>
      <Navbar />

      <div style={styles.container}>
        <div style={styles.card}>
          <div style={styles.headerBadge}>
            {activeRole === "admin" ? (
              <span style={{ display: "inline-flex", alignItems: "center", gap: "6px" }}>
                <FaUserShield /> COMMAND CENTER ACCESS
              </span>
            ) : activeRole === "volunteer" ? (
              <span style={{ display: "inline-flex", alignItems: "center", gap: "6px" }}>
                <FaHandsHelping /> RESCUE FORCE PORTAL
              </span>
            ) : (
              <span style={{ display: "inline-flex", alignItems: "center", gap: "6px" }}>
                <FaUserFriends /> CITIZEN PORTAL
              </span>
            )}
          </div>

          <h1 style={styles.title}>
            {activeRole === "admin" ? "Admin Command Login" : "Welcome Back"}
          </h1>

          <p style={styles.subtitle}>
            {activeRole === "admin"
              ? "Authorized disaster command and district assignment portal."
              : "Sign in to DisasterConnect AI emergency intelligence system."}
          </p>

          {/* Role Selection Tabs */}
          <div style={styles.tabContainer}>
            <button
              type="button"
              onClick={() => handleRoleTabClick("citizen")}
              style={{
                ...styles.roleTab,
                ...(activeRole === "citizen" ? styles.activeTab : {}),
              }}
            >
              <FaUserFriends style={{ marginRight: 6 }} /> Citizen
            </button>

            <button
              type="button"
              onClick={() => handleRoleTabClick("volunteer")}
              style={{
                ...styles.roleTab,
                ...(activeRole === "volunteer" ? styles.activeTab : {}),
              }}
            >
              <FaHandsHelping style={{ marginRight: 6 }} /> Volunteer
            </button>

            <button
              type="button"
              onClick={() => handleRoleTabClick("admin")}
              style={{
                ...styles.roleTab,
                ...(activeRole === "admin" ? styles.activeAdminTab : {}),
              }}
            >
              <FaUserShield style={{ marginRight: 6 }} /> Admin
            </button>
          </div>

          {/* Dedicated 1-Click Admin Access Banner */}
          {activeRole === "admin" && (
            <div style={styles.adminBanner}>
              <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "8px" }}>
                <FaBolt color="#800020" size={18} />
                <strong style={{ color: "#800020" }}>Emergency Command Quick Access</strong>
              </div>
              <p style={{ margin: 0, fontSize: "12.5px", color: "#555", lineHeight: "1.4" }}>
                Auto-assigned district dispatch, AI triage monitor, and multi-volunteer management.
              </p>
              <button
                type="button"
                onClick={handleAdminQuickLogin}
                disabled={isLoading}
                style={styles.oneClickAdminBtn}
              >
                <FaBolt style={{ marginRight: 6 }} /> 1-Click Instant Admin Login
              </button>
            </div>
          )}

          <form onSubmit={handleSubmit} style={{ marginTop: "15px" }}>
            <div style={styles.inputGroup}>
              <FaEnvelope color="#800020" />
              <input
                type="email"
                name="email"
                placeholder={activeRole === "admin" ? "admin@disasterconnect.ai" : "Email Address"}
                value={formData.email}
                onChange={handleChange}
                style={styles.input}
                required
              />
            </div>

            <div style={styles.inputGroup}>
              <FaLock color="#800020" />
              <input
                type="password"
                name="password"
                placeholder="Password"
                value={formData.password}
                onChange={handleChange}
                style={styles.input}
                required
              />
            </div>

            <button type="submit" disabled={isLoading} style={styles.button}>
              {isLoading ? "Authenticating..." : `Login as ${activeRole.toUpperCase()}`}
            </button>
          </form>

          {/* If on Citizen or Volunteer tabs, show a quick shortcut to switch to Admin */}
          {activeRole !== "admin" && (
            <div style={{ marginTop: "18px", padding: "12px", background: "#fff5f5", borderRadius: "10px", border: "1px dashed #800020" }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <span style={{ fontSize: "12.5px", color: "#800020", fontWeight: "600" }}>
                  Are you a Disaster Administrator?
                </span>
                <button
                  type="button"
                  onClick={() => handleRoleTabClick("admin")}
                  style={styles.adminShortcutBtn}
                >
                  <FaUserShield style={{ marginRight: 4 }} /> Admin Login
                </button>
              </div>
            </div>
          )}

          <p style={{ marginTop: 22, fontSize: "14px", color: "#555" }}>
            Don't have an account?{" "}
            <Link
              to="/register"
              style={{
                color: "#800020",
                fontWeight: "bold",
                textDecoration: "underline",
              }}
            >
              Register here
            </Link>
          </p>
        </div>
      </div>

      <Footer />
    </>
  );
}

const styles = {
  container: {
    minHeight: "90vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    background: "linear-gradient(135deg,#800020 0%, #4a0011 100%)",
    padding: "40px 15px",
  },

  card: {
    width: "460px",
    maxWidth: "95vw",
    background: "#fff",
    padding: "36px 30px",
    borderRadius: "20px",
    boxShadow: "0 20px 45px rgba(0,0,0,.35)",
    textAlign: "center",
  },

  headerBadge: {
    display: "inline-block",
    padding: "4px 14px",
    background: "#fde8e8",
    color: "#800020",
    borderRadius: "20px",
    fontSize: "11px",
    fontWeight: "800",
    letterSpacing: "1px",
    marginBottom: "12px",
  },

  title: {
    color: "#800020",
    marginBottom: "6px",
    fontSize: "30px",
    fontWeight: "800",
  },

  subtitle: {
    color: "#666",
    marginBottom: "20px",
    fontSize: "13.5px",
    lineHeight: "1.4",
  },

  tabContainer: {
    display: "flex",
    background: "#f1f3f5",
    borderRadius: "12px",
    padding: "4px",
    marginBottom: "18px",
    gap: "4px",
  },

  roleTab: {
    flex: 1,
    padding: "10px 6px",
    border: "none",
    background: "transparent",
    borderRadius: "9px",
    cursor: "pointer",
    fontSize: "13px",
    fontWeight: "600",
    color: "#495057",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    transition: "all 0.2s ease",
  },

  activeTab: {
    background: "#800020",
    color: "#ffffff",
    boxShadow: "0 2px 8px rgba(128,0,32,0.3)",
  },

  activeAdminTab: {
    background: "linear-gradient(135deg, #800020, #b00030)",
    color: "#ffffff",
    boxShadow: "0 2px 8px rgba(128,0,32,0.4)",
  },

  adminBanner: {
    backgroundColor: "#fff0f2",
    border: "1px solid #f8d7da",
    borderRadius: "12px",
    padding: "14px",
    textAlign: "left",
    marginBottom: "12px",
  },

  oneClickAdminBtn: {
    width: "100%",
    marginTop: "10px",
    padding: "10px",
    background: "linear-gradient(135deg, #d90429, #800020)",
    color: "#fff",
    border: "none",
    borderRadius: "8px",
    fontSize: "13.5px",
    fontWeight: "700",
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    boxShadow: "0 3px 10px rgba(217,4,41,0.35)",
  },

  adminShortcutBtn: {
    background: "#800020",
    color: "#fff",
    border: "none",
    padding: "6px 12px",
    borderRadius: "6px",
    fontSize: "11.5px",
    fontWeight: "700",
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
  },

  inputGroup: {
    display: "flex",
    alignItems: "center",
    border: "1px solid #ddd",
    borderRadius: "10px",
    padding: "12px 14px",
    marginBottom: "14px",
    gap: "10px",
    background: "#fafafa",
  },

  input: {
    flex: 1,
    border: "none",
    outline: "none",
    fontSize: "15px",
    background: "transparent",
  },

  button: {
    width: "100%",
    padding: "14px",
    background: "#800020",
    color: "white",
    border: "none",
    borderRadius: "10px",
    cursor: "pointer",
    fontSize: "16px",
    fontWeight: "700",
    boxShadow: "0 4px 12px rgba(128,0,32,0.25)",
    transition: "background 0.2s ease",
  },
};

export default Login;