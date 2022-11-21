# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : User Interface Actions for Web, In future other platforms can Inherit from it
# ----------------------------------------------------------------------------------------

import allure
from selenium.webdriver.remote.webelement import WebElement

from SOLATO.TestCases.conftest import action


class UiActions:

    @staticmethod
    @allure.step("Click On Element")
    def Click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step("Clear field")
    def Clear(elem: WebElement):
        elem.clear()

    @staticmethod
    @allure.step("Updating text")
    def UpdateText(elem: WebElement, value: str):
        elem.send_keys(value)

    @staticmethod
    @allure.step("Mouse hover")
    def MouseHover(elem1: WebElement, elem2: WebElement):
        action.move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step("Mouse Right Click")
    def MouseRightClick(elem: WebElement):
        action.context_click(elem).perform()

    @staticmethod
    @allure.step("Drag And Drop")
    def DragAndDrop(elem1: WebElement, elem2: WebElement):
        action.drag_and_drop(elem1, elem2).perform()
