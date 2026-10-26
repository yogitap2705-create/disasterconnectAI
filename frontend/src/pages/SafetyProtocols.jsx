import { useState } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import {
  FaShieldAlt,
  FaWater,
  FaFire,
  FaWind,
  FaHospital,
  FaCheckCircle,
  FaTimesCircle,
  FaFirstAid,
  FaBiohazard,
} from "react-icons/fa";

const PROTOCOLS = {
  flood: {
    title: "Flood & Flash Inundation Protocol",
    category: "Hydrological Hazard",
    icon: FaWater,
    color: "#0284c7",
    summary:
      "Flash floods can develop within minutes of intense monsoon cloudbursts or river dam spillway releases.",
    dos: [
      "Move immediately to the highest accessible reinforced concrete floor or elevated ground.",
      "Turn off the primary domestic electrical main circuit breaker and gas cylinder valves.",
      "Store 3 to 5 days of drinkable water in sealed, clean containers before municipal supply cutoffs.",
      "Monitor official DisasterConnect AI and All India Radio emergency updates.",
      "Carry emergency survival kits including dry rations, whistle, flashlight, and medical essentials.",
    ],
    donts: [
      "Never attempt to walk, swim, or drive through flowing floodwater (15 cm of moving water can knock down an adult).",
      "Do not touch submerged or wet electrical equipment, wall switches, or downed power wires.",
      "Do not consume tap water or submerged food items without chlorination or thorough boiling.",
      "Never park vehicles in underground basements during red-alert cloudburst warnings.",
    ],
    gear: [
      "Life jackets & personal flotation devices",
      "Water purification tablets (Chlorine/Halazone)",
      "High-decibel emergency whistle",
      "Waterproof torch / headlamp with spare batteries",
    ],
  },
  fire: {
    title: "Fire & High-Rise Evacuation Protocol",
    category: "Thermal / Industrial Hazard",
    icon: FaFire,
    color: "#ea580c",
    summary:
      "Rapid fire propagation and smoke inhalation are the primary life hazards in structural fires.",
    dos: [
      "Crawl low under smoke toward the nearest fire exit (cool air and oxygen remain near the floor).",
      "Feel door handles with the back of your hand before opening; if hot, do not open.",
      "Activate the nearest manual fire pull station and dial 101 or 112 immediately.",
      "If clothes catch fire: Stop, Drop, and Roll on the floor to extinguish flames.",
      "Close doors behind you as you exit to isolate smoke spread.",
    ],
    donts: [
      "Never use elevators or passenger lifts during a fire; always use enclosed stairwells.",
      "Do not re-enter a burning building to retrieve personal valuables or pets.",
      "Do not jump from high floors unless directed by fire rescue inflatable cushions.",
      "Never store combustible materials in exit staircases or escape pathways.",
    ],
    gear: [
      "Smoke / particulate filter respirators (N95 / FFP3)",
      "Fire-resistant emergency blanket",
      "ABC dry chemical powder fire extinguisher",
      "Emergency burn gel and sterile trauma pads",
    ],
  },
  cyclone: {
    title: "Cyclone & Severe Gale Storm Protocol",
    category: "Atmospheric Hazard",
    icon: FaWind,
    color: "#0891b2",
    summary:
      "Cyclones bring destructive winds in excess of 100 km/h, torrential rainfall, and storm surge inundation along coastal belts.",
    dos: [
      "Board up or tape glass window panes diagonally to prevent flying glass shrapnel.",
      "Move inland from low-lying coastal areas to designated concrete cyclone shelters.",
      "Secure or dismantle loose rooftop solar panels, corrugated metal sheets, and antennas.",
      "Charge cellphones, power banks, and battery-operated emergency transceivers in advance.",
      "Remain inside reinforced interior rooms without windows during the passage of the cyclone eye.",
    ],
    donts: [
      "Do not go outside during the lull of the storm; the eye will be followed by violent reverse winds.",
      "Do not take shelter under trees, tin sheds, or electrical transformers.",
      "Avoid coastal harbors, beaches, and sea walls until the official all-clear is broadcast.",
      "Do not spread unverified rumors on social media.",
    ],
    gear: [
      "Battery/hand-crank radio receiver",
      "Heavy-duty tarpaulin sheets and nylon ropes",
      "Canned / ready-to-eat food rations",
      "First aid trauma kit with antiseptic bandages",
    ],
  },
  chemical: {
    title: "Chemical & Industrial Toxic Leak Protocol",
    category: "CBRN Industrial Hazard",
    icon: FaBiohazard,
    color: "#ca8a04",
    summary:
      "Hazardous chemical leaks (chlorine, ammonia, hydrocarbon gases) require immediate respiratory defense and crosswind evacuation.",
    dos: [
      "Determine wind direction and evacuate immediately perpendicular (crosswind) to the plume.",
      "Cover nose and mouth with a wet cloth or multi-layer damp towel to absorb water-soluble vapors.",
      "If trapped indoors, seal windows, doors, and AC vents with damp towels and plastic tape.",
      "Remove contaminated outer clothing and wash exposed skin thoroughly with running water.",
    ],
    donts: [
      "Never run downwind (in the direction the wind is blowing toxic fumes).",
      "Do not smoke, light matches, or operate electrical switches in flammable vapor zones.",
      "Do not rub eyes if irritated; flush gently with copious clean water for 15 minutes.",
    ],
    gear: [
      "Activated carbon respiratory mask",
      "Eye protection goggles (sealed chemical splash)",
      "Sterile saline eye wash pods",
      "Nitrile protective gloves",
    ],
  },
  medical: {
    title: "Emergency First Aid & CPR Protocol",
    category: "Life-Support Medical Protocol",
    icon: FaFirstAid,
    color: "#dc2626",
    summary:
      "Immediate bystander CPR and hemorrhage control can triple survival rates before ambulances arrive.",
    dos: [
      "Assess scene safety first: Ensure no live wires, collapse hazard, or fire threat.",
      "Check responsiveness: Tap collarbones firmly and shout 'Are you okay?'.",
      "If unresponsive and not breathing: Start chest compressions at 100-120 beats per minute (center of breastbone).",
      "Apply firm, continuous direct pressure with sterile pads to heavily bleeding wounds.",
      "Keep hypothermic or shock victims warm with dry blankets and elevate legs 30 cm if no fracture.",
    ],
    donts: [
      "Do not give fluids or food orally to an unconscious or drowsy casualty.",
      "Never move a victim with suspected spinal trauma unless immediate life danger exists.",
      "Do not apply tourniquets directly over joints (knees, elbows); place 5 cm above wound.",
      "Never interrupt chest compressions for more than 10 seconds.",
    ],
    gear: [
      "CPR pocket face shield with one-way valve",
      "Sterile trauma pressure dressings & gauze rolls",
      "Medical tourniquet (Combat Application Tourniquet)",
      "Splinting material and triangular bandages",
    ],
  },
};

function SafetyProtocols() {
  const [activeTab, setActiveTab] = useState("flood");
  const current = PROTOCOLS[activeTab];
  const Icon = current.icon;

  return (
    <>
      <Navbar />

      <div style={styles.container}>
        {/* Header */}
        <div style={styles.header}>
          <div style={styles.badge}>
            <FaShieldAlt style={{ marginRight: 6 }} />
            STANDARD OPERATING PROCEDURES (SOP)
          </div>
          <h1 style={styles.title}>Crisis Survival & Safety Guidelines</h1>
          <p style={styles.subtitle}>
            Certified civil defense action checklists, evacuation protocols, and emergency medical guidelines for citizens and community volunteers.
          </p>
        </div>

        {/* Tab Buttons */}
        <div style={styles.tabBar}>
          {Object.keys(PROTOCOLS).map((key) => {
            const p = PROTOCOLS[key];
            const TabIcon = p.icon;
            const isActive = activeTab === key;

            return (
              <button
                key={key}
                onClick={() => setActiveTab(key)}
                style={{
                  ...styles.tabBtn,
                  ...(isActive ? styles.tabBtnActive : {}),
                }}
              >
                <TabIcon style={{ marginRight: 8 }} />
                {p.title.split("&")[0].trim()}
              </button>
            );
          })}
        </div>

        {/* Active Protocol Card */}
        <div style={styles.protocolCard}>
          <div style={styles.protocolHeader}>
            <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
              <div style={{ ...styles.iconCircle, color: current.color, borderColor: current.color }}>
                <Icon size={24} />
              </div>
              <div>
                <span style={styles.categoryBadge}>{current.category}</span>
                <h2 style={styles.protocolTitle}>{current.title}</h2>
              </div>
            </div>
          </div>

          <p style={styles.summaryText}>{current.summary}</p>

          {/* Dos & Don'ts Grid */}
          <div style={styles.dosDontsGrid}>
            {/* Do's Column */}
            <div style={styles.dosColumn}>
              <h3 style={styles.columnTitle}>
                <FaCheckCircle color="#16a34a" style={{ marginRight: 8 }} />
                Critical Action Directives (Do's)
              </h3>
              <ul style={styles.list}>
                {current.dos.map((item, idx) => (
                  <li key={idx} style={styles.listItem}>
                    {item}
                  </li>
                ))}
              </ul>
            </div>

            {/* Don'ts Column */}
            <div style={styles.dontsColumn}>
              <h3 style={styles.columnTitle}>
                <FaTimesCircle color="#dc2626" style={{ marginRight: 8 }} />
                Hazardous Behaviors to Avoid (Don'ts)
              </h3>
              <ul style={styles.list}>
                {current.donts.map((item, idx) => (
                  <li key={idx} style={styles.listItem}>
                    {item}
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* Recommended Field Kit */}
          <div style={styles.kitSection}>
            <h4 style={styles.kitTitle}>
              <FaHospital style={{ marginRight: 6, color: "#800020" }} />
              Mandatory Emergency Relief Supplies for this Scenario:
            </h4>
            <div style={styles.kitGrid}>
              {current.gear.map((g, idx) => (
                <div key={idx} style={styles.kitItem}>
                  <FaCheckCircle color="#800020" size={12} style={{ marginRight: 8 }} />
                  <span>{g}</span>
                </div>
              ))}
            </div>
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
    maxWidth: "1280px",
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

  tabBar: {
    display: "flex",
    gap: "10px",
    flexWrap: "wrap",
    marginBottom: "24px",
  },

  tabBtn: {
    padding: "10px 18px",
    borderRadius: "10px",
    border: "1px solid #cbd5e1",
    background: "#ffffff",
    color: "#334155",
    fontSize: "13.5px",
    fontWeight: "600",
    cursor: "pointer",
    display: "inline-flex",
    alignItems: "center",
    transition: "all 0.2s ease",
  },

  tabBtnActive: {
    background: "#800020",
    color: "#ffffff",
    borderColor: "#800020",
    boxShadow: "0 3px 8px rgba(128,0,32,0.25)",
  },

  protocolCard: {
    background: "#ffffff",
    border: "1px solid #e2e8f0",
    borderRadius: "16px",
    padding: "32px",
    boxShadow: "0 4px 16px rgba(0,0,0,0.04)",
  },

  protocolHeader: {
    borderBottom: "1px solid #f1f5f9",
    paddingBottom: "16px",
    marginBottom: "16px",
  },

  iconCircle: {
    width: "48px",
    height: "48px",
    borderRadius: "12px",
    backgroundColor: "#f8fafc",
    border: "1px solid",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },

  categoryBadge: {
    fontSize: "11px",
    fontWeight: "700",
    color: "#64748b",
    textTransform: "uppercase",
    letterSpacing: "0.5px",
  },

  protocolTitle: {
    fontSize: "22px",
    fontWeight: "800",
    color: "#0f172a",
    margin: "4px 0 0 0",
  },

  summaryText: {
    fontSize: "14.5px",
    color: "#475569",
    lineHeight: "1.6",
    margin: "0 0 24px 0",
  },

  dosDontsGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))",
    gap: "24px",
    marginBottom: "28px",
  },

  dosColumn: {
    background: "#f0fdf4",
    border: "1px solid #bbf7d0",
    borderRadius: "12px",
    padding: "20px",
  },

  dontsColumn: {
    background: "#fef2f2",
    border: "1px solid #fecaca",
    borderRadius: "12px",
    padding: "20px",
  },

  columnTitle: {
    fontSize: "15px",
    fontWeight: "700",
    color: "#0f172a",
    margin: "0 0 14px 0",
    display: "flex",
    alignItems: "center",
  },

  list: {
    margin: 0,
    paddingLeft: "20px",
    display: "flex",
    flexDirection: "column",
    gap: "10px",
  },

  listItem: {
    fontSize: "13.5px",
    color: "#334155",
    lineHeight: "1.45",
  },

  kitSection: {
    backgroundColor: "#f8fafc",
    border: "1px solid #e2e8f0",
    borderRadius: "12px",
    padding: "20px",
  },

  kitTitle: {
    fontSize: "13.5px",
    fontWeight: "700",
    color: "#0f172a",
    margin: "0 0 14px 0",
    display: "flex",
    alignItems: "center",
  },

  kitGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))",
    gap: "12px",
  },

  kitItem: {
    display: "flex",
    alignItems: "center",
    backgroundColor: "#ffffff",
    border: "1px solid #e2e8f0",
    padding: "10px 14px",
    borderRadius: "8px",
    fontSize: "13px",
    color: "#1e293b",
    fontWeight: "500",
  },
};

export default SafetyProtocols;
