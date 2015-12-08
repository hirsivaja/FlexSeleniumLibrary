import os
import unittest

from src.FlexSeleniumLibrary.keywords.flexselenium_keywords import FlexSeleniumKeywords
from Selenium2Library import Selenium2Library

application_name = "Flex3Tester"
application_url = "http://localhost:8080/flex3test/index.html"

# application_name = "Flex4Tester"
# application_url = "http://localhost:8080/flex4test/index.html"

api_version = 28
sleep_after_call = 0
sleep_after_fail = 0.1
number_of_retries = 30
ensure_timeout = 30

buttons_view = "0"
radio_buttons_view = "1"
combo_box_view = "2"
check_box_view = "3"
date_view = "4"
data_grid_view = "5"
tab_navigator_view = "6"
stepper_view = "7"
mouse_view = "8"
tree_view = "9"


class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = Selenium2Library(run_on_failure='')
        cls.selenium.open_browser("")
        cls.selenium.maximize_browser_window()
        cls.flex_selenium = FlexSeleniumKeywords(cls.selenium._current_browser(), application_name, api_version,
                                                 sleep_after_call, sleep_after_fail, number_of_retries, ensure_timeout)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.close_browser()

    def setUp(self):
        self.selenium.go_to(application_url)
        # Wait until "buttonBar" is found
        self.flex_selenium.ensure_enabled_state("buttonBar", True)

    def test_locators(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        # Locating with id:
        assert "clickButton" == self.flex_selenium.get_property("clickButton", "name")
        # Locating with property:
        assert "buttonBar" == self.flex_selenium.get_property("className=ButtonBar", "name")
        # Locating with child number:
        assert "radioButtons" == self.flex_selenium.get_property("viewStack/getChildAt:1", "name")
        # Locating with child and property:
        assert "clickButton" == self.flex_selenium.get_property("buttons/getChildAt:0/className:Button", "name")
        # Locating a element using id and grandparent id
        assert "clickButton" == self.flex_selenium.get_property("viewStack/clickButton", "name")
        # Get full path with locator
        assert "viewStack" in self.flex_selenium.get_path_for_locator("viewStack/clickButton")

    def test_capture_screenshot(self):
        file_path = 'screenshot.jpg'
        if os.path.isfile(file_path):
            os.remove(file_path)
        self.selenium.capture_page_screenshot(file_path)
        assert os.path.isfile(file_path)
        os.remove(file_path)

    def test_add_notification(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        self.flex_selenium.add_notification("This is a test.")
        assert "Label" in self.flex_selenium.get_property("text=This is a test.", "name")

    def test_click(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        self.flex_selenium.click("clickButton")
        assert "Number of clicks: 1" == self.flex_selenium.get_text("buttonClicks")
        self.flex_selenium.click("clickButton")
        assert "Number of clicks: 2" == self.flex_selenium.get_text("buttonClicks")
        self.flex_selenium.click("clickButton")
        assert "Number of clicks: 3" == self.flex_selenium.get_text("buttonClicks")
        self.flex_selenium.click("buttonBar", "DataGrid view")
        assert self.flex_selenium.is_visible("dataGrid")

    def test_click_alert(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        self.flex_selenium.click("alertButton")
        assert self.flex_selenium.is_alert_visible()
        self.flex_selenium.click_alert("OK")
        assert not self.flex_selenium.is_alert_visible()

    def test_click_data_grid_column_header(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "Element1" == self.flex_selenium.get_data_grid_cell_label("dataGrid", 0, 0)
        self.flex_selenium.click_data_grid_column_header("dataGrid", 0)
        self.flex_selenium.click_data_grid_column_header("dataGrid", 0)
        assert "Element3" == self.flex_selenium.get_data_grid_cell_label("dataGrid", 0, 0)

    def test_click_data_grid_item_by_label(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        self.flex_selenium.select_by_matching_on_field("dataGrid", "attribute1", "Element2")
        assert "Selected item: Element = Element2, 2, false" == self.flex_selenium.get_text("selectedGridItem")
        self.flex_selenium.click_data_grid_item_by_label("dataGrid", "2", "false")
        assert "Selected item: Element = Element2, 2, true" == self.flex_selenium.get_text("selectedGridItem")

    def test_click_data_grid_ui_component(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        self.flex_selenium.select_by_matching_on_field("dataGrid", "attribute1", "Element2")
        assert "Selected item: Element = Element2, 2, false" == self.flex_selenium.get_text("selectedGridItem")
        self.flex_selenium.click_data_grid_ui_component("dataGrid", 1, 2)
        assert "Selected item: Element = Element2, 2, true" == self.flex_selenium.get_text("selectedGridItem")

    def test_click_menu_bar_component(self):
        self.flex_selenium.click_menu_bar_component("menuBar", 0, 0, 0)
        assert "Clicked: Buttons view" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")
        self.flex_selenium.click_menu_bar_component("menuBar", 0, 1, 0)
        assert "Clicked: Radio buttons view" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")
        self.flex_selenium.click_menu_bar_component("menuBar", 1, 0, 0)
        assert "Clicked: About" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")

    def test_click_selected_data_grid_item(self):
        # Tested by: self.test_select_data_grid_index()
        pass

    def test_create_mouse_events(self):
        self.flex_selenium.select_index("buttonBar", mouse_view)

        self.flex_selenium.create_mouse_down_event("mouseEventCatcher")
        assert "Mouse event: mouseDown" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")

        self.flex_selenium.create_mouse_event("mouseEventCatcher", "mouseOut")
        assert "Mouse event: mouseOut" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")

        self.flex_selenium.create_mouse_move_event("mouseEventCatcher", "200", "200")
        assert "Mouse event: mouseMove" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")

        self.flex_selenium.create_mouse_over_event("mouseEventCatcher")
        assert "Mouse event: mouseOver" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")

        self.flex_selenium.create_mouse_roll_out_event("mouseEventCatcher")
        assert "Mouse event: rollOut" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")

        self.flex_selenium.create_mouse_roll_over_event("mouseEventCatcher")
        assert "Mouse event: rollOver" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")

        self.flex_selenium.create_mouse_up_event("mouseEventCatcher")
        assert "Mouse event: mouseUp" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")

    def test_double_click(self):
        self.flex_selenium.select_index("buttonBar", mouse_view)
        self.flex_selenium.double_click("dataGrid1")
        assert "Mouse event: doubleClick" == self.flex_selenium.get_alert_text()

    def test_double_click_data_grid_component(self):
        self.flex_selenium.select_index("buttonBar", mouse_view)
        self.flex_selenium.double_click_data_grid_component("dataGrid1", "0", "0")
        assert "Mouse event: doubleClick" == self.flex_selenium.get_alert_text()

    def test_drag_element_to(self):
        self.flex_selenium.select_index("buttonBar", mouse_view)
        position = self.flex_selenium.get_global_position("dataGrid2")
        coordinates = position.split(',')
        assert "0" == self.flex_selenium.get_data_grid_row_count("dataGrid2")
        assert "true" == self.flex_selenium.drag_element_to("text=Element1", coordinates[0], coordinates[1])
        # TODO
        # assert "1" == self.flex_selenium.get_data_grid_row_count("dataGrid2")

    def test_enter_date(self):
        self.flex_selenium.select_index("buttonBar", date_view)
        self.flex_selenium.enter_date("dateField", "20.11.2011")
        assert "Selected date: 20/11/2011" == self.flex_selenium.get_text("selectedDate")

    def test_enter_date_to_data_grid_cell(self):
        pass

    def test_enter_text(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        self.flex_selenium.enter_text("alertText", "test")
        assert "test" == self.flex_selenium.get_text("alertText")
        self.flex_selenium.enter_text("alertText", "ing", True)
        assert "testing" == self.flex_selenium.get_text("alertText")
        self.flex_selenium.enter_text("alertText", "reset", False)
        assert "reset" == self.flex_selenium.get_text("alertText")

    def test_exists(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        assert self.flex_selenium.exists("buttonBar")
        assert self.flex_selenium.exists("clickButton")
        assert not self.flex_selenium.exists("notButton")

    def test_is_alert_visible(self):
        # Tested by: self.test_click_alert()
        pass

    def test_is_checkbox_checked(self):
        # Tested by: self.test_select_checkbox()
        pass

    def test_is_checkbox_in_data_grid_checked(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert self.flex_selenium.is_checkbox_in_data_grid_checked("dataGrid", "0", "2")
        assert not self.flex_selenium.is_checkbox_in_data_grid_checked("dataGrid", "1", "2")
        assert self.flex_selenium.is_checkbox_in_data_grid_checked("dataGrid", "2", "2")

    def test_is_enabled(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        assert self.flex_selenium.is_enabled("clickButton")
        assert not self.flex_selenium.is_enabled("disabledButton")

    def test_is_label_in_combo_data(self):
        self.flex_selenium.select_index("buttonBar", combo_box_view)
        assert self.flex_selenium.is_label_in_combo_data("comboBox", "Element = Element3, 3, true")
        assert not self.flex_selenium.is_label_in_combo_data("comboBox", "Element = Element3, 3, false")

    def test_is_radiobutton_checked(self):
        self.flex_selenium.select_index("buttonBar", radio_buttons_view)
        self.flex_selenium.set_radiobutton_value("radioButton3")
        assert not self.flex_selenium.is_radiobutton_checked("radioButton1")
        assert not self.flex_selenium.is_radiobutton_checked("radioButton2")
        assert self.flex_selenium.is_radiobutton_checked("radioButton3")
        self.flex_selenium.set_radiobutton_value("radioButton2")
        assert not self.flex_selenium.is_radiobutton_checked("radioButton1")
        assert self.flex_selenium.is_radiobutton_checked("radioButton2")
        assert not self.flex_selenium.is_radiobutton_checked("radioButton3")
        self.flex_selenium.set_radiobutton_value("radioButton3")
        assert not self.flex_selenium.is_radiobutton_checked("radioButton1")
        assert not self.flex_selenium.is_radiobutton_checked("radioButton2")
        assert self.flex_selenium.is_radiobutton_checked("radioButton3")

    def test_is_text_present(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        assert self.flex_selenium.is_text_present("buttonClicks", "Number of clicks: 0")
        assert not self.flex_selenium.is_text_present("buttonClicks", "Number of clicks: 1")
        assert self.flex_selenium.is_text_present("buttonClicks", "Number of clicks")

    def test_is_visible(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        assert self.flex_selenium.is_visible("clickButton")
        assert not self.flex_selenium.is_visible("invisibleButton")

    def test_get_alert_text(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        self.flex_selenium.click("alertButton")
        assert "Alert! The world has ended!" == self.flex_selenium.get_alert_text()

    def test_get_child_elements(self):
        children = self.flex_selenium.get_child_elements("viewStack", True, False)
        assert "viewStack" in children and "buttons" in children
        children = self.flex_selenium.get_child_elements("viewStack", False, False)
        assert "viewStack" not in children and "buttons" in children
        children = self.flex_selenium.get_child_elements("viewStack", True, True)
        assert "buttons" in children and "viewStack" in children and "radioButtons" not in children
        children = self.flex_selenium.get_child_elements("viewStack", False, True)
        assert "buttons" in children and "viewStack" not in children and "radioButtons" not in children

    def test_get_combobox_selected_item(self):
        # Tested by: self.test_select_combobox_item_by_label()
        pass

    def test_get_combobox_values(self):
        self.flex_selenium.select_index("buttonBar", combo_box_view)
        assert "Element = Element2, 2, false" in self.flex_selenium.get_combobox_values("comboBox")

    def test_get_component_info(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        info = self.flex_selenium.get_component_info("clickButton").split(',')
        assert len(info) == 4

    def test_get_data_grid_cell_label(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "Element1" == self.flex_selenium.get_data_grid_cell_label("dataGrid", "0", "0")
        assert "Element3" == self.flex_selenium.get_data_grid_cell_label("dataGrid", "2", "0")

    def test_get_data_grid_cell_value(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "2" == self.flex_selenium.get_data_grid_cell_value("dataGrid", "1", "1")
        assert "Element3" == self.flex_selenium.get_data_grid_cell_value("dataGrid", "2", "0")

    def test_get_data_grid_component_label(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        print self.flex_selenium.get_data_grid_component_label("dataGrid", "1", "2")

    def test_get_data_grid_field_count(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "3" == self.flex_selenium.get_data_grid_field_count("dataGrid", True)
        assert "3" == self.flex_selenium.get_data_grid_field_count("dataGrid", False)

    def test_get_data_grid_field_data_fields(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "attribute1" in self.flex_selenium.get_data_grid_field_data_fields("dataGrid", True)
        assert "attribute3" in self.flex_selenium.get_data_grid_field_data_fields("dataGrid", False)

    def test_get_data_grid_field_value_by_row_index(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "Element2" == self.flex_selenium.get_data_grid_field_value_by_row_index("dataGrid", "attribute1", "1")
        assert "3" == self.flex_selenium.get_data_grid_field_value_by_row_index("dataGrid", "attribute2", "2")

    def test_get_data_grid_field_values(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "2" in self.flex_selenium.get_data_grid_field_values("dataGrid", "1")
        assert "false" in self.flex_selenium.get_data_grid_field_values("dataGrid", "2")
        # assert "2" in self.flex_selenium.get_data_grid_field_values("dataGrid", "1", False)

    def test_get_data_grid_field_label_by_row_index(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "false" == self.flex_selenium.get_data_grid_field_label_by_row_index("dataGrid", "attribute3", "1")
        assert "Element1" == self.flex_selenium.get_data_grid_field_label_by_row_index("dataGrid", "attribute1", "0")

    def test_get_data_grid_row_count(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "3" == self.flex_selenium.get_data_grid_row_count("dataGrid")

    def test_get_data_grid_row_index_by_field_label(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "2" == self.flex_selenium.get_data_grid_row_index_by_field_label("dataGrid", "attribute1", "Element3")
        assert "1" == self.flex_selenium.get_data_grid_row_index_by_field_label("dataGrid", "attribute2", "2")

    def test_get_data_grid_row_index_by_field_value(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "2" == self.flex_selenium.get_data_grid_row_index_by_field_value("dataGrid", "attribute1", "Element3")
        assert "1" == self.flex_selenium.get_data_grid_row_index_by_field_value("dataGrid", "attribute2", "2")

    def test_get_data_grid_values(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "Element1" in self.flex_selenium.get_data_grid_values("dataGrid", True)[0]
        assert "false" in self.flex_selenium.get_data_grid_values("dataGrid", False)[1]

    def test_get_date(self):
        self.flex_selenium.select_index("buttonBar", date_view)
        self.flex_selenium.enter_date("dateField", "20.01.2001")
        assert "20/01/2001" == self.flex_selenium.get_date("dateField")

    def test_get_error_string(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        assert "" == self.flex_selenium.get_error_string("errorButton")
        self.flex_selenium.click("errorButton")
        assert "I have an error!" == self.flex_selenium.get_error_string("errorButton")

    def test_get_global_position(self):
        position = self.flex_selenium.get_global_position("buttonBar")
        coordinates = position.split(',')
        assert len(coordinates) == 2

    def test_get_number_of_selected_items(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        self.flex_selenium.select_by_matching_on_field("dataGrid", "attribute1", "Element3")
        assert "1" == self.flex_selenium.get_number_of_selected_items("dataGrid")
        self.flex_selenium.select_by_matching_on_field("dataGrid", "attribute1", "Element2", True)
        assert "2" == self.flex_selenium.get_number_of_selected_items("dataGrid")

    def test_get_properties(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        assert "clickButton,clickButton,Click" == self.flex_selenium.get_properties("clickButton", "id", "name",
                                                                                    "label")

    def test_get_property(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        assert "buttonClicks" == self.flex_selenium.get_property("buttonClicks", "id")
        assert "Number of clicks: 0" == self.flex_selenium.get_property("buttonClicks", "text")
        assert "TextInput" == self.flex_selenium.get_property("alertText", "className")
        assert "buttonClicks" == self.flex_selenium.get_property("buttonClicks", "name")

    def test_get_selection_index(self):
        self.flex_selenium.select_index("buttonBar", combo_box_view)
        assert "0" == self.flex_selenium.get_selection_index("comboBox")
        self.flex_selenium.select_index("comboBox", "2")
        assert "2" == self.flex_selenium.get_selection_index("comboBox")

    def test_get_selected_item_at_index(self):
        # Tested by: self.test_select_by_matching_on_field()
        pass

    def test_get_stepper_value(self):
        # Tested by: self.test_set_stepper()
        pass

    def test_get_tab_labels(self):
        self.flex_selenium.select_index("buttonBar", tab_navigator_view)
        assert "Tab 1,Tab 2,Tab 3" == self.flex_selenium.get_tab_labels("tabNavigator")

    def test_get_text(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        assert "Number of clicks: 0" == self.flex_selenium.get_text("buttonClicks")
        assert "Click" == self.flex_selenium.get_text("clickButton")

    def test_press_key_on_element(self):
        self.flex_selenium.select_index("buttonBar", mouse_view)
        self.flex_selenium.press_enter_on_element("keyboardEventCatcher")
        assert "Key event: keyUp, 13" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")
        self.flex_selenium.press_key_on_element("keyboardEventCatcher", "66")
        assert "Key event: keyUp, 66" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")
        self.flex_selenium.press_space_on_element("keyboardEventCatcher")
        assert "Key event: keyUp, 32" == self.flex_selenium.get_alert_text()
        self.flex_selenium.click_alert("OK")

    def test_select(self):
        self.flex_selenium.select_index("buttonBar", combo_box_view)
        assert "Element = Element1, 1, true" == self.flex_selenium.get_combobox_selected_item("comboBox")
        self.flex_selenium.select("comboBox", "Element = Element2, 2, false")
        assert "Element = Element2, 2, false" == self.flex_selenium.get_combobox_selected_item("comboBox")

    def test_select_by_matching_on_field(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        self.flex_selenium.select_by_matching_on_field("dataGrid", "attribute1", "Element3")
        assert "2" == self.flex_selenium.get_selection_index("dataGrid")
        self.flex_selenium.select_by_matching_on_field("dataGrid", "attribute1", "Element2", True)
        assert "Element = Element3, 3, true" == self.flex_selenium.get_selected_item_at_index("dataGrid", "0")
        assert "Element = Element2, 2, false" == self.flex_selenium.get_selected_item_at_index("dataGrid", "1")

    def test_select_checkbox(self):
        self.flex_selenium.select_index("buttonBar", check_box_view)
        assert self.flex_selenium.is_checkbox_checked("checkBox")
        self.flex_selenium.set_checkbox_value("checkBox", False)
        assert not self.flex_selenium.is_checkbox_checked("checkBox")
        self.flex_selenium.set_checkbox_value("checkBox", True)
        assert self.flex_selenium.is_checkbox_checked("checkBox")

    def test_select_combobox_item_by_label(self):
        self.flex_selenium.select_index("buttonBar", combo_box_view)
        assert "Element = Element1, 1, true" == self.flex_selenium.get_combobox_selected_item("comboBox")
        self.flex_selenium.select_combobox_item_by_label("comboBox", "Element = Element2, 2, false")
        assert "Element = Element2, 2, false" == self.flex_selenium.get_combobox_selected_item("comboBox")
        self.flex_selenium.select_combobox_item_by_label("comboBox", "Element = Element3, 3, true")
        assert "Element = Element3, 3, true" == self.flex_selenium.get_combobox_selected_item("comboBox")

    def test_select_combobox_item_by_label_from_data_grid(self):
        pass

    def test_select_data_grid_index(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "Selected item: " == self.flex_selenium.get_text("selectedGridItem")
        self.flex_selenium.select_data_grid_index("dataGrid", "2")
        self.flex_selenium.click_selected_data_grid_item("dataGrid")
        assert "Selected item: Element = Element3, 3, true" == self.flex_selenium.get_text("selectedGridItem")

    def test_select_index(self):
        assert self.flex_selenium.is_visible("buttonClicks")
        self.flex_selenium.select_index("buttonBar", check_box_view)
        assert self.flex_selenium.is_visible("checkBox")
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert self.flex_selenium.is_visible("dataGrid")
        self.flex_selenium.select_index("dataGrid", "1")
        self.flex_selenium.select_index("dataGrid", "2", True)
        assert "Element = Element2, 2, false" == self.flex_selenium.get_selected_item_at_index("dataGrid", "0")
        assert "Element = Element3, 3, true" == self.flex_selenium.get_selected_item_at_index("dataGrid", "1")

    def test_select_radiobutton(self):
        # Tested by: self.test_is_radiobutton_checked()
        pass

    def test_select_tree_item(self):
        self.flex_selenium.select_index("buttonBar", tree_view)
        self.flex_selenium.select_tree_item("tree", "node", "Node1")
        assert "Selected item: Node1" == self.flex_selenium.get_text("selectedTreeItem")
        self.flex_selenium.select_tree_item("tree", "node", "Node1Item1")
        assert "Selected item: Node1Item1" == self.flex_selenium.get_text("selectedTreeItem")
        self.flex_selenium.select_tree_item("tree", "node", "Node1Item3SubItem2")
        assert "Selected item: Node1Item3SubItem2" == self.flex_selenium.get_text("selectedTreeItem")

    def test_set_data_grid_cell_value(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        self.flex_selenium.set_property("dataGrid", "editable", "true")
        self.flex_selenium.set_data_grid_cell_value("dataGrid", "0", "0", "test")
        self.flex_selenium.set_data_grid_cell_value("dataGrid", "0", "1", "123")
        assert "test" == self.flex_selenium.get_data_grid_cell_value("dataGrid", "0", "0")
        assert "123" == self.flex_selenium.get_data_grid_cell_value("dataGrid", "0", "1")

    def test_set_data_grid_checkbox_value(self):
        self.flex_selenium.select_index("buttonBar", data_grid_view)
        assert "true" == self.flex_selenium.get_data_grid_cell_value("dataGrid", "0", "2")
        self.flex_selenium.set_data_grid_checkbox_value("dataGrid", "0", "2", False)
        assert "false" == self.flex_selenium.get_data_grid_cell_value("dataGrid", "0", "2")

    def test_set_focus(self):
        self.flex_selenium.select_index("buttonBar", buttons_view)
        assert not self.flex_selenium.is_visible("invisibleButton")
        self.flex_selenium.set_focus("invisibleButton")
        assert self.flex_selenium.is_visible("invisibleButton")
        self.flex_selenium.set_focus("clickButton")
        assert not self.flex_selenium.is_visible("invisibleButton")

    def test_set_property(self):
        assert "true" == self.flex_selenium.get_property("buttonBar", "visible")
        self.flex_selenium.set_property("buttonBar", "visible", "false")
        assert "false" == self.flex_selenium.get_property("buttonBar", "visible")

    def test_set_stepper(self):
        self.flex_selenium.select_index("buttonBar", stepper_view)
        assert "0" == self.flex_selenium.get_stepper_value("stepper")
        self.flex_selenium.set_stepper_value("stepper", "10")
        assert "10" == self.flex_selenium.get_stepper_value("stepper")
        self.flex_selenium.set_stepper_value("stepper", "30")
        assert "30" == self.flex_selenium.get_stepper_value("stepper")

    def test_wait_for_element_to_exist(self):
        self.selenium.go_to(application_url)
        self.flex_selenium.wait_for_element_to_exist("buttonBar", 10)

    def test_wait_for_element_to_be_visible(self):
        self.selenium.go_to(application_url)
        self.flex_selenium.wait_for_element_to_be_visible("buttonBar", 10)
