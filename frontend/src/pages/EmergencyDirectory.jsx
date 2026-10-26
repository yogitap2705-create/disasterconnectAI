import { useState } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import {
  FaPhoneAlt,
  FaShieldAlt,
  FaAmbulance,
  FaFireExtinguisher,
  FaSearch,
  FaHospital,
  FaMapMarkerAlt,
  FaHeadset,
  FaBuilding,
} from "react-icons/fa";

const CENTRAL_HOTLINES = [
  {
    service: "Unified National Emergency Helpline",
    number: "112",
    desc: "Single emergency response number for Police, Fire, and Medical assistance.",
    icon: FaHeadset,
    color: "#d90429",
  },
  {
    service: "Emergency Medical & Ambulance Dispatch",
    number: "108",
    desc: "24/7 centralized ambulance and emergency medical technician deployment.",
    icon: FaAmbulance,
    color: "#0284c7",
  },
  {
    service: "Fire & Rescue Operations",
    number: "101",
    desc: "Rapid deployment fire brigades, hazardous material response squads.",
    icon: FaFireExtinguisher,
    color: "#ea580c",
  },
  {
    service: "NDRF Central Disaster Control Room",
    number: "1078",
    desc: "National Disaster Response Force apex emergency deployment headquarters.",
    icon: FaShieldAlt,
    color: "#800020",
  },
  {
    service: "District Disaster Management Cell (DDMC)",
    number: "1077",
    desc: "Direct toll-free link to the local District Collectorate crisis room.",
    icon: FaBuilding,
    color: "#166534",
  },
  {
    service: "Women & Child Distress Helpline",
    number: "1091",
    desc: "Emergency rescue, shelter, and trauma counseling for vulnerable persons.",
    icon: FaHospital,
    color: "#7c3aed",
  },
];

const DISTRICT_DIRECTORIES = [
  {
    district: "Pune",
    collectorate: "+91 20 2612 3370",
    policeControl: "+91 20 2612 2880",
    civilHospital: "+91 20 2612 8000",
    ddmoOfficer: "+91 94225 11200",
    ndrfBattalion: "+91 2114 247000 (5th Bn, Talegaon)",
  },
  {
    district: "Mumbai",
    collectorate: "+91 22 2266 1231",
    policeControl: "+91 22 2262 0111",
    civilHospital: "+91 22 2262 0361",
    ddmoOfficer: "+91 98200 45678",
    ndrfBattalion: "+91 22 2742 2200 (Andheri Base)",
  },
  {
    district: "Thane",
    collectorate: "+91 22 2534 4041",
    policeControl: "+91 22 2544 3535",
    civilHospital: "+91 22 2547 2577",
    ddmoOfficer: "+91 98199 44321",
    ndrfBattalion: "+91 22 2742 2200",
  },
  {
    district: "Nashik",
    collectorate: "+91 253 257 8500",
    policeControl: "+91 253 230 5233",
    civilHospital: "+91 253 257 2101",
    ddmoOfficer: "+91 94231 99011",
    ndrfBattalion: "+91 2114 247000",
  },
  {
    district: "Nagpur",
    collectorate: "+91 712 256 0600",
    policeControl: "+91 712 256 1234",
    civilHospital: "+91 712 274 4444",
    ddmoOfficer: "+91 98230 88765",
    ndrfBattalion: "+91 712 256 9900",
  },
  {
    district: "Chhatrapati Sambhajinagar",
    collectorate: "+91 240 233 1250",
    policeControl: "+91 240 224 0500",
    civilHospital: "+91 240 233 4477",
    ddmoOfficer: "+91 94222 33445",
    ndrfBattalion: "+91 2114 247000",
  },
  {
    district: "Solapur",
    collectorate: "+91 217 273 1001",
    policeControl: "+91 217 274 4600",
    civilHospital: "+91 217 231 2200",
    ddmoOfficer: "+91 94235 66778",
    ndrfBattalion: "+91 2114 247000",
  },
  {
    district: "Kolhapur",
    collectorate: "+91 231 265 4811",
    policeControl: "+91 231 266 2323",
    civilHospital: "+91 231 264 1177",
    ddmoOfficer: "+91 94220 44556",
    ndrfBattalion: "+91 2114 247000",
  },
  {
    district: "Raigad",
    collectorate: "+91 2141 222 001",
    policeControl: "+91 2141 222 100",
    civilHospital: "+91 2141 222 045",
    ddmoOfficer: "+91 98211 77889",
    ndrfBattalion: "+91 22 2742 2200",
  },
  {
    district: "Ratnagiri",
    collectorate: "+91 2352 222 301",
    policeControl: "+91 2352 222 222",
    civilHospital: "+91 2352 222 366",
    ddmoOfficer: "+91 94238 11223",
    ndrfBattalion: "+91 22 2742 2200",
  },
];

function EmergencyDirectory() {
  const [search, setSearch] = useState("");

  const filteredDistricts = DISTRICT_DIRECTORIES.filter((d) =>
    d.district.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <>
      <Navbar />

      <div style={styles.container}>
        {/* Header */}
        <div style={styles.header}>
          <div style={styles.badge}>
            <FaShieldAlt style={{ marginRight: 6 }} />
            OFFICIAL GOVERNMENT CRISIS DIRECTORY
          </div>
          <h1 style={styles.title}>Emergency Operations & Helplines</h1>
          <p style={styles.subtitle}>
            Direct communication channels for District Disaster Control Rooms, Police HQs, Civil Hospitals, and NDRF battalions throughout Maharashtra.
          </p>
        </div>

        {/* Central Hotlines Grid */}
        <h2 style={styles.sectionTitle}>Centralized 24/7 Emergency Helplines</h2>
        <div style={styles.hotlinesGrid}>
          {CENTRAL_HOTLINES.map((h, idx) => {
            const Icon = h.icon;
            return (
              <div key={idx} style={styles.hotlineCard}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
                  <div style={{ ...styles.iconWrap, color: h.color, borderColor: h.color }}>
                    <Icon size={20} />
                  </div>
                  <a href={`tel:${h.number}`} style={styles.dialBtn}>
                    <FaPhoneAlt size={11} style={{ marginRight: 4 }} /> Call
                  </a>
                </div>

                <div style={styles.hotlineNumber}>{h.number}</div>
                <h3 style={styles.hotlineName}>{h.service}</h3>
                <p style={styles.hotlineDesc}>{h.desc}</p>
              </div>
            );
          })}
        </div>

        {/* District Collectorate & Control Rooms */}
        <div style={styles.districtSection}>
          <div style={styles.districtSectionHeader}>
            <div>
              <h2 style={{ ...styles.sectionTitle, margin: "0 0 4px 0" }}>
                District Disaster Management Cells (DDMC)
              </h2>
              <p style={{ margin: 0, fontSize: "13.5px", color: "#64748b" }}>
                Contact verified local administration officers and district control rooms.
              </p>
            </div>

            <div style={styles.searchBox}>
              <FaSearch color="#64748b" style={{ marginRight: 8 }} />
              <input
                type="text"
                placeholder="Search district..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                style={styles.searchInput}
              />
            </div>
          </div>

          <div style={styles.districtGrid}>
            {filteredDistricts.map((d, idx) => (
              <div key={idx} style={styles.districtCard}>
                <div style={styles.districtCardHead}>
                  <FaMapMarkerAlt color="#800020" style={{ marginRight: 8 }} />
                  <h3 style={styles.districtName}>{d.district} District</h3>
                </div>

                <div style={styles.contactList}>
                  <div style={styles.contactRow}>
                    <span style={styles.contactLabel}>District Collectorate:</span>
                    <a href={`tel:${d.collectorate}`} style={styles.contactValue}>
                      {d.collectorate}
                    </a>
                  </div>

                  <div style={styles.contactRow}>
                    <span style={styles.contactLabel}>Police Control Room:</span>
                    <a href={`tel:${d.policeControl}`} style={styles.contactValue}>
                      {d.policeControl}
                    </a>
                  </div>

                  <div style={styles.contactRow}>
                    <span style={styles.contactLabel}>Civil Hospital / Trauma:</span>
                    <a href={`tel:${d.civilHospital}`} style={styles.contactValue}>
                      {d.civilHospital}
                    </a>
                  </div>

                  <div style={styles.contactRow}>
                    <span style={styles.contactLabel}>DDMO Disaster Officer:</span>
                    <a href={`tel:${d.ddmoOfficer}`} style={styles.contactValue}>
                      {d.ddmoOfficer}
                    </a>
                  </div>

                  <div style={styles.contactRow}>
                    <span style={styles.contactLabel}>NDRF Batt. Contact:</span>
                    <span style={{ fontSize: "12px", color: "#475569" }}>
                      {d.ndrfBattalion}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
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
    marginBottom: "32px",
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

  sectionTitle: {
    fontSize: "20px",
    fontWeight: "700",
    color: "#0f172a",
    marginBottom: "16px",
  },

  hotlinesGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
    gap: "18px",
    marginBottom: "40px",
  },

  hotlineCard: {
    background: "#ffffff",
    border: "1px solid #e2e8f0",
    borderRadius: "14px",
    padding: "20px",
    boxShadow: "0 3px 10px rgba(0,0,0,0.03)",
  },

  iconWrap: {
    width: "42px",
    height: "42px",
    borderRadius: "10px",
    backgroundColor: "#f8fafc",
    border: "1px solid",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },

  dialBtn: {
    backgroundColor: "#0f172a",
    color: "#ffffff",
    padding: "6px 12px",
    borderRadius: "6px",
    fontSize: "12px",
    fontWeight: "700",
    textDecoration: "none",
    display: "inline-flex",
    alignItems: "center",
  },

  hotlineNumber: {
    fontSize: "32px",
    fontWeight: "900",
    color: "#0f172a",
    margin: "12px 0 4px 0",
    letterSpacing: "-0.5px",
  },

  hotlineName: {
    fontSize: "15px",
    fontWeight: "700",
    color: "#800020",
    margin: "0 0 6px 0",
  },

  hotlineDesc: {
    fontSize: "12.5px",
    color: "#64748b",
    lineHeight: "1.4",
    margin: 0,
  },

  districtSection: {
    background: "#ffffff",
    border: "1px solid #e2e8f0",
    borderRadius: "16px",
    padding: "26px",
    boxShadow: "0 3px 12px rgba(0,0,0,0.03)",
  },

  districtSectionHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "24px",
    flexWrap: "wrap",
    gap: "16px",
  },

  searchBox: {
    display: "flex",
    alignItems: "center",
    background: "#f1f5f9",
    borderRadius: "8px",
    padding: "8px 14px",
    minWidth: "220px",
  },

  searchInput: {
    border: "none",
    background: "transparent",
    outline: "none",
    fontSize: "13.5px",
  },

  districtGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))",
    gap: "18px",
  },

  districtCard: {
    border: "1px solid #e2e8f0",
    borderRadius: "12px",
    padding: "18px",
    backgroundColor: "#fafafa",
  },

  districtCardHead: {
    display: "flex",
    alignItems: "center",
    borderBottom: "1px solid #e2e8f0",
    paddingBottom: "10px",
    marginBottom: "12px",
  },

  districtName: {
    margin: 0,
    fontSize: "16px",
    fontWeight: "700",
    color: "#0f172a",
  },

  contactList: {
    display: "flex",
    flexDirection: "column",
    gap: "8px",
  },

  contactRow: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    fontSize: "12.5px",
  },

  contactLabel: {
    color: "#64748b",
    fontWeight: "500",
  },

  contactValue: {
    color: "#0d6efd",
    fontWeight: "700",
    textDecoration: "none",
  },
};

export default EmergencyDirectory;
