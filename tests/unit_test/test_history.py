# ============================================================
# test_history.py - Tests du endpoint GET /api/v1/query/history
# ============================================================
from unittest.mock import patch, MagicMock


def test_query_history_empty(client):
    """GET /api/v1/query/history should return empty list when no queries exist."""
    response = client.get("/api/v1/query/history")
    assert response.status_code == 200
    assert response.json() == []


@patch("rag.retrieval.retriever.get_hybrid_retriever")
@patch("rag.generation.chain.create_medical_rag_chain")
def test_query_history_with_data(mock_chain_factory, mock_retriever, client):
    """GET /api/v1/query/history should return previously created queries."""
    mock_chain = MagicMock()
    mock_chain.invoke.return_value = {"answer": "Réponse test"}
    mock_chain_factory.return_value = mock_chain
    mock_retriever.return_value = MagicMock()

    # Create two queries
    client.post("/api/v1/query/ask", json={"query": "Question 1"})
    client.post("/api/v1/query/ask", json={"query": "Question 2"})

    response = client.get("/api/v1/query/history")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    queries = [item["query"] for item in data]
    assert "Question 1" in queries
    assert "Question 2" in queries
