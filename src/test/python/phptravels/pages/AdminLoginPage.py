from BasePage import BasePage
from ..elements.BasePageInputElement import BasePageInputElement
from ..locators.AdminLoginPageLocators import AdminLoginPageLocators

class UsernameInputElement(BasePageInputElement):
    locator = AdminLoginPageLocators.USERNAME_INPUT
     
class PasswordInputElement(BasePageInputElement):
    locator = AdminLoginPageLocators.PASSWORD_INPUT
    
class AdminLoginPage(BasePage):
    
    usernameInputElement = UsernameInputElement()
    passwordInputElement = PasswordInputElement()
    
    def enterUserName(self, username):
        self.usernameInputElement = username
    
    def enterPassword(self, password):
        self.passwordInputElement = password
    
    def clickLoginButton(self):
        element = self.driver.find_element(*AdminLoginPageLocators.LOGIN_BUTTON)
        element.click()
        
    def adminLogin(self, username, password):
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLoginButton()
        