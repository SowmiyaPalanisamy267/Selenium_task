from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live")
    yield driver
    driver.quit()
