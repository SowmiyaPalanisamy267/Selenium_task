from POM_task17.Pages.loginpage import LoginPage
from POM_task17.Pages.logoutpage import LogoutPage


def test_valid_login(page):
    loginpage=LoginPage(page)
    loginpage.enter_username("valid@gmail.com")
    loginpage.enter_password("123456")
    loginpage.click_login()
    loginpage.close_popup()
    loginpage.assert_dashboard_visible()

def test_invalid_login(page):
    loginpage=LoginPage(page)
    loginpage.enter_username("invalid@gmail.com")
    loginpage.enter_password("invalid")
    loginpage.click_login()
    loginpage.assert_dashboard_not_visible()

def test_login_invalid_password(page):
    loginpage = LoginPage(page)
    loginpage.enter_username("valid@gmail.com")
    loginpage.enter_password("invalid")
    loginpage.click_login()
    loginpage.assert_dashboard_not_visible()

def test_login_empty_credentials(page):
    loginpage = LoginPage(page)
    loginpage.enter_username("")#empty
    loginpage.enter_password("")#empty
    loginpage.click_login()
    loginpage.assert_dashboard_not_visible()


def test_login_only_username(page):
     loginpage = LoginPage(page)
     loginpage.enter_username("valid@gmail.com")
     loginpage.click_login()
     loginpage.assert_dashboard_not_visible()

def test_login_only_password(page):
    loginpage = LoginPage(page)
    loginpage.enter_password("valid")
    loginpage.click_login()
    loginpage.assert_dashboard_not_visible()


def test_valid_logout(page):
    loginpage=LoginPage(page)
    loginpage.enter_username("valid@gmail.com")
    loginpage.enter_password("valid")
    loginpage.click_login()
    loginpage.close_popup()
    logout=LogoutPage(page)
    logout.click_on_menu()
    logout.click_logout()
    logout.is_logged_out()