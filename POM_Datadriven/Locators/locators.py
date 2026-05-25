from selenium.webdriver.common.by import By

class Locators:
    # LoginPage
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button   = (By.XPATH, "//button[normalize-space()='Login']")

    #Dashboard Page
    user_dropdown = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    logout_link   = (By.XPATH, "//a[text()='Logout']")

   

