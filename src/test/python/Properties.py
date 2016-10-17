import os
import sys

drivers = {'chrome_mac64':'chromedriver_mac64', 'chrome_win32':'chromedriver_win32.exe'}

driver = '../resources/webdrivers/' + (drivers[os.environ['WEBDRIVER']] if os.environ.has_key('WEBDRIVER') else drivers['chrome_win32'])

adminLoginUrl = 'http://phptravels.net/admin'
customerLoginUrl = 'http://phptravels.net/login'
 
demoAdminUser = 'admin@phptravels.com'
demoAdminPass = 'demoadmin'
 
demoCustomerUser = 'user@phptravels.com'
demoCustomerPass = 'demouser'
