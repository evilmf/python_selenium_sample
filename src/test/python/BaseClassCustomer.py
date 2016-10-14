import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from phptravels.pages.CustomerLoginPage import CustomerLoginPage
from phptravels.pages.CustomerAccountPage import CustomerAccountPage
import Properties

class BaseClassCustomer(object):
    
    def test_1_customer_login(self):
        self.driver.get(Properties.customerLoginUrl)
        customerLoginPage = CustomerLoginPage(self.driver)
        customerLoginPage.customerLogin(Properties.demoCustomerUser, Properties.demoCustomerPass)
        customerAccountPage = CustomerAccountPage(self.driver)
        self.assertTrue(customerAccountPage.customerThumbnailExists())

    
