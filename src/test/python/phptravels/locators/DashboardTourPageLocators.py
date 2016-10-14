from selenium.webdriver.common.by import By


class DashboardTourPageLocators(object):
    #Tour form
    TOUR_NAME_INPUT = (By.CSS_SELECTOR, 'input[name=tourname]')
    TOUR_MAX_ADULT_INPUT = (By.CSS_SELECTOR, 'input[name=maxadult]')
    TOUR_ADULT_PRICE_INPUT = (By.CSS_SELECTOR, 'input[name=adultprice]')
    TOUR_STAR_SELECT = (By.CSS_SELECTOR, 'select[name=tourstars]')
    TOUR_DAY_INPUT = (By.CSS_SELECTOR, 'input[name=tourdays]')
    TOUR_NIGHT_INPUT = (By.CSS_SELECTOR, 'input[name=tournights]')
    TOUR_TYPE_SELECT = (By.CSS_SELECTOR, 'select[name=tourtype]')
    TOUR_LOCATION_SELECT = (By.CSS_SELECTOR, 'select.chosen-select.select2-offscreen')
    TOUR_ADD_BUTTON = (By.CSS_SELECTOR, 'button#add')
    
    TOUR_ROW = (By.CSS_SELECTOR, 'tr.xcrud-row')