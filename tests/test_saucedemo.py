"""
These tests will cover the required functionality for our test.
"""

from pages.SauceDemoPage import SauceDemoPage

def test_FirstInstance(browser):
    HomePage = SauceDemoPage(browser)

    TITLE = "Swag Labs"

    # Visits the homepage
    HomePage.GoTo()

    # Logs into the Demo Site
    HomePage.Login()

    # Asserts the page title is as expected
    assert TITLE in HomePage.Title()

def test_Second_Instance(browser):
    NewHomePage = SauceDemoPage(browser)

    TITLE = "Swag Labs"

    NewHomePage.GoTo()

    NewHomePage.Login()

    assert TITLE in NewHomePage.Title()



