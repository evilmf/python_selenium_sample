import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from phptravels.pages.AdminLoginPage import AdminLoginPage
from phptravels.pages.DashboardPage import DashboardPage
import Properties

class BaseClassAdmin(object):
    
    def test_1_placeholder(self):
        self.assertTrue(1 == 1)
    
    def test_2_admin_login(self):
        self.driver.get(Properties.adminLoginUrl)
        adminLoginPage = AdminLoginPage(self.driver)
        adminLoginPage.adminLogin(Properties.demoAdminUser, Properties.demoAdminPass)
        
        dashboardPage = DashboardPage(self.driver)
        self.assertEqual('Dashboard', dashboardPage.dashboardHomeButtonText())

if __name__ == "__main__":
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    
