import pytest
from playwright.sync_api import sync_playwright
from app_context import AppContext
from utilities.users_generator import UserGenerator

def pytest_addoption(parser):
    parser.addoption(
        "--headless-toggle", action="store_true", default=False, help="Run tests in headed mode"
    )


@pytest.fixture(scope="module")
def browser(request):
    headless_toggle = request.config.getoption("--headless-toggle")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headless_toggle)
        yield browser
        browser.close()


@pytest.fixture(scope="module")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="module")
def app_objects(page):
    return AppContext(page)

@pytest.fixture(scope="module")
def user(app_objects):
    # Ensure user is created once for the whole module
    return UserGenerator.create_and_register_user(app_objects.api_utils)