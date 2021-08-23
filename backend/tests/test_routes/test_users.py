import json


def test_create_user(client):
    data = {
        "username": "tuser01",
        "email": "tuser01@google.com",
        "password": "qwer1234!",
    }
    res = client.post("/users/", json.dumps(data))

    assert res.status_code == 200
    assert res.json()["email"] == "tuser01@google.com"
    assert res.json()["is_active"] == True
