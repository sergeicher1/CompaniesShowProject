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

from NetboostMedia.Extensions.UiActions import UiActions
from NetboostMedia.Extensions.Verifications import Verifications
from NetboostMedia.Utilities import ManagePages


# Web Business Flows
class WebFlows:

    @staticmethod
    @allure.step("Accept cookies")
    def AcceptCookies():
        UiActions.Click(ManagePages.mainPage.GetAcceptCookies())

    @staticmethod
    @allure.step("Verify elements on upper menu navigation bar")
    def VerifyElementsUpperNavBar():
        for el in ManagePages.upperMenuBar.GetUpperMenuListElements():
            print(el.text)
        elems = [
            ManagePages.upperMenuBar.GetHome(),
            ManagePages.upperMenuBar.GetAboutUs(),
            ManagePages.upperMenuBar.GetOurTeam(),
            ManagePages.upperMenuBar.GetJoinUs(),
            ManagePages.upperMenuBar.GetContactUs(),
            ManagePages.upperMenuBar.GetFacebook(),
            ManagePages.upperMenuBar.GetLinkedin()
        ]
        Verifications.SmartAssert(elems=elems)

    @staticmethod
    @allure.step("Verify Links in Upper Menu Nav Bar")
    def VerifyWorkingLinksUpperNavBar():
        UiActions.Click(ManagePages.upperMenuBar.GetHome())
        actual = ManagePages.mainPage.GetHeader().text
        expected = "Playing since 2006"
        print(f"Actual: ", actual, " | Expected: ", expected)
        Verifications.VerifyEquals(actual=actual, expected=expected)
        UiActions.Click(ManagePages.upperMenuBar.GetAboutUs())
        actual = ManagePages.aboutUsPage.GetHeader().text
        expected = "About Us"
        print(f"Actual: ", actual, " | Expected: ", expected)
        Verifications.VerifyEquals(actual=actual, expected=expected)
        UiActions.Click(ManagePages.upperMenuBar.GetOurTeam())
        actual = ManagePages.ourTeamPage.GetHeader().text
        expected = "Netboost owes it all to a magical group of talents"
        print(f"Actual: ", actual, " | Expected: ", expected)
        Verifications.VerifyEquals(actual=actual, expected=expected)
        UiActions.Click(ManagePages.upperMenuBar.GetJoinUs())
        actual = ManagePages.joinUsPage.GetHeader().text
        expected = "If you’re looking for a positive, challenging and playful work place, you’ve found it!"
        print(f"Actual: ", actual, " | Expected: ", expected)
        Verifications.VerifyEquals(actual=actual, expected=expected)
        UiActions.Click(ManagePages.upperMenuBar.GetContactUs())
        actual = ManagePages.contactUsPage.GetHeader().text
        expected = "We can’t wait to hear from you"
        print(f"Actual: ", actual, " | Expected: ", expected)
        Verifications.VerifyEquals(actual=actual, expected=expected)

    @staticmethod
    @allure.step("Fill the contact form and verify it was sent")
    def FillAndVerifyContactUsForm():
        WebFlows.AcceptCookies()
        UiActions.Click(ManagePages.upperMenuBar.GetContactUs())
        UiActions.UpdateText(ManagePages.contactUsPage.GetInputName(), "Sergei Chernyahovsky")
        UiActions.UpdateText(ManagePages.contactUsPage.GetInputEmail(), "sergeicher87@gmail.com")
        UiActions.UpdateText(ManagePages.contactUsPage.GetInputSubject(), "Found BUG")
        UiActions.UpdateText(ManagePages.contactUsPage.GetInputMessage(), "While browsing site, found BUG")
        UiActions.Click(ManagePages.contactUsPage.GetHitBtn())
        sleep(3)  # if displayed, so the feature doesn't work!
        Verifications.VerifyIsDisplayed(ManagePages.contactUsPage.GetErrorMessage())
        pytest.fail("The test failed because there is an error message and the form doesn't send message")
