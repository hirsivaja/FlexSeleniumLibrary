from ..sfapicommands import SeleniumFlexAPICommands


class FlexSeleniumKeywords(object):
    """
    The keywords that manipulate the Flex application
    """

    def __init__(self, web_driver=None, flash_object_id=None, api_version=28, sleep_after_call=0,
                 sleep_after_fail=0.1, number_of_retries=30):
        """Flex keywords

        Args:
            web_driver: WebDriver instance to use sending the calls to Flex application
            flash_object_id: the name of the tested Flex application
            sleep_after_call: wait time after each call
            sleep_after_fail: wait time after each fail before trying again
            number_of_retries: number of times to retry the command
        """
        self.sf_api_commands = SeleniumFlexAPICommands(web_driver, flash_object_id, api_version, sleep_after_call,
                                                       sleep_after_fail, number_of_retries)

    def add_notification(self, message):
        return self.sf_api_commands.do_flex_notify(message)

    def click(self, element_id, button_label=''):
        """Click Flex element.

        Args:
            element_id: the value of the elements id property.
            button_label: if element is a ButtonBar, click item with this label
        Returns:
            true if success, error text otherwise
        """
        return self.sf_api_commands.do_flex_click(element_id, button_label)

    def click_alert(self, response):
        """Closes first alert by clicking specified button.

        Args:
            response: the text of the button to click. OK, cancel, NO, ...
        Returns:
            true if success, error text otherwise
        """
        return self.sf_api_commands.do_flex_alert_response(response)

    def click_data_grid_column_header(self, element_id, column_index):
        self.sf_api_commands.do_flex_data_grid_click_column_header(element_id, column_index)

    def click_data_grid_item_by_label(self, element_id, column_index, label):
        self.sf_api_commands.raw_flex_click_data_grid_item(element_id, column_index, label)

    def click_data_grid_ui_component(self, element_id, row_index, column_index, component_number_in_cell=-1):
        self.sf_api_commands.do_flex_click_data_grid_ui_component(element_id, row_index, column_index,
                                                                  component_number_in_cell)

    def click_menu_bar_component(self, element_id, menu_bar_item_index,
                                 menu_item_row_index, menu_item_column_index, component_index_in_cell=0):
        self.sf_api_commands.raw_flex_click_menu_bar_ui_component(element_id,
                                                                  menu_bar_item_index, menu_item_row_index,
                                                                  menu_item_column_index, component_index_in_cell)

    def create_mouse_down_event(self, element_id):
        return self.sf_api_commands.do_flex_mouse_down(element_id)

    def create_mouse_event(self, element_id, event):
        return self.sf_api_commands.do_flex_mouse_event(element_id, event)

    def create_mouse_move_event(self, element_id, x, y):
        return self.sf_api_commands.do_flex_mouse_move(element_id, x, y)

    def create_mouse_over_event(self, element_id):
        return self.sf_api_commands.do_flex_mouse_over(element_id)

    def create_mouse_roll_out_event(self, element_id):
        return self.sf_api_commands.do_flex_mouse_roll_out(element_id)

    def create_mouse_roll_over_event(self, element_id):
        return self.sf_api_commands.do_flex_mouse_roll_over(element_id)

    def create_mouse_up_event(self, element_id):
        return self.sf_api_commands.do_flex_mouse_up(element_id)

    def double_click(self, element_id):
        return self.sf_api_commands.do_flex_double_click(element_id)

    def double_click_data_grid_component(self, element_id, row_index, column_index):
        return self.sf_api_commands.do_flex_double_click_data_grid_ui_component(element_id, row_index, column_index)

    def drag_element_to(self, element_id, x, y):
        return self.sf_api_commands.do_flex_drag_to(element_id, x, y)

    def enter_date(self, element_id, date_as_text):
        """Enters a date to a DateField

        Args:
            element_id: the value of the elements id property.
            date_as_text: the date as text. For example: 31/12/2015
        Returns:
            true if success, error text otherwise
        """
        return self.sf_api_commands.do_flex_date(element_id, date_as_text)

    def enter_date_to_data_grid_cell(self, element_id, row_index, column_index, date):
        return self.sf_api_commands.do_flex_data_grid_date(element_id, row_index, column_index, date)

    def enter_text(self, element_id, text, append=False):
        """Enters text to a compatible element such as TextInput

        Args:
            element_id: the value of the elements id property.
            text: the text to enter
            append: if set to true will append to existing text
        Returns:
            true if success, error text otherwise
        """
        if append:
            return self.sf_api_commands.do_flex_type_append(element_id, text)
        else:
            return self.sf_api_commands.do_flex_type(element_id, text)

    def exists(self, element_id):
        """Check if Flex element exists.

        Args:
            element_id: the value of the elements id property.
        Returns:
            existence of the element as boolean
        Raises:
            AssertionError: for other values than True and False
        """
        exists = self.sf_api_commands.get_flex_exists(element_id)
        if exists != 'true' and exists != 'false':
            raise AssertionError("Existence check of '{}' returned an unexpected value: {}"
                                 .format(element_id, exists))
        return exists == 'true'

    def is_alert_visible(self):
        """Check if Flex alert is visible.

        Args:

        Returns:
            existence of alerts as boolean
        Raises:
            AssertionError: for other values than True and False
        """
        visibility = self.sf_api_commands.get_flex_alert_present()
        if visibility != 'true' and visibility != 'false':
            raise AssertionError("The check for alert visibility returned an unexpected value: {}"
                                 .format(visibility))
        return visibility == 'true'

    def is_checkbox_checked(self, element_id):
        """Check if checkbox element is checked.

        Args:
            element_id: the value of the elements id property.
        Returns:
            is the element checked as boolean
        Raises:
            AssertionError: for other values than True and False
        """
        checked = self.sf_api_commands.get_flex_checkbox_checked(element_id)
        if checked != 'true' and checked != 'false':
            raise AssertionError("Checkbox state of '{}' returned an unexpected value: {}"
                                 .format(element_id, checked))
        return checked == 'true'

    def is_checkbox_in_data_grid_checked(self, element_id, row_index, column_index):
        """Check if checkbox element located in a data grid is checked.

        Args:
            element_id: the value of the elements id property.
            row_index: row where the element is found
            column_index: column where the element is found
        Returns:
            is the element checked as boolean
        Raises:
            AssertionError: for other values than True and False
        """
        checked = self.sf_api_commands.get_flex_data_grid_checkbox_checked(element_id, row_index, column_index)
        if checked != 'true' and checked != 'false':
            raise AssertionError("Checkbox state of '{}[{}][{}]' returned an unexpected value: {}"
                                 .format(element_id, row_index, column_index, checked))
        return checked == 'true'

    def is_enabled(self, element_id):
        """Check if Flex element is enabled.

        Args:
            element_id: the value of the elements id property.
        Returns:
            enabled state of the element as boolean
        Raises:
            AssertionError: for other values than True and False
        """
        enabled = self.sf_api_commands.get_flex_enabled(element_id)
        if enabled != 'true' and enabled != 'false':
            raise AssertionError("Enabled state of '{}' returned an unexpected value: {}"
                                 .format(element_id, enabled))
        return enabled == 'true'

    def is_label_in_combo_data(self, element_id, label):
        """Check if combobox contains a label.

        Args:
            element_id: the value of the elements id property.
            label: the label to look for
        Returns:
            is the label in the combobox as boolean
        Raises:
            AssertionError: for other values than True and False
        """
        enabled = self.sf_api_commands.raw_flex_combo_contains_label(element_id, label)
        if enabled != 'true' and enabled != 'false':
            raise AssertionError("Presence check of label '{}' in element {} returned an unexpected value: {}"
                                 .format(label, element_id, enabled))
        return enabled == 'true'

    def is_radiobutton_checked(self, element_id):
        """Check if radiobutton is checked.

        Args:
            element_id: the value of the elements id property.
        Returns:
            is the radiobutton checked as boolean
        Raises:
            AssertionError: for other values than True and False
        """
        checked = self.sf_api_commands.get_flex_radio_button(element_id)
        if checked != 'true' and checked != 'false':
            raise AssertionError("Radiobutton state of '{}' returned an unexpected value: {}"
                                 .format(element_id, checked))
        return checked == 'true'

    def is_text_present(self, element_id, text):
        """Check if the element contains given text.

        Args:
            element_id: the value of the elements id property.
            text: the text to look for
        Returns:
            is the text in the element as boolean
        Raises:
            AssertionError: for other values than True and False
        """
        present = self.sf_api_commands.get_flex_text_present(element_id, text)
        if present != 'true' and present != "Error: The element '{}' was not found in the application".format(text):
            raise AssertionError("Presence check of text '{}' on element {} returned an unexpected value: {}"
                                 .format(text, element_id, present))
        return present == 'true'

    def is_visible(self, element_id):
        """Check if the element is visible.

        Args:
            element_id: the value of the elements id property.
        Returns:
            is the element visible as boolean
        Raises:
            AssertionError: for other values than True and False
        """
        visibility = self.sf_api_commands.get_flex_visible(element_id)
        if visibility != 'true' and visibility != 'false':
            raise AssertionError("Visibility of '{}' returned an unexpected value: {}"
                                 .format(element_id, visibility))
        return visibility == 'true'

    def get_alert_text(self):
        return self.sf_api_commands.get_flex_alert_text()

    def get_combobox_selected_item(self, element_id):
        return self.sf_api_commands.get_flex_selection(element_id)

    def get_component_info(self, element_id):
        return self.sf_api_commands.get_flex_component_info(element_id)

    def get_data_grid_cell_label(self, element_id, row_index, column_index):
        return self.sf_api_commands.raw_flex_data_grid_cell_text(element_id, row_index, column_index)

    def get_data_grid_cell_value(self, element_id, row_index, column_index):
        return self.sf_api_commands.raw_flex_data_grid_cell(element_id, row_index, column_index)

    def get_data_grid_component_label(self, element_id, row_index, column_index, component_index_in_cell=0):
        return self.sf_api_commands.raw_flex_data_grid_ui_component_label(element_id, row_index, column_index,
                                                                          component_index_in_cell)

    def get_data_grid_field_value_by_row_index(self, element_id, field, row_index):
        return self.sf_api_commands.raw_flex_data_grid_field_value_for_grid_row(element_id, field, row_index)

    def get_data_grid_field_label_by_row_index(self, element_id, field, row):
        return self.sf_api_commands.raw_flex_data_grid_field_label_for_grid_row(element_id, field, row)

    def get_data_grid_row_count(self, element_id):
        return self.sf_api_commands.get_flex_data_grid_row_count(element_id)

    def get_data_grid_row_index_by_field_label(self, element_id, field, label):
        return self.sf_api_commands.raw_flex_data_grid_row_index_for_field_label(element_id, field, label)

    def get_data_grid_row_index_by_field_value(self, element_id, field, value):
        return self.sf_api_commands.raw_flex_data_grid_row_index_for_field_value(element_id, field, value)

    def get_date(self, element_id):
        return self.sf_api_commands.get_flex_date(element_id)

    def get_error_string(self, element_id):
        return self.sf_api_commands.get_flex_error_string(element_id)

    def get_global_position(self, element_id):
        return self.sf_api_commands.raw_flex_global_position(element_id)

    def get_number_of_selected_items(self, element_id):
        return self.sf_api_commands.get_flex_num_selected_items(element_id)

    def get_properties(self, element_id, *flex_properties):
        return self.sf_api_commands.raw_flex_properties(element_id, *flex_properties)

    def get_property(self, element_id, flex_property):
        return self.sf_api_commands.raw_flex_property(element_id, flex_property)

    def get_selection_index(self, element_id):
        return self.sf_api_commands.get_flex_selection_index(element_id)

    def get_selected_item_at_index(self, element_id, index):
        return self.sf_api_commands.get_flex_selected_item_at_index(element_id, index)

    def get_stepper_value(self, element_id):
        return self.sf_api_commands.get_flex_stepper(element_id)

    def get_text(self, element_id):
        return self.sf_api_commands.get_flex_text(element_id)

    def press_enter_on_element(self, element_id):
        return self.press_key_on_element(element_id, "13")

    def press_key_on_element(self, element_id, key_code):
        key_down = self.sf_api_commands.do_flex_key_down(element_id, key_code)
        key_up = self.sf_api_commands.do_flex_key_up(element_id, key_code)
        if key_up == "true" and key_down == "true":
            return "true"
        return "{} {}".format(key_down, key_up)

    def press_space_on_element(self, element_id):
        return self.press_key_on_element(element_id, "32")

    def select(self, element_id, item_to_select):
        """Select item from compatible element.

        Args:
            element_id: the value of the elements id property.
            item_to_select: the visible value of the item to select
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_select(element_id, item_to_select)

    def select_by_matching_on_field(self, element_id, underlying_field, underlying_value,
                                    add_to_existing_selection=False):
        """Select item from compatible element by matching a value to a field.

        For example: | DataGridID | columnID | cellValue | True |

        Args:
            element_id: the value of the elements id property.
            underlying_field: the name of field to match on
            underlying_value: the value of the field
            add_to_existing_selection: append to current selection
        Returns:
            true if command succeeds
        """
        if add_to_existing_selection:
            return self.sf_api_commands.do_flex_add_select_matching_on_field(element_id, underlying_field,
                                                                             underlying_value)
        else:
            return self.sf_api_commands.raw_flex_select_matching_on_field(element_id, underlying_field,
                                                                          underlying_value)

    def select_combobox_item_by_label(self, element_id, item_to_select):
        """Select item from a combobox by label

        Args:
            element_id: the value of the elements id property.
            item_to_select: the visible value of the item to select
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_select_combo_by_label(element_id, item_to_select)

    def select_combobox_item_by_label_from_data_grid(self, element_id, row_index, column_index, item_to_select):
        return self.sf_api_commands.do_flex_data_grid_select_combo_by_label(element_id, row_index, column_index,
                                                                            item_to_select)

    def select_index(self, element_id, index_to_select, add_to_selection=False):
        """Select item from compatible element by index.

        Args:
            element_id: the value of the elements id property.
            index_to_select: the index to select. Starts from 0.
            add_to_selection: add to existing selection
        Returns:
            true if command succeeds
        """
        if add_to_selection:
            return self.sf_api_commands.do_flex_add_select_index(element_id, index_to_select)
        else:
            return self.sf_api_commands.do_flex_select_index(element_id, index_to_select)

    def set_checkbox_value(self, element_id, value):
        """Set checkbox value to true or false.

        Args:
            element_id: the value of the elements id property.
            value: true for checked, false for unchecked
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_checkbox(element_id, "true" if value else "false")

    def set_data_grid_cell_value(self, element_id, row_index, column_index, value):
        """Set data grid cell value

        Args:
            element_id: the value of the elements id property.
            row_index: index of the row to change. Starts from 0
            column_index: index of the column to change. Starts from 0
            value: the value to insert
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.raw_flex_set_data_grid_cell(element_id, row_index, column_index, value)

    def set_data_grid_checkbox_value(self, element_id, row_index, column_index, value):
        return self.sf_api_commands.do_flex_data_grid_checkbox(element_id, row_index, column_index,
                                                               "true" if value else "false")

    def set_focus(self, element_id):
        """Set focus to the element.

        Args:
            element_id: the value of the elements id property.
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_set_focus(element_id)

    def set_property(self, element_id, flex_property, value):
        """Set element property.

        Args:
            element_id: the value of the elements id property.
            flex_property: the property to modify
            value: the value to insert
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_property(element_id, flex_property, value)

    def set_radiobutton_value(self, element_id, state=True):
        """Set radiobutton value to true or false.

        Args:
            element_id: the value of the elements id property.
            state: true for checked, false for unchecked
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_radio_button(element_id, "true" if state else "false")

    def set_stepper_value(self, element_id, value):
        """Set the value of a NumericStepper.

        Args:
            element_id: the value of the elements id property.
            value: the value to set. Must be valid for the specific stepper
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_stepper(element_id, value)

    def wait_for_element_to_exist(self, element_id, timeout):
        return self.sf_api_commands.do_flex_wait_for_element(element_id, timeout)

    def wait_for_element_to_be_visible(self, element_id, timeout):
        return self.sf_api_commands.do_flex_wait_for_element_visible(element_id, timeout)
