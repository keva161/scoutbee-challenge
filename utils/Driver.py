from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

"""
This file contains the fixture which will be run before the tests.

Webdriver_Manager is used to ensure the latest version of the driver executables are being used.

"""

class Driver(object):
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.prefs = {"profile.default_content_setting_values.notifications": 2}
        self.chrome_options.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def GetDriver(self):
        driver = self.driver
        return driver