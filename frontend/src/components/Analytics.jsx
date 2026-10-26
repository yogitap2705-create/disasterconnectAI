import {
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
} from "recharts";

function Analytics({ disasters }) {
  const statusData = [
    {
      name: "Pending",
      value: disasters.filter(d => d.status === "Pending").length,
    },
    {
      name: "In Progress",
      value: disasters.filter(d => d.status === "In Progress").length,
    },
    {
      name: "Resolved",
      value: disasters.filter(d => d.status === "Resolved").length,
    },
  ];

  const COLORS = ["#FFA500", "#007BFF", "#800020"];

  const typeCount = {};

  disasters.forEach((d) => {
    typeCount[d.disasterType] =
      (typeCount[d.disasterType] || 0) + 1;
  });

  const typeData = Object.keys(typeCount).map((key) => ({
    type: key,
    reports: typeCount[key],
  }));

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "1fr 1fr",
        gap: "20px",
        marginBottom: "30px",
      }}
    >
      <div
        style={{
          background: "white",
          borderRadius: "15px",
          padding: "20px",
          boxShadow: "0 5px 15px rgba(0,0,0,.15)",
        }}
      >
        <h2 style={{ textAlign: "center", color: "#800020" }}>
          Report Status
        </h2>

        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie
              data={statusData}
              dataKey="value"
              outerRadius={100}
              label
            >
              {statusData.map((entry, index) => (
                <Cell
                  key={index}
                  fill={COLORS[index]}
                />
              ))}
            </Pie>

            <Tooltip />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </div>

      <div
        style={{
          background: "white",
          borderRadius: "15px",
          padding: "20px",
          boxShadow: "0 5px 15px rgba(0,0,0,.15)",
        }}
      >
        <h2 style={{ textAlign: "center", color: "#800020" }}>
          Disaster Types
        </h2>

        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={typeData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="type" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="reports" fill="#800020" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default Analytics;