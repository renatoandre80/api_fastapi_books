from fastapi.testclient import TestClient
from app.main import app
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

client = TestClient(app)

def test_get_books():
    response = client.get("/api/books?query=python")
    assert response.status_code == 200
    assert response.json()["kind"] == "books#volumes"