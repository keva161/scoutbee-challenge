import pytest
from selenium.common.exceptions import WebDriverException

from utils.Driver import Driver

"""
This file contains the fixture which will be run before the tests.

"""
browser = None

@pytest.fixture()
def browser():
    factory = Driver()
    browser = factory.GetDriver()

    if browser is not None:
        print("New driver instance created!")
    else:
        raise WebDriverException("Never created!")

    yield browser

    browser.quit()


