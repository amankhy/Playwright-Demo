from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_example(page: Page):

    #  START tracing manually
    # page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    # some action
    page.get_by_role("link", name="Dashboard").click()

    # STOP tracing and SAVE file
    # page.context.tracing.stop(path="trace.zip")

    def test_login(page, base_url, credentials):
        login = LoginPage(page)
        dashboard = DashboardPage(page)

        login.load(base_url)
        login.login(credentials["username"], credentials["password"])

        dashboard.verify_dashboard()