from keywords.flexselenium_keywords import FlexSeleniumKeywords
from keywords.flexpilot_keywords import FlexPilotKeywords
from sfapicommands import SeleniumFlexAPICommands
from flexpilotcommands import FlexPilotCommands
from Selenium2Library import Selenium2Library


class FlexSeleniumLibrary(
            FlexSeleniumKeywords,
            FlexPilotKeywords,
            Selenium2Library
        ):
    """
    Test library for Adobe/Apache Flex. Imports Selenium2Library keywords to manipulate rest of the web pages.

    Uses the SeleniumFlexAPI to send the commands to the Flex application. The SFAPI library needs to be taken in use
    in the Flex application for the commands to work.
    """
    ROBOT_LIBRARY_VERSION = '0.3.0'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self,
                 flash_app, api_version=28, sleep_after_call=0, sleep_after_fail=0.1, number_of_retries=30,
                 ensure_timeout=30, selenium_timeout=5.0, selenium_implicit_wait=0.0, selenium_run_on_failure='',
                 selenium_screenshot_root_directory=None):
        """Initializes the library. Next use 'Open browser' keyword.

        Args:
            flash_app: the name for the flash application
            api_version: the version of SeleniumFlexAPI build into the application
            sleep_after_call: the wait after each executed command. Helpful for manually watching execution
            sleep_after_fail: wait time after each fail before trying again
            number_of_retries: number of times to retry the command
            ensure_timeout: how long to wait for ensure commands to succeed before giving up
            selenium_timeout: see Selenium2Library documentation
            selenium_implicit_wait: see Selenium2Library documentation
            selenium_run_on_failure: see Selenium2Library documentation
            selenium_screenshot_root_directory: see Selenium2Library documentation
        """
        Selenium2Library.__init__(self, selenium_timeout, selenium_implicit_wait, selenium_run_on_failure,
                                  selenium_screenshot_root_directory)

        self.flash_object_id = flash_app
        self.api_version = int(api_version)
        self.sleep_after_call = float(sleep_after_call)
        self.sleep_after_fail = float(sleep_after_fail)
        self.number_of_retries = int(number_of_retries)
        self.ensure_timeout = float(ensure_timeout)
        self.web_driver = None
        self.flex_selenium = None
        self.flex_pilot = None

    def set_flash_app(self, flash_app):
        """Change the flash application name under test. The application name is used to create the JavaScript
            call to control the Flex application

        Args:
            flash_app: the value for the new application. The name of the application.
        """
        self.flex_selenium.sf_api_commands.set_flash_app(flash_app)
        self.flex_pilot.flex_pilot_commands.set_flash_app(flash_app)

    def set_api_version(self, api_version):
        """Change the expected version of SFAPI used in the application under test.
        Some keywords are available only on some versions of the API and some commands
        have different syntax between API versions. The API version can also be asked from
        the SFAPI starting with version 28. Use keyword 'Get API version'.

        Args:
            api_version: The expected API version.
        """
        self.flex_selenium.sf_api_commands.set_api_version(int(api_version))

    def set_sleep_after_call(self, sleep_after_call):
        """Change the delay after each command issued to the flash application.

        Args:
            sleep_after_call: the value for the delay
        """
        self.flex_selenium.sf_api_commands.set_sleep_after_call(float(sleep_after_call))

    def set_sleep_after_fail(self, sleep_after_fail):
        """Change the delay after each failed command attempt to the flash application.

        Args:
            sleep_after_fail: the value for the delay
        """
        self.flex_selenium.sf_api_commands.set_sleep_after_fail(float(sleep_after_fail))

    def set_number_of_retries(self, number_of_retries):
        """Change the number of retries to execute a command with the flash application.
        If the command fails for the first time it can be because the flash application has not yet loaded
        successfully. So let's try again after little delay...

        Args:
            number_of_retries: the number of retries before giving up
        """
        self.flex_selenium.sf_api_commands.set_number_of_retries(int(number_of_retries))

    def set_ensure_timeout(self, ensure_timeout):
        """Change how long to wait for ensure commands to succeed before giving up

        Args:
             ensure_timeout: Maximum time in seconds to wait for the expected value
        """
        self.flex_selenium.sf_api_commands.set_ensure_timeout(float(ensure_timeout))

    def open_browser(self, url='', browser='firefox', alias=None, remote_url=False, desired_capabilities=None,
                     ff_profile_dir=None):
        """Opens a new browser instance to given URL.

        Returns the index of this browser instance which can be used later to
        switch back to it. Index starts from 1 and is reset back to it when
        `Close All Browsers` keyword is used. See `Switch Browser` for
        example.

        For more information see Selenium2Library documentation:
        http://robotframework.org/Selenium2Library/doc/Selenium2Library.html

        Args:
            url: The URL to open
            browser: The browser to use
            alias: an alias to identify the browser instance
            remote_url: see Selenium2Library documentation
            desired_capabilities: see Selenium2Library documentation
            ff_profile_dir: see Selenium2Library documentation
        """
        super(FlexSeleniumLibrary, self).open_browser(url, browser, alias, remote_url, desired_capabilities,
                                                      ff_profile_dir)
        self.flex_selenium = FlexSeleniumKeywords(self._current_browser(), self.flash_object_id, self.api_version,
                                                  self.sleep_after_call, self.sleep_after_fail, self.number_of_retries,
                                                  self.ensure_timeout)
        self.flex_pilot = FlexPilotKeywords(self._current_browser(), self.flash_object_id)

    def close_browser(self):
        """Closes the current browser.
        """
        super(FlexSeleniumLibrary, self).close_browser()

    def close_all_browsers(self):
        """Closes all the browsers
        """
        super(FlexSeleniumLibrary, self).close_all_browsers()
        self.web_driver = None
        self.flex_selenium = None
        self.flex_pilot = None

    def get_text_selenium(self, locator):
        """Get text using Selenium
        """
        return self._get_text(locator)
