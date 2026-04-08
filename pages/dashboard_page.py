from playwright.sync_api import expect

class DashboardPage:

    def __init__(self, page):
        self.page = page

    def verify_dashboard(self):
        expect(self.page.locator("h6")).to_contain_text("Dashboard")