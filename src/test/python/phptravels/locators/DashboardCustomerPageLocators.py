from selenium.webdriver.common.by import By


class DashboardCustomerPageLocators(object):
    DASHBOARD_CUSTOMER_ADD_BUTTON = (By.CSS_SELECTOR, 'form.add_button button')
    
    #Create new customer form
    DASHBOARD_CUSTOMER_FNAME_INPUT = (By.CSS_SELECTOR, 'input[name=fname]')
    DASHBOARD_CUSTOMER_LNAME_INPUT = (By.CSS_SELECTOR, 'input[name=lname]')
    DASHBOARD_CUSTOMER_EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name=email]')
    DASHBOARD_CUSTOMER_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name=password]')
    DASHBOARD_CUSTOMER_MOBILE_INPUT = (By.CSS_SELECTOR, 'input[name=mobile]')
    DASHBOARD_CUSTOMER_COUNTRY_SELECT = (By.CSS_SELECTOR, 'select[name=country]')
    DASHBOARD_CUSTOMER_ADDRESS1_INPUT = (By.CSS_SELECTOR, 'input[name=address1]')
    DASHBOARD_CUSTOMER_ADDRESS2_INPUT = (By.CSS_SELECTOR, 'input[name=address2]')
    DASHBOARD_CUSTOMER_STATUS_SELECT = (By.CSS_SELECTOR, 'select[name=status]')
    DASHBOARD_CUSTOMER_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'div.panel-footer button')
    
    CUSTOMERS_ROWS = (By.CSS_SELECTOR, 'tr.xcrud-row')
    