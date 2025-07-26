from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)

def test_full_analyze_endpoint():
    payload = {
        "text": "I really enjoy this new feature!",
        "context_texts": [
            "This company is praised for its innovation.",
            "They introduced this feature in 2023.",
            "Users have responded positively."
        ]
    }

    response = client.post("/analyze", json=payload)
    assert response.status_code == 200
    result = response.json()

    assert "sentiment" in result
    assert "rag_response" in result
    assert result["sentiment"] in {"POSITIVE", "NEGATIVE", "NEUTRAL"}
    assert "context" in result["rag_response"].lower() or "\n- " in result["rag_response"]
