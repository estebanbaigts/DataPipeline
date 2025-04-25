from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/predict", json={"sepal_width": 3.0})
    assert response.status_code == 200, "Le code de réponse doit être 200."
    assert "predicted_sepal_length" in response.json(), "La réponse doit contenir la clé 'predicted_sepal_length'."
    assert isinstance(response.json()["predicted_sepal_length"], float), "La prédiction doit être un float."