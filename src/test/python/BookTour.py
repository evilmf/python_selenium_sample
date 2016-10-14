import unittest
from BaseClassCustomer import BaseClassCustomer
import time
from selenium import webdriver

from phptravels.pages.CustomerAccountPage import CustomerAccountPage
from phptravels.pages.CustomerTourPage import CustomerTourPage
from phptravels.pages.InvoicePage import InvoicePage
import Properties

class BookTour(unittest.TestCase, BaseClassCustomer):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(Properties.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def test_2_book_tour(self):
        customerAccountPage = CustomerAccountPage(self.driver)
        customerAccountPage.clickToursButton()
        time.sleep(2)
        
        customerTourPage = CustomerTourPage(self.driver)
        customerTourPage.bookTour()
        
        invoicePage = InvoicePage(self.driver)
        
        #check if tour is booked successfully
        self.assertEquals('Unpaid', invoicePage.unpaidElement())
         
    @classmethod                     
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))