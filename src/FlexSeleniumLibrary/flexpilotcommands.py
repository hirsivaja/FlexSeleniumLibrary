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
        result = self.web_driver.execute_script(script)
        return result

    def set_flash_app(self, flash_app):
        self.flash_object_id = flash_app
