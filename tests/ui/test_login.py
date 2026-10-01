import pytest
from playwright.sync_api import expect

from tests.ui.pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    login_page = LoginPage(page)
    login_page.goto()
    return login_page


@pytest.mark.ui
def test_login_valid_credentials(login_page, registered_user):
    login_page.login(registered_user["email"], registered_user["password"])

    logged_in = login_page.get_logged_in_locator()
    expect(logged_in).to_be_visible()
    expect(logged_in).to_contain_text(f"Logged in as {registered_user['name']}")


@pytest.mark.ui
def test_login_invalid_credentials(login_page, registered_user):
    login_page.login(registered_user["email"], "wrong_password")

    expect(login_page.get_error_locator()).to_be_visible()
    expect(login_page.get_logged_in_locator()).to_have_count(0)

@pytest.mark.ui
def test_invalid_email(login_page):
    login_page.login("nobody_12345@example.com", "SomePassword123")
    expect(login_page.get_error_locator()).to_be_visible()