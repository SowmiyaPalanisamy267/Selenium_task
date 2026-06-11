from POM_Automation_Framework.Pages.loginPage import LoginPage
from POM_Automation_Framework.Pages.logoutPage import LogoutPage
import time

class TestLogin:

    def test_login_valid(self,setup_browser):
        driver = setup_browser
        driver.get("https://www.zenclass.in/login")
        login = LoginPage(driver)
        login.enter_username("valid@gmail.com") #valid userid
        login.enter_password("123456") #valid password
        login.click_login()
        time.sleep(5)
        login.close_popup()
        assert login.is_dashboard_loaded() is True

    def test_login_invalid_username(self,setup_browser):
        driver = setup_browser
        driver.get("https://www.zenclass.in/login")
        login = LoginPage(driver)
        login.enter_username("wronguser@gmail.com") #invalid userid
        login.enter_password("123456") #valid password
        login.click_login()
        assert login.is_dashboard_loaded() is False

    def test_login_invalid_password(self,setup_browser):
        driver = setup_browser
        driver.get("https://www.zenclass.in/login")
        login = LoginPage(driver)
        login.enter_username("test@gmail.com") #valid userid
        login.enter_password("WrongPassword123") #invalid password
        login.click_login()
        assert login.is_dashboard_loaded() is False

    def test_login_empty_credentials(self,setup_browser):
        driver = setup_browser
        driver.get("https://www.zenclass.in/login")
        login = LoginPage(driver)
        login.enter_username("") #blank userid
        login.enter_password("") #blank password
        login.click_login()
        assert login.is_dashboard_loaded() is False

    def test_login_only_username(self,setup_browser):
        driver = setup_browser
        driver.get("https://www.zenclass.in/login")
        login = LoginPage(driver)
        login.enter_username("test@gmail.com") #valid userid
        login.enter_password("") #empty password
        login.click_login()
        assert login.is_dashboard_loaded() is False

    def test_login_only_password(self,setup_browser):
        driver = setup_browser
        driver.get("https://www.zenclass.in/login")
        login = LoginPage(driver)
        login.enter_username("") #empty userid
        login.enter_password("123456") #valid password
        login.click_login()
        assert login.is_dashboard_loaded() is False

    def test_logout_valid(self,setup_browser):
        driver = setup_browser
        driver.get("https://www.zenclass.in/login")
        login = LoginPage(driver)
        login.enter_username("valid@gmail.com") #valid userid
        login.enter_password("123456") #valid password
        login.click_login()
        login.close_popup()
        logout= LogoutPage(driver)
        logout.click_on_menu()
        logout.click_logout()
        time.sleep(5)
        assert logout.is_logged_out() is True





