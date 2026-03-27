# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# # import pytest
# #
# # @pytest.mark.positive
# driver = webdriver.Chrome()  # Initialize the chrome
# driver.get("https://www.saucedemo.com/")# Open the webpage
#
#
# driver.find_element(By.ID, "user-name").send_keys("standard_user")# Log in using provided credentials
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# driver.find_element(By.ID, "login-button").click()
#
# time.sleep(2)
#
# title = driver.title
# print("Page Title:", title)
#
# current_url = driver.current_url
# print("Current URL:", current_url)
#
#
# page_source = driver.page_source #Extract entire contents of the webpage
# file = open("Webpage_task_11.txt", "w", encoding="utf-8")# Save to text file
# file.write(page_source)
# file.close()
#
# print("Webpage contents saved to Webpage_task_11.txt")
#
# driver.quit()

#####################################################################
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# ✅ Positive test: correct title
def test_title(driver):
    driver.get("https://www.saucedemo.com/")
    assert driver.title == "Swag Labs"   # This will pass

# ❌ Negative test: deliberately wrong title
def test_wrong_title(driver):
    driver.get("https://www.saucedemo.com/")
    assert driver.title == "Sauce Demo"   # This will fail

# ✅ Positive test: valid login goes to dashboard
def test_dashboard_url_positive(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"   # This will pass

# ❌ Negative test: invalid login should NOT reach dashboard
def test_dashboard_url_negative(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    # This will fail because invalid login stays on homepage, not dashboard
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

