from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def setup():
    #setup code
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    time.sleep(5)
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(5)
    yield driver
    driver.quit()

@pytest.mark.positive
def test_login_url(setup):

    driver = setup
    assert "https://www.guvi.in/sign-in/" in driver.current_url


@pytest.mark.positive
def test_page_title(setup):

    driver = setup
    driver.get("https://www.guvi.in/sign-in/")

    assert "GUVI" in driver.title

@pytest.mark.positive
def test_email_with_subdomain(setup):

    driver = setup

    email = driver.find_element(By.ID, "email")
    email.send_keys("user@mail.company.com")

    assert email.get_attribute("value").endswith(".com")

@pytest.mark.positive
def test_submit_button_valid_login(setup):

    driver = setup

    email = driver.find_element(By.ID, "email")
    email.send_keys("user@gmail.com") #valid username

    password = driver.find_element(By.ID, "password")
    password.send_keys("123456") #validpassword

    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)

    assert "https://www.guvi.in/" in driver.current_url

@pytest.mark.negative
def test_submit_button_invalid_login(setup):

    driver = setup

    email=driver.find_element(By.ID, "email")
    email.send_keys("test@gmail.com")

    password=driver.find_element(By.ID, "password")
    password.send_keys("test123")

    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)

    error_message = driver.find_element(By.CLASS_NAME, "invalid-feedback").text  # Check for error message
    assert "Incorrect Email or Password" in error_message

@pytest.mark.negative
def test_email_not_endswith_com(setup):

    driver = setup

    email = driver.find_element(By.ID, "email")
    email.send_keys("user@example.org")
    value = email.get_attribute("value")
    time.sleep(5)

    assert not value.endswith(".com")


@pytest.mark.negative
def test_submit_button_with_blank_fields(setup):
    driver = setup

    email = driver.find_element(By.ID, "email")
    email.click()
    email.send_keys(Keys.TAB)

    password = driver.find_element(By.ID, "password")
    password.click()
    password.send_keys(Keys.TAB)

    driver.find_element(By.ID, "login-btn").click()
    time.sleep(3)
    error_text = driver.find_element(By.XPATH,"//div[contains(@class,'invalid-feedback') and contains(@class,'is-invalid')]").text

    assert "Password should not be empty." in error_text

@pytest.mark.negative
def test_submit_button_with_empty_fields(setup):
    driver = setup

    email=driver.find_element(By.ID, "email")
    email.send_keys("")

    password=driver.find_element(By.ID, "password")
    password.send_keys("")

    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)
    assert "Hey, Did you forgot your password? Try again." in driver.page_source

@pytest.mark.negative
def test_submit_button_with_password_blank(setup):

    driver = setup

    email = driver.find_element(By.ID, "email")
    email.send_keys("test@gmail.com")

    password = driver.find_element(By.ID, "password")
    password.send_keys("")

    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)

    assert "Hey, Did you forgot your password? Try again." in driver.page_source


@pytest.mark.negative
def test_submit_button_with_email_blank(setup):
    driver = setup

    email = driver.find_element(By.ID, "email")
    email.send_keys("")  # leave email blank

    password = driver.find_element(By.ID, "password")
    password.send_keys("123456")   # valid password

    driver.find_element(By.ID, "login-btn").click()
    time.sleep(5)

    errors = driver.find_elements(By.CSS_SELECTOR, ".invalid-feedback.is-invalid")# Extract text from all error elements
    error_texts = [e.text for e in errors]
    assert " Hmm...that doesnt look like an email address. Try again." in error_texts  # test case fails because no error message was displayed when try to log in with password and empty email id.








