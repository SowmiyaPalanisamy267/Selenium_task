from selenium.webdriver.common.by import By
from POM_Automation_Framework.Locators.locators import Locators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = Locators.username_textbox
        self.password_textbox = Locators.password_textbox
        self.login_button = Locators.login_button
        self.close_button = Locators.close_button

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox).clear()
        self.driver.find_element(By.XPATH, self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox).clear()
        self.driver.find_element(By.XPATH, self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def close_popup(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.close_button))).click()
        except Exception as e:
                print("Popup not found or already closed:", e)

    # def close_popup(self):
    #     try:
    #         popup_visible = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.close_button))            )
    #         if popup_visible.is_displayed():
    #             self.driver.execute_script("arguments[0].click();", popup_visible) #.execute_script(...)Runs JavaScript code inside the browser context."arguments[0].click();" The JavaScript snippet, it says: “Take the first argument passed in, and call its .click() method.”
    #             print("Popup closed successfully.")
    #     except Exception as e:
    #         print("Popup not found or already closed:", e)


    def is_dashboard_loaded(self):
        return "dashboard" in self.driver.current_url

    def wait_for_login_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.username_textbox))
        )

