from selenium.webdriver.common.by import By
from POM_Automation_Framework.Locators.locators import Locators



class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_menu= Locators.logout_menu
        self.logout=Locators.logout

    def click_on_menu(self):
        self.driver.find_element(By.XPATH, self.logout_menu).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout).click()

    def is_logged_out(self):
        return "login" in self.driver.current_url
    





