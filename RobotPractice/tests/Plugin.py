from SeleniumLibrary import BrowserManagementKeywords
from robot.api.deco import keyword
import time


class Plugin(BrowserManagementKeywords):
    @keyword
    def opendriver(self):
        from selenium import webdriver
        driver = webdriver.Chrome()
        return driver