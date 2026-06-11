import datetime
import os
from selenium.common import TimeoutException, NoSuchElementException
from Pages.LoginPages import LoginPage
from Pages.DashboardPages import DashboardPage
from Utilities import XLUtils

path = os.path.join(os.path.dirname(__file__), "..", "Utilities", "test.xlsx")
rows = XLUtils.get_row_count(path, 'Sheet1')

class TestLogin:

    def test_login(self,setup_browser):
        driver = setup_browser
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        for r in range(2, rows + 1):
            test_id = f"T{r-1:03d}"
            username = XLUtils.read_data(path, 'Sheet1', r, 2)
            password = XLUtils.read_data(path, 'Sheet1', r, 3)

            now = datetime.datetime.now()
            date = now.strftime("%Y-%m-%d")
            time_of_test = now.strftime("%H:%M:%S")
            tester_name = os.getlogin()

            try:
                login_page.enter_username(username)
                login_page.enter_password(password)
                login_page.click_login()

                dashboard_page.verify_login_success()
                print("Test Case Passed")
                result = "Test Passed"

                dashboard_page.logout()

            except (NoSuchElementException, TimeoutException):
                print("Test Case Failed")
                result = "Test Failed"

            except Exception as e:
                print(f"Login Failed : {e}")
                result = "Test Failed"
            # Write results back to Excel
            XLUtils.write_data(path, 'Sheet1', r, 1, test_id)
            XLUtils.write_data(path, 'Sheet1', r, 4, date)
            XLUtils.write_data(path, 'Sheet1', r, 5, time_of_test)
            XLUtils.write_data(path, 'Sheet1', r, 6, tester_name)
            XLUtils.write_data(path, 'Sheet1', r, 7, result)
