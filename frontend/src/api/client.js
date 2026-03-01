import axios from "axios";

// In dev the Vite proxy handles /api → backend:8000.
// In production, nginx does the same.
const api = axios.create({ baseURL: "/api/v1" });

// Attach the JWT token to every request automatically
export function setAuthToken(token) {
    if (token) {
        api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    } else {
        delete api.defaults.headers.common["Authorization"];
    }
}

// --- Auth ---

export async function loginRequest(username, password) {
    // FastAPI's OAuth2PasswordRequestForm expects form-urlencoded data
    const form = new URLSearchParams();
    form.append("username", username);
    form.append("password", password);
    const { data } = await api.post("/auth/login", form);
    return data;
}

export async function registerRequest(username, password) {
    const { data } = await api.post("/auth/register", { username, password });
    return data;
}

export async function fetchMe() {
    const { data } = await api.get("/auth/me");
    return data;
}

// --- Query ---

export async function askQuestion(query) {
    const { data } = await api.post("/query/ask", { query });
    return data;
}

export async function fetchHistory() {
    const { data } = await api.get("/query/history");
    return data;
}

export default api;
