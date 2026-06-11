from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Locators

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_login_success(self):
        """Wait until the user dropdown is visible, confirming login worked."""
        return self.wait.until(EC.presence_of_element_located(Locators.user_dropdown))

    def logout(self):
        """Click the user dropdown and then the logout link."""
        self.driver.find_element(*Locators.user_dropdown).click()
        self.wait.until(EC.element_to_be_clickable(Locators.logout_link)).click()
