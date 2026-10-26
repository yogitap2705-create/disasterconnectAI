const Groq = require("groq-sdk");
const { getEmergencyFallback } = require("../utils/emergencyAI");

let groq = null;
if (process.env.GROQ_API_KEY) {
  try {
    groq = new Groq({
      apiKey: process.env.GROQ_API_KEY,
    });
  } catch (err) {
    console.warn("[AI Chat] Could not initialize Groq client:", err.message);
  }
}

exports.chatWithAI = async (req, res) => {
  try {
    const { message, history } = req.body;

    if (!message || !message.trim()) {
      return res.status(400).json({
        message: "Please enter a message.",
      });
    }

    const trimmedMessage = message.trim();

    // 1. If Groq is available, attempt to get a live model response
    if (groq) {
      try {
        const conversationMessages = [
          {
            role: "system",
            content:
              "You are DisasterConnect AI, an emergency disaster and first-aid response assistant. Give structured, clear, calm, practical, and safe emergency guidance. Always highlight life-safety first. For life-threatening emergencies, advise the user to contact local emergency services immediately (112 / 108 / 101 in India).",
          },
        ];

        // Append recent multi-turn history if provided
        if (Array.isArray(history)) {
          history.slice(-6).forEach((h) => {
            if (h.role && h.content) {
              conversationMessages.push({
                role: h.role === "assistant" ? "assistant" : "user",
                content: h.content,
              });
            }
          });
        }

        // Add current user message
        conversationMessages.push({
          role: "user",
          content: trimmedMessage,
        });

        const completion = await groq.chat.completions.create({
          model: "llama-3.3-70b-versatile",
          messages: conversationMessages,
          temperature: 0.4,
          max_tokens: 600,
        });

        const reply = completion.choices[0]?.message?.content;
        if (reply) {
          return res.status(200).json({
            reply,
            source: "groq",
          });
        }
      } catch (groqErr) {
        console.warn(
          "[AI Chat] Groq request failed, switching to Emergency Knowledge Engine:",
          groqErr.message
        );
      }
    }

    // 2. Fallback to built-in Emergency Knowledge Engine
    const fallbackReply = getEmergencyFallback(trimmedMessage);
    return res.status(200).json({
      reply: fallbackReply,
      source: "emergency-knowledge-engine",
    });
  } catch (error) {
    console.error("[AI Chat Controller Error]:", error);
    const emergencyReply = getEmergencyFallback(req.body?.message || "");
    return res.status(200).json({
      reply: emergencyReply,
      source: "fallback",
    });
  }
};

// ===============================
// AI Description Enhancer / Auto-Summarizer
// ===============================
exports.enhanceDescription = async (req, res) => {
  try {
    const { description, disasterType, location } = req.body;

    if (!description || !description.trim()) {
      return res.status(400).json({
        message: "Please enter a description to enhance.",
      });
    }

    const raw = description.trim();

    // 1. Try Groq if available
    if (groq) {
      try {
        const prompt = `You are DisasterConnect AI. Rewrite and enhance the following raw citizen disaster description into a concise, professional emergency incident report (2-3 sentences max). Highlight the active hazards, potential structural/life threats, and requested assistance. Return ONLY the enhanced report text:
Disaster Type: ${disasterType || "Incident"}
Location: ${location || "Local Area"}
Raw Notes: "${raw}"`;

        const completion = await Promise.race([
          groq.chat.completions.create({
            model: "llama-3.3-70b-versatile",
            messages: [{ role: "user", content: prompt }],
            temperature: 0.3,
            max_tokens: 200,
          }),
          new Promise((_, reject) => setTimeout(() => reject(new Error("Timeout")), 3000)),
        ]);

        const enhanced = completion.choices[0]?.message?.content?.trim();
        if (enhanced) {
          return res.status(200).json({
            enhancedDescription: enhanced.replace(/^["']|["']$/g, ""),
            source: "groq",
          });
        }
      } catch (err) {
        console.log("[AI Enhance] Groq unavailable, using built-in enhancer:", err.message);
      }
    }

    // 2. Built-in Emergency Description Structuring Engine
    const capitalizedType = disasterType ? disasterType.toUpperCase() : "EMERGENCY HAZARD";
    const locSnippet = location ? `at ${location}` : "in the reported vicinity";
    const lower = raw.toLowerCase();

    let hazardLevel = "MODERATE PRIORITY";
    if (
      lower.includes("trapped") ||
      lower.includes("dead") ||
      lower.includes("collapsed") ||
      lower.includes("fire") ||
      lower.includes("severe") ||
      lower.includes("flood") ||
      lower.includes("sos")
    ) {
      hazardLevel = "CRITICAL / HIGH PRIORITY";
    }

    const formattedRaw = raw.charAt(0).toUpperCase() + raw.slice(1);
    const enhanced = `[${hazardLevel} REPORT] Active ${capitalizedType} reported ${locSnippet}. Situation Details: ${formattedRaw}. Immediate field assessment, perimeter safety verification, and emergency response units requested.`;

    return res.status(200).json({
      enhancedDescription: enhanced,
      source: "built-in-enhancer",
    });
  } catch (error) {
    console.error("[Enhance Description Error]:", error);
    return res.status(500).json({
      message: "Could not enhance description at this time.",
    });
  }
};
