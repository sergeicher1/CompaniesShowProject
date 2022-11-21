# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : This is a configuration file for the entire Project
# ----------------------------------------------------------------------------------------
from datetime import datetime
from time import sleep
import allure
import pytest
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium import webdriver

from SOLATO.Utilities.CommonOps import GetData
from SOLATO.Utilities.EventListener import EventListener
from SOLATO.Utilities.ManagePages import ManagePages
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

'''Objects Initialization'''
driver = None
action = None

'''WebDriver Initialization'''


@pytest.fixture(scope="class")
def InitWebDriver(request):
    edriver = GetWebDriver()
    globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()["driver"]
    driver.maximize_window()
    driver.implicitly_wait(int(GetData("WaitTime")))
    driver.get(GetData("URL"))
    request.cls.driver = driver
    globals()["action"] = ActionChains(driver)
    ManagePages.InitWebPages()

    yield
    sleep(2)
    globals()["driver"].quit()


# Checks which browser is requested for execution
def GetWebDriver():
    browser = GetData("Browser")
    if browser.lower() == "chrome":
        driver = GetChrome()
    elif browser.lower() == "firefox":
        driver = GetFirefox()
    elif browser.lower() == "edge":
        driver = GetEdge()
    else:
        driver = None
        raise Exception("Wrong Input for browser, check configuration in data.xml file!")
    return driver


'''Initialize specific WebDriver'''


def GetChrome():
    chromeDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return chromeDriver


def GetFirefox():
    ffDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    return ffDriver


def GetEdge():
    edgeDriver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    return edgeDriver


########################################################################################################

'''Catch Exceptions Errors and Screenshots'''


# This is exception for API test
# If it is None -> Screenshot will not be captured, because no browser is opened!
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()["driver"] is not None:
            image = GetData("ScreenshotPath") + "screen_" + str(datetime.now()).replace(":", "-") + ".png"
            globals()["driver"].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

########################################################################################################
