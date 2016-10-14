from BasePage import BasePage
from ..elements.BasePageInputElement import BasePageInputElement
from ..locators.CustomerLoginPageLocators import CustomerLoginPageLocators
import time

class UsernameInputElement(BasePageInputElement):
    locator = CustomerLoginPageLocators.USERNAME_INPUT
     
class PasswordInputElement(BasePageInputElement):
    locator = CustomerLoginPageLocators.PASSWORD_INPUT
    
class CustomerLoginPage(BasePage):
    
    usernameInputElement = UsernameInputElement()
    passwordInputElement = PasswordInputElement()
    
    def enterUserName(self, username):
        self.usernameInputElement = username
    
    def enterPassword(self, password):
        self.passwordInputElement = password
    
    def clickLoginButton(self):
        element = self.driver.find_element(*CustomerLoginPageLocators.LOGIN_BUTTON)
        element.click()
        
    def customerLogin(self, username, password):
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLoginButton()
        