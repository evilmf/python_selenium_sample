from selenium.webdriver.common.by import By


class AdminLoginPageLocators(object):
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.btn-lg')
    USERNAME_INPUT = (By.CSS_SELECTOR, 'input[name=email][type=text]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name=password][type=password]')