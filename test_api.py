from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_bad_scheme_return_400():
    response =  client.get("/scan", params={"url": "ftp://example.com"}) 
    assert response.status_code == 400

def test_empty_url_return_400():
    response = client.get("/scan", params={"url": "     "} ) 
    assert response.status_code == 400

def test_site_error_returns_502(monkeypatch):
    monkeypatch.setattr(
        "main.full_header_check",
        lambda url: {"error": "Server returned status 404"},
    )
    response = client.get("/scan", params={"url": "https://example.com"})
    assert response.status_code == 502