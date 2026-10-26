import { FaMapMarkerAlt, FaUser } from "react-icons/fa";

function RecentActivity({ disasters }) {
  return (
    <div
      style={{
        background: "white",
        padding: "20px",
        borderRadius: "15px",
        marginTop: "30px",
        boxShadow: "0 5px 15px rgba(0,0,0,.15)",
      }}
    >
      <h2
        style={{
          color: "#800020",
          marginBottom: "20px",
        }}
      >
        Recent Disaster Reports
      </h2>

      {disasters.length === 0 ? (
        <p>No Reports Found</p>
      ) : (
        disasters
          .slice()
          .reverse()
          .slice(0, 5)
          .map((d) => (
            <div
              key={d._id}
              style={{
                borderBottom: "1px solid #ddd",
                padding: "12px 0",
              }}
            >
              <h3
                style={{
                  color: "#800020",
                  marginBottom: "5px",
                }}
              >
                {d.disasterType}
              </h3>

              <p style={{ display: "flex", alignItems: "center", gap: "5px" }}>
                <FaMapMarkerAlt color="#800020" size={13} /> <strong>{d.location}</strong>
              </p>

              <p>{d.description}</p>

              <p style={{ display: "flex", alignItems: "center", gap: "5px", color: "#555" }}>
                <FaUser size={12} /> {d.reportedBy?.fullName || "Unknown"}
              </p>

              <span
                style={{
                  color:
                    d.status === "Pending"
                      ? "orange"
                      : d.status === "In Progress"
                      ? "blue"
                      : "green",
                  fontWeight: "bold",
                }}
              >
                {d.status}
              </span>
            </div>
          ))
      )}
    </div>
  );
}

export default RecentActivity;