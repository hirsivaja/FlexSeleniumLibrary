from selenium import webdriver


class SeleniumKeywords(object):

    def __init__(self):
        """
        Keywords related to manipulating the browser instance.

        The keywords utilize the selenium python module. See https://pypi.python.org/pypi/selenium
        """
        self.web_driver = None

    def open_browser(self, browser):
        """Create new Selenium WebDriver. Closes the old if it exists

        Args:
            browser: the browser to start. "firefox", "chrome" or "ie".
        Returns:
            the new Selenium instance
        """
        if self.web_driver is not None:
            self.exit_browser()
        if browser == 'firefox':
            self.web_driver = webdriver.Firefox()
        elif browser == 'chrome':
            self.web_driver = webdriver.Chrome()
        elif browser == 'ie':
            self.web_driver = webdriver.Ie()
        else:
            raise AttributeError("Unknown browser: {}".format(browser))
        return self.web_driver

    def capture_screenshot(self, file_path):
        """Take a screenshot with Selenium.

        Args:
            file_path: the path to store the file.
        Returns:
            true if success, false on error
        """
        return self.web_driver.save_screenshot(file_path)

    def get(self, url):
        """Navigate to given url

        Args:
            url: the url to navigate to
        """
        self.web_driver.get(url)

    def exit_browser(self):
        """Destroy the browser instance.

        """
        if self.web_driver is not None:
            self.web_driver.quit()
            self.web_driver = None
