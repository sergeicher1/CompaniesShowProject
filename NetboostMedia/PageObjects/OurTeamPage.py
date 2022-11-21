# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : Page Objects that are located on Our Team Page
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

'''Elements on page'''
header = (By.XPATH, "//h2/span")


class OurTeamPage:

    def __init__(self, driver):
        self.driver = driver

    def GetHeader(self):
        return self.driver.find_element(header[0], header[1])
