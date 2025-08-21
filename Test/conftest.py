import pytest 
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture 
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()