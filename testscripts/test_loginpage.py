import pytest
from selenium import webdriver
import selenium
from testscripts.configuration import setup
from pageobjects.LoginPage import Login
from selenium.webdriver.common.action_chains import ActionChains
from utilities.readProperties import ReadConfig

class Test_Valid_Login:
    baseURL = ReadConfig.getApplicationURL() # Used config.ini and ReadProperties file so that it can read and take the common data from those files without hardcoding it.
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

#this method validates the title of the application
    def test_title(self,setup):
        self.driver = setup                         #Made use of python fixture to prevent writing Reusable steps again and again
        self.driver.get(self.baseURL)               #lOGGING Into THE APPLICATION BASED ON THE url
        self.driver.title                           #Getting the title from the PAGE
        #Assertion to validate if logged in into the correct URL
        if self.driver.title == "Combyne":
            assert True
        else:
            assert False

# this explains the UnSuccessfull login to the application with validation message
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()              #Maximizing the Browser Window
        self.lp=Login(self.driver)                 #Creating an object of Login class
        self.lp.driver.implicitly_wait(10)         #Giving a wait time for the application to load
        self.lp.enter_username(self.username)      #Entering username which is a Invalid username
        self.lp.enter_password(self.password)      #Entering password which is a Invalid password
        self.lp.click_submit()                     #Clicking on the Next button
        self.lp.driver.implicitly_wait(10)
        message = self.lp.get_validationerror()    #Getting the Validation Error mesage
        assert message == "Whoops! That email is not associated with an account."  #Asserting the validation error
        self.driver.quit()                         #Close the browser

# this explains the UnSuccessfull login to the application when we click next button without email and password
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()              #Maximizing the Browser Window
        self.lp=Login(self.driver)                 #Creating an object of Login class
        self.lp.driver.implicitly_wait(10)         #Giving a wait time for the application to load
        self.lp.click_submit()                     #Clicking on the Next button
        self.lp.driver.implicitly_wait(10)
        message = self.lp.get_validationerror()    #Getting the Validation Error mesage
        assert message == "Either a phone number or email is required."  #Asserting the validation error
        self.driver.quit()

# this explains the Successfull Click to Create an Account Link and validate the header text;

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()              #Maximizing the Browser Window
        self.lp=Login(self.driver)                 #Creating an object of Login class
        self.lp.driver.implicitly_wait(5)         #Giving a wait time for the application to load
        self.lp.click_createaccount()             #clicking create account link
        message = self.lp.get_createaccountheader()  # Getting the Header text for Create an Account
        assert message == "Let's Get Started!"       # Asserting the validation error
        self.driver.quit()                         #Close the browser

# this explains the Successfull Click to Forget your password Link and validating its header text.

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()  # Maximizing the Browser Window
        self.lp = Login(self.driver)  # Creating an object of Login class
        self.lp.driver.implicitly_wait(5)  # Giving a wait time for the application to load
        self.lp.click_forgetpassword()  # clicking forget password link
        message = self.lp.get_pwdforgetheader()  # Getting the Header text for forget password
        assert message == "Trouble Logging in?"  # Asserting the validation error
        self.driver.quit()  # Close the browser