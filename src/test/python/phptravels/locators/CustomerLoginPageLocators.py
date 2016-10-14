from selenium.webdriver.common.by import By


class CustomerLoginPageLocators(object):
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.loginbtn')
    USERNAME_INPUT = (By.CSS_SELECTOR, 'input[name=username][type=email]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name=password][type=password]')
