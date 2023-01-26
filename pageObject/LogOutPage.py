from selenium.webdriver.common.by import By

class LogOutPage:

    def __init__(self, driver):
        self.driver = driver

    def clickOnImg(self):
        self.driver.find_element(By.XPATH, "//img[@alt='User Avatar']").click()

    def clickLogOut(self):
        self.driver.find_element(By.XPATH, "//a[@href='/bank/logout']").click()