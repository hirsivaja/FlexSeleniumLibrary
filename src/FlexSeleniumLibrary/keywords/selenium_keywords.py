from selenium import webdriver


class SeleniumKeywords(object):

    def __init__(self):
        """
        Keywords related to manipulating the browser instance.

        The keywords utilize the selenium python module. See https://pypi.python.org/pypi/selenium
        """
        self.selenium = None

    def open_browser(self, browser):
        """Create new Selenium WebDriver

        Args:
            browser: the browser to start. "firefox", "chrome" or "ie".
        Returns:
            the new Selenium instance
        """
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
        """Navigate to given url

        Args:
            url: the url to navigate to
        """
        self.selenium.get(url)

    def exit_browser(self):
        """Destroy the browser instance.

        """
        if self.selenium is not None:
            self.selenium.quit()
            self.selenium = None
