import { useState, useRef, useEffect } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import API from "../services/api";
import {
  FaRobot,
  FaPaperPlane,
  FaPhoneAlt,
  FaTrash,
  FaCopy,
  FaCheck,
  FaFirstAid,
  FaExclamationTriangle,
  FaUser,
  FaBuilding,
  FaWater,
  FaFire,
  FaBandAid,
  FaSuitcase,
} from "react-icons/fa";

const QUICK_PROMPTS = [
  { Icon: FaBuilding, label: "Earthquake Safety", query: "What should I do during an earthquake?" },
  { Icon: FaWater, label: "Flood Evacuation", query: "What are the immediate survival steps during a flood?" },
  { Icon: FaFire, label: "Building Fire Escape", query: "How to safely escape a building fire?" },
  { Icon: FaBandAid, label: "First Aid for Burns", query: "How do I give first aid for severe burns and wounds?" },
  { Icon: FaSuitcase, label: "72-Hr Survival Kit", query: "What should be in a 72-hour emergency survival kit?" },
  { Icon: FaPhoneAlt, label: "Emergency Helplines", query: "What are the essential emergency helpline numbers?" },
];

const EMERGENCY_NUMBERS = [
  { name: "All Emergency", number: "112", color: "#d90429" },
  { name: "Disaster (NDRF)", number: "1078", color: "#800020" },
  { name: "Ambulance", number: "108", color: "#e63946" },
  { name: "Fire", number: "101", color: "#f77f00" },
  { name: "Police", number: "100", color: "#1d3557" },
];

function AIChatbot() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Hello! I am your **DisasterConnect AI Emergency Assistant**.\n\nI can provide immediate survival steps, evacuation guidance, first aid instructions, and disaster protocols. If you or someone else is in immediate life-threatening danger, please contact emergency services right away at **112** or **108**.\n\nHow can I help you today?",
      time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [copiedIndex, setCopiedIndex] = useState(null);

  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, loading]);

  const handleSend = async (textToSend) => {
    const query = (textToSend || input).trim();
    if (!query || loading) return;

    const userMessage = {
      role: "user",
      content: query,
      time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const historyPayload = messages.map((m) => ({
        role: m.role,
        content: m.content,
      }));

      const res = await API.post("/chat", {
        message: query,
        history: historyPayload,
      });

      const replyContent = res.data?.reply || "I couldn't process that request. Please try again.";

      const aiMessage = {
        role: "assistant",
        content: replyContent,
        time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error("Chat error:", error);
      const errorMessage = {
        role: "assistant",
        content:
          "**Emergency Notice:** Unable to reach network servers.\n\nFor immediate life safety emergencies, please call **112** (National Emergency) or **108** (Ambulance).",
        time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
      setTimeout(() => inputRef.current?.focus(), 100);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const clearChat = () => {
    if (window.confirm("Are you sure you want to clear this conversation?")) {
      setMessages([
        {
          role: "assistant",
          content:
            "Chat cleared. How can I assist you with emergency response or disaster guidelines?",
          time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
        },
      ]);
    }
  };

  const copyToClipboard = (text, index) => {
    navigator.clipboard.writeText(text);
    setCopiedIndex(index);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  const formatMessageText = (content) => {
    // Simple line renderer supporting bold markdown and linebreaks
    const lines = content.split("\n");
    return lines.map((line, idx) => {
      // Replace **text** with <strong>text</strong>
      const parts = line.split(/(\*\*.*?\*\*)/g);
      return (
        <span key={idx} style={{ display: "block", minHeight: line ? "auto" : "10px" }}>
          {parts.map((part, pIdx) => {
            if (part.startsWith("**") && part.endsWith("**")) {
              return <strong key={pIdx}>{part.slice(2, -2)}</strong>;
            }
            return part;
          })}
        </span>
      );
    });
  };

  return (
    <>
      <Navbar />

      <div style={styles.pageWrapper}>
        <div style={styles.container}>
          {/* Header Banner */}
          <div style={styles.header}>
            <div style={styles.headerLeft}>
              <div style={styles.botIconWrapper}>
                <FaRobot size={24} color="#ffffff" />
              </div>
              <div>
                <h1 style={styles.title}>AI Emergency Responder</h1>
                <p style={styles.subtitle}>
                  24/7 Disaster Guidance, First Aid & Crisis Decision Support
                </p>
              </div>
            </div>
            <div style={styles.headerRight}>
              <span style={styles.onlineBadge}>
                <span style={styles.onlineDot}></span> Active
              </span>
              <button
                style={styles.clearBtn}
                onClick={clearChat}
                title="Clear conversation"
              >
                <FaTrash size={13} style={{ marginRight: "6px" }} /> Clear
              </button>
            </div>
          </div>

          {/* Quick Helplines Bar */}
          <div style={styles.helplineBar}>
            <div style={styles.helplineTitle}>
              <FaPhoneAlt size={12} color="#800020" style={{ marginRight: "6px" }} />
              <span>SOS Helplines:</span>
            </div>
            <div style={styles.helplineBadges}>
              {EMERGENCY_NUMBERS.map((item, idx) => (
                <a
                  key={idx}
                  href={`tel:${item.number}`}
                  style={{
                    ...styles.helplineItem,
                    borderColor: item.color,
                  }}
                  title={`Call ${item.name}`}
                >
                  <span style={styles.helplineName}>{item.name}:</span>
                  <strong style={{ color: item.color, marginLeft: "4px" }}>
                    {item.number}
                  </strong>
                </a>
              ))}
            </div>
          </div>

          {/* Messages Area */}
          <div style={styles.messagesContainer}>
            {messages.map((msg, index) => {
              const isAssistant = msg.role === "assistant";
              return (
                <div
                  key={index}
                  style={{
                    ...styles.messageRow,
                    justifyContent: isAssistant ? "flex-start" : "flex-end",
                  }}
                >
                  {isAssistant && (
                    <div style={styles.avatarBot}>
                      <FaRobot size={15} color="#800020" />
                    </div>
                  )}

                  <div
                    style={{
                      ...styles.messageBubble,
                      ...(isAssistant
                        ? styles.assistantBubble
                        : styles.userBubble),
                    }}
                  >
                    <div style={styles.messageContent}>
                      {formatMessageText(msg.content)}
                    </div>

                    <div
                      style={{
                        ...styles.messageFooter,
                        justifyContent: isAssistant ? "space-between" : "flex-end",
                      }}
                    >
                      {isAssistant && (
                        <button
                          style={styles.copyBtn}
                          onClick={() => copyToClipboard(msg.content, index)}
                          title="Copy response"
                        >
                          {copiedIndex === index ? (
                            <>
                              <FaCheck size={11} color="#2b8a3e" style={{ marginRight: "4px" }} />
                              <span style={{ color: "#2b8a3e" }}>Copied</span>
                            </>
                          ) : (
                            <>
                              <FaCopy size={11} style={{ marginRight: "4px" }} /> Copy
                            </>
                          )}
                        </button>
                      )}
                      <span style={styles.timestamp}>{msg.time}</span>
                    </div>
                  </div>

                  {!isAssistant && (
                    <div style={styles.avatarUser}>
                      <FaUser size={13} color="#ffffff" />
                    </div>
                  )}
                </div>
              );
            })}

            {loading && (
              <div style={styles.loadingRow}>
                <div style={styles.avatarBot}>
                  <FaRobot size={15} color="#800020" />
                </div>
                <div style={styles.loadingBubble}>
                  <span style={styles.dot}></span>
                  <span style={{ ...styles.dot, animationDelay: "0.2s" }}></span>
                  <span style={{ ...styles.dot, animationDelay: "0.4s" }}></span>
                  <span style={styles.loadingText}>Analyzing safety protocols...</span>
                </div>
              </div>
            )}

            <div ref={messagesEndRef} />
          </div>

          {/* Suggested Quick Prompt Chips */}
          <div style={styles.promptsSection}>
            <div style={styles.promptLabel}>
              <FaFirstAid size={12} color="#800020" style={{ marginRight: "6px" }} />
              <span>Common Inquiries:</span>
            </div>
            <div style={styles.promptsGrid}>
              {QUICK_PROMPTS.map((item, idx) => {
                const IconComp = item.Icon;
                return (
                  <button
                    key={idx}
                    style={styles.promptChip}
                    onClick={() => handleSend(item.query)}
                    disabled={loading}
                  >
                    <IconComp style={{ marginRight: "6px" }} />
                    {item.label}
                  </button>
                );
              })}
            </div>
          </div>

          {/* Chat Input Section */}
          <div style={styles.inputArea}>
            <textarea
              ref={inputRef}
              rows={2}
              style={styles.input}
              placeholder="Ask an emergency question (e.g., 'What to do during a flood?'). Press Enter to send..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              disabled={loading}
            />
            <button
              style={{
                ...styles.sendBtn,
                opacity: input.trim() && !loading ? 1 : 0.6,
                cursor: input.trim() && !loading ? "pointer" : "not-allowed",
              }}
              onClick={() => handleSend()}
              disabled={!input.trim() || loading}
              title="Send message"
            >
              <FaPaperPlane size={16} />
            </button>
          </div>

          {/* Safety Notice */}
          <div style={styles.disclaimer}>
            <FaExclamationTriangle size={12} color="#e63946" style={{ marginRight: "6px" }} />
            <span>
              <strong>Emergency Notice:</strong> AI advice is for preparedness and guidance. For life-threatening emergencies, always call <strong>112</strong> immediately.
            </span>
          </div>
        </div>
      </div>

      <Footer />
    </>
  );
}

const styles = {
  pageWrapper: {
    backgroundColor: "#f4f5f7",
    minHeight: "calc(100vh - 140px)",
    padding: "24px 16px",
    display: "flex",
    justifyContent: "center",
    alignItems: "flex-start",
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
  },
  container: {
    width: "100%",
    maxWidth: "960px",
    backgroundColor: "#ffffff",
    borderRadius: "16px",
    boxShadow: "0 10px 30px rgba(0, 0, 0, 0.08)",
    border: "1px solid #e5e7eb",
    display: "flex",
    flexDirection: "column",
    overflow: "hidden",
  },
  header: {
    backgroundColor: "#800020",
    color: "#ffffff",
    padding: "20px 24px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    flexWrap: "wrap",
    gap: "12px",
  },
  headerLeft: {
    display: "flex",
    alignItems: "center",
    gap: "14px",
  },
  botIconWrapper: {
    width: "44px",
    height: "44px",
    borderRadius: "12px",
    backgroundColor: "rgba(255, 255, 255, 0.2)",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  title: {
    margin: 0,
    fontSize: "20px",
    fontWeight: "700",
    letterSpacing: "-0.3px",
  },
  subtitle: {
    margin: "4px 0 0 0",
    fontSize: "13px",
    opacity: 0.9,
  },
  headerRight: {
    display: "flex",
    alignItems: "center",
    gap: "12px",
  },
  onlineBadge: {
    display: "inline-flex",
    alignItems: "center",
    gap: "6px",
    fontSize: "12px",
    backgroundColor: "rgba(255, 255, 255, 0.2)",
    padding: "4px 10px",
    borderRadius: "20px",
    fontWeight: "500",
  },
  onlineDot: {
    width: "8px",
    height: "8px",
    borderRadius: "50%",
    backgroundColor: "#2ecc71",
  },
  clearBtn: {
    display: "inline-flex",
    alignItems: "center",
    backgroundColor: "rgba(255, 255, 255, 0.15)",
    color: "#ffffff",
    border: "1px solid rgba(255, 255, 255, 0.25)",
    padding: "6px 12px",
    borderRadius: "8px",
    fontSize: "12px",
    cursor: "pointer",
    transition: "background 0.2s",
  },
  helplineBar: {
    backgroundColor: "#fff5f5",
    borderBottom: "1px solid #fed7d7",
    padding: "10px 20px",
    display: "flex",
    alignItems: "center",
    flexWrap: "wrap",
    gap: "10px",
  },
  helplineTitle: {
    display: "flex",
    alignItems: "center",
    fontSize: "12px",
    fontWeight: "700",
    color: "#800020",
    textTransform: "uppercase",
    letterSpacing: "0.5px",
  },
  helplineBadges: {
    display: "flex",
    flexWrap: "wrap",
    gap: "8px",
  },
  helplineItem: {
    textDecoration: "none",
    fontSize: "12px",
    padding: "3px 8px",
    backgroundColor: "#ffffff",
    borderRadius: "6px",
    border: "1px solid",
    display: "inline-flex",
    alignItems: "center",
    transition: "transform 0.15s",
  },
  helplineName: {
    color: "#4a5568",
  },
  messagesContainer: {
    height: "460px",
    overflowY: "auto",
    padding: "24px 20px",
    backgroundColor: "#fbfbfc",
    display: "flex",
    flexDirection: "column",
    gap: "18px",
  },
  messageRow: {
    display: "flex",
    alignItems: "flex-end",
    gap: "10px",
    maxWidth: "100%",
  },
  avatarBot: {
    width: "32px",
    height: "32px",
    borderRadius: "50%",
    backgroundColor: "#fce8e6",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    flexShrink: 0,
    border: "1px solid #fed7d7",
  },
  avatarUser: {
    width: "32px",
    height: "32px",
    borderRadius: "50%",
    backgroundColor: "#800020",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    flexShrink: 0,
  },
  messageBubble: {
    maxWidth: "78%",
    borderRadius: "14px",
    padding: "14px 18px",
    fontSize: "14.5px",
    lineHeight: "1.55",
    boxShadow: "0 2px 6px rgba(0, 0, 0, 0.04)",
  },
  assistantBubble: {
    backgroundColor: "#ffffff",
    color: "#1a202c",
    border: "1px solid #e2e8f0",
    borderBottomLeftRadius: "3px",
  },
  userBubble: {
    backgroundColor: "#800020",
    color: "#ffffff",
    borderBottomRightRadius: "3px",
  },
  messageContent: {
    wordBreak: "break-word",
  },
  messageFooter: {
    display: "flex",
    alignItems: "center",
    marginTop: "8px",
    paddingTop: "6px",
    borderTop: "1px solid rgba(0, 0, 0, 0.06)",
    fontSize: "11px",
  },
  copyBtn: {
    background: "transparent",
    border: "none",
    color: "#718096",
    cursor: "pointer",
    display: "inline-flex",
    alignItems: "center",
    fontSize: "11px",
    padding: "2px 4px",
    borderRadius: "4px",
  },
  timestamp: {
    color: "#a0aec0",
    fontSize: "11px",
  },
  loadingRow: {
    display: "flex",
    alignItems: "center",
    gap: "10px",
  },
  loadingBubble: {
    backgroundColor: "#ffffff",
    border: "1px solid #e2e8f0",
    borderRadius: "14px",
    padding: "12px 18px",
    display: "inline-flex",
    alignItems: "center",
    gap: "6px",
  },
  dot: {
    width: "7px",
    height: "7px",
    borderRadius: "50%",
    backgroundColor: "#800020",
    display: "inline-block",
  },
  loadingText: {
    fontSize: "12px",
    color: "#718096",
    marginLeft: "6px",
    fontStyle: "italic",
  },
  promptsSection: {
    padding: "12px 20px 8px 20px",
    borderTop: "1px solid #edf2f7",
    backgroundColor: "#ffffff",
  },
  promptLabel: {
    fontSize: "11px",
    fontWeight: "700",
    color: "#718096",
    textTransform: "uppercase",
    letterSpacing: "0.5px",
    marginBottom: "8px",
    display: "flex",
    alignItems: "center",
  },
  promptsGrid: {
    display: "flex",
    flexWrap: "wrap",
    gap: "8px",
  },
  promptChip: {
    backgroundColor: "#f7fafc",
    border: "1px solid #e2e8f0",
    color: "#2d3748",
    padding: "6px 12px",
    borderRadius: "20px",
    fontSize: "12.5px",
    cursor: "pointer",
    transition: "all 0.15s ease",
    display: "inline-flex",
    alignItems: "center",
  },
  inputArea: {
    padding: "14px 20px 10px 20px",
    backgroundColor: "#ffffff",
    display: "flex",
    gap: "12px",
    alignItems: "flex-end",
  },
  input: {
    flex: 1,
    padding: "12px 16px",
    borderRadius: "12px",
    border: "1px solid #cbd5e0",
    fontSize: "14px",
    fontFamily: "inherit",
    outline: "none",
    resize: "none",
    lineHeight: "1.4",
  },
  sendBtn: {
    backgroundColor: "#800020",
    color: "#ffffff",
    border: "none",
    width: "48px",
    height: "48px",
    borderRadius: "12px",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    flexShrink: 0,
    transition: "background 0.2s, transform 0.1s",
  },
  disclaimer: {
    padding: "10px 20px 14px 20px",
    backgroundColor: "#ffffff",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: "11.5px",
    color: "#718096",
    borderTop: "1px solid #f1f3f5",
    textAlign: "center",
  },
};

export default AIChatbot;