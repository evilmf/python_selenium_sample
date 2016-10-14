from BasePage import BasePage
from ..locators.DashboardPageLocators import DashboardPageLocators

    
class DashboardPage(BasePage):
    
    def dashboardHomeButtonText(self):
        return self.driver.find_element(*DashboardPageLocators.DASHBOARD_HOME_BUTTON).text
    
    def clickAccountsButton(self):
        self.driver.find_element(*DashboardPageLocators.ACCOUNTS_BUTTON).click()
        
    def clickCustomersButton(self):
        self.driver.find_element(*DashboardPageLocators.CUSTOMERS_BUTTON).click()
        
    def clickToursButton(self):
        self.driver.find_element(*DashboardPageLocators.TOURS_BUTTON).click()
        
    def clickAddToursButton(self):
        self.driver.find_element(*DashboardPageLocators.ADD_TOURS_BUTTON).click()