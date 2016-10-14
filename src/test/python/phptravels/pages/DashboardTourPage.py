from BasePage import BasePage
from selenium.webdriver.support.ui import Select
from ..elements.BasePageInputElement import BasePageInputElement
from ..locators.DashboardTourPageLocators import DashboardTourPageLocators

class TourNameInputElement(BasePageInputElement):
    locator = DashboardTourPageLocators.TOUR_NAME_INPUT

class MaxAdultInputElement(BasePageInputElement):
    locator = DashboardTourPageLocators.TOUR_MAX_ADULT_INPUT

class AdultPriceInputElement(BasePageInputElement):
    locator = DashboardTourPageLocators.TOUR_ADULT_PRICE_INPUT
    
class DayInputElement(BasePageInputElement):
    locator = DashboardTourPageLocators.TOUR_DAY_INPUT

class NightInputElement(BasePageInputElement):
    locator = DashboardTourPageLocators.TOUR_NIGHT_INPUT

class DashboardTourPage(BasePage):
    
    tourNameInputElement = TourNameInputElement()
    maxAdultInputElement = MaxAdultInputElement()
    adultPriceInputElement = AdultPriceInputElement()
    dayInputElement = DayInputElement()
    nightInputElement = NightInputElement()
    
    def enterTourName(self, tourName):
        self.tourNameInputElement = tourName
        
    def enterMaxAdult(self, maxAdult):
        self.maxAdultInputElement = maxAdult
        
    def enterAdultPrice(self, adultPrice):
        self.adultPriceInputElement = adultPrice
    
    def selectStar(self, star):
        element = self.driver.find_element(*DashboardTourPageLocators.TOUR_STAR_SELECT)
        Select(element).select_by_value(star)
        
    def enterDay(self, day):
        self.dayInputElement = day
        
    def enterNight(self, night):
        self.nightInputElement = night
        
    def selectType(self, type):
        element = self.driver.find_element(*DashboardTourPageLocators.TOUR_TYPE_SELECT)
        Select(element).select_by_value(type)      
        
    def selectLocation1(self, location):
        element = self.driver.find_elements(*DashboardTourPageLocators.TOUR_LOCATION_SELECT)
        Select(element[1]).select_by_value(location)  
    
    def clickAddTourButton(self):
        self.driver.find_element(*DashboardTourPageLocators.TOUR_ADD_BUTTON).click()
        
    def createNewTour(self, tourname):
        self.enterTourName(tourname)
        self.enterMaxAdult(100)
        self.enterAdultPrice(100)
        self.selectStar('5')
        self.enterDay('5')
        self.enterNight('5')
        self.selectType('187')
        self.selectLocation1('32')
        
        self.clickAddTourButton()
        
    def tourExists(self, tourname):
        rows = self.driver.find_elements(*DashboardTourPageLocators.TOUR_ROW)
        for r in rows:
            tds = r.find_elements_by_tag_name('td')
            if tds[4].text == tourname:
                return True
        
        return False
        
     
    
    
    