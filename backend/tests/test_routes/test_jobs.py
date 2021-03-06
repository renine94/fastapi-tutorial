import json


def test_create_job(client, normal_user_token_headers):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.fdj.com",
        "location": "Korea, Incheon",
        "description": "Testing",
        "date_posted": "2022-07-20",
    }

    res = client.post(
        "/jobs/create-job", json.dumps(data), headers=normal_user_token_headers
    )

    assert res.status_code == 200
    assert res.json()["company"] == "testhoo"
    assert res.json()["location"] == "Korea, Incheon"


def test_retreive_job_by_id(client, normal_user_token_headers):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.fdj.com",
        "location": "Korea, Incheon",
        "description": "Testing",
        "date_posted": "2022-07-20",
    }
    client.post("/jobs/create-job", json.dumps(data), headers=normal_user_token_headers)
    response = client.get("/jobs/get/1")

    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1 Yahoo"


def test_retreive_all_jobs(client, normal_user_token_headers):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.fdj.com",
        "location": "Korea, Incheon",
        "description": "Testing",
        "date_posted": "2022-07-20",
    }
    data2 = {
        "title": "SDE 2 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.fdj.com",
        "location": "Korea, Incheon",
        "description": "Testing",
        "date_posted": "2022-07-20",
    }
    client.post("/jobs/create-job", json.dumps(data), headers=normal_user_token_headers)
    client.post(
        "/jobs/create-job", json.dumps(data2), headers=normal_user_token_headers
    )
    response = client.get("/jobs/all")

    assert response.status_code == 200
    assert response.json()[1]["title"] == "SDE 2 Yahoo"
    assert len(response.json()) == 2
