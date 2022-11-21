# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : WEB flows (dirty work) of test cases
# ----------------------------------------------------------------------------------------
from time import sleep

import allure
import pytest

from SOLATO.Extensions.UiActions import UiActions
from SOLATO.Extensions.Verifications import Verifications
from SOLATO.Utilities import ManagePages
from SOLATO.Utilities.CommonOps import Wait, For


# Web Business Flows
class WebFlows:

    @staticmethod
    @allure.step("Verify Main Page Title")
    def VerifyMainPageTitle():
        actual = ManagePages.mainPage.GetHeader().text
        expected = "Where Innovative Technology Redefines The Experience\nOf Ice Cream"
        print(f"Actual: ", actual, " | Expected: ", expected)
        Verifications.VerifyEquals(actual=actual, expected=expected)

    @staticmethod
    @allure.step("Verify presence of sidebar elements")
    def VerifySidebarElements():
        UiActions.Click(ManagePages.mainPage.GetSideBar())
        for el in ManagePages.sidebarPage.GetSideBarLinks():
            print(el.text)
        elems = [
            ManagePages.sidebarPage.GetMachForBusiness(),
            ManagePages.sidebarPage.GetHowDoesItWork(),
            ManagePages.sidebarPage.GetNothingTastesBetter(),
            ManagePages.sidebarPage.GetOurGreenAgenda(),
            ManagePages.sidebarPage.GetFAQ(),
            ManagePages.sidebarPage.GetNutritionValues(),
            ManagePages.sidebarPage.GetJoinOurTeam(),
            ManagePages.sidebarPage.GetContactUs()
        ]
        Verifications.SmartAssert(elems=elems)
        UiActions.Click(ManagePages.sidebarPage.GetCloseBtn())

    @staticmethod
    @allure.step("Verifying working links on sidebar")
    def VerifyWorkingLinks():
        UiActions.Click(ManagePages.mainPage.GetSideBar())
        UiActions.Click(ManagePages.sidebarPage.GetMachForBusiness())
        sleep(1)
        actual = ManagePages.solatoForBusinessPage.GetHeader().text
        expected = "Solato for businesses"
        Verifications.VerifyEquals(actual=actual, expected=expected)
        UiActions.Click(ManagePages.mainPage.GetSideBar())
        UiActions.Click(ManagePages.sidebarPage.GetFAQ())
        sleep(1)
        actual = ManagePages.solatoForBusinessPage.GetHeader().text
        expected = "Frequently Asked Questions"
        Verifications.VerifyEquals(actual=actual, expected=expected)
        UiActions.Click(ManagePages.mainPage.GetSideBar())
        UiActions.Click(ManagePages.sidebarPage.GetNutritionValues())
        sleep(1)
        actual = ManagePages.solatoForBusinessPage.GetHeader().text
        expected = "Nutritional Values"
        Verifications.VerifyEquals(actual=actual, expected=expected)
        UiActions.Click(ManagePages.mainPage.GetSideBar())
        UiActions.Click(ManagePages.sidebarPage.GetJoinOurTeam())
        sleep(1)
        actual = ManagePages.solatoForBusinessPage.GetHeader().text
        expected = "Join Our Team"
        Verifications.VerifyEquals(actual=actual, expected=expected)
        UiActions.Click(ManagePages.mainPage.GetSideBar())
        UiActions.Click(ManagePages.sidebarPage.GetContactUs())
        sleep(1)
        actual = ManagePages.solatoForBusinessPage.GetHeader().text
        expected = "Contact Us"
        Verifications.VerifyEquals(actual=actual, expected=expected)
