import time
from selenium.common.exceptions import WebDriverException


class SeleniumFlexAPICommands(object):
    def __init__(self, web_driver, flash_object_id, sleep_after_call=0, sleep_after_fail=0.1, number_of_retries=30):
        self.web_driver = web_driver
        self.flash_object_id = flash_object_id
        self.sleep_after_call = sleep_after_call
        self.sleep_after_fail = sleep_after_fail
        self.number_of_retries = number_of_retries

    def set_flash_app(self, flash_app):
        self.flash_object_id = flash_app

    def set_sleep_after_call(self, sleep_after_call):
        self.sleep_after_call = sleep_after_call

    def set_sleep_after_fail(self, sleep_after_fail):
        self.sleep_after_fail = sleep_after_fail

    def set_number_of_retries(self, number_of_retries):
        self.number_of_retries = number_of_retries

    def call(self, function_name, *function_parameters):
        if self.web_driver is None:
            raise AssertionError("WebDriver is not initialized!")
        params = ""
        for param in function_parameters:
            params += "'" + str(param) + "',"
        script = "return document.{}.{}({});".format(self.flash_object_id, function_name, params[:-1])
        tries = self.number_of_retries
        while True:
            try:
                result = self.web_driver.execute_script(script)
                break
            except WebDriverException as e:
                if tries < 1:
                    raise e
                tries -= 1
                time.sleep(self.sleep_after_fail)
        if self.sleep_after_call > 0:
            time.sleep(self.sleep_after_call)
        return result

    def do_flex_add_select_index(self, element_id, index):
        return self.call("doFlexAddSelectIndex", element_id, index)

    def do_flex_add_select_matching_on_field(self, element_id, underlying_field, underlying_value):
        return self.call("doFlexAddSelectMatchingOnField", element_id, underlying_field, underlying_value)

    def do_flex_alert_response(self, response):
        return self.call("doFlexAlertResponse", response, response)

    def do_flex_checkbox(self, element_id, value):
        return self.call("doFlexCheckBox", element_id, value)

    def do_flex_click(self, element_id, button_label):
        return self.call("doFlexClick", element_id, button_label)

    def do_flex_click_data_grid_item(self):
        raise NotImplementedError("The function call 'doFlexClickDataGridItem' is not implemented. "
                                  "Use 'rawFlexClickDataGridItem' instead.")

    def do_flex_click_data_grid_ui_component(self, element_id, row_index, column_index, component_number_in_cell=-1):
        return self.call("doFlexClickDataGridUIComponent", element_id,
                         "{},{},{}".format(row_index, column_index, component_number_in_cell))

    def do_flex_click_menu_bar_ui_component(self, element_id, menu_bar_item_index, menu_item_row_index,
                                            menu_item_column_index, component_index_in_cell=0):
        raise NotImplementedError("The function call 'doFlexClickMenuBarUIComponent' is not implemented. "
                                  "Use 'rawFlexClickMenuBarUIComponent' instead.")

    def do_flex_data_grid_checkbox(self, element_id, row_index, column_index, checkbox_state):
        return self.call("doFlexDataGridCheckBox", element_id,
                         "{},{},{}".format(row_index, column_index, checkbox_state))

    def do_flex_data_grid_click_column_header(self, element_id, column_index):
        return self.call("doFlexDataGridClickColumnHeader", element_id, column_index)

    def do_flex_data_grid_date(self, element_id, row_index, column_index, date):
        return self.call("doFlexDataGridDate", element_id, "{},{},{}".format(row_index, column_index, date))

    def do_flex_data_grid_select_combo_by_label(self, element_id, row_index, column_index, label):
        return self.call("doFlexDataGridSelectComboByLabel", element_id,
                         "{},{},{}".format(row_index, column_index, label))

    def do_flex_date(self, element_id, date_as_text):
        return self.call("doFlexDate", element_id, date_as_text)

    def do_flex_double_click(self, element_id):
        return self.call("doFlexDoubleClick", element_id, '')

    def do_flex_double_click_data_grid_ui_component(self, element_id, row_index, column_index):
        return self.call("doFlexDoubleClickDataGridUIComponent", element_id, '{},{}'.format(row_index, column_index))

    def do_flex_drag_to(self, element_id, x, y):
        return self.call("doFlexDragTo", element_id, '{},{}'.format(x, y))

    def do_flex_key_down(self, element_id, key_code):
        return self.call("doFlexKeyDown", element_id, key_code)

    def do_flex_key_up(self, element_id, key_code):
        return self.call("doFlexKeyUp", element_id, key_code)

    def do_flex_mouse_down(self, element_id):
        return self.call("doFlexMouseDown", element_id, '')

    def do_flex_mouse_event(self, element_id, event):
        return self.call("doFlexMouseEvent", element_id, event)

    def do_flex_mouse_move(self, element_id, x, y):
        return self.call("doFlexMouseMove", element_id, '{},{}'.format(x, y))

    def do_flex_mouse_over(self, element_id):
        return self.call("doFlexMouseOver", element_id, '')

    def do_flex_mouse_roll_out(self, element_id):
        return self.call("doFlexMouseRollOut", element_id, '')

    def do_flex_mouse_roll_over(self, element_id):
        return self.call("doFlexMouseRollOver", element_id, '')

    def do_flex_mouse_up(self, element_id):
        return self.call("doFlexMouseUp", element_id, '')

    def do_flex_notify(self, message):
        return self.call("doFlexNotify", message, '')

    def do_flex_property(self, element_id, flex_property, value):
        return self.call("doFlexProperty", "{}\.{}".format(element_id, flex_property), value)

    def do_flex_radio_button(self, element_id, state='true'):
        return self.call("doFlexRadioButton", element_id, state)

    def do_flex_refresh_id_tool_tips(self):
        return self.call("doFlexRefreshIDToolTips", '', '')

    def do_flex_right_mouse_down(self, element_id):
        return self.call("doFlexRightMouseDown", element_id, '')

    def do_flex_select(self, element_id, item_to_select):
        return self.call("doFlexSelect", element_id, item_to_select)

    def do_flex_select_matching_on_field(self, element_id, underlying_field, underlying_value):
        raise NotImplementedError("The function call 'doFlexSelectMatchingOnField' is not implemented. "
                                  "Use 'rawFlexSelectMatchingOnField' instead.")

    def do_flex_select_combo_by_label(self, element_id, item_to_select):
        return self.call("doFlexSelectComboByLabel", element_id, item_to_select)

    def do_flex_select_index(self, element_id, index_to_select):
        return self.call("doFlexSelectIndex", element_id, index_to_select)

    def do_flex_set_data_grid_cell(self, element_id, row_index, column_index, value):
        raise NotImplementedError("The function call 'doFlexSetDataGridCell' is not implemented. "
                                  "Use 'rawFlexSetDataGridCell' instead.")

    def do_flex_set_focus(self, element_id):
        return self.call("doFlexSetFocus", element_id)

    def do_flex_stepper(self, element_id, number):
        return self.call("doFlexStepper", element_id, number)

    def do_flex_type(self, element_id, text):
        return self.call("doFlexType", element_id, text)

    def do_flex_type_append(self, element_id, text):
        return self.call("doFlexTypeAppend", element_id, text)

    def do_flex_wait_for_element(self, element_id, timeout):
        return self.call("doFlexWaitForElement", element_id, timeout)

    def do_flex_wait_for_element_visible(self, element_id, timeout):
        return self.call("doFlexWaitForElementVisible", element_id, timeout)

    def get_flex_alert_present(self):
        return self.call("getFlexAlertPresent", '', '')

    def get_flex_alert_text(self):
        return self.call("getFlexAlertText", '', '')

    def get_flex_alert_text_present(self):
        raise NotImplementedError("The function call 'getFlexAlertTextPresent' is not implemented.")

    def get_flex_checkbox_checked(self, element_id):
        return self.call("getFlexCheckBoxChecked", element_id, '')

    def get_flex_combo_contains_label(self, element_id, label):
        raise NotImplementedError("The function call 'getFlexComboContainsLabel' is not implemented. "
                                  "Use 'rawFlexComboContainsLabel' instead.")

    def get_flex_component_info(self, element_id):
        return self.call("getFlexComponentInfo", element_id)

    def get_flex_data_grid_cell(self, element_id, row_index, column_index):
        raise NotImplementedError("The function call 'getFlexDataGridCell' is not implemented. "
                                  "Use 'rawFlexDataGridCell' instead.")

    def get_flex_data_grid_cell_text(self):
        raise NotImplementedError("The function call 'getFlexDataGridCellText' is not implemented. "
                                  "Use 'rawFlexDataGridCellText' instead.")

    def get_flex_data_grid_checkbox_checked(self, element_id, row_index, column_index):
        return self.call("getFlexDataGridCheckBoxChecked", "{},{},{}".format(element_id, row_index, column_index), "")

    def get_flex_data_grid_field_label_for_grid_row(self, element_id, field, row):
        raise NotImplementedError("The function call 'getFlexDataGridFieldLabelForGridRow' is not implemented. "
                                  "Use 'rawFlexDataGridFieldLabelForGridRow' instead.")

    def get_flex_data_grid_field_value_for_grid_row(self, element_id, field, row_index):
        raise NotImplementedError("The function call 'getFlexDataGridFieldValueForGridRow' is not implemented. "
                                  "Use 'rawFlexDataGridFieldValueForGridRow' instead.")

    def get_flex_data_grid_row_count(self, element_id):
        return self.call("getFlexDataGridRowCount", element_id, '')

    def get_flex_data_grid_row_index_for_field_label(self, element_id, field, label):
        raise NotImplementedError("The function call 'getFlexDataGridRowIndexForFieldLabel' is not implemented. "
                                  "Use 'rawFlexDataGridRowIndexForFieldLabel' instead.")

    def get_flex_data_grid_row_index_for_field_value(self, element_id, field, value):
        raise NotImplementedError("The function call 'getFlexDataGridRowIndexForFieldValue' is not implemented. "
                                  "Use 'rawFlexDataGridRowIndexForFieldValue' instead.")

    def get_flex_data_grid_ui_component_label(self):
        raise NotImplementedError("The function call 'getFlexDataGridUIComponentLabel' is not implemented. "
                                  "Use 'rawFlexDataGridUIComponentLabel' instead.")

    def get_flex_date(self, element_id):
        return self.call("getFlexDate", element_id, '')

    def get_flex_enabled(self, element_id):
        return self.call("getFlexEnabled", element_id, '')

    def get_flex_error_string(self, element_id):
        return self.call("getFlexErrorString", element_id, '')

    def get_flex_exists(self, element_id):
        return self.call("getFlexExists", element_id, '')

    def get_flex_global_position(self, element_id):
        raise NotImplementedError("The function call 'getFlexGlobalPosition' is not implemented. "
                                  "Use 'rawFlexGlobalPosition' instead.")

    def get_flex_num_selected_items(self, element_id):
        return self.call("getFlexNumSelectedItems", element_id)

    def get_flex_numeric(self):
        raise NotImplementedError("The function call 'getFlexNumeric' is not implemented.")

    def get_flex_parse_int(self):
        raise NotImplementedError("The function call 'getFlexParseInt' is not implemented.")

    def get_flex_property(self, element_id, flex_property):
        raise NotImplementedError("The function call 'getFlexProperty' is not implemented. "
                                  "Use 'rawFlexProperty' instead.")

    def get_flex_radio_button(self, element_id):
        return self.call("getFlexRadioButton", element_id, '')

    def get_flex_selected_item_at_index(self, element_id, index):
        return self.call("getFlexSelectedItemAtIndex", element_id, index)

    def get_flex_selection(self, element_id):
        return self.call("getFlexSelection", element_id, '')

    def get_flex_selection_index(self, element_id):
        return self.call("getFlexSelectionIndex", element_id, '')

    def get_flex_stepper(self, element_id):
        return self.call("getFlexStepper", element_id, '')

    def get_flex_text(self, element_id):
        return self.call("getFlexText", element_id, '')

    def get_flex_text_present(self, element_id, text):
        return self.call("getFlexTextPresent", element_id, text)

    def get_flex_visible(self, element_id):
        return self.call("getFlexVisible", element_id, '')

    def raw_flex_click_data_grid_item(self, element_id, column_index, item_text):
        return self.call("rawFlexClickDataGridItem", element_id, column_index, item_text)

    def raw_flex_click_menu_bar_ui_component(self, element_id, menu_bar_item_index, menu_item_row_index,
                                             menu_item_column_index, component_index_in_cell=0):
        return self.call("rawFlexClickMenuBarUIComponent", element_id, menu_bar_item_index, menu_item_row_index,
                         menu_item_column_index, component_index_in_cell)

    def raw_flex_combo_contains_label(self, element_id, label):
        return self.call("rawFlexComboContainsLabel", element_id, label)

    def raw_flex_data_grid_cell(self, element_id, row_index, column_index):
        return self.call("rawFlexDataGridCell", element_id, row_index, column_index)

    def raw_flex_data_grid_cell_text(self, element_id, row_index, column_index):
        return self.call("rawFlexDataGridCellText", element_id, row_index, column_index)

    def raw_flex_data_grid_field_label_for_grid_row(self, element_id, field, row):
        return self.call("rawFlexDataGridFieldLabelForGridRow", element_id, field, row)

    def raw_flex_data_grid_field_value_for_grid_row(self, element_id, field, row_index):
        return self.call("rawFlexDataGridFieldValueForGridRow", element_id, field, row_index)

    def raw_flex_data_grid_row_index_for_field_value(self, element_id, field, value):
        return self.call("rawFlexDataGridRowIndexForFieldValue", element_id, field, value)

    def raw_flex_data_grid_row_index_for_field_label(self, element_id, field, label):
        return self.call("rawFlexDataGridRowIndexForFieldLabel", element_id, field, label)

    def raw_flex_data_grid_ui_component_label(self, element_id, row_index, column_index, component_index_in_cell=0):
        return self.call("rawFlexDataGridUIComponentLabel", element_id, row_index, column_index,
                         component_index_in_cell)

    def raw_flex_global_position(self, element_id):
        return self.call("rawFlexGlobalPosition", element_id, 'false')

    def raw_flex_properties(self, element_id, *properties):
        return self.call("rawFlexProperties", element_id, ','.join(properties))

    def raw_flex_property(self, element_id, flex_property):
        return self.call("rawFlexProperty", element_id, flex_property)

    def raw_flex_select_matching_on_field(self, element_id, underlying_field, underlying_value):
        return self.call("rawFlexSelectMatchingOnField", element_id, underlying_field, underlying_value)

    def raw_flex_set_data_grid_cell(self, element_id, row_index, column_index, value):
        return self.call("rawFlexSetDataGridCell", element_id, row_index, column_index, value)
