from BasePage import BasePage
from selenium.webdriver.support.ui import Select
from ..elements.BasePageInputElement import BasePageInputElement
from ..locators.DashboardCustomerPageLocators import DashboardCustomerPageLocators

class FnameInputElement(BasePageInputElement):
    locator = DashboardCustomerPageLocators.DASHBOARD_CUSTOMER_FNAME_INPUT
     
class LnameInputElement(BasePageInputElement):
    locator = DashboardCustomerPageLocators.DASHBOARD_CUSTOMER_LNAME_INPUT
    
class EmailInputElement(BasePageInputElement):
    locator = DashboardCustomerPageLocators.DASHBOARD_CUSTOMER_EMAIL_INPUT
    
class PasswordInputElement(BasePageInputElement):
    locator = DashboardCustomerPageLocators.DASHBOARD_CUSTOMER_PASSWORD_INPUT

class DashboardCustomerPage(BasePage):
    
    fnameInputElement = FnameInputElement()
    lnameInputElement = LnameInputElement()
    emailInputElement = EmailInputElement()
    passwordInputElement = PasswordInputElement()
    
    def clickCustomerAddButton(self):
        self.driver.find_element(*DashboardCustomerPageLocators.DASHBOARD_CUSTOMER_ADD_BUTTON).click()
        
    def enterCustomerFname(self, fname):
        self.fnameInputElement = fname
    
    def enterCustomerLname(self, lname):
        self.lnameInputElement = lname
        
    def enterCustomerEmail(self, email):
        self.emailInputElement= email
        
    def enterCustomerPassword(self, password):
        self.passwordInputElement = password
        
    def selectCustomerCountry(self, country):
        element = self.driver.find_element(*DashboardCustomerPageLocators.DASHBOARD_CUSTOMER_COUNTRY_SELECT)
        Select(element).select_by_value(country)
        
    def clickCustomerSubmitButton(self):
        self.driver.find_element(*DashboardCustomerPageLocators.DASHBOARD_CUSTOMER_SUBMIT_BUTTON).click()
        
    def hasCustomer(self, customer):
        rows = self.driver.find_elements(*DashboardCustomerPageLocators.CUSTOMERS_ROWS)
        for r in rows:
            tds = r.find_elements_by_tag_name('td')
            if tds[2].text == customer['first_name'] \
                and tds[3].text == customer['last_name'] \
                and tds[4].text == customer['email']:
                return True
        
        return False
    
    def createCustomerAccount(self, customerInfo):
        self.clickCustomerAddButton()
        self.enterCustomerFname(customerInfo['first_name'])
        self.enterCustomerLname(customerInfo['last_name'])
        self.enterCustomerEmail(customerInfo['email'])
        self.enterCustomerPassword('password')
        self.selectCustomerCountry('US')
        
        self.clickCustomerSubmitButton()
            
           
    
    
    