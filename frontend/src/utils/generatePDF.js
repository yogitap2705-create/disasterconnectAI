import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";


const generatePDF = (disasters) => {

  const doc = new jsPDF();

  // Title
  doc.setFontSize(20);
  doc.setTextColor(128, 0, 32);
  doc.text("DisasterConnect AI", 70, 15);

  doc.setFontSize(14);
  doc.text("Admin Disaster Report", 72, 25);
const admin = JSON.parse(localStorage.getItem("user"));

doc.text(
  `Prepared By : ${admin?.fullName}`,
  14,
  30
);
  doc.setFontSize(10);
  doc.text(
    "Generated on: " + new Date().toLocaleString(),
    14,
    35
  );
  const total = disasters.length;

const pending = disasters.filter(
  d => d.status === "Pending"
).length;

const progress = disasters.filter(
  d => d.status === "In Progress"
).length;

const resolved = disasters.filter(
  d => d.status === "Resolved"
).length;

doc.setFontSize(11);

doc.text(`Total Reports : ${total}`, 14, 45);
doc.text(`Pending : ${pending}`, 70, 45);
doc.text(`In Progress : ${progress}`, 120, 45);
doc.text(`Resolved : ${resolved}`, 170, 45);

  const tableColumn = [
    "Disaster",
    "Location",
    "Status",
    "Reported By",
    "Date",
  ];

  const tableRows = [];

  disasters.forEach((d) => {

    tableRows.push([
      d.disasterType,
      d.location,
      d.status,
      d.reportedBy?.fullName || "Unknown",
      new Date(d.createdAt).toLocaleDateString(),
    ]);

  });

  autoTable(doc, {
    head: [tableColumn],
    body: tableRows,
    startY: 55,
    theme: "grid",
    headStyles: {
      fillColor: [128, 0, 32],
    },
  });
const pageCount = doc.internal.getNumberOfPages();

for (let i = 1; i <= pageCount; i++) {

  doc.setPage(i);

  doc.setFontSize(10);

  doc.setTextColor(120);

  doc.text(
    `DisasterConnect AI | Page ${i} of ${pageCount}`,
    14,
    290
  );

}
doc.save(
  `Disaster_Report_${new Date()
    .toLocaleDateString()
    .replace(/\//g, "-")}.pdf`
);};

export default generatePDF;