import pytest
from selenium.common.exceptions import WebDriverException

from utils.Driver import Driver

"""
This file contains the fixture which will be run before the tests.

"""

@pytest.fixture()
def browser():
    factory = Driver()
    driver = factory.GetDriver()

    if driver is not None:
        print("New driver instance created!")
    else:
        raise WebDriverException("Never created!")

    yield driver

    driver.quit()