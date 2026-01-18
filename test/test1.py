import json
from app.app import create_app


def test_users_flow():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/users",
        data=json.dumps({"name": "Wojciech", "lastname": "Oczkowski"}),
        content_type="application/json",
    )
    assert response.status_code == 201
