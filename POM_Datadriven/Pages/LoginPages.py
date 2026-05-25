from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Locators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        field = self.wait.until(EC.presence_of_element_located(Locators.username_field))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.presence_of_element_located(Locators.password_field))
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.driver.find_element(*Locators.login_button).click()
