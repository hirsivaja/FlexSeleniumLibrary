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

    def __init__(self, flash_app='Main'):
        """Initializes the library

        Args:
            flash_app: the name for the flash application
        """
        super(FlexSeleniumLibrary, self).__init__()
        self.selenium = SeleniumKeywords()
        self.flex_selenium = FlexSeleniumKeywords(self.selenium, flash_app)
        self.sfapi_commands = SeleniumFlexAPICommands(self)
        self.flash_object_id = flash_app

    def set_flex_selenium_flash_app(self, flash_app):
        """Change the flash application name under test. The application name is used to create the JavaScript
        call to control the Flex application

       Args:
           flash_app: the value for the new application. The name of the application.
       """
        self.flex_selenium = FlexSeleniumKeywords(self.selenium, flash_app)
