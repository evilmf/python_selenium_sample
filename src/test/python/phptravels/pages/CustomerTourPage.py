from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasePage import BasePage
from ..locators.CustomerTourPageLocators import CustomerTourPageLocators

import time

    
class CustomerTourPage(BasePage):
    
    def selectTour(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CustomerTourPageLocators.TOUR_LINKS)
            )
        
        location = element.location_once_scrolled_into_view
        self.driver.execute_script('window.scrollBy(%s, %s);' % (location['x'], location['y']))
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CustomerTourPageLocators.TOUR_LINKS)
            )
        
        element.click()
        
    def clickBookTourButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CustomerTourPageLocators.BOOK_BUTTON)
            )
        
        location = element.location_once_scrolled_into_view
        self.driver.execute_script('window.scrollBy(%s, %s);' % (location['x'], location['y']))
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CustomerTourPageLocators.BOOK_BUTTON)
            )
        
        element.click()
    
    def clickCompleteBookButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CustomerTourPageLocators.COMPLETE_BOOK_BUTTON)
            )
        
        location = element.location_once_scrolled_into_view
        self.driver.execute_script('window.scrollBy(%s, %s);' % (location['x'], location['y']))
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CustomerTourPageLocators.COMPLETE_BOOK_BUTTON)
            )
        
        element.click()
        
    def bookTour(self):
        self.selectTour()
        self.clickBookTourButton()
        self.clickCompleteBookButton()
