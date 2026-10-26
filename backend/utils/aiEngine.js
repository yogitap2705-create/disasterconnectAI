const Groq = require("groq-sdk");

let groq = null;
if (process.env.GROQ_API_KEY) {
  try {
    groq = new Groq({ apiKey: process.env.GROQ_API_KEY });
  } catch (e) {
    console.warn("[AIEngine] Groq init notice:", e.message);
  }
}

/**
 * Intelligent Disaster Action Plan & Triage Engine
 * Generates tailored action plans, risk scores, supplies, and volunteer field briefings.
 */
async function generateDisasterActionPlan({ disasterType, location, description, severity }) {
  const typeLower = (disasterType || "").toLowerCase();
  const descLower = (description || "").toLowerCase();

  // Try live Groq API first if available with a fast timeout (3.5s)
  if (groq) {
    try {
      const prompt = `You are DisasterConnect AI, an emergency response intelligence system.
Analyze this incident report and reply ONLY with valid JSON (no markdown formatting, no backticks):
Disaster Type: ${disasterType}
Location: ${location}
Severity: ${severity}
Description: ${description}

JSON Schema required:
{
  "aiRiskScore": number between 1 and 10,
  "aiThreatAssessment": "1-2 sentence threat assessment",
  "aiActionPlan": ["Step 1 immediate action", "Step 2 safety precaution", "Step 3 evacuation guidance", "Step 4 medical or communication step"],
  "aiRecommendedSupplies": ["Supply 1", "Supply 2", "Supply 3", "Supply 4"],
  "aiVolunteerBriefing": "2-3 sentences of tactical guidance for the assigned emergency volunteer (PPE, approach precautions, priority triage)"
}`;

      const completion = await Promise.race([
        groq.chat.completions.create({
          model: "llama-3.3-70b-versatile",
          messages: [{ role: "user", content: prompt }],
          temperature: 0.2,
          max_tokens: 500,
        }),
        new Promise((_, reject) => setTimeout(() => reject(new Error("Timeout")), 3500)),
      ]);

      const raw = completion.choices[0]?.message?.content?.trim();
      if (raw) {
        // Strip markdown backticks if returned
        const cleaned = raw.replace(/^```json/i, "").replace(/^```/, "").replace(/```$/, "").trim();
        const parsed = JSON.parse(cleaned);
        if (parsed.aiActionPlan && parsed.aiActionPlan.length > 0) {
          return {
            aiRiskScore: Math.min(10, Math.max(1, Number(parsed.aiRiskScore) || 7)),
            aiThreatAssessment: parsed.aiThreatAssessment || `Active ${disasterType} incident detected in ${location}. Immediate caution advised.`,
            aiActionPlan: parsed.aiActionPlan,
            aiRecommendedSupplies: parsed.aiRecommendedSupplies || ["First Aid Kit", "Emergency Drinking Water", "Flashlight"],
            aiVolunteerBriefing: parsed.aiVolunteerBriefing || `Proceed with caution to ${location}. Assess casualties and coordinate with local teams.`,
          };
        }
      }
    } catch (err) {
      console.log("[AIEngine] Using built-in Disaster Intelligence Engine:", err.message);
    }
  }

  // Built-in High-Accuracy Emergency Intelligence Engine
  let riskScore = 5;
  let threatAssessment = `Active ${disasterType} reported in ${location}. Exercise immediate caution and prioritize life safety.`;
  let actionPlan = [];
  let supplies = [];
  let volunteerBriefing = "";

  if (typeLower.includes("flood") || descLower.includes("flood") || descLower.includes("water")) {
    riskScore = severity === "High" ? 9 : 7;
    threatAssessment = `Severe water inundation risk in ${location}. Rapid flash floods and submerged electrical hazards pose critical life danger.`;
    actionPlan = [
      "Move to the highest ground or upper level of sturdy concrete buildings immediately.",
      "Shut off main electricity breaker and gas cylinder valves before water touches sockets.",
      "Never attempt to walk, swim, or drive through flowing water — 6 inches of moving water can sweep you away.",
      "Boil or purify all water before drinking; avoid contact with contaminated flood runoff.",
      "Keep a high-frequency whistle or flashlight ready to signal emergency rescue boats.",
    ];
    supplies = [
      "Packaged Drinking Water (min 3L/person)",
      "Life Jackets / Buoyancy Aids",
      "Waterproof Pouch for IDs & Medicines",
      "High-Power LED Torch & Spare Batteries",
      "Non-perishable High Energy Foods",
    ];
    volunteerBriefing = `Deploy with personal flotation devices (PFD) and reflective gear. Verify if high-voltage power lines have been cut in ${location}. Coordinate flat-bottom inflatable boats for trapped elderly or children.`;

  } else if (typeLower.includes("fire") || descLower.includes("fire") || descLower.includes("smoke") || descLower.includes("blaze")) {
    riskScore = severity === "High" ? 10 : 8;
    threatAssessment = `Rapidly spreading fire and toxic smoke hazard in ${location}. Critical thermal injury and smoke inhalation risks.`;
    actionPlan = [
      "Evacuate the premises immediately — do not stop to gather personal belongings.",
      "Crawl low on hands and knees beneath the rising smoke layer to breathe cleaner air.",
      "Feel all door handles with the back of your hand before turning; if hot, do NOT open.",
      "If clothes catch fire: Stop immediately, Drop to the ground, and Roll to smother flames.",
      "Call Fire Emergency (101 / 112) immediately once at a safe distance; never re-enter a burning structure.",
    ];
    supplies = [
      "Wet Cotton Towels / N95 Smoke Masks",
      "Sterile Burn Dressings & Clean Cling Wrap",
      "Fire Blanket / ABC Fire Extinguisher",
      "Burn Ointment & Rehydration Fluids",
    ];
    volunteerBriefing = `Do NOT enter burning structures without Fire Brigade clearance. Establish an initial triage staging post 150m upwind from smoke plume in ${location}. Provide immediate burn care and oxygen support to evacuees.`;

  } else if (typeLower.includes("earthquake") || descLower.includes("earthquake") || descLower.includes("quake")) {
    riskScore = severity === "High" ? 9 : 7;
    threatAssessment = `Active seismic event in ${location}. High risk of secondary structural collapses, ruptured gas pipelines, and intense aftershocks.`;
    actionPlan = [
      "DROP, COVER, and HOLD ON immediately under a solid desk or interior load-bearing frame.",
      "Stay away from exterior glass windows, mirrors, facades, and heavy overhead cabinets.",
      "If outside, move to an open clearing away from utility poles, buildings, and overhead cables.",
      "Expect significant aftershocks over the next 24-48 hours; do not use elevators under any circumstances.",
      "Check for gas leaks by smell — if suspected, evacuate immediately and do not flick any electrical switches.",
    ];
    supplies = [
      "First Aid Kit with Splints & Gauze",
      "Emergency Whistle to Signal Under Debris",
      "Dust Masks & Work Gloves",
      "Multi-Tool & Sturdy Footwear",
      "Portable Power Bank & AM/FM Radio",
    ];
    volunteerBriefing = `Bring search whistles, crowbars, and heavy-duty work gloves. Screen ${location} for structural masonry instability before entry. Prioritize locating trapped individuals by establishing regular periods of silence to listen for tapping.`;

  } else if (typeLower.includes("collapse") || descLower.includes("trapped") || descLower.includes("collapsed")) {
    riskScore = 10;
    threatAssessment = `Catastrophic structural failure in ${location}. Imminent crush hazard with high probability of trapped survivors needing extrication.`;
    actionPlan = [
      "Remain calm if trapped: Cover mouth with clothing to conserve breath and avoid inhaling fine concrete dust.",
      "Tap rhythmically on a metal pipe or wall so acoustic search sensors can detect your position.",
      "Avoid unnecessary shouting to prevent inhaling toxic pulverized dust and conserving oxygen.",
      "Clear immediate perimeter of unstable rubble only if safe to prevent secondary collapses.",
      "Keep phone battery conserved: Send short SMS with exact room/floor location to emergency contacts.",
    ];
    supplies = [
      "Acoustic / Whistle Signaling Devices",
      "Sterile Pressure Bandages & Tourniquets",
      "Dust Respirator Masks",
      "Thermal Blankets to Prevent Shock",
    ];
    volunteerBriefing = `Coordinate immediately with NDRF / Fire Department heavy extrication teams. Establish a zero-vibration perimeter around ${location} to avoid shifting debris onto victims. Prepare trauma kits for crush injury syndrome.`;

  } else if (typeLower.includes("cyclone") || typeLower.includes("storm") || descLower.includes("wind") || descLower.includes("storm")) {
    riskScore = 8;
    threatAssessment = `High-velocity cyclonic winds and flying debris hazard in ${location}. Uprooted trees and severed power lines likely.`;
    actionPlan = [
      "Take shelter in an interior room on the lowest floor without windows (e.g., hallway or bathroom).",
      "Disconnect all non-essential electrical appliances to prevent surge damage.",
      "Do NOT go outside during the 'eye of the storm' when winds temporarily lull — severe reverse winds will resume quickly.",
      "Keep domestic livestock and pets untied so they can escape rising waters if necessary.",
      "Monitor official IMD / Disaster Management broadcasts via battery radio or verified apps.",
    ];
    supplies = [
      "Heavy Waterproof Tarpaulins",
      "Cell Phone Power Bank fully charged",
      "Battery-Powered Weather Radio",
      "Emergency Canned Provisions for 72 Hours",
    ];
    volunteerBriefing = `Equip chainsaw and clearance gear for downed trees blocking relief access in ${location}. Exercise extreme caution around submerged or dangling power cables. Assist in escorting vulnerable residents to designated storm shelters.`;

  } else if (typeLower.includes("accident") || descLower.includes("crash") || descLower.includes("injured")) {
    riskScore = severity === "High" ? 8 : 6;
    threatAssessment = `Transit / Industrial trauma incident in ${location}. Risk of severe hemorrhage, shock, and secondary traffic obstruction.`;
    actionPlan = [
      "Secure the scene: Place hazard warning triangles or hazard lights 50 meters back to prevent chain collisions.",
      "Do NOT move injured persons with suspected spinal or neck injury unless there is imminent fire or explosion threat.",
      "Apply direct, continuous pressure to heavily bleeding wounds with clean cloth or sterile dressing.",
      "Keep casualties warm and reassure them to prevent clinical circulatory shock.",
      "Clear access lanes for incoming ambulances (call 108 / 112 with exact landmark coordinates).",
    ];
    supplies = [
      "C-Spine Supportive Collars / Splints",
      "Hemostatic Dressings & Sterile Bandages",
      "High-Visibility Reflective Safety Vests",
      "Foil Space Blankets",
    ];
    volunteerBriefing = `Direct vehicular traffic away from the accident scene at ${location}. Coordinate rapid triage (Green/Yellow/Red) and assist paramedics with stretcher loading.`;

  } else {
    // General emergency / SOS
    riskScore = severity === "High" ? 9 : 5;
    threatAssessment = `Emergency hazard reported at ${location}. Life-safety precautions and active response dispatch underway.`;
    actionPlan = [
      "Keep your smartphone charged and close by; monitor local emergency announcements.",
      "Ensure all family members or coworkers are accounted for at an agreed rendezvous point.",
      "Avoid circulating unverified social media rumors; rely exclusively on official disaster authorities.",
      "If instructed to evacuate, do so immediately using designated primary evacuation routes.",
      "Call National Emergency Number 112 if immediate physical rescue or police assistance is required.",
    ];
    supplies = [
      "Emergency First Aid Kit",
      "Sealed Water Bottles & Dry Rations",
      "Emergency Contacts List (Written Paper)",
      "High-Power Flashlight & Extra Batteries",
    ];
    volunteerBriefing = `Establish contact with the reporter in ${location}. Conduct initial scene assessment, log victim counts, and update DisasterConnect AI status.`;
  }

  return {
    aiRiskScore: riskScore,
    aiThreatAssessment: threatAssessment,
    aiActionPlan: actionPlan,
    aiRecommendedSupplies: supplies,
    aiVolunteerBriefing: volunteerBriefing,
  };
}

module.exports = {
  generateDisasterActionPlan,
};
