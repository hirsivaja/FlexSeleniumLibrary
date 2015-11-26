import unittest
from src.FlexSeleniumLibrary.keywords.flexpilot_keywords import FlexPilotKeywords
from Selenium2Library import Selenium2Library

application_name = "Flex4Tester"
application_url = "http://localhost:8080/flex4test/index.html"


class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = Selenium2Library(run_on_failure='')
        cls.selenium._run_on_failure_keyword = None
        cls.selenium.open_browser("")
        cls.selenium.maximize_browser_window()
        cls.flex_pilot = FlexPilotKeywords(cls.selenium._current_browser(), application_name)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.close_browser()

    def setUp(self):
        self.selenium.go_to(application_url)
        # Wait until application ready
        self.flex_pilot.fp_wait_for_flex_ready(10)

    def test_fp_assert_display_object(self):
        assert self.flex_pilot.fp_assert_display_object(self.flex_pilot.fp_id_locator("buttonBar"))

    def test_fp_assert_property(self):
        assert self.flex_pilot.fp_assert_property(self.flex_pilot.fp_id_locator("buttonBar"), "visible|true")

    def test_fp_assert_text(self):
        assert self.flex_pilot.fp_assert_text(self.flex_pilot.fp_id_locator("buttonClicks"),
                                              "Number of clicks: 0")

    def test_fp_assert_text_in(self):
        assert self.flex_pilot.fp_assert_text_in(self.flex_pilot.fp_id_locator("buttonClicks"), "of click")

    def test_fp_check(self):
        self.flex_pilot.fp_click("label:'CheckBox view'")
        assert "CheckBox is checked" in self.flex_pilot.fp_get_text_value(
            self.flex_pilot.fp_id_locator("selectedCheckBoxItem"))
        self.flex_pilot.fp_check(self.flex_pilot.fp_id_locator("checkBox"))
        assert "CheckBox is not checked" in self.flex_pilot.fp_get_text_value(
            self.flex_pilot.fp_id_locator("selectedCheckBoxItem"))

    def test_fp_click(self):
        assert "Number of clicks: 0" in self.flex_pilot.fp_get_text_value(
            self.flex_pilot.fp_id_locator("buttonClicks"))
        self.flex_pilot.fp_click(self.flex_pilot.fp_id_locator("clickButton"))
        assert "Number of clicks: 1" in self.flex_pilot.fp_get_text_value(
            self.flex_pilot.fp_id_locator("buttonClicks"))

    def test_fp_date(self):
        pass

    def test_fp_drag_drop_to_coordinates(self):
        pass

    def test_fp_drag_drop_elem_to_elem(self):
        pass

    def test_fp_double_click(self):
        self.flex_pilot.fp_click("label:'Mouse view'")
        self.flex_pilot.fp_double_click(self.flex_pilot.fp_id_locator("mouseEventCatcher"))
        assert self.flex_pilot.fp_assert_display_object("label:'OK'")

    def test_fp_dump(self):
        assert "ButtonBarButton" in self.flex_pilot.fp_dump("id:'buttonBar'")

    def test_fp_get_object_coordinates(self):
        assert "(" and ")" in self.flex_pilot.fp_get_object_coordinates("id:'buttonBar'")

    def test_fp_get_property_value(self):
        assert "clickButton" == self.flex_pilot.fp_get_property_value(
            self.flex_pilot.fp_id_locator("clickButton"), "id")

    def test_fp_get_text_value(self):
        assert "The world has ended!" in self.flex_pilot.fp_get_text_value(
            self.flex_pilot.fp_id_locator("alertText"))

    def test_fp_get_version(self):
        assert "FlexPilot" in self.flex_pilot.fp_get_version()

    def test_fp_lookup_flash(self):
        assert self.flex_pilot.fp_lookup_flash(self.flex_pilot.fp_id_locator("buttonBar"))
        assert not self.flex_pilot.fp_lookup_flash(self.flex_pilot.fp_id_locator("nonExistingObject"))

    def test_fp_mouse_out(self):
        self.flex_pilot.fp_click("label:'Mouse view'")
        self.flex_pilot.fp_mouse_out(self.flex_pilot.fp_id_locator("mouseEventCatcher"))
        assert self.flex_pilot.fp_assert_display_object("label:'OK'")

    def test_fp_mouse_over(self):
        self.flex_pilot.fp_click("label:'Mouse view'")
        self.flex_pilot.fp_mouse_over(self.flex_pilot.fp_id_locator("mouseEventCatcher"))
        assert self.flex_pilot.fp_assert_display_object("label:'OK'")

    def test_fp_radio(self):
        self.flex_pilot.fp_click("label:'RadioButtons view'")
        self.flex_pilot.fp_radio(self.flex_pilot.fp_id_locator("radioButton3"))
        assert "Selected value: 3" in self.flex_pilot.fp_get_text_value(self.flex_pilot.
                                                                        fp_id_locator("selectedRadioButton"))

    def test_fp_select(self):
        selected_combo_item = self.flex_pilot.fp_id_locator("selectedComboItem")
        self.flex_pilot.fp_click("label:'ComboBox view'")
        self.flex_pilot.fp_select("id:'comboBox',index:'2'")
        assert "Selected label: Element = Element3, 3, true" in self.flex_pilot.fp_get_text_value(selected_combo_item)

    def test_fp_type(self):
        alert_text = self.flex_pilot.fp_id_locator("alertText")
        assert "The world has ended!" in self.flex_pilot.fp_get_text_value(alert_text)
        self.flex_pilot.fp_type(alert_text, "test")
        assert "test" in self.flex_pilot.fp_get_text_value(alert_text)

    def test_fp_wait_for_flex_ready(self):
        self.flex_pilot.fp_wait_for_flex_ready(10)

    def test_fp_wait_for_flex_object(self):
        self.flex_pilot.fp_wait_for_flex_object("id:'buttonBar'", 10)
