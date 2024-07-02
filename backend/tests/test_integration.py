import requests

def test_backend_login():
    url = "http://devops-bot-backend-service:5000/login"
    payload = {"username": "admin", "password": "admin"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert data["message"] == "Welcome to DevOps Bot", f"Unexpected response message: {data['message']}"

def test_ui_login():
    url = "http://devops-bot-ui-service:80/login"
    payload = {"username": "admin", "password": "admin"}
    response = requests.post(url, data=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "Welcome to DevOps Bot" in response.text, "Login failed in UI"

if __name__ == "__main__":
    test_backend_login()
    test_ui_login()
    print("All integration tests passed!")
