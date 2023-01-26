from pageObject.LoginPage import LoginPage
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class Test_002_Login:
    baseUrl = "http://dbankdemo.com/bank/login"
    username = "kim_brown@hotmail.com"
    wrong_username= "kim@hotmail.com"
    password = "KimBrown12345"
    wrong_password = "kim12345"

    logger = LogGen.loggen()

    def test_successful_login(self, setup):
        self.logger.info("*** Test_002_Login ***")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("*** Login with valid username and password ***")
        self.login = LoginPage(self.driver)
        self.login.set_username(self.username)
        self.login.set_password(self.password)
        self.login.clickButton()

        assert "Digital Bank" in self.driver.title
        self.driver.close()
        self.logger.info("*** Successfuly logged in ***")

    def test_wrong_password(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("*** Login with valid username and invalid password ***")
        self.login = LoginPage(self.driver)
        self.login.set_username(self.username)
        self.login.set_password(self.wrong_password)
        self.login.clickButton()

        error_message = self.driver.find_element(By.XPATH, "//div[@class='sufee-alert alert with-close alert-danger alert-dismissible fade show']")
        assert error_message.is_displayed()
        self.driver.save_screenshot(".\\Screenshots\\" + "wrong_password.png")
        self.driver.close()
        self.logger.info("*** An error message is displayed and user is not logged in ***")

    def test_wrong_username(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("*** Login with invalid username and valid password ***")
        self.login = LoginPage(self.driver)
        self.login.set_username(self.wrong_username)
        self.login.set_password(self.password)
        self.login.clickButton()

        error_message = self.driver.find_element(By.XPATH, "//div[@class='sufee-alert alert with-close alert-danger alert-dismissible fade show']")
        assert error_message.is_displayed()
        self.driver.save_screenshot(".\\Screenshots\\" + "wrong_username.png")
        self.driver.close()
        self.logger.info("*** An error message is displayed and user is not logged in ***")

    def test_wrong_username_and_wrong_password(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("*** Login with invalid username and invalid password ***")
        self.login = LoginPage(self.driver)
        self.login.set_username(self.wrong_username)
        self.login.set_password(self.wrong_password)
        self.login.clickButton()

        error_message = self.driver.find_element(By.XPATH, "//div[@class='sufee-alert alert with-close alert-danger alert-dismissible fade show']")
        assert error_message.is_displayed()
        self.driver.save_screenshot(".\\Screenshots\\" + "wrong_username_and_wrong_password.png")
        self.driver.close()
        self.logger.info("*** An error message is displayed and user is not logged in ***")

    def test_empty_fields(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("*** Login without entering username and password ***")
        self.login = LoginPage(self.driver)
        self.login.clickButton()

        error_message = self.driver.find_element(By.XPATH, "//div[@class='sufee-alert alert with-close alert-danger alert-dismissible fade show']")
        assert error_message.is_displayed()
        self.driver.save_screenshot(".\\Screenshots\\" + "empty_fields.png")
        self.driver.close()
        self.logger.info("*** An error message is displayed and user is not logged in ***")

    def test_empty_username_and_valid_password(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("*** Login without username and valid password ***")
        self.login = LoginPage(self.driver)
        self.login.set_password(self.password)
        self.login.clickButton()

        error_message = self.driver.find_element(By.XPATH, "//div[@class='sufee-alert alert with-close alert-danger alert-dismissible fade show']")
        assert error_message.is_displayed()
        self.driver.save_screenshot(".\\Screenshots\\" + "empty_username_and_valid_password.png")
        self.driver.close()
        self.logger.info("*** An error message is displayed and user is not logged in ***")

    def test_empty_username_and_invalid_password(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("*** Login without username and invalid password ***")
        self.login = LoginPage(self.driver)
        self.login.set_password(self.wrong_password)
        self.login.clickButton()

        error_message = self.driver.find_element(By.XPATH, "//div[@class='sufee-alert alert with-close alert-danger alert-dismissible fade show']")
        assert error_message.is_displayed()
        self.driver.save_screenshot(".\\Screenshots\\" + "empty_username_and_invalid_password.png")
        self.driver.close()
        self.logger.info("*** An error message is displayed and user is not logged in ***")

    def test_empty_password_and_valid_username(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("*** Login with valid username and without password ***")
        self.login = LoginPage(self.driver)
        self.login.set_username(self.username)
        self.login.clickButton()

        error_message = self.driver.find_element(By.XPATH, "//div[@class='sufee-alert alert with-close alert-danger alert-dismissible fade show']")
        assert error_message.is_displayed()
        self.driver.save_screenshot(".\\Screenshots\\" + "empty_password_and_valid_username.png")
        self.driver.close()
        self.logger.info("*** An error message is displayed and user is not logged in ***")

    def test_empty_password_and_invalid_username(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("*** Login with invalid username and without password ***")
        self.login = LoginPage(self.driver)
        self.login.set_username(self.wrong_username)
        self.login.clickButton()

        error_message = self.driver.find_element(By.XPATH, "//div[@class='sufee-alert alert with-close alert-danger alert-dismissible fade show']")
        assert error_message.is_displayed()
        self.driver.save_screenshot(".\\Screenshots\\" + "empty_password_and_invalid_username.png")
        self.driver.close()
        self.logger.info("*** An error message is displayed and user is not logged in ***")
