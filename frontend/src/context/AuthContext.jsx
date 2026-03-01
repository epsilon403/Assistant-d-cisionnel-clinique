import { createContext, useContext, useState, useEffect } from "react";
import { setAuthToken, fetchMe } from "../api/client";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
    const [token, setToken] = useState(() => localStorage.getItem("cliniq_token"));
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(!!token);

    // When the app mounts with an existing token, try to fetch the user profile
    useEffect(() => {
        if (token) {
            setAuthToken(token);
            fetchMe()
                .then((u) => setUser(u))
                .catch(() => {
                    // Token is invalid or expired — clear it
                    logout();
                })
                .finally(() => setLoading(false));
        }
    }, []); // eslint-disable-line react-hooks/exhaustive-deps

    function login(accessToken, userData) {
        localStorage.setItem("cliniq_token", accessToken);
        setAuthToken(accessToken);
        setToken(accessToken);
        setUser(userData);
    }

    function logout() {
        localStorage.removeItem("cliniq_token");
        setAuthToken(null);
        setToken(null);
        setUser(null);
    }

    if (loading) {
        return (
            <div style={{ display: "grid", placeItems: "center", height: "100vh", color: "#64748b" }}>
                Loading…
            </div>
        );
    }

    return (
        <AuthContext.Provider value={{ token, user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const ctx = useContext(AuthContext);
    if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
    return ctx;
}
