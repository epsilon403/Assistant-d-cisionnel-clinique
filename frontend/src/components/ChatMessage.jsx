import ReactMarkdown from "react-markdown";

export default function ChatMessage({ role, content }) {
    const isUser = role === "user";

    return (
        <div className={`chat-message ${role}`}>
            <div className="msg-avatar">{isUser ? "U" : "CQ"}</div>
            <div className="msg-body">
                {isUser ? (
                    <p>{content}</p>
                ) : (
                    <ReactMarkdown>{content}</ReactMarkdown>
                )}
            </div>
        </div>
    );
}
