class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self,email,password):
        self.page.locator("[data-qa='login-email']").fill(email)
        self.page.locator("[data-qa='login-password']").fill(password)
        self.page.locator("[data-qa='login-button']").click()

    def get_error_locator(self):
        return self.page.get_by_text("Your email or password is incorrect!")

    # Opens the login page directly (an entry page)
    def goto(self):
        self.page.goto("https://automationexercise.com/login")

