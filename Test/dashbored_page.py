from selenium.webdriver.common.by import By 
from selenium.webdriver import ActionChains
class DashboardPage:
    def _init_(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.user_dropdown = (By.CLASS_NAME, "oxd-userdropdown-tab")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")

    def hover_and_click_pim(self):
        pim_element = self.driver.find_element(*self.pim_menu)
        ActionChains(self.driver).move_to_element(pim_element).click().perform()

    def logout(self):
        self.driver.find_element(*self.user_dropdown).click()
        self.driver.find_element(*self.logout_button).click()