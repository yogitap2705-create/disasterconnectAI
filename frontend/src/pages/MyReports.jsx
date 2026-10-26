import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import API from "../services/api";

function MyReports() {
  const user = JSON.parse(localStorage.getItem("user") || "null");
  const [reports, setReports] = useState([]);

  useEffect(() => {
    if (user?._id) {
      fetchReports();
    }
  }, [user?._id]);

  const fetchReports = async () => {
    try {
      if (!user?._id) return;
      const res = await API.get(`/disasters/user/${user._id}`);
      setReports(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <>
      <Navbar />

      <div style={{ padding: "30px" }}>
        <h1>My Disaster Reports</h1>

        {reports.length === 0 ? (
          <h3>No reports found.</h3>
        ) : (
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fill, minmax(320px,1fr))",
              gap: "20px",
              marginTop: "20px",
            }}
          >
            {reports.map((report) => (
              <div
                key={report._id}
                style={{
                  border: "1px solid #ddd",
                  borderRadius: "10px",
                  padding: "15px",
                  boxShadow: "0 0 8px lightgray",
                }}
              >
                <h2>{report.disasterType}</h2>

                <p><b>Location:</b> {report.location}</p>

                <p><b>Description:</b> {report.description}</p>

                <p>
                  <b>Status:</b>{" "}
                  <span
                    style={{
                      color:
                        report.status === "Pending"
                          ? "orange"
                          : report.status === "In Progress"
                          ? "blue"
                          : "green",
                      fontWeight: "bold",
                    }}
                  >
                    {report.status}
                  </span>
                </p>

                {report.image && (
                  <img
                    src={`http://localhost:5000/uploads/${report.image}`}
                    alt="Disaster"
                    style={{
                      width: "100%",
                      height: "180px",
                      objectFit: "cover",
                      borderRadius: "10px",
                    }}
                  />
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      <Footer />
    </>
  );
}

export default MyReports;