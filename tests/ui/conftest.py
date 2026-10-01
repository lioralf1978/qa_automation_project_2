import time

import pytest

API_URL = "https://automationexercise.com/api"


@pytest.fixture(scope="session")
def registered_user(playwright):
    """Create a fresh account via the site's API and delete it after the session."""
    user = {
        "name": "QA Tester",
        "email": f"qa_tester_{int(time.time())}@example.com",
        "password": "Test1234!",
    }
    request = playwright.request.new_context()
    response = request.post(f"{API_URL}/createAccount", form={
        **user,
        "title": "Mr",
        "birth_date": "1",
        "birth_month": "1",
        "birth_year": "1990",
        "firstname": "QA",
        "lastname": "Tester",
        "company": "QA",
        "address1": "1 Test St",
        "country": "Israel",
        "zipcode": "12345",
        "state": "Center",
        "city": "Tel Aviv",
        "mobile_number": "0500000000",
    })
    assert response.json()["responseCode"] == 201, response.text()

    yield user

    request.delete(f"{API_URL}/deleteAccount",
                   form={"email": user["email"], "password": user["password"]})
    request.dispose()
