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

from SOLATO.Workflows.Webflows import *


@pytest.mark.usefixtures("InitWebDriver")
class Test_Web:

    @allure.title("Test Case 01: Verify Main page title")
    @allure.description("This test verifies title in main page")
    def test_TC01VerifyMainPageTitle(self):
        WebFlows.VerifyMainPageTitle()

    @allure.title("Test Case 02: Verify Sidebar Elements")
    @allure.description("This test verifies presence of sidebar elements")
    def test_TC02VerifySidebarElements(self):
        WebFlows.VerifySidebarElements()

    @allure.title("Test Case 03: Verify working links on sidebar")
    @allure.description("This test verifies working links on sidebar")
    def test_TC03VerifyWorkingLinks(self):
        WebFlows.VerifyWorkingLinks()
