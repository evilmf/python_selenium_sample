import unittest
from BaseClassAdmin import BaseClassAdmin
import time
from selenium import webdriver

from phptravels.pages.DashboardPage import DashboardPage 
from phptravels.pages.DashboardTourPage import DashboardTourPage
from time import sleep
import Properties

class NewTour(unittest.TestCase, BaseClassAdmin):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(Properties.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def test_3_create_tour(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.clickToursButton()
        dashboard_page.clickAddToursButton()        
        
        tourname = 'Test Tour ' + str(int(time.time()))
        tourPage = DashboardTourPage(self.driver)
        tourPage.createNewTour(tourname)
        
        #check if tour is created successfully
        self.assertTrue(tourPage.tourExists(tourname))
                
    @classmethod                     
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))