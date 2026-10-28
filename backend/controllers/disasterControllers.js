const axios = require("axios");
const Disaster = require("../models/Disaster");
const User = require("../models/users");
const sendEmail = require("../utils/sendEmail");
const { generateDisasterActionPlan } = require("../utils/aiEngine");

// ===============================
// Create Disaster Report & AI Triage
// ===============================
exports.createDisaster = async (req, res) => {
  try {
    const {
      disasterType,
      location,
      district: reqDistrict,
      description,
      reportedBy,
      latitude: clientLat,
      longitude: clientLng,
    } = req.body;

    // Detect or normalize district
    let district = reqDistrict || "Pune";
    const maharashtraDistricts = [
      "Pune", "Mumbai", "Thane", "Nashik", "Nagpur",
      "Chhatrapati Sambhajinagar", "Solapur", "Kolhapur", "Satara",
      "Ahmednagar", "Amravati", "Nanded", "Jalgaon", "Akola",
      "Latur", "Dhule", "Sangli", "Chandrapur", "Parbhani",
      "Raigad", "Ratnagiri", "Sindhudurg", "Palghar", "Wardha"
    ];
    if (!reqDistrict && location) {
      for (const d of maharashtraDistricts) {
        if (new RegExp(`\\b${d}\\b`, "i").test(location)) {
          district = d;
          break;
        }
      }
    }

    let severity = "Low";
    const text = (description || "").toLowerCase();

    if (
      text.includes("dead") ||
      text.includes("death") ||
      text.includes("trapped") ||
      text.includes("collapsed") ||
      text.includes("major") ||
      text.includes("severe") ||
      text.includes("sos") ||
      text.includes("emergency")
    ) {
      severity = "High";
    } else if (
      text.includes("injured") ||
      text.includes("flood") ||
      text.includes("fire") ||
      text.includes("earthquake") ||
      text.includes("cyclone")
    ) {
      severity = "Medium";
    }

    let latitude = null;
    let longitude = null;

    // 1. Use direct GPS coordinates if provided by client
    if (clientLat !== undefined && clientLng !== undefined && !isNaN(Number(clientLat)) && !isNaN(Number(clientLng))) {
      latitude = Number(clientLat);
      longitude = Number(clientLng);
    } else if (location && location.trim()) {
      // 2. Otherwise try Nominatim OpenStreetMap geocoding with timeout
      try {
        const geoResponse = await axios.get(
          "https://nominatim.openstreetmap.org/search",
          {
            params: {
              q: location + ", Maharashtra, India",
              format: "json",
              limit: 1,
            },
            headers: {
              "User-Agent": "DisasterConnectAI/1.0",
            },
            timeout: 5000,
          }
        );

        if (geoResponse.data && geoResponse.data.length > 0) {
          latitude = Number(geoResponse.data[0].lat);
          longitude = Number(geoResponse.data[0].lon);
        }
      } catch (geoErr) {
        console.warn("[Geocoding] Nominatim lookup skipped or timed out:", geoErr.message);
      }
    }

    // 3. Generate AI Action Plan & Triage Assessment
    const aiPlan = await generateDisasterActionPlan({
      disasterType,
      location,
      description,
      severity,
    });

    // 4. Save to Database
    const disaster = await Disaster.create({
      disasterType,
      location,
      district,
      latitude,
      longitude,
      description,
      reportedBy,
      severity,
      image: req.file ? req.file.filename : "",
      aiRiskScore: aiPlan.aiRiskScore,
      aiThreatAssessment: aiPlan.aiThreatAssessment,
      aiActionPlan: aiPlan.aiActionPlan,
      aiRecommendedSupplies: aiPlan.aiRecommendedSupplies,
      aiVolunteerBriefing: aiPlan.aiVolunteerBriefing,
    });

    // 5. Send automated confirmation & AI Advisory Email to the reporter
   
    // 5. Send confirmation & AI advisory email to the reporter
    if (reportedBy) {
      try {
        const citizen = await User.findById(reportedBy);

        if (!citizen || !citizen.email) {
          console.warn(
            "[Report Email] Citizen not found or email address missing."
          );
        } else {
          const actionPlanHtmlList = (aiPlan.aiActionPlan || [])
            .map(
              (step) =>
                `<li style="margin-bottom: 6px;">${step}</li>`
            )
            .join("");

          const suppliesHtmlList = (
            aiPlan.aiRecommendedSupplies || []
          )
            .map(
              (item) =>
                `<li style="margin-bottom: 4px;">${item}</li>`
            )
            .join("");

          const emailResult = await sendEmail({
            to: citizen.email,
            recipientId: citizen._id,
            recipientName: citizen.fullName,
            notificationType: "citizen_advisory",
            disasterId: disaster._id,

            subject: `[DISASTER ALERT] Incident Logged: ${disasterType} in ${location}`,

            text: `Hello ${citizen.fullName},

Your disaster report has been recorded successfully.

Disaster Type: ${disasterType}
Location: ${location}
Severity: ${severity}

AI Threat Assessment:
${aiPlan.aiThreatAssessment}

Immediate Action Steps:
${(aiPlan.aiActionPlan || [])
  .map((step, index) => `${index + 1}. ${step}`)
  .join("\n")}

Recommended Supplies:
${(aiPlan.aiRecommendedSupplies || [])
  .map((item) => `- ${item}`)
  .join("\n")}

Emergency Number: 112

Stay safe.
DisasterConnect AI Team`,

            html: `
              <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 620px; margin: auto; border: 1px solid #ddd; border-radius: 8px; overflow: hidden;">

                <div style="background: #800020; color: white; padding: 20px;">
                  <h2>DisasterConnect AI</h2>
                  <p>Incident Confirmation & Safety Advisory</p>
                </div>

                <div style="padding: 24px;">
                  <p>Hello <strong>${citizen.fullName}</strong>,</p>

                  <p>Your disaster report has been successfully recorded.</p>

                  <p><strong>Disaster Type:</strong> ${disasterType}</p>
                  <p><strong>Location:</strong> ${location}</p>
                  <p><strong>Severity:</strong> ${severity}</p>

                  <div style="background: #fff5f5; padding: 15px; border-left: 4px solid #d90429;">
                    <h3>AI Threat Assessment</h3>
                    <p>${aiPlan.aiThreatAssessment}</p>
                    <p><strong>Risk Score:</strong> ${aiPlan.aiRiskScore}/10</p>
                  </div>

                  <h3>Immediate Safety Action Plan</h3>
                  <ol>${actionPlanHtmlList}</ol>

                  <h3>Recommended Emergency Supplies</h3>
                  <ul>${suppliesHtmlList}</ul>

                  <div style="background: #f8f9fa; padding: 15px;">
                    <strong>Emergency Hotline: 112</strong>
                    <p>Ambulance: 108 | Fire: 101</p>
                  </div>

                  <p>Stay safe.</p>
                  <p><strong>DisasterConnect AI Emergency Team</strong></p>
                </div>
              </div>
            `,
          });

          console.log(
            "[Report Email Result]:",
            JSON.stringify(emailResult)
          );
        }
      } catch (emailError) {
        console.error(
          "[Report Email Error]:",
          emailError.message
        );
      }
    } else {
      console.warn(
        "[Report Email] reportedBy is missing from the request."
      );
    }
    return res.status(201).json({
  message: "Disaster Report Submitted Successfully",
  disaster,
  aiActionPlan: aiPlan,
});

} catch (error) {
  console.error("[Create Disaster Error]:", error);
  return res.status(500).json({
    message: error.message,
  });
}
};


// ===============================
// Get All Disaster Reports
// ===============================
exports.getAllDisasters = async (req, res) => {
  try {
    const disasters = await Disaster.find()
      .populate("reportedBy", "fullName email phone district")
      .populate("assignedVolunteer", "fullName email district phone skills")
      .sort({ createdAt: -1 });

    res.status(200).json(disasters);
  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

// ===============================
// Get Specific User's Disasters
// ===============================
exports.getUserDisasters = async (req, res) => {
  try {
    const { id } = req.params;
    const disasters = await Disaster.find({
      reportedBy: id,
    })
      .populate("assignedVolunteer", "fullName email district phone skills")
      .sort({ createdAt: -1 });

    res.status(200).json(disasters);
  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

// ===============================
// Update Disaster Status & Resolution Notes
// ===============================
exports.updateDisasterStatus = async (req, res) => {
  try {
    const { id } = req.params;
    const { status, resolutionNotes } = req.body;

    const updateFields = { status };
    if (resolutionNotes !== undefined) {
      updateFields.resolutionNotes = resolutionNotes;
    }
    if (status === "Resolved") {
      updateFields.resolvedAt = new Date();
    }

    const disaster = await Disaster.findByIdAndUpdate(id, updateFields, {
      new: true,
    })
      .populate("reportedBy", "fullName email")
      .populate("assignedVolunteer", "fullName email");

    if (!disaster) {
      return res.status(404).json({
        message: "Disaster Report Not Found",
      });
    }

    // If marked Resolved, send notification to citizen
    if (status === "Resolved" && disaster.reportedBy?.email) {
      sendEmail({
        to: disaster.reportedBy.email,
        recipientId: disaster.reportedBy._id,
        recipientName: disaster.reportedBy.fullName,
        notificationType: "incident_resolution",
        disasterId: disaster._id,
        subject: `[INCIDENT RESOLUTION] Incident Marked Resolved: ${disaster.disasterType} at ${disaster.location}`,
        text: `Hello ${disaster.reportedBy.fullName},\n\nYour disaster report has been successfully resolved.\nLocation: ${disaster.location}\nResolution Notes: ${resolutionNotes || "Relief operations concluded successfully."}\n\nThank you for using DisasterConnect AI.`,
        html: `
          <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden;">
            <div style="background-color: #2b8a3e; color: #ffffff; padding: 18px 24px;">
              <h2 style="margin: 0;">DisasterConnect AI — Incident Resolved</h2>
            </div>
            <div style="padding: 24px;">
              <p>Hello <strong>${disaster.reportedBy.fullName}</strong>,</p>
              <p>The disaster incident you reported has been officially marked as <strong>Resolved</strong> by the response team.</p>
              <table style="width: 100%; border-collapse: collapse; margin: 16px 0;">
                <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Incident:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${disaster.disasterType}</td></tr>
                <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Location:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${disaster.location}</td></tr>
                <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Resolved At:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${new Date().toLocaleString()}</td></tr>
                <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Resolution Notes:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${resolutionNotes || "On-site relief completed successfully."}</td></tr>
              </table>
              <p style="margin-top: 24px; font-size: 13px; color: #777;">Thank you for helping keep your community safe.<br/>— DisasterConnect AI Team</p>
            </div>
          </div>
        `,
      }).catch((err) => console.error("[Resolution Email Error]:", err.message));
    }

    res.status(200).json({
      message: "Status Updated Successfully",
      disaster,
    });

  } catch (error) {
    console.error(error);
    res.status(500).json({
      message: error.message,
    });
  }
};

// ===============================
// Delete Disaster Report
// ===============================
exports.deleteDisaster = async (req, res) => {
  try {
    const { id } = req.params;
    const disaster = await Disaster.findByIdAndDelete(id);

    if (!disaster) {
      return res.status(404).json({
        message: "Disaster Report Not Found",
      });
    }

    res.status(200).json({
      message: "Disaster Report Deleted Successfully",
    });

  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

// ===============================
// Assign Volunteer (Admin Action)
// ===============================
exports.assignVolunteer = async (req, res) => {
  try {
    const { id } = req.params;
    const { volunteerId } = req.body;

    const disaster = await Disaster.findByIdAndUpdate(
      id,
      {
        assignedVolunteer: volunteerId,
        assignedAt: new Date(),
        status: "Assigned",
      },
      { new: true }
    )
      .populate("reportedBy", "fullName email phone district")
      .populate("assignedVolunteer", "fullName email district phone skills");

    if (!disaster) {
      return res.status(404).json({
        message: "Disaster not found",
      });
    }

    // Notify assigned volunteer via email with AI Field Briefing
    try {
      const volunteer = await User.findById(volunteerId);
      if (volunteer && volunteer.email) {
        const briefingText = disaster.aiVolunteerBriefing || "Proceed with caution. Assess situation and report back.";
        const suppliesList = (disaster.aiRecommendedSupplies || [])
          .map((item) => `<li>${item}</li>`)
          .join("");

        sendEmail({
          to: volunteer.email,
          recipientId: volunteer._id,
          recipientName: volunteer.fullName,
          notificationType: "volunteer_assignment",
          disasterId: disaster._id,
          subject: `[EMERGENCY MISSION ORDER] Incident Assignment: ${disaster.disasterType} in ${disaster.location}`,
          text: `Hello ${volunteer.fullName},\n\nYou have been assigned to respond to an emergency disaster incident:\n- Type: ${disaster.disasterType}\n- Severity: ${disaster.severity} (Risk: ${disaster.aiRiskScore || 7}/10)\n- Location: ${disaster.location}\n- Description: ${disaster.description}\n\nAI Tactical Briefing:\n${briefingText}\n\nPlease check your Volunteer Dashboard.\n\nDisasterConnect AI Team`,
          html: `
            <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 620px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden;">
              <div style="background-color: #800020; color: #ffffff; padding: 20px 24px;">
                <h2 style="margin: 0;">DisasterConnect AI — Emergency Mission Assignment</h2>
              </div>
              <div style="padding: 24px;">
                <p>Hello <strong>${volunteer.fullName}</strong>,</p>
                <p>You have been assigned by command administration to respond to an active emergency incident:</p>

                <table style="width: 100%; border-collapse: collapse; margin: 16px 0;">
                  <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold; width: 32%;">Incident Type:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${disaster.disasterType}</td></tr>
                  <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Severity Level:</td><td style="padding: 8px; border-bottom: 1px solid #eee; color: ${disaster.severity === "High" ? "#d32f2f" : "#f57c00"}; font-weight: bold;">${disaster.severity} (Risk: ${disaster.aiRiskScore || 7}/10)</td></tr>
                  <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Location:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${disaster.location}</td></tr>
                  <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Description:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${disaster.description}</td></tr>
                </table>

                <div style="background-color: #f8f9fa; border-left: 4px solid #800020; padding: 14px 16px; margin: 18px 0; border-radius: 4px;">
                  <strong style="color: #800020;">🤖 AI Tactical Field Briefing for You:</strong>
                  <p style="margin: 6px 0 0 0; font-size: 13.5px; color: #212529;">${briefingText}</p>
                </div>

                ${
                  suppliesList
                    ? `<h4 style="margin: 14px 0 6px 0; color: #495057;">Recommended Field Gear / Supplies:</h4>
                       <ul style="padding-left: 20px; font-size: 13px; color: #555;">${suppliesList}</ul>`
                    : ""
                }

                <p>Please log in to your Volunteer Dashboard to mark your response status as <strong>In Progress</strong> or <strong>Resolved</strong> once on scene.</p>
                <p style="margin-top: 24px; font-size: 13px; color: #777;">Stay safe and alert.<br/>— DisasterConnect AI Command</p>
              </div>
            </div>
          `,
        }).catch((err) => console.error("[Volunteer Email Notification Error]:", err.message));
      }
    } catch (err) {
      console.warn("[Volunteer Fetch Error]:", err.message);
    }

    res.status(200).json({
      message: "Volunteer Assigned Successfully",
      disaster,
    });

  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

// ===============================
// Get Volunteer's Assigned Disasters
// ===============================
exports.getVolunteerDisasters = async (req, res) => {
  try {
    const { id } = req.params;

    const disasters = await Disaster.find({
      assignedVolunteer: id,
    })
      .populate("reportedBy", "fullName email")
      .sort({ createdAt: -1 });

    res.status(200).json(disasters);

  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};
