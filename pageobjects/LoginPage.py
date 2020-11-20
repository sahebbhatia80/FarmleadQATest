#This Class acts as a Repository for Login Page where we list out all the Web Elements and the actions that can be performed for the same
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login():
    username_textbox_xpath = "//*[@id='ui']/div/div[1]/form/div/div[3]/div[1]/div/div[1]/fieldset/div/input"
    password_textbox_xpath  = "//*[@id='ui']/div/div[1]/form/div/div[3]/div[2]/div/div[1]/fieldset/div/input"
    submit_button_xpath     = "//input[@type='submit']"
    wrong_emailvalidationMsg_xpath = "//div[@class='Input_caption__3AYcS']"
    create_account_xpath = "//span[text()='Create an Account']"
    header_create_account_xpath = "//div[@class='Onboard_title__12piM']"
    forget_password_xpath = "//div[text()='Forgot your password?']"
    header_pwd_forget_xpath = "//div[@class='RecovPasswdForm_title__7ZdwX']"

# This defines the Constructor of the class
    def __init__(self, driver):
        self.driver = driver

# Action to click on Create Account Link
    def click_createaccount(self):
        self.driver.find_element_by_xpath(self.create_account_xpath).click()

# Action to click on Forget Password Link
    def click_forgetpassword(self):
        self.driver.find_element_by_xpath(self.forget_password_xpath).click()

# Action to enter username
    def enter_username(self, name):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(name)

    # Action to enter Password
    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    # Action to click on Submit button
    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()

    #Action to get the text for validation message
    def get_validationerror(self, wrong_emailvalidationMsg_xpath):
        error = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(wrong_emailvalidationMsg_xpath))
        return error.text

#Action to get the text for Create Account Header
    def get_createaccountheader(self, header_create_account_xpath):
        error = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(header_create_account_xpath))
        return error.text

#Action to get the text for Forget Password Header
    def get_pwdforgetheader(self, header_pwd_forget_xpath):
        error = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(header_pwd_forget_xpath))
        return error.text