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

    def __init__(self, flash_app, browser='firefox', sleep_after_call=0, sleep_after_fail=0.1,
                 number_of_retries=30):
        """Initializes the library. Opens a browser instance

        Args:
            flash_app: the name for the flash application
            browser: the browser to start. "none", "firefox", "chrome" or "ie". "none" does not start the browser.
            sleep_after_call: the wait after each executed command. Helpful for manually watching execution
            sleep_after_fail: wait time after each fail before trying again
            number_of_retries: number of times to retry the command
        """
        self.flash_object_id = flash_app
        self.sleep_after_call = sleep_after_call
        self.sleep_after_fail = sleep_after_fail
        self.number_of_retries = number_of_retries
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

    def set_sleep_after_call(self, sleep_after_call):
        """Change the delay after each command issued to the flash application.

        Args:
            sleep_after_call: the value for the delay
        """
        self.sfapi_commands.sleep_after_call = sleep_after_call

    def set_sleep_after_fail(self, sleep_after_fail):
        """Change the delay after each failed command attempt to the flash application.

        Args:
            sleep_after_fail: the value for the delay
        """
        self.sfapi_commands.sleep_after_fail = sleep_after_fail

    def set_number_of_retries(self, number_of_retries):
        """Change the number of retries to execute a command with the flash application.
        If the command fails for the first time it can be because the flash application has not yet loaded
        successfully. So let's try again after little delay...

        Args:
            number_of_retries: the number of retries before giving up
        """
        self.sfapi_commands.number_of_retries = number_of_retries

    def open_browser(self, browser):
        self.web_driver = self.selenium.open_browser(browser)
        self.flex_selenium = FlexSeleniumKeywords(self.web_driver, self.flash_object_id, self.sleep_after_call)
        self.sfapi_commands = SeleniumFlexAPICommands(self.web_driver, self.flash_object_id, self.sleep_after_call)
