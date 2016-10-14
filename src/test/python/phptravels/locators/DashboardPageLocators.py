from selenium.webdriver.common.by import By


class DashboardPageLocators(object):
    DASHBOARD_HOME_BUTTON = (By.CSS_SELECTOR, 'div.navbar-header span')
    
    ACCOUNTS_BUTTON = (By.CSS_SELECTOR, '#social-sidebar-menu > li:nth-child(4) > a')
    CUSTOMERS_BUTTON = (By.CSS_SELECTOR , '#Accounts > li:nth-child(3) > a')
    
    TOURS_BUTTON = (By.CSS_SELECTOR, '#social-sidebar-menu > li:nth-child(6) > a')
    ADD_TOURS_BUTTON = (By.CSS_SELECTOR , '#Tours > li:nth-child(2) > a')