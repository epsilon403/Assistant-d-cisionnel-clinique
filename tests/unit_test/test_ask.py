# ============================================================
# test_ask.py - Tests du endpoint POST /api/v1/query/ask
# ============================================================
from unittest.mock import patch, MagicMock


@patch("rag.retrieval.retriever.get_hybrid_retriever")
@patch("rag.generation.chain.create_medical_rag_chain")
def test_ask_medical_assistant(mock_chain_factory, mock_retriever, client):
    """POST /api/v1/query/ask should return a valid QueryResponse."""
    mock_chain = MagicMock()
    mock_chain.invoke.return_value = {"answer": "Le patient présente de la fièvre."}
    mock_chain_factory.return_value = mock_chain
    mock_retriever.return_value = MagicMock()

    response = client.post(
        "/api/v1/query/ask",
        json={"query": "Quels sont les symptômes?"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["query"] == "Quels sont les symptômes?"
    assert data["reponse"] == "Le patient présente de la fièvre."
    assert "id" in data
    assert "created_at" in data


def test_ask_empty_body(client):
    """POST /api/v1/query/ask with no body should return 422."""
    response = client.post("/api/v1/query/ask")
    assert response.status_code == 422


def test_ask_invalid_body(client):
    """POST /api/v1/query/ask with wrong field names should return 422."""
    response = client.post(
        "/api/v1/query/ask",
        json={"question": "this is the wrong field name"}
    )
    assert response.status_code == 422


@patch("rag.retrieval.retriever.get_hybrid_retriever", side_effect=Exception("Ollama is down"))
def test_ask_rag_failure_graceful(mock_retriever, client):
    """POST /api/v1/query/ask should still save to DB even if RAG fails."""
    response = client.post(
        "/api/v1/query/ask",
        json={"query": "Test with broken RAG"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "RAG pipeline not available" in data["reponse"]
    assert data["query"] == "Test with broken RAG"
