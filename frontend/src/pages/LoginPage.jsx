import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { loginRequest, registerRequest, fetchMe } from "../api/client";
import { FiUser, FiLock, FiMail } from "react-icons/fi";

export default function LoginPage() {
    const [tab, setTab] = useState("login");
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [success, setSuccess] = useState("");
    const [busy, setBusy] = useState(false);

    const { login } = useAuth();
    const navigate = useNavigate();

    async function handleLogin(e) {
        e.preventDefault();
        setError("");
        setBusy(true);
        try {
            const data = await loginRequest(username, password);
            const user = await fetchMe().catch(() => ({ username }));
            login(data.access_token, user);
            navigate("/", { replace: true });
        } catch (err) {
            const msg = err.response?.data?.detail || "Login failed. Please try again.";
            setError(msg);
        } finally {
            setBusy(false);
        }
    }

    async function handleRegister(e) {
        e.preventDefault();
        setError("");
        setSuccess("");
        setBusy(true);
        try {
            await registerRequest(username, email, password);
            setSuccess("Compte créé ! Vous pouvez maintenant vous connecter.");
            setTab("login");
            setPassword("");
            setEmail("");
        } catch (err) {
            const msg = err.response?.data?.detail || "Registration failed.";
            setError(msg);
        } finally {
            setBusy(false);
        }
    }

    function switchTab(t) {
        setTab(t);
        setError("");
        setSuccess("");
    }

    return (
        <div className="auth-wrapper">
            <div className="auth-card glass">
                {/* Logo */}
                <div className="auth-logo">
                    <span className="icon">🏥</span>
                    <h1>CliniQ</h1>
                    <p>Assistant Décisionnel Clinique</p>
                </div>

                {/* Tabs */}
                <div className="auth-tabs">
                    <button
                        className={tab === "login" ? "active" : ""}
                        onClick={() => switchTab("login")}
                    >
                        Connexion
                    </button>
                    <button
                        className={tab === "register" ? "active" : ""}
                        onClick={() => switchTab("register")}
                    >
                        Inscription
                    </button>
                </div>

                {/* Feedback */}
                {error && <div className="auth-error">{error}</div>}
                {success && <div className="auth-success">{success}</div>}

                {/* Form */}
                <form
                    className="auth-form"
                    onSubmit={tab === "login" ? handleLogin : handleRegister}
                    style={{ marginTop: error || success ? 16 : 0 }}
                >
                    <div className="input-group">
                        <label htmlFor="username">Nom d'utilisateur</label>
                        <FiUser className="input-icon" />
                        <input
                            id="username"
                            type="text"
                            placeholder="Entrez votre nom"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            required
                            autoComplete="username"
                        />
                    </div>

                    {tab === "register" && (
                        <div className="input-group">
                            <label htmlFor="email">Email</label>
                            <FiMail className="input-icon" />
                            <input
                                id="email"
                                type="email"
                                placeholder="docteur@cliniq.com"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                required
                                autoComplete="email"
                            />
                        </div>
                    )}

                    <div className="input-group">
                        <label htmlFor="password">Mot de passe</label>
                        <FiLock className="input-icon" />
                        <input
                            id="password"
                            type="password"
                            placeholder="••••••••"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                            autoComplete={tab === "login" ? "current-password" : "new-password"}
                        />
                    </div>

                    <button className="btn-primary" type="submit" disabled={busy}>
                        {busy
                            ? "Chargement…"
                            : tab === "login"
                                ? "Se connecter"
                                : "Créer un compte"}
                    </button>
                </form>
            </div>
        </div>
    );
}
