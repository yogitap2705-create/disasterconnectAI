import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import API from "../services/api";
import { FaMapMarkerAlt, FaFileAlt, FaUser, FaExclamationTriangle } from "react-icons/fa";

import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
} from "react-leaflet";

import L from "leaflet";
import "leaflet/dist/leaflet.css";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
  iconUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
  shadowUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
});

function MapPage() {

  const [disasters, setDisasters] = useState([]);

  useEffect(() => {
    fetchDisasters();
  }, []);

  const fetchDisasters = async () => {
    try {

      const res = await API.get("/disasters");

      setDisasters(res.data);

    } catch (error) {
      console.log(error);
    }
  };

  return (
    <>
      <Navbar />

      <div
        style={{
          height: "90vh",
          padding: "20px",
          background: "#f8f8f8",
        }}
      >

        <h1
          style={{
            textAlign: "center",
            color: "#800020",
            marginBottom: "20px",
          }}
        >
          Maharashtra Disaster Map
        </h1>

        <MapContainer
          center={[19.7515, 75.7139]}
          zoom={7}
          style={{
            height: "80vh",
            borderRadius: "15px",
          }}
        >
          <TileLayer
            attribution="© OpenStreetMap"
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
                    {disasters.map((d) => {

            if (!d.latitude || !d.longitude) return null;

            return (
              <Marker
                key={d._id}
                position={[d.latitude, d.longitude]}
              >
                <Popup>

                  <div style={{ width: "220px" }}>

                    <h3
                      style={{
                        color: "#800020",
                        marginBottom: "10px",
                      }}
                    >
                      {d.disasterType}
                    </h3>

                    {d.image && (
                      <img
                        src={`http://localhost:5000/uploads/${d.image}`}
                        alt="Disaster"
                        width="200"
                        style={{
                          borderRadius: "10px",
                          marginBottom: "10px",
                        }}
                      />
                    )}

                    <p>
                      <strong style={{ display: "inline-flex", alignItems: "center", gap: "4px" }}>
                        <FaMapMarkerAlt /> Location:
                      </strong><br />
                      {d.location}
                    </p>

                    <p>
                      <strong style={{ display: "inline-flex", alignItems: "center", gap: "4px" }}>
                        <FaFileAlt /> Description:
                      </strong><br />
                      {d.description}
                    </p>

                    <p>
                      <strong style={{ display: "inline-flex", alignItems: "center", gap: "4px" }}>
                        <FaUser /> Reported By:
                      </strong><br />
                      {d.reportedBy?.fullName || "Unknown"}
                    </p>

                    <p>
                      <strong style={{ display: "inline-flex", alignItems: "center", gap: "4px" }}>
                        <FaExclamationTriangle /> Severity:
                      </strong>{" "}
                      <span
                        style={{
                          color:
                            d.severity === "High"
                              ? "#d90429"
                              : d.severity === "Medium"
                              ? "#f77f00"
                              : "#2b8a3e",
                          fontWeight: "bold",
                        }}
                      >
                        {d.severity || "Low"}
                      </span>
                    </p>

                    <p>
                      <strong>Status:</strong>{" "}
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
                    </p>

                  </div>

                </Popup>
              </Marker>
            );

          })}

        </MapContainer>

      </div>

      <Footer />

    </>
  );
}

export default MapPage;