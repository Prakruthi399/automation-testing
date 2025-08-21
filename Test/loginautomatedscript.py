from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome with log suppression
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])  # suppress logs

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Open OrangeHRM
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(100)
driver.maximize_window()

# Explicit wait setup
wait = WebDriverWait(driver, 10)

# Step 2: Wait for and enter username
username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
username_field.send_keys("Admin")

# Step 3: Wait for and enter password
password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password_field.send_keys("admin123")

# Step 4: Click Login button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

# Step 5: Verify successful login
time.sleep(3)
if "dashboard" in driver.current_url.lower():
    print("Test Passed: Login successful")
else:
    print("Test Failed: Login not successful")

# Close the browser
driver.quit()
