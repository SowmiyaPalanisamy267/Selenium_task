from POM_task17.Locators.locators import Locators
from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page

    def enter_username(self, username):
        self.page.locator(Locators.username_textbox).clear()
        self.page.locator(Locators.username_textbox).fill(username)

    def enter_password(self, password):
        self.page.locator(Locators.password_textbox).clear()
        self.page.locator(Locators.password_textbox).fill(password)

    def click_login(self):
        self.page.locator(Locators.login_button).click()

    def close_popup(self):
        self.page.locator(Locators.close_button).click()

    def assert_dashboard_visible(self):
        expect(self.page.locator(Locators.dashboard_text)).to_be_visible()

    def assert_dashboard_not_visible(self):
        expect(self.page.locator(Locators.dashboard_text)).not_to_be_visible()
