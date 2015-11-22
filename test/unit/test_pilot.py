import time
import unittest
from selenium.common.exceptions import WebDriverException

from src.FlexSeleniumLibrary.keywords.flexpilot_keywords import FlexPilotKeywords
from src.FlexSeleniumLibrary.keywords.selenium_keywords import SeleniumKeywords

application_name = "Flex4Tester"
application_url = "http://localhost:8080/flex4test/index.html"


class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = SeleniumKeywords()
        cls.flex_pilot = FlexPilotKeywords(cls.selenium.open_browser('firefox'), application_name)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.exit_browser()

    def setUp(self):
        self.selenium.get(application_url)
        # Wait until application ready
        tries = 100
        while True:
            try:
                self.flex_pilot.fp_get_property_value(self.flex_pilot.flex_pilot_id_locator("buttonBar"), "visible")
                break
            except WebDriverException as e:
                if not e.msg == "document.getElementById(...).fp_getPropertyValue is not a function":
                    raise e
                tries -= 1
                if tries == 0:
                    raise e
                time.sleep(0.1)

    def test_fp_assert_display_object(self):
        pass

    def test_fp_assert_property(self):
        pass

    def test_fp_assert_text(self):
        pass

    def test_fp_assert_text_in(self):
        pass

    def test_fp_check(self):
        pass

    def test_fp_click(self):
        assert "Number of clicks: 0" in self.flex_pilot.fp_get_text_value(
            self.flex_pilot.flex_pilot_id_locator("buttonClicks"))
        self.flex_pilot.fp_click(self.flex_pilot.flex_pilot_id_locator("clickButton"))
        assert "Number of clicks: 1" in self.flex_pilot.fp_get_text_value(
            self.flex_pilot.flex_pilot_id_locator("buttonClicks"))

    def test_fp_date(self):
        pass

    def test_fp_drag_drop_to_coordinates(self):
        pass

    def test_fp_drag_drop_elem_to_elem(self):
        pass

    def test_fp_double_click(self):
        pass

    def test_fp_dump(self):
        pass

    def test_fp_get_object_coordinates(self):
        pass

    def test_fp_get_property_value(self):
        pass

    def test_fp_get_text_value(self):
        pass

    def test_fp_get_version(self):
        assert "FlexPilot" in self.flex_pilot.fp_get_version()

    def test_fp_lookup_flash(self):
        assert self.flex_pilot.fp_lookup_flash(self.flex_pilot.flex_pilot_id_locator("buttonBar"))
        assert not self.flex_pilot.fp_lookup_flash(self.flex_pilot.flex_pilot_id_locator("nonExistingObject"))

    def test_fp_mouse_out(self):
        pass

    def test_fp_mouse_over(self):
        pass

    def test_fp_radio(self):
        pass

    def test_fp_select(self):
        pass

    def test_fp_type(self):
        alert_text = self.flex_pilot.flex_pilot_id_locator("alertText")
        assert "The world has ended!" in self.flex_pilot.fp_get_text_value(alert_text)
        self.flex_pilot.fp_type(alert_text, "test")
        assert "test" in self.flex_pilot.fp_get_text_value(alert_text)
