# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# import pytest


# def test_drag_and_drop():
#     driver = webdriver.Chrome() # Setup driver
#     driver.maximize_window()


#     driver.get("http://jqueryui.com/droppable/")# Open URL

#     iframe = driver.find_element(By.CLASS_NAME, "demo-frame") # Switch to iframe FIRST
#     driver.switch_to.frame(iframe)

#     # Locate elements
#     source = driver.find_element(By.ID, "draggable")
#     target = driver.find_element(By.ID, "droppable")

#     # Create ActionChains object
#     actions = ActionChains(driver)
#     actions.drag_and_drop(source, target).perform()

#     time.sleep(3)

#     driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time


# Fixture
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


#  Positive test
def test_drag_and_drop_positive(setup):
    driver = setup
    try:
        driver.get("https://jqueryui.com/droppable/")
        time.sleep(2)  # wait for page load

        # Switch to iframe
        iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
        driver.switch_to.frame(iframe)
        time.sleep(1)

        source = driver.find_element(By.ID, "draggable")
        target = driver.find_element(By.ID, "droppable")

        #  Create ActionChains object
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()    

        time.sleep(2)

        assert target.text == "Dropped!"
    finally:
        print("Test finished")


# Negative test
def test_drag_and_drop_negative(setup):
    driver = setup
    try:
        driver.get("https://jqueryui.com/droppable/")
        time.sleep(2)

        # Switch to iframe
        iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
        driver.switch_to.frame(iframe)
        time.sleep(1)

        target = driver.find_element(By.ID, "droppable")

        # No drag action

        assert target.text != "Dropped!", "Drop should not happen without drag action"

    finally:
        print("Test finished")

def test_switch_to_invalid_iframe(setup):
    driver = setup
    try:
        driver.get("https://jqueryui.com/droppable/")
        time.sleep(2)

        try:
            driver.switch_to.frame("invalid_frame") #iframe does not exist it should move to except block and print the exception message
            assert False, "Expected NoSuchFrameException but it did not occur"

        except NoSuchFrameException as e:
            print("Test Passed - Correct exception occurred:", e)

    finally:
        print("Test finished")

def test_iframe_not_present(setup):
    driver = setup
    try:
        driver.get("https://jqueryui.com/droppable/")
        time.sleep(2)

        try:
            driver.find_element(By.CLASS_NAME, "wrong-frame")#iframe name is wrong-frame and does not exist it should move to except block and print the exception message
            assert False, "Element was found but should not exist"

        except NoSuchElementException:
            #  assert True  # Test passes if NoSuchElementException is raised
             print("Test passed - element not found as expected")

    finally:
        print("Test finished")