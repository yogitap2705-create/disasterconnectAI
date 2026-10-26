/**
 * Emergency Knowledge Base & Fallback Guidance Engine
 * Provides instant, life-saving advice when external LLM APIs are unreachable or offline.
 */

const EMERGENCY_TOPICS = [
  {
    keywords: ["earthquake", "quake", "tremor", "shaking"],
    title: "🚨 Earthquake Safety Protocol",
    response: `**DURING AN EARTHQUAKE:**
1. **Drop, Cover, and Hold On:** Drop to hands and knees, take cover under a sturdy desk or table, and hold on until shaking stops.
2. **If Indoors:** Stay inside! Keep away from glass windows, exterior doors, hanging lights, and heavy furniture that could topple.
3. **If Outdoors:** Move to an open area away from buildings, streetlights, trees, and power lines. Drop low to avoid being knocked down.
4. **If in a Moving Vehicle:** Pull over to a clear location, stop safely, and stay inside with your seatbelt fastened until shaking ends.

**AFTER THE SHAKING STOPS:**
• Check yourself and others for injuries.
• Inspect for gas leaks (do NOT turn on light switches or light matches if you smell gas).
• Be prepared for aftershocks.
• Call emergency services (**112**) if anyone is trapped or severely injured.`,
  },
  {
    keywords: ["flood", "flooding", "water level", "drowning", "heavy rain"],
    title: "🌊 Flood Survival Guidelines",
    response: `**IMMEDIATE FLOOD ACTIONS:**
1. **Move to Higher Ground:** Immediately seek elevated ground or upper floors. Do not wait for instructions if water is rising rapidly.
2. **Turn Off Utilities:** Disconnect electricity and gas mains if safe to do so before water enters your premises.
3. **Turn Around, Don't Drown:**
   • Never walk through moving water. Just 6 inches (15 cm) of moving water can knock you off your feet.
   • Never drive into flooded streets. 12 inches of water can float small cars; 2 feet can sweep away trucks.
4. **Avoid Floodwater Contact:** Floodwaters often carry sewage, hazardous chemicals, and live electrical currents from submerged wires.
5. **Emergency Contacts:** Call **108** (Ambulance) or **1078** (Disaster Management) for rescue assistance.`,
  },
  {
    keywords: ["fire", "smoke", "burns", "flame", "blaze"],
    title: "🔥 Fire & Smoke Evacuation Protocol",
    response: `**IF A FIRE BREAKS OUT:**
1. **Get Out Immediately:** Do not try to collect personal possessions. Evacuate calmly.
2. **Crawl Low Under Smoke:** Smoke rises and contains deadly carbon monoxide. Stay on your hands and knees where air is cleaner.
3. **Check Doors Before Opening:** Feel door handles with the back of your hand. If hot, DO NOT OPEN—find another exit.
4. **Stop, Drop, and Roll:** If your clothes catch fire, do NOT run. Stop immediately, drop to the ground, cover your face, and roll until flames are smothered.
5. **Never Use Elevators:** Always use the emergency stairwell.
6. **Call Fire Service:** Dial **101** or **112** as soon as you are safely outside.`,
  },
  {
    keywords: ["cyclone", "hurricane", "typhoon", "storm", "high wind"],
    title: "🌀 Cyclone & High Wind Safety",
    response: `**CYCLONE SAFETY MEASURES:**
1. **Secure Your Home:** Board up or tape windows, secure loose outdoor objects (tins, pots, debris) that could turn into projectiles.
2. **Stay Indoors:** Remain in the strongest part of your home (interior room or hallway on the lowest floor).
3. **Beware the Eye of the Storm:** If winds suddenly calm, do NOT venture outside. The opposite side of the storm wall will follow shortly.
4. **Keep Essentials Ready:** Charge your phone, keep a battery-operated radio, flashlights, water bottles, and emergency medicines at hand.
5. **Emergency Helpline:** Dial **1070** or **1078** for regional disaster assistance.`,
  },
  {
    keywords: ["first aid", "bleeding", "wound", "cut", "blood"],
    title: "🩹 First Aid: Severe Bleeding & Wounds",
    response: `**CONTROLLING SEVERE BLEEDING:**
1. **Apply Direct Pressure:** Use a clean cloth, sterile gauze, or your bare hand (if nothing else is available) and press firmly on the wound.
2. **Maintain Constant Pressure:** Keep pressing without lifting the dressing for at least 5-10 minutes. If blood soaks through, add more cloth on top—do not remove the bottom layer.
3. **Elevate:** If possible and there are no broken bones, elevate the bleeding limb above the heart.
4. **Keep Warm & Calm:** Help the person lie down and keep them warm to prevent shock.
5. **Call for Immediate Help:** Dial **108** or **112** for paramedic assistance.`,
  },
  {
    keywords: ["burn", "scald", "scalding"],
    title: "🩹 First Aid: Thermal Burns",
    response: `**TREATING BURNS:**
1. **Cool Immediately:** Run cool (NOT ice-cold) running tap water over the burn for 10 to 20 minutes.
2. **DO NOT Use Ice, Butter, or Toothpaste:** These can worsen tissue damage and cause infection.
3. **Remove Constricting Items:** Gently remove rings, belts, or tight clothing around the burn before swelling starts (do NOT remove clothing stuck to burned skin).
4. **Cover Cleanly:** Cover with clean, sterile, non-fluffy gauze or clean cling wrap.
5. **Seek Medical Care:** For large burns, facial burns, or burns that blister heavily, call **108** immediately.`,
  },
  {
    keywords: ["cpr", "unconscious", "breathing", "choking", "heart attack"],
    title: "❤️ Life-Saving CPR & Unconscious Care",
    response: `**CPR (ADULT RESUSCITATION):**
1. **Check Responsiveness:** Tap their shoulders firmly and shout: "Are you okay?"
2. **Call for Help:** Immediately shout for someone to call **108** or **112**.
3. **Check Breathing:** Look at the chest for 5-10 seconds. If not breathing or only gasping:
4. **Hands-Only CPR:**
   • Place the heel of one hand in the center of the chest; place your other hand on top and interlock fingers.
   • Push hard and fast at a rate of 100-120 beats per minute (to the rhythm of "Stayin' Alive").
   • Compress at least 2 inches (5 cm) deep and allow full chest recoil between compressions.
   • Continue until emergency responders arrive or an automated external defibrillator (AED) is ready.`,
  },
  {
    keywords: ["kit", "bag", "supplies", "survival", "prepare", "emergency kit"],
    title: "🎒 72-Hour Emergency Go-Bag Checklist",
    response: `**ESSENTIAL 72-HOUR DISASTER SURVIVAL KIT:**
1. **Water:** 3-4 liters per person per day (for drinking and sanitation).
2. **Non-Perishable Food:** Ready-to-eat canned goods, energy bars, dry fruits, and a manual can opener.
3. **Light & Power:** High-power LED flashlight, spare batteries, and fully charged power banks with cables.
4. **First Aid Kit:** Sterile gauze, bandages, antiseptic wipes, painkillers, burn ointment, and personal prescription medications.
5. **Sanitation:** Hand sanitizer, moist towelettes, masks, and garbage bags.
6. **Important Documents:** Copies of IDs, insurance, medical records in a waterproof sealed pouch.
7. **Multi-Tool & Whistle:** A whistle to signal for help under debris, plus a pocket multi-tool.`,
  },
  {
    keywords: ["helpline", "number", "contact", "police", "ambulance", "hospital", "phone"],
    title: "📞 Essential Emergency Helplines (India)",
    response: `**CRITICAL EMERGENCY CONTACT NUMBERS:**
• **National All-in-One Emergency:** **112**
• **Police:** **100**
• **Fire Service:** **101**
• **Ambulance / Medical Emergency:** **108** / **102**
• **National Disaster Management (NDRF / NDMA):** **1078**
• **State Disaster Emergency Ops (Maharashtra):** **1070**
• **Women Helpline:** **1091**
• **Child Helpline:** **1098**
• **Traffic Police Emergency:** **103**

*Tip: In high-stress situations, keep calm, state your exact location, describe the immediate danger, and stay on the line until instructed.*`,
  },
];

/**
 * Generates an intelligent, context-aware emergency safety response
 * when external LLMs are unreachable.
 */
function getEmergencyFallback(message) {
  const query = (message || "").toLowerCase().trim();

  // Find the most relevant emergency topic
  let matchedTopic = null;
  let maxMatches = 0;

  for (const topic of EMERGENCY_TOPICS) {
    let matchCount = 0;
    for (const kw of topic.keywords) {
      if (query.includes(kw)) {
        matchCount++;
      }
    }
    if (matchCount > maxMatches) {
      maxMatches = matchCount;
      matchedTopic = topic;
    }
  }

  if (matchedTopic) {
    return matchedTopic.response;
  }

  // Default emergency guidance
  return `**DisasterConnect AI Emergency Assistant**

I am ready to help you with emergency preparedness, incident response, and first aid guidance.

**Key Emergency Steps:**
1. **Ensure Immediate Safety:** Move yourself and dependents away from immediate physical hazards (collapsing structures, fire, rising water, falling debris).
2. **Call Emergency Services:** If lives are in danger, immediately dial **112** (National Emergency) or **108** (Ambulance).
3. **Stay Informed:** Monitor official local advisories and news channels.
4. **Submit a Report:** Use the **Report Disaster** page in DisasterConnect AI to notify responders and alert volunteers with your coordinates.

*You can ask me specific questions like: "What to do during an earthquake?", "How to treat a burn?", "Flood safety checklist", or "Emergency helpline numbers".*`;
}

module.exports = {
  getEmergencyFallback,
  EMERGENCY_TOPICS,
};
