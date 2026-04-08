class LoginPage:

    def __init__(self, page):
        self.page = page

    def load(self, base_url):
        self.page.goto(f"{base_url}/web/index.php/auth/login")

    def login(self, username, password):
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()