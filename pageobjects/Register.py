from selenium.webdriver.common.by import By


class Register_page:
    #constructor
    def __init__(self, driver):
        self.driver = driver

    # signUp_login xpath
    signUp_login = (By.XPATH, "//a[contains(text(),' Signup / Login')]")

    # new_user_signup_text  xpath
    new_user_signup_text=(By.XPATH,"//h2[contains(text(),'New User Signup!')]")

    # name  xpath
    name = (By.XPATH, "//input[@name=\"name\"]")

    #email1 xpath
    email1 = (By.XPATH, "//button[contains(text(),'Signup')]/preceding::input[2]")

    # signUp_button xpath
    signUp_button = (By.XPATH, "//button[contains(text(),'Signup')]")

    # title_button xpath
    title_button = (By.XPATH, "//input[@id='id_gender2']")

    # email2 xpath
    email2 = (By.XPATH, "//input[@id='password']")

    # daysDropdown xpath
    daysDropdown = (By.XPATH, "//select[@id='days']")

    monthsDropdown = (By.XPATH, "//select[@id='months']")

    yearsDropdown = (By.XPATH, "//select[@id='years']")

    first_name = (By.XPATH, "//input[@id='first_name']")

    last_name = (By.XPATH, "//input[@id='last_name']")

    company = (By.XPATH, "//input[@id='company']")

    address = (By.XPATH, "//input[@id='address1']")

    countryDropdown = (By.XPATH, "//select[@id='country']")

    state = (By.XPATH, "//input[@id='state']")

    city = (By.XPATH, "//input[@id='city']")

    zipcode = (By.XPATH, "//input[@id='zipcode']")

    mobile_number = (By.XPATH, "//input[@id='mobile_number']")

    create_account = (By.XPATH, "//section[@id='form']/div/div/div/div[1]/form/button")

##################################
    def signUp_login_met(self):
        return self.driver.find_element(*landing_page.signUp_login)

    def new_user_signup_text_met(self):
        return self.driver.find_elements(*landing_page.new_user_signup_text)

    def name_met(self):
        return self.driver.find_element(*landing_page.name)

    def email1_met(self):
        return self.driver.find_element(*landing_page.email1)

    def signUp_button_met(self):
        return self.driver.find_element(*landing_page.signUp_button)

    def title_button_met(self):
        return self.driver.find_element(*landing_page.title_button)

    def email2_met(self):
        return self.driver.find_element(*landing_page.email2)

    def daysDropdown_met(self):
        return self.driver.find_element(*landing_page.daysDropdown)

    def monthsDropdown_met(self):
        return self.driver.find_element(*landing_page.monthsDropdown)

    def yearsDropdown_met(self):
        return self.driver.find_element(*landing_page.yearsDropdown)

    def first_name_met(self):
        return self.driver.find_element(*landing_page.first_name)

    def last_name_met(self):
        return self.driver.find_element(*landing_page.last_name)

    def company_met(self):
        return self.driver.find_element(*landing_page.company)




