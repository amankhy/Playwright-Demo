import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page (browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def api_context(playwright):
    return playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={
            "Content-Type": "application/json"
        }
    )

def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="")
    parser.addoption("--username", action="store", default="Admin")
    parser.addoption("--password", action="store", default="admin123")

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url") or "https://opensource-demo.orangehrmlive.com"


@pytest.fixture(scope="session")
def credentials(request):
    return {
        "username": request.config.getoption("--username"),
        "password": request.config.getoption("--password"),
    }