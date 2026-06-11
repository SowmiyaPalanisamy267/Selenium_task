import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAjax:
    def test_ajax(self, setup_browser):
        driver = setup_browser
        try:
            while True:
                population_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='counter-ticker is-size-2-mobile']"))).text
                print("Current Population:", population_element)
                print("Press Ctrl+C to stop the script.")                
                time.sleep(5)  # refresh every 5 seconds
        except KeyboardInterrupt:
            print("Stopped by user (Ctrl+C).")
       