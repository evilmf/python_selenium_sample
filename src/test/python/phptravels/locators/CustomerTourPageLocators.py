from selenium.webdriver.common.by import By


class CustomerTourPageLocators(object):
    TOUR_LINKS = (By.CSS_SELECTOR, 'div.itemlabel3 h4.RTL>a')
    BOOK_BUTTON = (By.CSS_SELECTOR, 'button.btn-action.btn-lg')
    COMPLETE_BOOK_BUTTON = (By.CSS_SELECTOR, 'button.completebook')
