import { useState, useRef, useEffect } from "react";
import { Routes, Route, useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { askQuestion, fetchHistory } from "../api/client";
import ChatMessage from "../components/ChatMessage";
import {
    FiMessageSquare,
    FiClock,
    FiLogOut,
    FiSend,
    FiMenu,
    FiX,
} from "react-icons/fi";

// Quick prompts shown when the chat is empty
const QUICK_PROMPTS = [
    "Quels sont les signes d'un AVC ?",
    "Protocole de prise en charge du diabète",
    "Conduite à tenir devant une douleur thoracique",
];

export default function ChatPage() {
    const { user, logout } = useAuth();
    const navigate = useNavigate();
    const location = useLocation();

    const [sidebarOpen, setSidebarOpen] = useState(false);

    // Determine which page we're on
    const isHistory = location.pathname === "/history";

    function goTo(path) {
        navigate(path);
        setSidebarOpen(false);
    }

    return (
        <div className="chat-layout">
            {/* Mobile backdrop */}
            {sidebarOpen && (
                <div className="sidebar-backdrop" onClick={() => setSidebarOpen(false)} />
            )}

            {/* Sidebar */}
            <aside className={`sidebar ${sidebarOpen ? "open" : ""}`}>
                <div className="sidebar-header">
                    <div className="brand">
                        <span className="brand-icon">🏥</span>
                        <div>
                            <h2>CliniQ</h2>
                            <p>Assistant Clinique IA</p>
                        </div>
                    </div>
                </div>

                <nav className="sidebar-nav">
                    <button className={!isHistory ? "active" : ""} onClick={() => goTo("/")}>
                        <FiMessageSquare className="nav-icon" />
                        Chat
                    </button>
                    <button className={isHistory ? "active" : ""} onClick={() => goTo("/history")}>
                        <FiClock className="nav-icon" />
                        Historique
                    </button>
                </nav>

                <div className="sidebar-footer">
                    <div className="sidebar-user">
                        <div className="avatar">
                            {(user?.username || "U").charAt(0).toUpperCase()}
                        </div>
                        <div className="user-info">
                            <div className="username">{user?.username || "Utilisateur"}</div>
                            <div className="role">Médecin</div>
                        </div>
                    </div>
                    <button
                        className="btn-logout"
                        onClick={() => {
                            logout();
                            navigate("/login", { replace: true });
                        }}
                    >
                        <FiLogOut /> Déconnexion
                    </button>
                </div>
            </aside>

            {/* Main */}
            <div className="main-content">
                <div className="topbar">
                    <button className="menu-toggle" onClick={() => setSidebarOpen(!sidebarOpen)}>
                        {sidebarOpen ? <FiX /> : <FiMenu />}
                    </button>
                    <h1>{isHistory ? "Historique" : "Assistant Médical"}</h1>
                    <span className="dot" />
                    <span className="status">En ligne</span>
                </div>

                <Routes>
                    <Route path="/" element={<ChatView />} />
                    <Route path="/history" element={<HistoryView />} />
                </Routes>
            </div>
        </div>
    );
}

/* ── Chat View ── */

function ChatView() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const [loading, setLoading] = useState(false);
    const bottomRef = useRef(null);
    const textareaRef = useRef(null);

    // Auto-scroll when messages change
    useEffect(() => {
        bottomRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages, loading]);

    // Auto-resize the textarea
    function handleInputChange(e) {
        setInput(e.target.value);
        const el = e.target;
        el.style.height = "auto";
        el.style.height = Math.min(el.scrollHeight, 140) + "px";
    }

    async function handleSend(e) {
        e.preventDefault();
        const q = input.trim();
        if (!q || loading) return;

        setMessages((prev) => [...prev, { role: "user", content: q }]);
        setInput("");
        if (textareaRef.current) textareaRef.current.style.height = "auto";
        setLoading(true);

        try {
            const data = await askQuestion(q);
            setMessages((prev) => [
                ...prev,
                { role: "assistant", content: data.reponse || "Aucune réponse." },
            ]);
        } catch {
            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    content: "Désolé, une erreur est survenue. Veuillez réessayer.",
                },
            ]);
        } finally {
            setLoading(false);
        }
    }

    function handleKeyDown(e) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSend(e);
        }
    }

    function usePrompt(text) {
        setInput(text);
        textareaRef.current?.focus();
    }

    return (
        <>
            <div className="messages-area">
                {messages.length === 0 && !loading ? (
                    <div className="welcome-state">
                        <span className="welcome-icon">🩺</span>
                        <h2>Comment puis-je vous aider ?</h2>
                        <p>
                            Posez une question médicale et obtenez une réponse basée sur les
                            protocoles cliniques.
                        </p>
                        <div className="quick-prompts">
                            {QUICK_PROMPTS.map((p) => (
                                <button key={p} onClick={() => usePrompt(p)}>
                                    {p}
                                </button>
                            ))}
                        </div>
                    </div>
                ) : (
                    <>
                        {messages.map((m, i) => (
                            <ChatMessage key={i} role={m.role} content={m.content} />
                        ))}
                        {loading && (
                            <div className="chat-message assistant">
                                <div className="msg-avatar">CQ</div>
                                <div className="msg-body">
                                    <div className="typing-indicator">
                                        <span />
                                        <span />
                                        <span />
                                    </div>
                                </div>
                            </div>
                        )}
                    </>
                )}
                <div ref={bottomRef} />
            </div>

            <div className="input-bar">
                <form onSubmit={handleSend}>
                    <textarea
                        ref={textareaRef}
                        rows={1}
                        placeholder="Posez votre question médicale…"
                        value={input}
                        onChange={handleInputChange}
                        onKeyDown={handleKeyDown}
                        disabled={loading}
                    />
                    <button className="btn-send" type="submit" disabled={!input.trim() || loading}>
                        <FiSend />
                    </button>
                </form>
            </div>
        </>
    );
}

/* ── History View ── */

function HistoryView() {
    const [items, setItems] = useState([]);
    const [loaded, setLoaded] = useState(false);

    useEffect(() => {
        fetchHistory()
            .then((data) => setItems(data))
            .catch(() => setItems([]))
            .finally(() => setLoaded(true));
    }, []);

    if (!loaded) {
        return (
            <div className="history-page">
                <p style={{ color: "var(--text-muted)" }}>Chargement…</p>
            </div>
        );
    }

    return (
        <div className="history-page">
            <h2>Historique des requêtes</h2>
            {items.length === 0 ? (
                <div className="history-empty">Aucun historique pour le moment.</div>
            ) : (
                <div className="history-list">
                    {items.map((item) => (
                        <div className="history-card" key={item.id}>
                            <div className="q">❓ {item.query}</div>
                            <div className="a">{item.reponse}</div>
                            <div className="ts">
                                {new Date(item.created_at).toLocaleString("fr-FR")}
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}
