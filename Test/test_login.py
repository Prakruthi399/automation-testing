# test_login.py
from login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_valid():
    # Setup WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)


    try:
        login_page = LoginPage(driver)
        login_page.login("Admin", "admin123")

        time.sleep(3)  # optional, better to use waits in real-world

        # Validation
        if "dashboard" in driver.current_url.lower():
            print(" Test Passed: Login successful")
        else:
            print("Test Failed: Login not successful")
    finally:
        driver.quit()