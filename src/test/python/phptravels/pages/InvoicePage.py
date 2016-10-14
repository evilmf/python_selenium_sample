from BasePage import BasePage
from ..locators.InvoicePageLocators import InvoicePageLocators

    
class InvoicePage(BasePage):
    
    def unpaidElement(self):
        return self.driver.find_element(*InvoicePageLocators.UNPAID_ELEMENT).text
    