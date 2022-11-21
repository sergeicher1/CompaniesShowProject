# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : Page Objects that are located on Main Page
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

'''Elements on page'''

header = (By.XPATH, "//div[@data-testid='richTextElement']")
sidebar = (By.XPATH, "//span[@data-testid='stylablebutton-icon']")


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def GetHeader(self):
        return self.driver.find_element(header[0], header[1])

    def GetSideBar(self):
        return self.driver.find_element(sidebar[0], sidebar[1])
