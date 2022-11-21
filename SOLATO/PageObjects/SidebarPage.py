# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : Page Objects that are located on Sidebar Page
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

'''Elements on page'''

sidebarLinks = (By.XPATH, "//nav[@id='comp-kxggg55a']/ul/li")
closeBtn = (By.XPATH, "//div[@data-testid='popupCloseIconButtonRoot']")
machForBusiness = (By.XPATH, "//a[@data-testid='linkElement-0']")
howDoesItWork = (By.XPATH, "//a[@data-testid='linkElement-1']")
nothingTastesBetter = (By.XPATH, "//a[@data-testid='linkElement-2']")
ourGreenAgenda = (By.XPATH, "//a[@data-testid='linkElement-3']")
FAQ = (By.XPATH, "//a[@data-testid='linkElement-4']")
nutritionalValues = (By.XPATH, "//a[@data-testid='linkElement-5']")
joinOurTeam = (By.XPATH, "//a[@data-testid='linkElement-6']")
contactUs = (By.XPATH, "//a[@data-testid='linkElement-7']")


class SidebarPage:

    def __init__(self, driver):
        self.driver = driver

    def GetSideBarLinks(self):
        return self.driver.find_elements(sidebarLinks[0], sidebarLinks[1])

    def GetCloseBtn(self):
        return self.driver.find_element(closeBtn[0], closeBtn[1])

    def GetMachForBusiness(self):
        return self.driver.find_element(machForBusiness[0], machForBusiness[1])

    def GetHowDoesItWork(self):
        return self.driver.find_element(howDoesItWork[0], howDoesItWork[1])

    def GetNothingTastesBetter(self):
        return self.driver.find_element(nothingTastesBetter[0], nothingTastesBetter[1])

    def GetOurGreenAgenda(self):
        return self.driver.find_element(ourGreenAgenda[0], ourGreenAgenda[1])

    def GetFAQ(self):
        return self.driver.find_element(FAQ[0], FAQ[1])

    def GetNutritionValues(self):
        return self.driver.find_element(nutritionalValues[0], nutritionalValues[1])

    def GetJoinOurTeam(self):
        return self.driver.find_element(joinOurTeam[0], joinOurTeam[1])

    def GetContactUs(self):
        return self.driver.find_element(contactUs[0], contactUs[1])
