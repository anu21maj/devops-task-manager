from app.app import app #Go into the app package → find app.py → import the Flask application called app.

def test_home():
    client = app.test_client() #This creates a test client. Think of it as a fake browser that can make requests to your Flask application without actually running a server.

    response = client.get("/") #This simulates GET /

    assert response.status_code == 200 #I expect the status code to be 200.

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

