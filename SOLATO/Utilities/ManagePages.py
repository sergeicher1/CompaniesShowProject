# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : Managing pages with their Page Objects
# ----------------------------------------------------------------------------------------

from SOLATO.PageObjects.ContactUsPage import ContactUsPage
from SOLATO.PageObjects.FAQPage import FAQPage
from SOLATO.PageObjects.JoinOurTeamPage import JoinOurTeamPage
from SOLATO.PageObjects.MainPage import MainPage
from SOLATO.PageObjects.NutritionalValuesPage import NutritionalValuesPage
from SOLATO.PageObjects.SidebarPage import SidebarPage
from SOLATO.PageObjects.SolatoForBusinessPage import SolatoForBusinessPage
from SOLATO.TestCases import conftest

'''Web Objects'''
mainPage = None
sidebarPage = None
solatoForBusinessPage = None
faqPage = None
nutritionalValuesPage = None
joinOurTeamPage = None
contactUsPage = None


class ManagePages:

    # Initialization of web objects
    @staticmethod
    def InitWebPages():
        globals()["mainPage"] = MainPage(conftest.driver)
        globals()["sidebarPage"] = SidebarPage(conftest.driver)
        globals()["solatoForBusinessPage"] = SolatoForBusinessPage(conftest.driver)
        globals()["faqPage"] = FAQPage(conftest.driver)
        globals()["nutritionalValuesPage"] = NutritionalValuesPage(conftest.driver)
        globals()["joinOurTeamPage"] = JoinOurTeamPage(conftest.driver)
        globals()["contactUsPage"] = ContactUsPage(conftest.driver)
