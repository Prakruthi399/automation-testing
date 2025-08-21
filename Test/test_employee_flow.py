from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from login_page import LoginPage
from pim_page import PimPage
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_add_employees():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Login
        login = LoginPage(driver)
        login.login("Admin", "admin123")
        print("Logged in")

        # Navigate to PIM and add employees
        pim = PimPage(driver)
        pim.go_to_pim_module()

        employees = [
            ("John1", "Doe"),
            ("Jane", "Smith"),
            ("Alice", "Johnson"),
            ("Bob", "Williams")
        ]

        for first, last in employees:
            pim.go_to_pim_module()
            pim.click_add_employee()
            pim.add_employee(first, last)
            print(f"Added Employee: {first} {last}")
            time.sleep(100)

        # Verify each employee
        for first, last in employees:
            pim.verify_employee_in_list(first)

    finally:
        driver.quit()