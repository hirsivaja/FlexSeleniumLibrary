import time
from selenium.common.exceptions import WebDriverException
from robot.api import logger


class SeleniumFlexAPICommands(object):
    def __init__(self, ctx, flash_object_id, api_version=28, sleep_after_call=0, sleep_after_fail=0.1,
                 number_of_retries=30, ensure_timeout=30):
        self.ctx = ctx
        self.flash_object_id = flash_object_id
        self.api_version = api_version
        self.sleep_after_call = sleep_after_call
        self.sleep_after_fail = sleep_after_fail
        self.number_of_retries = number_of_retries
        self.ensure_timeout = ensure_timeout

    def set_flash_app(self, flash_app):
        self.flash_object_id = flash_app

    def set_api_version(self, api_version):
        self.api_version = api_version

    def set_sleep_after_call(self, sleep_after_call):
        self.sleep_after_call = sleep_after_call

    def set_sleep_after_fail(self, sleep_after_fail):
        self.sleep_after_fail = sleep_after_fail

    def set_number_of_retries(self, number_of_retries):
        self.number_of_retries = number_of_retries

    def set_ensure_timeout(self, ensure_timeout):
        self.ensure_timeout = ensure_timeout

    def call(self, function_name, *function_parameters):
        params = ""
        for param in function_parameters:
            params += "'" + str(param) + "',"
        script = "return document.{}.{}({});".format(self.flash_object_id, function_name, params[:-1])
        tries = self.number_of_retries
        logger.debug("JavaScript to execute: '{}'".format(script))
        while True:
            try:
                result = self.ctx.driver.execute_script(script)
                break
            except WebDriverException as e:
                if tries < 1:
                    raise e
                tries -= 1
                time.sleep(self.sleep_after_fail)
        if self.sleep_after_call > 0:
            time.sleep(self.sleep_after_call)
        return result

    def ensure_result(self, expected_result, function, *function_parameters):
        tries = self.ensure_timeout / self.sleep_after_fail
        while True:
            result = function(*function_parameters)
            if result == expected_result:
                return result
            if tries < 1:
                raise AssertionError("Could not ensure result '{}' for function '{}'. Last result was '{}'".format(
                    expected_result, function, result))
            tries -= 1
            time.sleep(self.sleep_after_fail)

    def is_function_defined(self, function_name):
        script = "return document.{}.{};".format(self.flash_object_id, function_name)
        result = self.ctx.driver.execute_script(script)
        if result is None:
            return False
        if "{}()".format(function_name) in result:
            return True
        if isinstance(result, (dict, list)) and len(result) == 0:  # firefox/chrome return empty dict, IE return
            return True                                            # empty list via latest webdriver 20170312.
        raise AssertionError("Unknown result for function existence: {}".format(result))

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

    def do_flex_click_data_grid_item(self, element_id, column_index, item_text):
        return self.raw_flex_click_data_grid_item(element_id, column_index, item_text)

    def do_flex_click_data_grid_ui_component(self, element_id, row_index, column_index, component_number_in_cell=-1):
        if self.api_version < 28:
            return self.call("doFlexClickDataGridUIComponent", element_id, row_index, column_index,
                             component_number_in_cell)
        return self.call("doFlexClickDataGridUIComponent", element_id,
                         "{},{},{}".format(row_index, column_index, component_number_in_cell))

    def do_flex_click_menu_bar_ui_component(self, element_id, menu_bar_item_index, menu_item_row_index,
                                            menu_item_column_index, component_index_in_cell=0):
        return self.raw_flex_click_menu_bar_ui_component(element_id, menu_bar_item_index, menu_item_row_index,
                                                         menu_item_column_index, component_index_in_cell)

    def do_flex_click_selected_data_grid_item(self, element_id):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'doFlexClickSelectedDataGridItem' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("doFlexClickSelectedDataGridItem", element_id, '')

    def do_flex_data_grid_checkbox(self, element_id, row_index, column_index, checkbox_state):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'doFlexDataGridCheckBox' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("doFlexDataGridCheckBox", element_id,
                         "{},{},{}".format(row_index, column_index, checkbox_state))

    def do_flex_combo_send_event(self, element_id, event):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'doFlexComboSendEvent' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("doFlexComboSendEvent", element_id, event)

    def do_flex_data_grid_click_column_header(self, element_id, column_index):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'doFlexDataGridClickColumnHeader' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        elif self.api_version < 28:
            return self.call("flexDataGridClickHeader", element_id, "{},DESC".format(column_index))
        return self.call("doFlexDataGridClickColumnHeader", element_id, column_index)

    def do_flex_data_grid_date(self, element_id, row_index, column_index, date):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'doFlexDataGridDate' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("doFlexDataGridDate", element_id, "{},{},{}".format(row_index, column_index, date))

    def do_flex_data_grid_expand_all(self, element_id):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'doFlexDataGridExpandAll' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        elif self.api_version < 28:
            return self.call("flexDataGridExpandAll", element_id)
        return self.call("doFlexDataGridExpandAll", element_id)

    def do_flex_data_grid_search_value(self, element_id, item_name, item_property, property_value):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'doFlexDataGridSearchValue' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        elif self.api_version < 28:
            return self.call("flexDataGridSearchValue", element_id, "{},{},{}".format(item_name, item_property,
                                                                                    property_value))
        return self.call("doFlexDataGridSearchValue", element_id, "{},{},{}".format(item_name, item_property,
                                                                                    property_value))

    def do_flex_data_grid_select_combo_by_label(self, element_id, row_index, column_index, label):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'doFlexDataGridSelectComboByLabel' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("doFlexDataGridSelectComboByLabel", element_id,
                         "{},{},{}".format(row_index, column_index, label))

    def do_flex_date(self, element_id, date_as_text):
        return self.call("doFlexDate", element_id, date_as_text)

    def do_flex_double_click(self, element_id):
        return self.call("doFlexDoubleClick", element_id, '')

    def do_flex_double_click_data_grid_ui_component(self, element_id, row_index, column_index):
        if self.api_version < 28:
            raise NotImplementedError("The function call 'doFlexDoubleClickDataGridUIComponent' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("doFlexDoubleClickDataGridUIComponent", element_id, '{},{}'.format(row_index, column_index))

    def do_flex_drag_to(self, element_id, x, y):
        return self.call("doFlexDragTo", element_id, '{},{}'.format(x, y))

    def do_flex_enter_key(self, element_id):
        if self.api_version > 27:
            raise NotImplementedError("The function call 'doFlexEnterKey' is not implemented. "
                                      "The call was replaced with 'doFlexKeyDown' and 'doFlexKeyUp'.")
        return self.call("doFlexEnterKey", element_id, '')

    def do_flex_key_down(self, element_id, key_code):
        if self.api_version < 28:
            raise NotImplementedError("The function call 'doFlexKeyDown' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("doFlexKeyDown", element_id, key_code)

    def do_flex_key_up(self, element_id, key_code):
        if self.api_version < 28:
            raise NotImplementedError("The function call 'doFlexKeyUp' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
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
        if self.api_version < 28:
            raise NotImplementedError("The function call 'doFlexProperty' is not working. "
                                      "Update to newer version of Selenium Flex API.")
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
        return self.raw_flex_select_matching_on_field(element_id, underlying_field, underlying_value)

    def do_flex_select_combo_by_label(self, element_id, item_to_select):
        return self.call("doFlexSelectComboByLabel", element_id, item_to_select)

    def do_flex_select_data_grid_index(self, element_id, index_to_select):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'doFlexSelectDataGridIndex' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("doFlexSelectDataGridIndex", element_id, index_to_select)

    def do_flex_select_index(self, element_id, index_to_select):
        return self.call("doFlexSelectIndex", element_id, index_to_select)

    def do_flex_select_tree_item(self, element_id, property_name, *search_words):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'doFlexSelectTreeItem' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("doFlexSelectTreeItem", element_id, "{}|,|{}".format(property_name, "#,#".join(search_words)))

    def do_flex_set_data_grid_cell(self, element_id, row_index, column_index, value):
        return self.raw_flex_set_data_grid_cell(element_id, row_index, column_index, value)

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

    def get_flex_api_version(self):
        return self.call("getFlexAPIVersion")

    def get_flex_checkbox_checked(self, element_id):
        if self.api_version < 27:
            pass
        elif self.api_version < 28:
            return self.call("getFlexCheckBoxChecked", element_id)
        return self.call("getFlexCheckBoxChecked", element_id, '')

    def get_flex_children(self, element_id, full_path, visible):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'getFlexChildren' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("getFlexChildren", element_id, full_path, visible)

    def get_flex_combo_contains_label(self, element_id, label):
        return self.raw_flex_combo_contains_label(element_id, label)

    def get_flex_combo_values(self, element_id):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'getFlexComboValues' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        elif self.api_version < 28:
            return self.call("doFlexGetComboValues", element_id)
        return self.call("getFlexComboValues", element_id)

    def get_flex_component_info(self, element_id):
        return self.call("getFlexComponentInfo", element_id)

    def get_flex_data_grid_cell(self, element_id, row_index, column_index):
        return self.raw_flex_data_grid_cell(element_id, row_index, column_index)

    def get_flex_data_grid_cell_text(self, element_id, row_index, column_index):
        return self.raw_flex_data_grid_cell_text(element_id, row_index, column_index)

    def get_flex_data_grid_checkbox_checked(self, element_id, row_index, column_index):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'getFlexDataGridCheckBoxChecked' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("getFlexDataGridCheckBoxChecked", "{},{},{}".format(element_id, row_index, column_index), "")

    def get_flex_data_grid_col_count(self, element_id, only_visible):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'getFlexDataGridColCount' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("getFlexDataGridColCount", element_id, "true" if only_visible else "false")

    def get_flex_data_grid_col_data_fields(self, element_id, only_visible):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'getFlexDataGridColDataFields' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("getFlexDataGridColDataFields", element_id, "true" if only_visible else "false")

    def get_flex_data_grid_field_label_for_grid_row(self, element_id, field, row):
        return self.raw_flex_data_grid_field_label_for_grid_row(element_id, field, row)

    def get_flex_data_grid_field_value_for_grid_row(self, element_id, field, row_index):
        return self.raw_flex_data_grid_field_value_for_grid_row(element_id, field, row_index)

    def get_flex_data_grid_row_count(self, element_id):
        if self.api_version < 28:
            return self.call("getFlexDataGridRowCount", element_id)
        return self.call("getFlexDataGridRowCount", element_id, '')

    def get_flex_data_grid_row_index_for_field_label(self, element_id, field, label):
        return self.raw_flex_data_grid_row_index_for_field_label(element_id, field, label)

    def get_flex_data_grid_row_index_for_field_value(self, element_id, field, value):
        return self.raw_flex_data_grid_row_index_for_field_value(element_id, field, value)

    def get_flex_data_grid_ui_component_label(self, element_id, row_index, column_index, component_index_in_cell):
        return self.raw_flex_data_grid_ui_component_label(element_id, row_index, column_index, component_index_in_cell)

    def get_flex_data_grid_values(self, element_id, only_visible):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'getFlexDataGridValues' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        elif self.api_version < 28:
            return self.call("getDataGridValues", element_id, "true" if only_visible else "false")
        return self.call("getFlexDataGridValues", element_id, "true" if only_visible else "false")

    def get_flex_date(self, element_id):
        return self.call("getFlexDate", element_id, '')

    def get_flex_enabled(self, element_id):
        return self.call("getFlexEnabled", element_id, '')

    def get_flex_error_string(self, element_id):
        return self.call("getFlexErrorString", element_id, '')

    def get_flex_exists(self, element_id):
        return self.call("getFlexExists", element_id, '')

    def get_flex_global_position(self, element_id):
        return self.raw_flex_global_position(element_id)

    def get_flex_num_selected_items(self, element_id):
        return self.call("getFlexNumSelectedItems", element_id)

    def get_flex_numeric(self):
        raise NotImplementedError("The function call 'getFlexNumeric' is not implemented.")

    def get_flex_parse_int(self):
        raise NotImplementedError("The function call 'getFlexParseInt' is not implemented.")

    def get_flex_property(self, element_id, flex_property):
        return self.raw_flex_property(element_id, flex_property)

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

    def get_flex_tab_labels(self, element_id):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'getFlexTabLabels' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("getFlexTabLabels", element_id)

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

    def raw_flex_data_grid_field_all_values(self, element_id, column_index, extra_data):
        if self.api_version < 28:
            raise NotImplementedError("The function call 'rawFlexDataGridFieldAllValues' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("rawFlexDataGridFieldAllValues", element_id, column_index, "true" if extra_data else "false")

    def raw_flex_data_grid_field_values_for_column(self, element_id, column_index):
        if self.api_version < 27:
            raise NotImplementedError("The function call 'rawFlexDataGridFieldValuesForColumn' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("rawFlexDataGridFieldValuesForColumn", element_id, column_index)

    def raw_flex_global_position(self, element_id):
        return self.call("rawFlexGlobalPosition", element_id, 'false')

    def raw_flex_properties(self, element_id, *properties):
        if self.api_version < 28:
            raise NotImplementedError("The function call 'rawFlexProperties' is not implemented. "
                                      "Update to newer version of Selenium Flex API.")
        return self.call("rawFlexProperties", element_id, ','.join(properties))

    def raw_flex_property(self, element_id, flex_property):
        return self.call("rawFlexProperty", element_id, flex_property)

    def raw_flex_select_matching_on_field(self, element_id, underlying_field, underlying_value):
        return self.call("rawFlexSelectMatchingOnField", element_id, underlying_field, underlying_value)

    def raw_flex_set_data_grid_cell(self, element_id, row_index, column_index, value):
        return self.call("rawFlexSetDataGridCell", element_id, row_index, column_index, value)
