# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : Page Objects that are located on Contact Us Page
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

'''Elements on page'''
header = (By.XPATH, "//h2/span")
inputName = (By.XPATH, "//input[@name='your-name']")
inputEmail = (By.XPATH, "//input[@name='your-email']")
inputSubject = (By.XPATH, "//input[@name='your-subject']")
inputMessage = (By.XPATH, "//textarea[@name='your-message']")
hitItBtn = (By.XPATH, "//input[@type='submit']")
errorMessage = (By.XPATH, "//div[@class='wpcf7-response-output']")


class ContactUsPage:

    def __init__(self, driver):
        self.driver = driver

    def GetHeader(self):
        return self.driver.find_element(header[0], header[1])

    def GetInputName(self):
        return self.driver.find_element(inputName[0], inputName[1])

    def GetInputEmail(self):
        return self.driver.find_element(inputEmail[0], inputEmail[1])

    def GetInputSubject(self):
        return self.driver.find_element(inputSubject[0], inputSubject[1])

    def GetInputMessage(self):
        return self.driver.find_element(inputMessage[0], inputMessage[1])

    def GetHitBtn(self):
        return self.driver.find_element(hitItBtn[0], hitItBtn[1])

    def GetErrorMessage(self):
        return self.driver.find_element(errorMessage[0], errorMessage[1])
