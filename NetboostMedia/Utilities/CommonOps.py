# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Language    : Python
# Version     : 3.11
# WebDriver   : Selenium
# Version     : 4.6.0 for driver initialization to work Only for WEB TESTS !!!!
# Description : Common Operations for entire Project
# ----------------------------------------------------------------------------------------

import csv
from datetime import datetime

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET
from NetboostMedia.TestCases import conftest

'''Functions to Read Files'''


# Reads data from data.xml for configuration of the Project
# Parameter   : Name of the attribute in xml file
# Return value: String
def GetData(name: str) -> str:
    root = ET.parse("D:\\pyCharm\\CompaniesShowProject\\NetboostMedia\\Configuration\\data.xml").getroot()
    return root.find(".//" + name).text


# Function to read CSV files for Data Driven Testing
def ReadCsv(fileName):
    data = []
    with open(fileName, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
        return data


'''Function to Explicitly Wait for elements'''


def Wait(forElement, elem):  # TODO: If needed in final version
    if forElement == "elementExists":
        WebDriverWait(conftest.driver, int(GetData("WaitTime"))).until(
            EC.presence_of_element_located((elem[0], elem[1])))
    elif forElement == "elementDisplayed":
        WebDriverWait(conftest.driver, int(GetData("WaitTime"))).until(
            EC.visibility_of_element_located((elem[0], elem[1])))
    '''Can be extended here '''


'''Enums for different conditions in entire project'''


# Enum For is for selecting displayed or exist element, my Wait method uses this enum
class For:
    elementExists = "elementExists"
    elementDisplayed = "elementDisplayed"


# Enum By is for search users By text or By index TODO: If needed in final version
class By:
    user = "user"
    index = "index"


# Enum Save is for selecting whether we want to save mortgage transaction or not TODO: If needed in final version
class Save:
    Yes = True
    No = False


# Enum for selecting whether we want to save mortgage transaction or not TODO: If needed in final version
class Direction:
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"
