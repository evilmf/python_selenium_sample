from selenium.webdriver.common.by import By


class CustomerAccountPageLocators(object):
    USER_THUMBNAIL = (By.CSS_SELECTOR, 'div.row img.go-right')
    TOURS_BUTTON = (By.CSS_SELECTOR, '#top > div.navbar.navbar-static-top.navbar-default > div > div > div.navbar-collapse.collapse > ul > li:nth-child(3) > a')
