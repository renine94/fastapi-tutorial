import json


def test_create_job(client):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.fdj.com",
        "location": "Korea, Incheon",
        "description": "Testing",
        "date_posted": "2022-07-20",
    }

    res = client.post("/job/create-job", json.dumps(data))

    assert res.status_code == 200
