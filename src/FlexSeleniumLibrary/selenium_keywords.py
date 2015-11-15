from selenium import webdriver
from flexselenium_keywords import FlexSeleniumKeywords


class SeleniumKeywords(object):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        """
        Import the library with two mandatory parameters. An initialized selenium instance and the name of the flash
        application to test.
        Example:
        | Library | FlexSeleniumLibrary | ${selenium} | FlashApp
        """
        self.selenium = None
        self.flex_selenium = None

    def open_browser(self, browser):
        if browser == 'firefox':
            self.selenium = webdriver.Firefox()
        elif browser == 'chrome':
            self.selenium = webdriver.Chrome()
        elif browser == 'ie':
            self.selenium = webdriver.Ie()
        else:
            raise AttributeError("Unknown browser: {}".format(browser))
        return self.selenium

    def capture_screenshot(self, file_path):
        """Take a screenshot with Selenium.

        Args:
            file_path: the path to store the file.
        Returns:
            true if success, false on error
        """
        return self.selenium.save_screenshot(file_path)

    def get(self, url):
        self.selenium.get(url)

    def exit_browser(self):
        if self.selenium is not None:
            self.selenium.quit()
            self.selenium = None
            self.flex_selenium = None


