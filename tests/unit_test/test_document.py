# ============================================================
# test_document.py - Tests du endpoint POST /api/v1/query/document
# ============================================================
from unittest.mock import patch, MagicMock


@patch("backend.api.v1.endpoints.query.RAGPipeline")
def test_ingest_document(mock_pipeline_class, client):
    """POST /api/v1/query/document should trigger RAG ingestion."""
    mock_pipeline = MagicMock()
    mock_pipeline.ingest.return_value = "System ready: Medical knowledge ingested."
    mock_pipeline_class.return_value = mock_pipeline

    response = client.post("/api/v1/query/document")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "System ready: Medical knowledge ingested."
    mock_pipeline.ingest.assert_called_once()


@patch("backend.api.v1.endpoints.query.RAGPipeline")
def test_ingest_document_custom_path(mock_pipeline_class, client):
    """POST /api/v1/query/document with custom file_path param."""
    mock_pipeline = MagicMock()
    mock_pipeline.ingest.return_value = "System ready: Medical knowledge ingested."
    mock_pipeline_class.return_value = mock_pipeline

    response = client.post(
        "/api/v1/query/document",
        params={"file_path": "data/raw/custom.pdf"}
    )
    assert response.status_code == 200
    mock_pipeline.ingest.assert_called_once_with("data/raw/custom.pdf")
