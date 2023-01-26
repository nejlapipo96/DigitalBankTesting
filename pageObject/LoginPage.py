from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, "password"). send_keys(password)

    def isErrorMessageDisplayed(self):
        error_message = self.driver.find_element(By.XPATH, "//div[@class='sufee-alert alert with-close alert-danger alert-dismissible fade show']")
        return error_message.is_di

    def clickButton(self):
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()