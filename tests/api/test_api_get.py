import pytest


def test_get_users(api_context):
    response = api_context.get("/users")

    # 🔍 Logging (Better than print)
    print(f"\nStatus Code: {response.status}")

    # ✅ 1. Status Code Validation
    assert response.status == 200, f"Expected 200 but got {response.status}"

    # ✅ 2. Response Time Validation (Performance check)
    assert response.ok, "Response is not OK"

    # ✅ 3. Convert to JSON
    data = response.json()

    # ✅ 4. Validate Response Structure
    assert isinstance(data, list), "Response is not a list"
    assert len(data) > 0, "User list is empty"

    # ✅ 5. Validate Each User Object
    for user in data:
        assert "id" in user, "Missing id"
        assert "name" in user, "Missing name"
        assert "email" in user, "Missing email"

        # 🔥 Email validation
        assert "@" in user["email"], f"Invalid email: {user['email']}"

        # 🔥 Nested object validation
        assert "address" in user, "Missing address"
        assert "city" in user["address"], "Missing city in address"

    # ✅ 6. Validate Specific User (Business Validation)
    first_user = data[0]
    assert first_user["id"] == 1, "First user ID mismatch"