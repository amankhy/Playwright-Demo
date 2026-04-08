import pytest
from test_data.users_data import users_test_data

# 🔥 Test data
test_data = [
    {"user_id": 1, "expected_name": "Leanne Graham"},
    {"user_id": 2, "expected_name": "Ervin Howell"},
    {"user_id": 3, "expected_name": "Clementine Bauch"},
]

@pytest.mark.parametrize("data", test_data)
def test_get_user_by_id(api_context, data):
    response = api_context.get(f"/users/{data['user_id']}")

    print(f"\nTesting user ID: {data['user_id']}")

    # ✅ Status validation
    assert response.status == 200

    json_data = response.json()

    # ✅ Data validation
    assert json_data["id"] == data["user_id"]
    assert json_data["name"] == data["expected_name"]

@pytest.mark.parametrize("data", users_test_data)
def test_user_email(api_context, data):
    response = api_context.get(f"/users/{data['user_id']}")

    assert response.status == 200

    json_data = response.json()

    assert json_data["email"] == data["expected_email"]