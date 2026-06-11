import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    time.sleep(5)
    yield driver
    driver.quit()

def test_courses_locators(setup):

    driver = setup

    parent = driver.find_element(By.XPATH, "//p[contains(@class,'menu-hover') and text()='Courses']/parent::div")
    assert parent.is_displayed()
    print("\nParent text:", parent.text)

    first_child = driver.find_element(By.XPATH, "(//p[contains(@class,'menu-hover') and text()='Courses']/parent::div/child::*)[1]")
    assert first_child.is_displayed()
    print("\nFirst child:", first_child)

    second_sibling = driver.find_element(By.XPATH, "//a[text()='Courses']/following-sibling::*[2]")
    assert second_sibling is not None
    print("\nSecond sibling HTML:\n", second_sibling.get_attribute("outerHTML"))


    parent_href = driver.find_element(By.XPATH, "//a[contains(@href,'#courses')]/parent::div")
    assert parent_href is not None
    print("\nParent href tag:", parent_href)

    ancestor = driver.find_element(By.XPATH, "//p[contains(text(), 'Courses')]/ancestor::div[@class='keen-slider__slide number-slide2']")
    assert ancestor is not None
    print("\nAncestor: ", ancestor)

    following_siblings = driver.find_elements(By.XPATH, "//a[@href='#courses']/following-sibling::*")
    assert len(following_siblings) > 0
    print("\nFollowing siblings", following_siblings)

    preceding_elements = driver.find_elements(By.XPATH, "//a[@href='#courses']/preceding-sibling::a")
    assert len(preceding_elements) > 0
    print("\nPreceding Elements", preceding_elements)


def test_live_courses_locators(setup):

    driver = setup

    parent = driver.find_element(By.XPATH, "//p[contains(@class,'menu-hover') and text()='LIVE Classes']/parent::div")
    assert parent.is_displayed()
    print("\nParent text:", parent.text)

    first_child = driver.find_element(By.XPATH,"(//p[contains(@class,'menu-hover') and text()='LIVE Classes']/parent::div/child::*)[1]")
    assert first_child.is_displayed()
    print("\nFirst child:", first_child)

    second_sibling = driver.find_element(By.XPATH, "//a[text()='LIVE Classes']/following-sibling::*[2]")
    assert second_sibling is not None
    print("\nSecond sibling HTML:\n", second_sibling.get_attribute("outerHTML"))

    parent_href = driver.find_element(By.XPATH, "//a[contains(@href,'#liveClass')]//parent::div")
    assert parent_href is not None
    print("\nParent href tag:", parent_href)

    ancestor = driver.find_element(By.XPATH,"//p[contains(text(),'LIVE Classes')]/ancestor::div[@class='keen-slider__slide number-slide1']")
    assert ancestor is not None
    print("\nAncestor: ", ancestor)

    following_siblings = driver.find_elements(By.XPATH, "//a[@href='#liveClass']/following-sibling::*")
    assert len(following_siblings) > 0
    print("\nFollowing siblings", following_siblings)

    preceding_elements = driver.find_elements(By.XPATH, "//a[@href='#liveClass']/preceding-sibling::a")
    assert len(preceding_elements) > 0
    print("\nPreceding Elements", preceding_elements)

def test_practice_locators(setup):

    driver = setup

    parent = driver.find_element(By.XPATH, "//p[contains(@class,'menu-hover') and text()='Practice']/parent::div")
    assert parent.is_displayed()
    print("\nParent text:", parent.text)

    first_child = driver.find_element(By.XPATH,"((//p[contains(@class,'menu-hover') and text()='Practice']/parent::div)//child::*)[1]")
    assert first_child.is_displayed()
    print("\nFirst child:", first_child)
    #no second sibling

    # no parent href

    ancestor = driver.find_element(By.XPATH,"//p[text()='Practice']/ancestor::div")
    assert ancestor is not None
    print("\nAncestor: ", ancestor)

    following_siblings = driver.find_elements(By.XPATH, "//p[text()='Practice']/following-sibling::*")
    assert len(following_siblings) > 0
    print("\nFollowing siblings", following_siblings)

    preceding_elements = driver.find_elements(By.XPATH, "//p[text()='Practice']/preceding::div")
    assert len(preceding_elements) > 0
    print("\nPreceding Elements", preceding_elements)

def test_resource_locators(setup):

    driver = setup

    parent = driver.find_element(By.XPATH,"//p[contains(@class,'menu-hover') and text()='Resources']/parent::div")
    assert parent.is_displayed()
    print("\nParent text:", parent.text)

    first_child = driver.find_element(By.XPATH,"((//p[contains(@class,'menu-hover') and text()='Resources']/parent::div)//child::*)[1]")
    assert first_child.is_displayed()
    print("\nFirst child:", first_child)

    # no second sibling

    # no parent href

    ancestor = driver.find_element(By.XPATH, "//p[text()='Resources']/ancestor::div")
    assert ancestor is not None
    print("\nAncestor: ", ancestor)

    following_siblings = driver.find_elements(By.XPATH, "(//p[text()='Resources']/following-sibling::*)[1]")
    assert len(following_siblings) > 0
    print("\nFollowing siblings", following_siblings)

    preceding_elements = driver.find_elements(By.XPATH, "//p[text()='Resources']/preceding::div")
    assert len(preceding_elements) > 0
    print("\nPreceding Elements", preceding_elements)


def test_our_products_locators(setup):
    driver = setup

    parent = driver.find_element(By.XPATH, "//p[contains(@class,'menu-hover') and text()='Our Products']/parent::div")
    assert parent.is_displayed()
    print("\nParent text:", parent.text)

    first_child = driver.find_element(By.XPATH,"((//p[contains(@class,'menu-hover') and text()='Our Products']/parent::div)//child::*)[1]")
    assert first_child.is_displayed()
    print("\nFirst child:", first_child)

    # no second sibling

    # no parent href

    ancestor = driver.find_element(By.XPATH, "//p[text()='Our Products']/ancestor::div")
    assert ancestor is not None
    print("\nAncestor: ", ancestor)

    following_siblings = driver.find_elements(By.XPATH, "(//p[text()='Our Products']/following-sibling::*)[1]")
    assert len(following_siblings) > 0
    print("\nFollowing siblings", following_siblings)

    preceding_elements = driver.find_elements(By.XPATH, "//p[text()='Our Products']/preceding::div")
    assert len(preceding_elements) > 0
    print("\nPreceding Elements", preceding_elements)


def test_login_locators(setup):
    driver = setup
    parent = driver.find_element(By.XPATH, "(//button[@id='login-btn' ])[1]/parent::div")
    assert parent.is_displayed()
    print("\nParent text:", parent.text)

    first_child = driver.find_element(By.XPATH,"(((//button[@id='login-btn' ])[1]/parent::div)//child::*)[1]")
    assert first_child.is_displayed()
    print("\nFirst child:", first_child)
    # no second sibling

    # no parent href
    ancestor = driver.find_element(By.XPATH,"//button[@id='login-btn']/ancestor::div")
    assert ancestor is not None
    print("\nAncestor: ", ancestor)

    following_siblings = driver.find_elements(By.XPATH, "((//button[@id='login-btn' ])[1])/following-sibling::*")
    assert len(following_siblings) > 0
    print("\nFollowing siblings", following_siblings)

    preceding_elements = driver.find_elements(By.XPATH, "(//button[@id='login-btn'])[1]/preceding::div")
    assert len(preceding_elements) > 0
    print("\nPreceding Elements", preceding_elements)

def test_signup_locators(setup):
    driver = setup
    parent = driver.find_element(By.XPATH, "(// button[text() = 'Sign up'])[1] / parent::div")
    assert parent.is_displayed()
    print("\nParent text:", parent.text)

    first_child = driver.find_element(By.XPATH,"(((//button[text()='Sign up'])[1]/parent::div)//child::*)[1]")
    assert first_child.is_displayed()
    print("\nFirst child:", first_child)

    # no second sibling

    # no parent href

    ancestor = driver.find_element(By.XPATH, "(//button[text()='Sign up'])[1]/ancestor::div")
    assert ancestor is not None
    print("\nAncestor: ", ancestor)

    #no following sibiling

    preceding_elements = driver.find_elements(By.XPATH, "(//button[text()='Sign up'])[1]/preceding::div")
    assert len(preceding_elements) > 0
    print("\nPreceding Elements", preceding_elements)





