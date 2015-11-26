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
    ROBOT_LIBRARY_VERSION = '0.1.0'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, flash_app, api_version=28, sleep_after_call=0, sleep_after_fail=0.1,
                 number_of_retries=30, timeout=5.0, implicit_wait=0.0, run_on_failure='',
                 screenshot_root_directory=None):
        """Initializes the library. Next use 'Open browser' keyword.

        Args:
            flash_app: the name for the flash application
            api_version: the version of SeleniumFlexAPI build into the application
            sleep_after_call: the wait after each executed command. Helpful for manually watching execution
            sleep_after_fail: wait time after each fail before trying again
            number_of_retries: number of times to retry the command
        """
        Selenium2Library.__init__(self, timeout, implicit_wait, run_on_failure, screenshot_root_directory)

        self.flash_object_id = flash_app
        self.api_version = api_version
        self.sleep_after_call = sleep_after_call
        self.sleep_after_fail = sleep_after_fail
        self.number_of_retries = number_of_retries
        self.web_driver = None
        self.flex_selenium = None
        self.sf_api_commands = None
        self.flex_pilot = None
        self.flex_pilot_commands = None

    def set_flash_app(self, flash_app):
        """Change the flash application name under test. The application name is used to create the JavaScript
            call to control the Flex application

        Args:
            flash_app: the value for the new application. The name of the application.
        """
        self.sf_api_commands.set_flash_app(flash_app)
        self.flex_pilot_commands.set_flash_app(flash_app)

    def set_sleep_after_call(self, sleep_after_call):
        """Change the delay after each command issued to the flash application.

        Args:
            sleep_after_call: the value for the delay
        """
        self.sf_api_commands.sleep_after_call = sleep_after_call

    def set_sleep_after_fail(self, sleep_after_fail):
        """Change the delay after each failed command attempt to the flash application.

        Args:
            sleep_after_fail: the value for the delay
        """
        self.sf_api_commands.sleep_after_fail = sleep_after_fail

    def set_number_of_retries(self, number_of_retries):
        """Change the number of retries to execute a command with the flash application.
        If the command fails for the first time it can be because the flash application has not yet loaded
        successfully. So let's try again after little delay...

        Args:
            number_of_retries: the number of retries before giving up
        """
        self.sf_api_commands.number_of_retries = number_of_retries

    def open_browser(self, url='', browser='firefox', alias=None, remote_url=False, desired_capabilities=None,
                     ff_profile_dir=None):
        super(FlexSeleniumLibrary, self).open_browser(url, browser, alias, remote_url, desired_capabilities,
                                                      ff_profile_dir)
        self.flex_selenium = FlexSeleniumKeywords(self._current_browser(), self.flash_object_id, self.api_version,
                                                  self.sleep_after_call)
        self.sf_api_commands = SeleniumFlexAPICommands(self._current_browser(), self.flash_object_id, self.api_version,
                                                       self.sleep_after_call)
        self.flex_pilot = FlexPilotKeywords(self._current_browser(), self.flash_object_id)
        self.flex_pilot_commands = FlexPilotCommands(self._current_browser(), self.flash_object_id)

    def close_browser(self):
        super(FlexSeleniumLibrary, self).close_browser()

    def close_all_browsers(self):
        super(FlexSeleniumLibrary, self).close_all_browsers()
        self.web_driver = None
        self.flex_selenium = None
        self.sf_api_commands = None
        self.flex_pilot = None
        self.flex_pilot_commands = None

    def get_text_selenium(self, locator):
        return self._get_text(locator)
