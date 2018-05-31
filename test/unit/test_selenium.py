import unittest

from src.FlexSeleniumLibrary import FlexSeleniumLibrary

application_name = "None"
application_url = "http://www.google.com"

api_version = 0
sleep_after_call = 0
sleep_after_fail = 0.1
number_of_retries = 30
ensure_timeout = 30


class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.flex_selenium = FlexSeleniumLibrary(application_name, api_version, sleep_after_call, sleep_after_fail,
                                                number_of_retries, ensure_timeout)
        cls.flex_selenium.open_browser("about:blank")
        cls.flex_selenium.maximize_browser_window()

    @classmethod
    def tearDownClass(cls):
        cls.flex_selenium.close_browser()

    def setUp(self):
        self.flex_selenium.go_to(application_url)
        # Wait until "search box" is found
        self.flex_selenium.wait_until_element_is_enabled("lst-ib")

    def test_input(self):
        self.flex_selenium.input_text("lst-ib", "test")
        self.flex_selenium.press_key("lst-ib", "\\13")
        self.flex_selenium.wait_until_page_contains("Test - Wikipedia")
