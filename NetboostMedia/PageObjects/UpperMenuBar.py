# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : Page Objects that are located on Upper Navigation Bar
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

'''Elements on page'''
upperMenuList = (By.XPATH, "//div[@id='menu']/ul/li")
transparentLogo = (By.XPATH, "//span[@id='transparent_logo']")
home = (By.XPATH, "//li[@id='menu-item-23849']")
aboutUs = (By.XPATH, "//li[@id='menu-item-23854']")
ourTeam = (By.XPATH, "//li[@id='menu-item-23848']")
joinUs = (By.XPATH, "//li[@id='menu-item-23892']")
contactUs = (By.XPATH, "//li[@id='menu-item-24023']")
facebook = (By.CSS_SELECTOR, "[id='menu-item-24260']")
linkedin = (By.CSS_SELECTOR, "[id='menu-item-24261']")


class UpperMenuBar:

    def __init__(self, driver):
        self.driver = driver

    def GetUpperMenuListElements(self):
        return self.driver.find_elements(upperMenuList[0], upperMenuList[1])

    def GetTransparentLogo(self):
        return self.driver.find_element(transparentLogo[0], transparentLogo[1])

    def GetHome(self):
        return self.driver.find_element(home[0], home[1])

    def GetAboutUs(self):
        return self.driver.find_element(aboutUs[0], aboutUs[1])

    def GetOurTeam(self):
        return self.driver.find_element(ourTeam[0], ourTeam[1])

    def GetJoinUs(self):
        return self.driver.find_element(joinUs[0], joinUs[1])

    def GetContactUs(self):
        return self.driver.find_element(contactUs[0], contactUs[1])

    def GetFacebook(self):
        return self.driver.find_element(facebook[0], facebook[1])

    def GetLinkedin(self):
        return self.driver.find_element(linkedin[0], linkedin[1])
