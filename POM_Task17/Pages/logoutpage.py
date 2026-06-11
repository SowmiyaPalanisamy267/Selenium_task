from POM_task17.Locators.locators import Locators
from playwright.sync_api import expect

class LogoutPage:
    def __init__(self, page):
        self.page = page

    def click_on_menu(self):
        self.page.locator(Locators.logout_menu).click()

    def click_logout(self):
        self.page.locator(Locators.logout).click()

    def is_logged_out(self):
        expect(self.page).to_have_url("https://www.zenclass.in/login")
