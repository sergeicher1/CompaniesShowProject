# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : Test Cases clean -> Using other scripts as helpers
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# to execute first of all MAKE SURE all imports are from appropriate projects
# change URL and SCREEN-PATH  in data.xml
# change GetData in CommonOps
# in test cases pytest -s -v --alluredir ./../allure-results
# in main project  allure serve allure-results

from NetboostMedia.Workflows.Webflows import *


@pytest.mark.usefixtures("InitWebDriver")
class Test_Web:

    @allure.title("Test Case 01: Verify items Upper Menu Nav Bar")
    @allure.description("This test verifies presence of elements on Upper Menu Navigation Bar")
    def test_TC01VerifyUpperMenuBarElements(self):
        WebFlows.VerifyElementsUpperNavBar()

    @allure.title("Test Case 02: Verify working links on upper menu nav bar")
    @allure.description("This test verifies working links on upper menu bar")
    def test_TC02VerifyLinksUpperMenuBar(self):
        WebFlows.VerifyWorkingLinksUpperNavBar()

    @allure.title("Test Case 03: Verify contact form")
    @allure.description("This test verifies Contact us form is working properly and sends the message")
    def test_TC03FillAndVerifyContactForm(self):
        WebFlows.FillAndVerifyContactUsForm()

