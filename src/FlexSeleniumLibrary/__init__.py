from keywords.flexselenium_keywords import FlexSeleniumKeywords
from keywords.selenium_keywords import SeleniumKeywords
from sfapicommands import SeleniumFlexAPICommands


class FlexSeleniumLibrary(
            SeleniumKeywords,
            FlexSeleniumKeywords
        ):
    """
    Test library for Adobe/Apache Flex with the help of Selenium2 WebDriver.

    Uses the SeleniumFlexAPI to send the commands to the Flex application. The SFAPI library needs to be taken in use
    in the Flex application for the commands to work.
    """
    ROBOT_LIBRARY_VERSION = '0.1.0'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, flash_app, browser='firefox', sleep_after_call=0):
        """Initializes the library. Opens a browser instance

        Args:
            flash_app: the name for the flash application
            browser: the browser to start. "none", "firefox", "chrome" or "ie". "none" does not start the browser.
            sleep_after_call: the wait after each executed command. Helpful for manually watching execution
        """
        self.flash_object_id = flash_app
        self.sleep_after_call = sleep_after_call
        self.selenium = SeleniumKeywords()
        if browser == 'none':
            self.web_driver = None
            self.flex_selenium = None
            self.sfapi_commands = None
        else:
            self.web_driver = self.selenium.open_browser(browser)
            self.flex_selenium = FlexSeleniumKeywords(self.web_driver, self.flash_object_id, self.sleep_after_call)
            self.sfapi_commands = SeleniumFlexAPICommands(self.web_driver, self.flash_object_id, self.sleep_after_call)

    def set_flash_app(self, flash_app):
        """Change the flash application name under test. The application name is used to create the JavaScript
        call to control the Flex application

       Args:
           flash_app: the value for the new application. The name of the application.
       """
        self.sfapi_commands.set_flash_app(flash_app)

    def open_browser(self, browser):
        self.web_driver = self.selenium.open_browser(browser)
        self.flex_selenium = FlexSeleniumKeywords(self.web_driver, self.flash_object_id, self.sleep_after_call)
        self.sfapi_commands = SeleniumFlexAPICommands(self.web_driver, self.flash_object_id, self.sleep_after_call)
