import unittest
from BaseClassAdmin import BaseClassAdmin
import time
from selenium import webdriver

from phptravels.pages.DashboardPage import DashboardPage 
from phptravels.pages.DashboardCustomerPage import DashboardCustomerPage
from time import sleep
import Properties

class NewCustomerAccount(unittest.TestCase, BaseClassAdmin):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(Properties.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def test_3_create_customer(self):
        dashboardPage = DashboardPage(self.driver)
        dashboardPage.clickAccountsButton()
        dashboardPage.clickCustomersButton()        
        
        customerInfo = {'first_name':'firstname', \
                        'last_name':'lastname', \
                        'email':'email%s@emaile.com' % str(int(time.time()))}
        dashboardCustomerPage = DashboardCustomerPage(self.driver)
        dashboardCustomerPage.createCustomerAccount(customerInfo)
        
        #check if the customer account is created successfully
        self.assertTrue(dashboardCustomerPage.hasCustomer(customerInfo))
        
    @classmethod                     
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))