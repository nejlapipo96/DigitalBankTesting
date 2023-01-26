from pageObject.LoginPage import LoginPage
from pageObject.LogOutPage import LogOutPage
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class Test_003_Login_Logout:

    baseUrl = "http://dbankdemo.com/bank/login"
    username = "kim_brown@hotmail.com"
    password = "KimBrown12345"

    logger = LogGen.loggen()

    def test_login_logout(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.login = LoginPage(self.driver)
        self.login.set_username(self.username)
        self.login.set_password(self.password)
        self.login.clickButton()

        self.logout = LogOutPage(self.driver)
        self.logout.clickOnImg()
        self.logout.clickLogOut()

        self.logout_message = self.driver.find_element(By.XPATH, "//div[@class='sufee-alert alert with-close alert-success alert-dismissible fade show']").text
        assert "Logout completed." in self.logout_message
        self.driver.save_screenshot(".\\Screenshots\\" + "logout_message.png")
        self.driver.close()
