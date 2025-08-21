from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_pim_module(self):
        # Click PIM from side menu
        pim_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
        pim_menu.click()
        
        # Wait for the Add button or Employee List tab to ensure PIM page is loaded
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='PIM']")))

    def click_add_employee(self):
        try:
            add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
            add_button.click()
        except Exception as e:
            print(" Add Employee button not clickable.")
            raise e

    def add_employee(self, first_name, last_name):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
        self.driver.find_element(By.NAME, "lastName").send_keys(last_name)

        # Wait for loader to disappear before clicking Save
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader")))

        save_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        save_btn.click()

        # Wait for any post-save loader to disappear
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader")))

    def go_to_employee_list(self):
        # Navigate to "Employee List" tab under PIM
        emp_list_tab = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Employee List")))
        emp_list_tab.click()

        # Wait for search field to appear
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))

    def verify_employee_in_list(self, first_name):
        # Refresh to ensure latest data
        time.sleep(1)
        self.driver.refresh()
        self.go_to_employee_list()

        # Search by first name
        search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
        search_input.clear()
        search_input.send_keys(first_name)

        # Click Search
        search_btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
        search_btn.click()

        # Wait for search results to load
        time.sleep(2)

        try:
            self.driver.find_element(By.XPATH, f"//div[text()='{first_name}']")
            print(f" Name Verified: {first_name}")
        except Exception as e:
            print(f" Name Not Found: {first_name}")