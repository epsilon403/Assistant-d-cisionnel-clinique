# ============================================================
# test_health.py - Test du endpoint /health
# ============================================================


def test_health(client):
    """GET /health should return status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
