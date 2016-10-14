from selenium.webdriver.common.by import By


class InvoicePageLocators(object):
    UNPAID_ELEMENT = (By.CSS_SELECTOR, '#top > div.modal-dialog.modal-lg > div > div:nth-child(1) > div > center > b')
    