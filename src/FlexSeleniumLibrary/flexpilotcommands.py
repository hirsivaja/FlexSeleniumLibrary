import time
from robot.api import logger


class FlexPilotCommands(object):

    def __init__(self, web_driver, flash_object_id):
        self.web_driver = web_driver
        self.flash_object_id = flash_object_id

    def call(self, function_name, *function_parameters):
        if self.web_driver is None:
            raise AssertionError("WebDriver is not initialized!")
        params = ""
        if len(function_parameters) > 0:
            for param in function_parameters:
                params += str(param) + ","
            params = "{" + params[:-1] + "}"
        script = "return document.getElementById('{}').{}({});".format(self.flash_object_id, function_name, params)
        logger.debug("JavaScript to execute: '{}'".format(script))
        result = self.web_driver.execute_script(script)
        return result

    def set_flash_app(self, flash_app):
        self.flash_object_id = flash_app

    def wait_for_flex_application_to_load(self, timeout):
        script = "return document.getElementById('{}').fp_click;".format(self.flash_object_id)
        tries = timeout * 10
        while True:
            result = self.web_driver.execute_script(script)
            if result is not None:
                break
            tries -= 1
            if tries == 0:
                raise AssertionError("Timeout when loading application. Timeout after {} seconds".format(timeout))
            time.sleep(0.1)

    def wait_for_flex_object(self, locator, timeout):
        tries = timeout * 10
        while True:
            result = self.call("fp_getPropertyValue", locator, "'attrName':'visible'")
            if result == "true" or result == "false":
                break
            tries -= 1
            if tries == 0:
                raise AssertionError("Timeout when loading application. Timeout after {} seconds".format(timeout))
            time.sleep(0.1)
