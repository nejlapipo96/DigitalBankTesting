from pageObject.SignUpAndLoginPage import SignUpPage
from utilities.customLogger import LogGen
from faker import Faker

fake = Faker()

class Test_001_SignUp:
    baseURL = "http://dbankdemo.com/bank/signup"
    value = "Mrs."
    firstName = "Kim"
    lastName = "Brown"
    gender = "F"
    dob = "10/02/2000"
    ssn = fake.ssn()
    email = fake.email()
    password = fake.password(length=12, digits=True, upper_case=True, lower_case=True)
    conpass = password
    address = "12 Private Drive"
    locality = "downtown"
    region = "Los Angeles"
    postcode = fake.zipcode()
    country = "US"
    home_phone = f"{fake.random_number(digits=3)}-{fake.random_number(digits=3)}-{fake.random_number(digits=4)}"
    mobile_phone = f"{fake.random_number(digits=3)}-{fake.random_number(digits=3)}-{fake.random_number(digits=4)}"
    work_phone = f"{fake.random_number(digits=3)}-{fake.random_number(digits=3)}-{fake.random_number(digits=4)}"
    log_password = password

    logger = LogGen.loggen()

    def test_signup(self, setup):
        self.logger.info('*** Test_001_SignUp ***')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.signup = SignUpPage(self.driver)
        self.signup.signUptitle(self.value)
        self.signup.signUpFirstName(self.firstName)
        self.signup.signUpLastName(self.lastName)
        self.signup.signUpGender(self.gender)
        self.signup.signUpDob(self.dob)
        self.signup.signUpSsn(self.ssn)
        self.signup.signUpEmail(self.email)
        self.signup.signUpPassword(self.password)
        self.signup.signUpConfpass(self.conpass)
        self.signup.clickNext()
        self.signup.signUpSecondPage(self.address, self.locality, self.region, self.postcode, self.country, self.home_phone, self.mobile_phone, self.work_phone)
        self.signup.clickRegister()

        self.signup.login(self.log_password)

        act_title = self.driver.title
        if act_title == "Digital Bank":
            assert True
            self.logger.info("*** Passed ***")
            self.driver.close()
        else:
            self.logger.error("*** Failed ***")
            self.driver.close()
            assert False

