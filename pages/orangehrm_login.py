from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="username")
        self.password_input = page.get_by_role("textbox", name="password")
        self.login_button = page.get_by_role("button", name="login")

    def enter_username(self,username:str):
        self.username_input.fill(username)

    def enter_password(self,password:str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()