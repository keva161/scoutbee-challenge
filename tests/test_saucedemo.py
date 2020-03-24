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

    # Test is the same as previous but with a negative assertion.

    NewHomePage = SauceDemoPage(browser)

    TITLE = "Incorrect Title"

    NewHomePage.GoTo()

    NewHomePage.Login()

    assert TITLE not in NewHomePage.Title()



