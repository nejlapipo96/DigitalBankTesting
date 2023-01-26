from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import re

class SignUpPage:
    def __init__(self,driver):
        self.driver = driver

    def signUptitle(self, value):
        title = Select(self.driver.find_element(By.ID, "title"))
        title.select_by_visible_text(value)

    def signUpFirstName(self,firstname):
        self.driver.find_element(By.ID, "firstName").send_keys(firstname)

    def signUpLastName(self, lastname):
        self.driver.find_element(By.ID, "lastName").send_keys(lastname)

    def signUpGender(self, gender):
        if gender == "M":
            self.driver.find_element(By.XPATH, "//label[@for='male']//input[@id='gender']").click()
        elif gender == "F":
            self.driver.find_element(By.XPATH, "//label[@for='female']//input[@id='gender']").click()
        else:
            self.driver.find_element(By.XPATH, "//label[@for='female']//input[@id='gender']").click()

    def signUpDob(self, dob):
        self.driver.find_element(By.ID, "dob").send_keys(dob)

    def signUpSsn(self, ssn):
        self.driver.find_element(By.ID, "ssn").send_keys(ssn)

    def is_valid_email(self, email):
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return email_regex.match(email)

    def signUpEmail(self, email):
        if self.is_valid_email(email):
            self.driver.find_element(By.ID, "emailAddress").send_keys(email)
        else:
            print("Invalid email address.")

    def signUpPassword(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def signUpConfpass(self, confpass):
        self.driver.find_element(By.ID, "confirmPassword").send_keys(confpass)

    def clickNext(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    def signUpSecondPage(self, address, locality, region, postcode, country, home_phone, mobile_phone, work_phone):
        self.driver.find_element(By.ID, "address").send_keys(address)
        self.driver.find_element(By.ID, "locality").send_keys(locality)
        self.driver.find_element(By.ID, "region").send_keys(region)
        self.driver.find_element(By.ID, "postalCode").send_keys(postcode)
        self.driver.find_element(By.ID, "country").send_keys(country)
        self.driver.find_element(By.ID, "homePhone").send_keys(home_phone)
        self.driver.find_element(By.ID, "mobilePhone").send_keys(mobile_phone)
        self.driver.find_element(By.ID, "workPhone").send_keys(work_phone)
        self.driver.find_element(By.XPATH, "//input[@id='agree-terms']").click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Register']").click()

    def login(self, log_password):
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(log_password)
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()







