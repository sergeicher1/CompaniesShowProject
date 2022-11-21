# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : Managing pages with their Page Objects
# ----------------------------------------------------------------------------------------
from NetboostMedia.PageObjects.AboutUsPage import AboutUsPage
from NetboostMedia.PageObjects.ContactUsPage import ContactUsPage
from NetboostMedia.PageObjects.JoinUsPage import JoinUsPage
from NetboostMedia.PageObjects.OurTeamPage import OurTeamPage
from NetboostMedia.PageObjects.PpcManagerPage import PpcManagerPage
from NetboostMedia.PageObjects.UpperMenuBar import UpperMenuBar
from NetboostMedia.PageObjects.MainPage import MainPage
from NetboostMedia.TestCases import conftest

'''Web Objects'''
upperMenuBar = None
mainPage = None
aboutUsPage = None
ourTeamPage = None
joinUsPage = None
contactUsPage = None
ppcManagerPage = None


class ManagePages:

    # Initialization of web objects
    @staticmethod
    def InitWebPages():
        globals()["upperMenuBar"] = UpperMenuBar(conftest.driver)
        globals()["mainPage"] = MainPage(conftest.driver)
        globals()["aboutUsPage"] = AboutUsPage(conftest.driver)
        globals()["ourTeamPage"] = OurTeamPage(conftest.driver)
        globals()["joinUsPage"] = JoinUsPage(conftest.driver)
        globals()["contactUsPage"] = ContactUsPage(conftest.driver)
        globals()["ppcManagerPage"] = PpcManagerPage(conftest.driver)
