# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : Different Verifications(assertions) for entire Project
# ----------------------------------------------------------------------------------------

import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:

    @staticmethod
    @allure.step("Equality Verification")
    def VerifyEquals(actual, expected):
        assert actual == expected, "Equality Verification FAILED, actual: " + str(
            actual) + " is not Equals to expected: " + str(expected)

    @staticmethod
    @allure.step("Verify if element is displayed on page")
    def VerifyIsDisplayed(elem: WebElement):
        assert elem.is_displayed(), "Verification is FAILED, Element: " + elem.text + " is not displayed!"

    '''Method to append FAILED assertion to list, and check only in the end of test case'''

    @staticmethod
    @allure.step("Soft Assert(Verification) using soft_assert")
    def SmartAssert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    @staticmethod
    @allure.step("Verification of amount of elements in table")
    def VerifyAmountOfElements(elems, expectedSize):
        assert len(elems) == expectedSize, "Number of elements in list: " + str(
            len(elems)) + " doesn't match expected size: " + str(expectedSize)
