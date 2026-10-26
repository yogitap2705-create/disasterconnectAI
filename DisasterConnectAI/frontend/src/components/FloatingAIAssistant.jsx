import { useState, useRef, useEffect } from "react";
import { Link } from "react-router-dom";
import API from "../services/api";
import {
  FaRobot,
  FaTimes,
  FaPaperPlane,
  FaExpandAlt,
  FaExclamationTriangle,
} from "react-icons/fa";

function FloatingAIAssistant() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Emergency AI Assistant online. Ask for immediate survival steps or first aid instructions.",
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  useEffect(() => {
    if (isOpen) {
      chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages, isOpen]);

  const handleSend = async (textToSend) => {
    const query = (textToSend || input).trim();
    if (!query || loading) return;

    setMessages((prev) => [...prev, { role: "user", content: query }]);
    setInput("");
    setLoading(true);

    try {
      const res = await API.post("/chat", {
        message: query,
        history: messages.map((m) => ({ role: m.role, content: m.content })),
      });
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: res.data?.reply || "Guidance unavailable. Please call 112 in emergency.",
        },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Network interrupted. For immediate life hazards call 112 / 108.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      {/* Floating Trigger Button */}
      {!isOpen && (
        <button
          onClick={() => setIsOpen(true)}
          style={styles.triggerButton}
          title="Open AI Emergency Assistant"
        >
          <FaRobot size={20} />
          <span style={styles.triggerText}>AI Emergency Help</span>
          <span style={styles.pulseDot}></span>
        </button>
      )}

      {/* Floating Chat Window */}
      {isOpen && (
        <div style={styles.chatWindow}>
          <div style={styles.header}>
            <div style={{ display: "flex", alignItems: "center", gap: "8px" }}>
              <div style={styles.botBadge}>
                <FaRobot size={15} color="#800020" />
              </div>
              <div>
                <h4 style={{ margin: 0, fontSize: "14px", color: "#ffffff" }}>
                  DisasterConnect AI
                </h4>
                <small style={{ fontSize: "10.5px", color: "#ffd4d4" }}>
                  Active Emergency Support
                </small>
              </div>
            </div>

            <div style={{ display: "flex", alignItems: "center", gap: "8px" }}>
              <Link
                to="/chatbot"
                style={styles.expandLink}
                title="Expand to Full Page"
                onClick={() => setIsOpen(false)}
              >
                <FaExpandAlt size={12} />
              </Link>
              <button
                style={styles.closeBtn}
                onClick={() => setIsOpen(false)}
                title="Close Assistant"
              >
                <FaTimes size={14} />
              </button>
            </div>
          </div>

          {/* Quick SOS Bar */}
          <div style={styles.sosBar}>
            <span>Hotlines: <strong>112</strong> (All) | <strong>108</strong> (Medical) | <strong>101</strong> (Fire)</span>
          </div>

          {/* Messages */}
          <div style={styles.messagesBox}>
            {messages.map((m, i) => (
              <div
                key={i}
                style={{
                  ...styles.bubble,
                  alignSelf: m.role === "user" ? "flex-end" : "flex-start",
                  backgroundColor: m.role === "user" ? "#800020" : "#ffffff",
                  color: m.role === "user" ? "#ffffff" : "#212529",
                  border: m.role === "user" ? "none" : "1px solid #e9ecef",
                }}
              >
                <div style={{ whiteSpace: "pre-wrap" }}>{m.content}</div>
              </div>
            ))}
            {loading && (
              <div style={{ ...styles.bubble, alignSelf: "flex-start", backgroundColor: "#f1f3f5", color: "#666", fontSize: "12px" }}>
                Analyzing safety protocols...
              </div>
            )}
            <div ref={chatEndRef} />
          </div>

          {/* Input Box */}
          <form
            onSubmit={(e) => {
              e.preventDefault();
              handleSend();
            }}
            style={styles.inputForm}
          >
            <input
              type="text"
              placeholder="Ask emergency advice..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              style={styles.inputField}
              disabled={loading}
            />
            <button
              type="submit"
              disabled={!input.trim() || loading}
              style={{
                ...styles.sendButton,
                opacity: input.trim() && !loading ? 1 : 0.6,
              }}
            >
              <FaPaperPlane size={13} />
            </button>
          </form>
        </div>
      )}
    </>
  );
}

const styles = {
  triggerButton: {
    position: "fixed",
    bottom: "24px",
    right: "24px",
    backgroundColor: "#800020",
    color: "#ffffff",
    border: "2px solid #ffffff",
    borderRadius: "30px",
    padding: "12px 20px",
    display: "flex",
    alignItems: "center",
    gap: "10px",
    boxShadow: "0 6px 20px rgba(128, 0, 32, 0.4)",
    cursor: "pointer",
    zIndex: 9999,
    fontSize: "14px",
    fontWeight: "700",
    transition: "transform 0.2s, box-shadow 0.2s",
  },
  triggerText: {
    letterSpacing: "0.2px",
  },
  pulseDot: {
    width: "8px",
    height: "8px",
    borderRadius: "50%",
    backgroundColor: "#2ecc71",
  },
  chatWindow: {
    position: "fixed",
    bottom: "24px",
    right: "24px",
    width: "360px",
    maxWidth: "90vw",
    height: "480px",
    backgroundColor: "#ffffff",
    borderRadius: "16px",
    boxShadow: "0 12px 35px rgba(0, 0, 0, 0.25)",
    border: "1px solid #e5e7eb",
    display: "flex",
    flexDirection: "column",
    overflow: "hidden",
    zIndex: 9999,
  },
  header: {
    backgroundColor: "#800020",
    padding: "12px 16px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },
  botBadge: {
    width: "28px",
    height: "28px",
    borderRadius: "50%",
    backgroundColor: "#ffffff",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  expandLink: {
    color: "#ffffff",
    display: "flex",
    alignItems: "center",
    textDecoration: "none",
    opacity: 0.85,
  },
  closeBtn: {
    background: "transparent",
    border: "none",
    color: "#ffffff",
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
  },
  sosBar: {
    backgroundColor: "#fff5f5",
    color: "#800020",
    padding: "6px 12px",
    fontSize: "11px",
    borderBottom: "1px solid #fed7d7",
    textAlign: "center",
  },
  messagesBox: {
    flex: 1,
    overflowY: "auto",
    padding: "14px",
    display: "flex",
    flexDirection: "column",
    gap: "10px",
    backgroundColor: "#f8f9fa",
  },
  bubble: {
    maxWidth: "85%",
    borderRadius: "12px",
    padding: "10px 14px",
    fontSize: "13px",
    lineHeight: "1.45",
    boxShadow: "0 1px 3px rgba(0,0,0,0.05)",
  },
  inputForm: {
    display: "flex",
    padding: "10px",
    borderTop: "1px solid #e9ecef",
    backgroundColor: "#ffffff",
    gap: "8px",
  },
  inputField: {
    flex: 1,
    border: "1px solid #ced4da",
    borderRadius: "20px",
    padding: "8px 14px",
    fontSize: "13px",
    outline: "none",
  },
  sendButton: {
    backgroundColor: "#800020",
    color: "#ffffff",
    border: "none",
    width: "36px",
    height: "36px",
    borderRadius: "50%",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    cursor: "pointer",
    flexShrink: 0,
  },
};

export default FloatingAIAssistant;
