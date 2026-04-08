from playwright.sync_api import Page, expect


def test_example(page: Page, base_url, credentials) -> None:

    # ✅ Dynamic URL
    page.goto(f"{base_url}/web/index.php/auth/login")

    # ✅ Dynamic credentials
    page.get_by_role("textbox", name="Username").fill(credentials["username"])
    page.get_by_role("textbox", name="Password").fill(credentials["password"])

    page.get_by_role("button", name="Login").click()

    # ✅ Assertion
    expect(page.get_by_role("button", name="Upgrade")).to_be_visible()

    page.get_by_role("link", name="Performance").click()
    page.get_by_role("link", name="Dashboard").click()