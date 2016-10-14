from BasePage import BasePage
from ..locators.CustomerAccountPageLocators import CustomerAccountPageLocators

    
class CustomerAccountPage(BasePage):
    
    def customerThumbnailExists(self):
        element = self.driver.find_element(*CustomerAccountPageLocators.USER_THUMBNAIL)
        isDisplay = element.is_displayed()
        return isDisplay
    
    def clickToursButton(self):
        self.driver.find_element(*CustomerAccountPageLocators.TOURS_BUTTON).click()
