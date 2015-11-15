from flexselenium_keywords import FlexSeleniumKeywords
from selenium_keywords import SeleniumKeywords
from sfapicommands import SeleniumFlexAPICommands


class FlexSeleniumLibrary(
            SeleniumKeywords,
            FlexSeleniumKeywords
        ):
    ROBOT_LIBRARY_VERSION = '0.1.0'

    def __init__(self, flash_app='Main'):
        super(FlexSeleniumLibrary, self).__init__()
        self.selenium = SeleniumKeywords()
        self.flex_selenium = FlexSeleniumKeywords(self.selenium, flash_app)
        self.sfapi_commands = SeleniumFlexAPICommands(self)
        self.flash_object_id = flash_app

    def initialize_flex_selenium(self, flash_app):
        self.flex_selenium = FlexSeleniumKeywords(self.selenium, flash_app)
        return self.flex_selenium
