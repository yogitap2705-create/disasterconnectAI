import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import API from "../services/api";
import {
  FaUser,
  FaEnvelope,
  FaLock,
  FaUserTag,
  FaMapMarkerAlt,
  FaPhoneAlt,
  FaTools,
} from "react-icons/fa";

const DISTRICTS = [
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

const SKILL_OPTIONS = [
  "First Aid & Emergency Medical Aid",
  "Flood & Swift Water Rescue",
  "Fire Fighting & Evacuation",
  "Heavy Vehicle & Drone Pilot",
  "Food, Shelter & Supply Logistics",
  "Communication & HAM Radio",
  "Search & Rescue (SAR)",
];

function Register() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    password: "",
    role: "citizen",
    district: "Pune",
    phone: "",
    skills: "First Aid & Emergency Medical Aid",
  });
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await API.post("/auth/register", formData);
      alert(res.data.message || "Registration Successful!");
      navigate("/login");
    } catch (error) {
      alert(error.response?.data?.message || "Registration Failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Navbar />

      <div style={styles.container}>
        <div style={styles.card}>
          <div style={styles.badge}>EMERGENCY COMMUNITY NETWORK</div>
          <h1 style={styles.title}>Create Account</h1>
          <p style={styles.subtitle}>
            Join DisasterConnect AI for intelligent community crisis response
          </p>

          <form onSubmit={handleSubmit}>
            <div style={styles.inputGroup}>
              <FaUser color="#800020" />
              <input
                type="text"
                name="fullName"
                placeholder="Full Name"
                value={formData.fullName}
                onChange={handleChange}
                style={styles.input}
                required
              />
            </div>

            <div style={styles.inputGroup}>
              <FaEnvelope color="#800020" />
              <input
                type="email"
                name="email"
                placeholder="Email Address"
                value={formData.email}
                onChange={handleChange}
                style={styles.input}
                required
              />
            </div>

            <div style={styles.inputGroup}>
              <FaPhoneAlt color="#800020" />
              <input
                type="tel"
                name="phone"
                placeholder="Mobile / Emergency Contact Number"
                value={formData.phone}
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
                placeholder="Password (min 6 characters)"
                value={formData.password}
                onChange={handleChange}
                style={styles.input}
                required
              />
            </div>

            <div style={styles.inputGroup}>
              <FaUserTag color="#800020" />
              <select
                name="role"
                value={formData.role}
                onChange={handleChange}
                style={styles.select}
              >
                <option value="citizen">Citizen (Report & Request Assistance)</option>
                <option value="volunteer">Volunteer (Assist & Field Response)</option>
              </select>
            </div>

            {/* District Selection */}
            <div style={styles.inputGroup}>
              <FaMapMarkerAlt color="#800020" />
              <select
                name="district"
                value={formData.district}
                onChange={handleChange}
                style={styles.select}
                required
              >
                {DISTRICTS.map((d) => (
                  <option key={d} value={d}>
                    District: {d}
                  </option>
                ))}
              </select>
            </div>

            {/* Volunteer Special Skill dropdown if Volunteer is chosen */}
            {formData.role === "volunteer" && (
              <div style={styles.volunteerSkillBox}>
                <label style={styles.skillLabel}>
                  <FaTools style={{ marginRight: 6, color: "#800020" }} />
                  Primary Emergency Relief Skill:
                </label>
                <div style={styles.inputGroup}>
                  <select
                    name="skills"
                    value={formData.skills}
                    onChange={handleChange}
                    style={styles.select}
                  >
                    {SKILL_OPTIONS.map((sk) => (
                      <option key={sk} value={sk}>
                        {sk}
                      </option>
                    ))}
                  </select>
                </div>
                <small style={{ color: "#666", fontSize: "11.5px" }}>
                  Admins will prioritize dispatching you for emergency incidents in{" "}
                  <strong>{formData.district}</strong> matching this skill.
                </small>
              </div>
            )}

            <button type="submit" disabled={loading} style={styles.button}>
              {loading ? "Registering..." : `Register as ${formData.role.toUpperCase()}`}
            </button>
          </form>

          <p style={{ marginTop: "20px", fontSize: "14px" }}>
            Already have an account?{" "}
            <Link
              to="/login"
              style={{
                color: "#800020",
                fontWeight: "bold",
                textDecoration: "underline",
              }}
            >
              Login
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
    background: "linear-gradient(135deg,#800020,#5C0013)",
    padding: "40px 15px",
  },

  card: {
    width: "480px",
    maxWidth: "95vw",
    background: "white",
    padding: "36px 30px",
    borderRadius: "20px",
    boxShadow: "0 10px 30px rgba(0,0,0,0.25)",
    textAlign: "center",
  },

  badge: {
    display: "inline-block",
    padding: "4px 12px",
    backgroundColor: "#fff0f2",
    color: "#800020",
    borderRadius: "15px",
    fontSize: "11px",
    fontWeight: "700",
    letterSpacing: "0.8px",
    marginBottom: "10px",
  },

  title: {
    fontSize: "30px",
    color: "#800020",
    marginBottom: "6px",
    fontWeight: "800",
  },

  subtitle: {
    color: "#666",
    marginBottom: "24px",
    fontSize: "13.5px",
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

  select: {
    flex: 1,
    border: "none",
    outline: "none",
    fontSize: "14.5px",
    background: "transparent",
    color: "#333",
  },

  volunteerSkillBox: {
    textAlign: "left",
    marginBottom: "14px",
    backgroundColor: "#fff9f9",
    padding: "12px",
    borderRadius: "10px",
    border: "1px dashed #f5c2c7",
  },

  skillLabel: {
    fontSize: "12.5px",
    fontWeight: "700",
    color: "#495057",
    marginBottom: "8px",
    display: "flex",
    alignItems: "center",
  },

  button: {
    width: "100%",
    padding: "14px",
    background: "#800020",
    color: "white",
    border: "none",
    borderRadius: "10px",
    fontSize: "16px",
    fontWeight: "bold",
    cursor: "pointer",
    marginTop: "10px",
    boxShadow: "0 4px 12px rgba(128,0,32,0.25)",
  },
};

export default Register;