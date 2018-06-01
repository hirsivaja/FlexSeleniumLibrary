from keywords.flexselenium_keywords import FlexSeleniumKeywords
from keywords.flexpilot_keywords import FlexPilotKeywords
from sfapicommands import SeleniumFlexAPICommands
from flexpilotcommands import FlexPilotCommands
from SeleniumLibrary import SeleniumLibrary
from SeleniumLibrary.base import keyword, LibraryComponent
from SeleniumLibrary.keywords import *


class FlexSeleniumLibrary(SeleniumLibrary):
    """
    Test library for Adobe/Apache Flex. Imports SeleniumLibrary keywords to manipulate rest of the web pages.

    Uses the SeleniumFlexAPI to send the commands to the Flex application. The SFAPI library needs to be taken in use
    in the Flex application for the commands to work.
    """
    ROBOT_LIBRARY_VERSION = '0.3.3'
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
            selenium_timeout: see SeleniumLibrary documentation
            selenium_implicit_wait: see SeleniumLibrary documentation
            selenium_run_on_failure: see SeleniumLibrary documentation
            selenium_screenshot_root_directory: see SeleniumLibrary documentation
        """
        SeleniumLibrary.__init__(self, selenium_timeout, selenium_implicit_wait, selenium_run_on_failure,
                                 selenium_screenshot_root_directory)
        self.add_library_components([FlexSeleniumKeywords(self, flash_app, int(api_version), float(sleep_after_call),
                                                          float(sleep_after_fail), int(number_of_retries), float(ensure_timeout)),
                                     FlexPilotKeywords(self, flash_app),
                                     OverwrittenKeywords(self)])

    def set_flash_app(self, flash_app):
        """Change the flash application name under test. The application name is used to create the JavaScript
            call to control the Flex application

        Args:
            flash_app: the value for the new application. The name of the application.
        """
        self.sf_api_commands.set_flash_app(flash_app)
        self.flex_pilot_commands.set_flash_app(flash_app)

    def set_api_version(self, api_version):
        """Change the expected version of SFAPI used in the application under test.
        Some keywords are available only on some versions of the API and some commands
        have different syntax between API versions. The API version can also be asked from
        the SFAPI starting with version 28. Use keyword 'Get API version'.

        Args:
            api_version: The expected API version.
        """
        self.sf_api_commands.set_api_version(int(api_version))

    def set_sleep_after_call(self, sleep_after_call):
        """Change the delay after each command issued to the flash application.

        Args:
            sleep_after_call: the value for the delay
        """
        self.sf_api_commands.set_sleep_after_call(float(sleep_after_call))

    def set_sleep_after_fail(self, sleep_after_fail):
        """Change the delay after each failed command attempt to the flash application.

        Args:
            sleep_after_fail: the value for the delay
        """
        self.sf_api_commands.set_sleep_after_fail(float(sleep_after_fail))

    def set_number_of_retries(self, number_of_retries):
        """Change the number of retries to execute a command with the flash application.
        If the command fails for the first time it can be because the flash application has not yet loaded
        successfully. So let's try again after little delay...

        Args:
            number_of_retries: the number of retries before giving up
        """
        self.sf_api_commands.set_number_of_retries(int(number_of_retries))

    def set_ensure_timeout(self, ensure_timeout):
        """Change how long to wait for ensure commands to succeed before giving up

        Args:
             ensure_timeout: Maximum time in seconds to wait for the expected value
        """
        self.sf_api_commands.set_ensure_timeout(float(ensure_timeout))


class OverwrittenKeywords(LibraryComponent):
    """
    Some of the SeleniumLibrary keywords need to be overwritten so that they work with Flex
    """

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)

    @keyword
    def open_browser(self, url='', browser='firefox', alias=None, remote_url=False, desired_capabilities=None,
                     ff_profile_dir=None):
        """Opens a new browser instance to given URL.

        Returns the index of this browser instance which can be used later to
        switch back to it. Index starts from 1 and is reset back to it when
        `Close All Browsers` keyword is used. See `Switch Browser` for
        example.

        For more information see SeleniumLibrary documentation:
        http://robotframework.org/SeleniumLibrary/SeleniumLibrary.html

        Args:
            url: The URL to open
            browser: The browser to use
            alias: an alias to identify the browser instance
            remote_url: see SeleniumLibrary documentation
            desired_capabilities: see SeleniumLibrary documentation
            ff_profile_dir: see SeleniumLibrary documentation
        """
        browser_management = BrowserManagementKeywords(self.ctx)
        browser_management.open_browser(url, browser, alias, remote_url, desired_capabilities, ff_profile_dir)

    @keyword
    def close_browser(self):
        """Closes the current browser.
        """
        browser_management = BrowserManagementKeywords(self.ctx)
        browser_management.close_browser()

    @keyword
    def close_all_browsers(self):
        """Closes all the browsers
        """
        browser_management = BrowserManagementKeywords(self.ctx)
        browser_management.close_all_browsers()

    @keyword
    def get_text_selenium(self, locator):
        """Get text using Selenium
        """
        element_keywords = ElementKeywords(self.ctx)
        return element_keywords.get_text(locator)