import { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import API from "../services/api";
import {
  FaCampground,
  FaMapMarkerAlt,
  FaPhoneAlt,
  FaUserNurse,
  FaTint,
  FaUtensils,
  FaBed,
  FaSearch,
  FaDirections,
  FaCheckCircle,
} from "react-icons/fa";

const DISTRICTS = [
  "All",
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
  "Raigad",
  "Ratnagiri",
];

function SheltersPage() {
  const [shelters, setShelters] = useState([]);
  const [selectedDistrict, setSelectedDistrict] = useState("All");
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchShelters();
  }, [selectedDistrict]);

  const fetchShelters = async () => {
    try {
      setLoading(true);
      const res = await API.get(
        `/shelters${selectedDistrict !== "All" ? `?district=${selectedDistrict}` : ""}`
      );
      setShelters(res.data);
    } catch (error) {
      console.error("Failed to fetch shelters:", error);
    } finally {
      setLoading(false);
    }
  };

  const filteredShelters = shelters.filter((s) => {
    const matchesSearch =
      s.name.toLowerCase().includes(search.toLowerCase()) ||
      s.address.toLowerCase().includes(search.toLowerCase()) ||
      s.district.toLowerCase().includes(search.toLowerCase());
    return matchesSearch;
  });

  const totalCapacity = shelters.reduce((acc, s) => acc + (s.capacity || 0), 0);
  const totalOccupancy = shelters.reduce((acc, s) => acc + (s.occupancy || 0), 0);
  const availableBeds = Math.max(0, totalCapacity - totalOccupancy);

  return (
    <>
      <Navbar />

      <div style={styles.container}>
        {/* Header */}
        <div style={styles.header}>
          <div style={styles.badge}>
            <FaCampground style={{ marginRight: 6 }} />
            CIVIL DEFENSE RELIEF NETWORK
          </div>
          <h1 style={styles.title}>Evacuation Shelters & Relief Camps</h1>
          <p style={styles.subtitle}>
            Statewide real-time registry of emergency transit shelters, relief centers, medical camps, and available beds across Maharashtra.
          </p>
        </div>

        {/* Aggregate Telemetry Row */}
        <div style={styles.metricsGrid}>
          <div style={styles.metricCard}>
            <div style={styles.metricVal}>{shelters.length}</div>
            <div style={styles.metricLabel}>Active Relief Camps</div>
          </div>
          <div style={styles.metricCard}>
            <div style={{ ...styles.metricVal, color: "#198754" }}>{availableBeds.toLocaleString()}</div>
            <div style={styles.metricLabel}>Available Bed Spaces</div>
          </div>
          <div style={styles.metricCard}>
            <div style={{ ...styles.metricVal, color: "#0d6efd" }}>{totalOccupancy.toLocaleString()}</div>
            <div style={styles.metricLabel}>Citizens Sheltered</div>
          </div>
          <div style={styles.metricCard}>
            <div style={{ ...styles.metricVal, color: "#800020" }}>{totalCapacity.toLocaleString()}</div>
            <div style={styles.metricLabel}>Total Capacity Ceiling</div>
          </div>
        </div>

        {/* Filter and Search Bar */}
        <div style={styles.filterBar}>
          <div style={styles.searchBox}>
            <FaSearch color="#64748b" style={{ marginRight: 10 }} />
            <input
              type="text"
              placeholder="Search camp name, address, or landmark..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              style={styles.searchInput}
            />
          </div>

          <div style={styles.districtWrap}>
            <FaMapMarkerAlt color="#800020" style={{ marginRight: 8 }} />
            <select
              value={selectedDistrict}
              onChange={(e) => setSelectedDistrict(e.target.value)}
              style={styles.select}
            >
              {DISTRICTS.map((d) => (
                <option key={d} value={d}>
                  {d === "All" ? "All Maharashtra Districts" : `${d} District`}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Shelters Grid */}
        {loading ? (
          <div style={{ textAlign: "center", padding: "60px", color: "#64748b" }}>
            Loading statewide shelter data...
          </div>
        ) : filteredShelters.length === 0 ? (
          <div style={styles.emptyCard}>
            <h3>No relief camps found for this filter</h3>
            <p>Try selecting another district or broadening your search terms.</p>
          </div>
        ) : (
          <div style={styles.grid}>
            {filteredShelters.map((s) => {
              const occupancyPct = Math.min(
                100,
                Math.round(((s.occupancy || 0) / (s.capacity || 1)) * 100)
              );
              const isFull = occupancyPct >= 95;

              return (
                <div key={s._id} style={styles.campCard}>
                  <div style={styles.cardHeader}>
                    <div>
                      <span style={styles.districtTag}>{s.district} District</span>
                      <h3 style={styles.campName}>{s.name}</h3>
                    </div>
                    <span
                      style={{
                        ...styles.statusTag,
                        backgroundColor: isFull ? "#fee2e2" : "#dcfce7",
                        color: isFull ? "#991b1b" : "#166534",
                      }}
                    >
                      {isFull ? "Camp at Capacity" : "Active & Accepting"}
                    </span>
                  </div>

                  <p style={styles.address}>
                    <FaMapMarkerAlt style={{ marginRight: 6, color: "#800020" }} />
                    {s.address}
                  </p>

                  {/* Occupancy Gauge */}
                  <div style={styles.capacitySection}>
                    <div style={styles.capLabelRow}>
                      <span style={{ fontSize: "12.5px", fontWeight: "600", color: "#334155" }}>
                        Occupancy Status:
                      </span>
                      <span style={{ fontSize: "12.5px", fontWeight: "700", color: "#0f172a" }}>
                        {s.occupancy} / {s.capacity} beds ({occupancyPct}%)
                      </span>
                    </div>
                    <div style={styles.progressBarBg}>
                      <div
                        style={{
                          ...styles.progressBarFill,
                          width: `${occupancyPct}%`,
                          backgroundColor:
                            occupancyPct > 85 ? "#dc2626" : occupancyPct > 60 ? "#ea580c" : "#16a34a",
                        }}
                      />
                    </div>
                  </div>

                  {/* Essential Amenities Badges */}
                  <div style={styles.amenitiesRow}>
                    <div style={styles.amenityChip}>
                      <FaUserNurse color="#0284c7" style={{ marginRight: 4 }} />
                      <span>{s.hasMedicalUnit ? "Medical Post: Yes" : "Basic Aid"}</span>
                    </div>
                    <div style={styles.amenityChip}>
                      <FaTint color="#0284c7" style={{ marginRight: 4 }} />
                      <span>{s.hasCleanWater ? "Clean Water: Yes" : "Water Tanker"}</span>
                    </div>
                    <div style={styles.amenityChip}>
                      <FaUtensils color="#0284c7" style={{ marginRight: 4 }} />
                      <span>{s.hasFoodSupplies ? "Hot Meals: Yes" : "Packaged"}</span>
                    </div>
                  </div>

                  {/* Contact Info and Action */}
                  <div style={styles.cardFooter}>
                    <div>
                      <small style={{ color: "#64748b", display: "block" }}>
                        In-Charge: {s.contactPerson}
                      </small>
                      <a href={`tel:${s.contactPhone}`} style={styles.phoneLink}>
                        <FaPhoneAlt size={11} style={{ marginRight: 4 }} />
                        {s.contactPhone}
                      </a>
                    </div>

                    <a
                      href={`https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(
                        s.address + ", Maharashtra"
                      )}`}
                      target="_blank"
                      rel="noreferrer"
                      style={styles.directionsBtn}
                    >
                      <FaDirections style={{ marginRight: 6 }} /> Route
                    </a>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>

      <Footer />
    </>
  );
}

const styles = {
  container: {
    padding: "40px 30px",
    background: "#f8fafc",
    minHeight: "90vh",
    maxWidth: "1350px",
    margin: "0 auto",
  },

  header: {
    marginBottom: "28px",
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
    marginBottom: "8px",
  },

  title: {
    fontSize: "32px",
    fontWeight: "800",
    color: "#0f172a",
    margin: "0 0 8px 0",
  },

  subtitle: {
    color: "#475569",
    fontSize: "14.5px",
    maxWidth: "800px",
    lineHeight: "1.5",
    margin: 0,
  },

  metricsGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
    gap: "16px",
    marginBottom: "28px",
  },

  metricCard: {
    background: "#ffffff",
    border: "1px solid #e2e8f0",
    borderRadius: "12px",
    padding: "18px 20px",
    boxShadow: "0 2px 6px rgba(0,0,0,0.03)",
  },

  metricVal: {
    fontSize: "26px",
    fontWeight: "800",
    color: "#0f172a",
  },

  metricLabel: {
    fontSize: "12.5px",
    color: "#64748b",
    marginTop: "4px",
    fontWeight: "600",
  },

  filterBar: {
    display: "flex",
    gap: "14px",
    flexWrap: "wrap",
    marginBottom: "26px",
    background: "#ffffff",
    padding: "14px",
    borderRadius: "12px",
    border: "1px solid #e2e8f0",
  },

  searchBox: {
    flex: 1,
    minWidth: "260px",
    display: "flex",
    alignItems: "center",
    background: "#f1f5f9",
    borderRadius: "8px",
    padding: "10px 14px",
  },

  searchInput: {
    flex: 1,
    border: "none",
    background: "transparent",
    outline: "none",
    fontSize: "14px",
    color: "#0f172a",
  },

  districtWrap: {
    display: "flex",
    alignItems: "center",
    padding: "0 10px",
  },

  select: {
    padding: "10px 14px",
    borderRadius: "8px",
    border: "1px solid #cbd5e1",
    fontSize: "13.5px",
    background: "#ffffff",
    cursor: "pointer",
    minWidth: "200px",
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(360px, 1fr))",
    gap: "20px",
  },

  campCard: {
    background: "#ffffff",
    border: "1px solid #e2e8f0",
    borderRadius: "14px",
    padding: "22px",
    boxShadow: "0 3px 10px rgba(0,0,0,0.04)",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
  },

  cardHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    gap: "12px",
    marginBottom: "10px",
  },

  districtTag: {
    fontSize: "11px",
    fontWeight: "700",
    color: "#800020",
    textTransform: "uppercase",
    letterSpacing: "0.5px",
  },

  campName: {
    fontSize: "16px",
    fontWeight: "700",
    color: "#0f172a",
    margin: "4px 0 0 0",
    lineHeight: "1.35",
  },

  statusTag: {
    padding: "3px 8px",
    borderRadius: "8px",
    fontSize: "11px",
    fontWeight: "700",
    whiteSpace: "nowrap",
  },

  address: {
    fontSize: "13px",
    color: "#475569",
    display: "flex",
    alignItems: "flex-start",
    margin: "8px 0 16px 0",
    lineHeight: "1.4",
  },

  capacitySection: {
    marginBottom: "14px",
  },

  capLabelRow: {
    display: "flex",
    justifyContent: "space-between",
    marginBottom: "6px",
  },

  progressBarBg: {
    width: "100%",
    height: "8px",
    backgroundColor: "#e2e8f0",
    borderRadius: "10px",
    overflow: "hidden",
  },

  progressBarFill: {
    height: "100%",
    borderRadius: "10px",
    transition: "width 0.4s ease",
  },

  amenitiesRow: {
    display: "flex",
    gap: "8px",
    flexWrap: "wrap",
    marginBottom: "18px",
  },

  amenityChip: {
    display: "inline-flex",
    alignItems: "center",
    backgroundColor: "#f0f9ff",
    border: "1px solid #e0f2fe",
    color: "#0369a1",
    fontSize: "11.5px",
    fontWeight: "600",
    padding: "4px 8px",
    borderRadius: "6px",
  },

  cardFooter: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    paddingTop: "14px",
    borderTop: "1px solid #f1f5f9",
  },

  phoneLink: {
    color: "#0d6efd",
    fontSize: "12.5px",
    fontWeight: "700",
    textDecoration: "none",
    display: "inline-flex",
    alignItems: "center",
    marginTop: "2px",
  },

  directionsBtn: {
    backgroundColor: "#800020",
    color: "#ffffff",
    padding: "7px 14px",
    borderRadius: "8px",
    fontSize: "12px",
    fontWeight: "700",
    textDecoration: "none",
    display: "inline-flex",
    alignItems: "center",
  },

  emptyCard: {
    textAlign: "center",
    padding: "50px",
    backgroundColor: "#fff",
    borderRadius: "14px",
    border: "1px solid #e2e8f0",
    color: "#64748b",
  },
};

export default SheltersPage;
