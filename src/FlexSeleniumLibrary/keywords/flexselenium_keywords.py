from ..sfapicommands import SeleniumFlexAPICommands
from SeleniumLibrary.base import keyword, LibraryComponent


class FlexSeleniumKeywords(LibraryComponent):
    """
    The keywords that manipulate the Flex application
    """

    def __init__(self, ctx, flash_object_id=None, api_version=28, sleep_after_call=0,
                 sleep_after_fail=0.1, number_of_retries=30, ensure_timeout=30):
        """Flex keywords

        Args:
            ctx: The Selenium context we are using
            flash_object_id: the name of the tested Flex application
            sleep_after_call: wait time after each call
            sleep_after_fail: wait time after each fail before trying again
            number_of_retries: number of times to retry the command
        """
        LibraryComponent.__init__(self, ctx)
        self.sf_api_commands = SeleniumFlexAPICommands(ctx, flash_object_id, api_version, sleep_after_call,
                                                       sleep_after_fail, number_of_retries, ensure_timeout)

    @keyword
    def add_notification(self, message):
        """Displays a message (in a label) in the bottom left corner to the user

        Args:
            message: the message to show to user
        """
        return self.sf_api_commands.do_flex_notify(message)

    @keyword
    def click(self, element_id, button_label=''):
        """Click Flex element.

        Args:
            element_id: the value of the elements id property.
            button_label: if element is a ButtonBar, click item with this label
        Returns:
            true if success, error text otherwise
        """
        return self.sf_api_commands.do_flex_click(element_id, button_label)

    @keyword
    def click_alert(self, response):
        """Closes first alert by clicking specified button.

        Args:
            response: the text of the button to click. OK, cancel, NO, ...
        Returns:
            true if success, error text otherwise
        """
        return self.sf_api_commands.do_flex_alert_response(response)

    @keyword
    def click_data_grid_column_header(self, element_id, column_index):
        """Clicks the header of the given column in a data grid thus sorting its content.
        Click once to sort in ascending order and twice to sort in descending order

        Args:
            element_id: the data grid to manipulate
            column_index: the index of the column to click
        """
        return self.sf_api_commands.do_flex_data_grid_click_column_header(element_id, column_index)

    @keyword
    def click_data_grid_item_by_label(self, element_id, column_index, label):
        """Clicks a data grid item from the given column by matching its label.

        Args:
            element_id: the data grid to manipulate
            column_index: the index of the column to search
            label: the label to match with
        """
        return self.sf_api_commands.raw_flex_click_data_grid_item(element_id, column_index, label)

    @keyword
    def click_data_grid_ui_component(self, element_id, row_index, column_index, component_number_in_cell=-1):
        """Click the UI component (Button, CheckBox...) in the given cell.

        Args:
             element_id: the data grid to manipulate
             row_index: row of the cell
             column_index: column of the cell
             component_number_in_cell: -1 clicks the cell itself, 0 clicks the first UI component,
             1 the second and so forth
        """
        return self.sf_api_commands.do_flex_click_data_grid_ui_component(element_id, row_index, column_index,
                                                                         component_number_in_cell)

    @keyword
    def click_menu_bar_component(self, element_id, menu_bar_item_index,
                                 menu_item_row_index, menu_item_column_index, component_index_in_cell=0):
        """Clicks an item in a menu.

        Example:
            | File | Help |
            ---------------
            | Open | Manual |
            | Save | About  |
            | Exit |

        Args:
             element_id: id of the menu bar
             menu_bar_item_index: to select 'File' menu use 0 and 1 to select 'Help'.
             menu_item_row_index: to select 'Exit' use 2
             menu_item_column_index: if the menu has several columns, choose one of them
             component_index_in_cell: if the specified cell has multiple UI component, select which to click
        """
        return self.sf_api_commands.raw_flex_click_menu_bar_ui_component(element_id, menu_bar_item_index,
                                                                         menu_item_row_index, menu_item_column_index,
                                                                         component_index_in_cell)

    @keyword
    def click_selected_data_grid_item(self, element_id):
        """Clicks the selected item (row) from the given data grid. Selection should be made beforehand.

        Args:
             element_id: the data grid with a selected item
        """
        return self.sf_api_commands.do_flex_click_selected_data_grid_item(element_id)

    @keyword
    def create_dropdown_event(self, element_id, open_event=True):
        """Dispatches a DropdownEvent to element

        Args:
             element_id: target element
             open_event: if true, dispatches DropdownEvent.OPEN. Else DropdownEvent.CLOSE
        """
        return self.sf_api_commands.do_flex_combo_send_event(element_id, "open" if open_event else "close")

    @keyword
    def create_mouse_down_event(self, element_id):
        """Dispatches a MouseEvent.MOUSE_DOWN event to element

        Args:
             element_id: target element
        """
        return self.sf_api_commands.do_flex_mouse_down(element_id)

    @keyword
    def create_mouse_event(self, element_id, event):
        """Dispatches a MouseEvent event to element

        Args:
             element_id: target element
             event: the mouse event to dispatch. See
                http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/events/MouseEvent.html
        """
        return self.sf_api_commands.do_flex_mouse_event(element_id, event)

    @keyword
    def create_mouse_move_event(self, element_id, x, y):
        """Dispatches a MouseEvent.MOUSE_MOVE event to element

        Args:
             element_id: target element
             x: where to move, x-coordinate
             y: where to move, y-coordinate
        """
        return self.sf_api_commands.do_flex_mouse_move(element_id, x, y)

    @keyword
    def create_mouse_over_event(self, element_id):
        """Dispatches a MouseEvent.MOUSE_OVER event to element

        Args:
             element_id: target element
        """
        return self.sf_api_commands.do_flex_mouse_over(element_id)

    @keyword
    def create_mouse_roll_out_event(self, element_id):
        """Dispatches a MouseEvent.ROLL_OUT event to element

        Args:
             element_id: target element
        """
        return self.sf_api_commands.do_flex_mouse_roll_out(element_id)

    @keyword
    def create_mouse_roll_over_event(self, element_id):
        """Dispatches a MouseEvent.ROLL_OVER event to element

        Args:
             element_id: target element
        """
        return self.sf_api_commands.do_flex_mouse_roll_over(element_id)

    @keyword
    def create_mouse_up_event(self, element_id):
        """Dispatches a MouseEvent.MOUSE_UP event to element

        Args:
             element_id: target element
        """
        return self.sf_api_commands.do_flex_mouse_up(element_id)

    @keyword
    def double_click(self, element_id):
        """Dispatches a MouseEvent.DOUBLE_CLICK event to element

        Args:
             element_id: target element
        """
        return self.sf_api_commands.do_flex_double_click(element_id)

    @keyword
    def double_click_data_grid_component(self, element_id, row_index, column_index):
        """Dispatches a MouseEvent.DOUBLE_CLICK event to an element in a data grid cell

        Args:
             element_id: target data grid
             row_index: row of the target cell
             column_index: column of the target cell
        """
        return self.sf_api_commands.do_flex_double_click_data_grid_ui_component(element_id, row_index, column_index)

    @keyword
    def drag_element_to(self, element_id, x, y):
        """Drag element to specified coordinates

        Args:
             element_id: element to drag
             x: destination, x-coordinate
             y: destination, y-coordinate
        """
        return self.sf_api_commands.do_flex_drag_to(element_id, x, y)

    @keyword
    def enter_date(self, element_id, date_as_text):
        """Enters a date to a DateField

        Args:
            element_id: the value of the elements id property.
            date_as_text: the date as text. For example: 31/12/2015
        Returns:
            true if success, error text otherwise
        """
        return self.sf_api_commands.do_flex_date(element_id, date_as_text)

    @keyword
    def enter_date_to_data_grid_cell(self, element_id, row_index, column_index, date):
        """Enters a date to a Date component in a data grid cell

        Args:
             element_id: data grid id
             row_index: row of the component
             column_index: column of the component
             date: the date to enter
        """
        return self.sf_api_commands.do_flex_data_grid_date(element_id, row_index, column_index, date)

    @keyword
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

    @keyword
    def ensure_enabled_state(self, element_id, expected_enabled_state):
        """Wait until the enabled state of the element is expected or timeout occurs.

        Args:
             element_id: element to check
             expected_enabled_state: should the element be enabled or disabled
        """
        self.sf_api_commands.ensure_result(expected_enabled_state, self.is_enabled, element_id)

    @keyword
    def ensure_exists(self, element_id, expected_existing_state):
        """Wait until the existence of the element is expected or timeout occurs.

        Args:
             element_id: element to check
             expected_existing_state: should the element exist or not
        """
        self.sf_api_commands.ensure_result(expected_existing_state, self.exists, element_id)

    @keyword
    def ensure_visibility(self, element_id, expected_visibility):
        """Wait until the visibility of the element is expected or timeout occurs.

        Args:
             element_id: element to check
             expected_visibility: should the element be visible or not
        """
        self.sf_api_commands.ensure_result(expected_visibility, self.is_visible, element_id)

    @keyword
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

    @keyword
    def expand_data_grid_elements(self, element_id):
        """Expand all items in a data grid. Works if the data grid contains a tree.

        Args:
             element_id: data grid id
        """
        return self.sf_api_commands.do_flex_data_grid_expand_all(element_id)

    @keyword
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

    @keyword
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

    @keyword
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

    @keyword
    def is_function_defined(self, function_name):
        """Check if the function is defined as an external JavaScript callback.

        Args:
            function_name: the name of the function
        Returns:
            existence of the function as boolean
        Raises:
            AssertionError: for other values than True and False
        """
        return self.sf_api_commands.is_function_defined(function_name)

    @keyword
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

    @keyword
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

    @keyword
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

    @keyword
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

    @keyword
    def is_visible(self, element_id, fail_if_not_found=True):
        """Check if the element is visible.

        Args:
            element_id: the value of the elements id property.
            fail_if_not_found: raise AssertionError if element is not found
        Returns:
            is the element visible as boolean
        Raises:
            AssertionError: for other values than True and False
        """
        visibility = self.sf_api_commands.get_flex_visible(element_id)
        if visibility != 'true' and visibility != 'false':
            if visibility == "Error: The element '{}' was not found in the application".format(element_id) \
                    and not fail_if_not_found:
                return False
            raise AssertionError("Visibility of '{}' returned an unexpected value: {}"
                                 .format(element_id, visibility))
        return visibility == 'true'

    @keyword
    def get_alert_text(self):
        """If an alert is shown, gets its text

        Returns:
            the alert text if visible, error otherwise
        """
        return self.sf_api_commands.get_flex_alert_text()

    @keyword
    def get_api_version(self):
        """Get the version of the SFAPI. If 'getFlexAPIVersion' function is not defined returns API version 26.

        Returns:
            version of the SeleniumFlexAPI present in the tested application
        """
        if self.is_function_defined("getFlexAPIVersion"):
            return self.sf_api_commands.get_flex_api_version().split(".")[1]
        return 26

    @keyword
    def get_child_elements(self, element_id, full_path, only_visible_children):
        """Get all the child elements of the given element

        Args:
             element_id: element which children to retrieve
             full_path: return full path of child elements or only its own id
             only_visible_children: return all or only visible child elements
        Returns:
            list of child element ids
        """
        return self.sf_api_commands.get_flex_children(element_id, "true" if full_path else "false",
                                                      "true" if only_visible_children else "false")

    @keyword
    def get_combobox_selected_item(self, element_id):
        """Get all the selected items from a combobox

        Args:
             element_id: combobox id
        Returns:
            list of selected items in a combobox
        """
        return self.sf_api_commands.get_flex_selection(element_id)

    @keyword
    def get_combobox_values(self, element_id):
        """Get all the possible values from a combobox

        Args:
             element_id: combobox id
        Returns:
            list of all the combobox values
        """
        return self.sf_api_commands.get_flex_combo_values(element_id).split("#;#")

    @keyword
    def get_component_info(self, element_id):
        """Get position and size of the component. X, Y, width, height.

        Args:
             element_id: component id
        Returns:
            component x-coordinate, y-coordinate, width and height
        """
        return self.sf_api_commands.get_flex_component_info(element_id)

    @keyword
    def get_data_grid_cell_label(self, element_id, row_index, column_index):
        """Get the label of a data grid cell

        Args:
             element_id: data grid id
             row_index: row of the cell
             column_index: column of the cell
        Returns:
            label of the cell
        """
        return self.sf_api_commands.raw_flex_data_grid_cell_text(element_id, row_index, column_index)

    @keyword
    def get_data_grid_cell_value(self, element_id, row_index, column_index):
        """Get the value of a data grid cell

        Args:
             element_id: data grid id
             row_index: row of the cell
             column_index: column of the cell
        Returns:
            value of the cell
        """
        return self.sf_api_commands.raw_flex_data_grid_cell(element_id, row_index, column_index)

    @keyword
    def get_data_grid_component_label(self, element_id, row_index, column_index, component_index_in_cell=0):
        """Get the label of a UI component in a data grid cell

        Args:
             element_id: data grid id
             row_index: row of the cell
             column_index: column of the cell
             component_index_in_cell: which component from the cell to choose if more than one is present
        Returns:
            label of the UI component
        """
        return self.sf_api_commands.raw_flex_data_grid_ui_component_label(element_id, row_index, column_index,
                                                                          component_index_in_cell)

    @keyword
    def get_data_grid_field_count(self, element_id, only_visible):
        """Get the number of fields (columns) in a data grid

        Args:
             element_id: data grid id
             only_visible: count only displayed fields
        Returns:
            number of fields
        """
        return self.sf_api_commands.get_flex_data_grid_col_count(element_id, only_visible)

    @keyword
    def get_data_grid_field_data_fields(self, element_id, only_visible):
        """Get the names of data fields (columns) in a data grid

        Args:
             element_id: data grid id
             only_visible: only displayed fields
        Returns:
            names of the data fields
        """
        return self.sf_api_commands.get_flex_data_grid_col_data_fields(element_id, only_visible).split("|")

    @keyword
    def get_data_grid_field_label_by_row_index(self, element_id, field, row):
        """Get the label from the given row in the field

        Args:
             element_id: data grid id
             field: name of the field to search
             row: the row for element
        Returns:
            label of the cell
        """
        return self.sf_api_commands.raw_flex_data_grid_field_label_for_grid_row(element_id, field, row)

    @keyword
    def get_data_grid_field_value_by_row_index(self, element_id, field, row_index):
        """Get the value from the given row in the field

        Args:
             element_id: data grid id
             field: name of the field to search
             row_index: the row for element
        Returns:
            value of the cell
        """
        return self.sf_api_commands.raw_flex_data_grid_field_value_for_grid_row(element_id, field, row_index)

    @keyword
    def get_data_grid_field_values(self, element_id, field, extra_data=None):
        """Get all the values from one field (column)

        Args:
             element_id: data grid id
             field: name of the field
             extra_data: include extra data
        Returns:
            list of all the values for the field
        """
        if extra_data is not None:
            return self.sf_api_commands.raw_flex_data_grid_field_all_values(element_id, field, extra_data)
        else:
            return self.sf_api_commands.raw_flex_data_grid_field_values_for_column(element_id, field).split("#;#")

    @keyword
    def get_data_grid_row_count(self, element_id):
        """Get the number of rows in a data grid

        Args:
             element_id: data grid id
        Returns:
            number of rows
        """
        return self.sf_api_commands.get_flex_data_grid_row_count(element_id)

    @keyword
    def get_data_grid_row_index_by_field_label(self, element_id, field, label):
        """Get the row number for the label by searching a field

        Args:
             element_id: data grid id
             field: name of the field to search
             label: the label to match
        Returns:
            row number where the label was found, -1 if not found
        """
        return self.sf_api_commands.raw_flex_data_grid_row_index_for_field_label(element_id, field, label)

    @keyword
    def get_data_grid_row_index_by_field_value(self, element_id, field, value):
        """Get the row number for the value by searching a field

        Args:
             element_id: data grid id
             field: name of the field to search
             value: the value to match
        Returns:
            row number where the value was found, -1 if not found
        """
        return self.sf_api_commands.raw_flex_data_grid_row_index_for_field_value(element_id, field, value)

    @keyword
    def get_data_grid_values(self, element_id, only_visible):
        """Get all the values in a data grid

        Args:
             element_id: data grid id
             only_visible: should only values from visible columns be returned
        Returns:
            all the values in the data grid
        """
        value_rows = self.sf_api_commands.get_flex_data_grid_values(element_id,
                                                                    only_visible).split("##ITEM####ROW####ITEM##")
        result = []
        for row in value_rows:
            result.append(row.split("##ITEM##"))
        return result

    @keyword
    def get_date(self, element_id):
        """Get the date from a Date component

        Args:
             element_id: date component id
        Returns:
            date as a string
        """
        return self.sf_api_commands.get_flex_date(element_id)

    @keyword
    def get_error_string(self, element_id):
        """Get the value of the elements 'errorString' property

        Args:
             element_id: component id
        Returns:
            the value of the errorString property
        """
        return self.sf_api_commands.get_flex_error_string(element_id)

    @keyword
    def get_global_position(self, element_id):
        """Get the global position of the element

        Args:
             element_id: component id
        Returns:
            x- and y-coordinates
        """
        return self.sf_api_commands.raw_flex_global_position(element_id)

    @keyword
    def get_number_of_selected_items(self, element_id):
        """Get the number of selected items from the element that supports selection

        Args:
             element_id: component that supports selection
        Returns:
            number of selected items
        """
        return self.sf_api_commands.get_flex_num_selected_items(element_id)

    @keyword
    def get_path_for_locator(self, element_id, allow_invisible=True):
        """Get the full path for a locator

        Args:
             element_id: locator for an element
             allow_invisible: are invisible elements allowed
        Returns:
            path of the element found by the locator
        """
        name, parent, visible = self.sf_api_commands.raw_flex_properties(
            element_id, "name", "parent", "visible").split(',')
        if "Error: The element '{}' was not found in the application".format(element_id) in name:
            raise AssertionError(name)
        path = "{}/{}".format(parent.replace(".", "/"), name)
        if not allow_invisible and visible == 'false':
            raise AssertionError("The element '{}' was not visible.".format(path))
        return path

    @keyword
    def get_properties(self, element_id, *flex_properties):
        """Get the listed properties

        Args:
             element_id: component id
             flex_properties: list of properties to get
        Returns:
            list of property values
        """
        return self.sf_api_commands.raw_flex_properties(element_id, *flex_properties)

    @keyword
    def get_property(self, element_id, flex_property):
        """Get the value of the given property

        Args:
             element_id: component id
             flex_property: property to get
        Returns:
            value of the property
        """
        return self.sf_api_commands.raw_flex_property(element_id, flex_property)

    @keyword
    def get_selection_index(self, element_id):
        """Get the index of the selected item

        Args:
             element_id: component id
        Returns:
            index of the selected item
        """
        return self.sf_api_commands.get_flex_selection_index(element_id)

    @keyword
    def get_selected_item_at_index(self, element_id, index):
        """Get the item that is found in the given position in the list of selected items

        Args:
             element_id: component id
             index: which item to return from the list of selected items. For example, if 5 items are selected, index 4
                returns the fifth selected item (zero-based indexing)
        Returns:
            item at given index
        """
        return self.sf_api_commands.get_flex_selected_item_at_index(element_id, index)

    @keyword
    def get_stepper_value(self, element_id):
        """Get the value of the stepper component

        Args:
             element_id: stepper id
        Returns:
            value of the stepper
        """
        return self.sf_api_commands.get_flex_stepper(element_id)

    @keyword
    def get_tab_labels(self, element_id):
        """Get the labels of tabs in a tab navigator

        Args:
             element_id: tab navigator id
        Returns:
            list of tab labels in the tab navigator
        """
        return self.sf_api_commands.get_flex_tab_labels(element_id)

    @keyword
    def get_text(self, element_id):
        """Get the text or label from an element

        Args:
             element_id: component id
        Returns:
            the text or label of the component depending on the component type
        """
        return self.sf_api_commands.get_flex_text(element_id)

    @keyword
    def press_enter_on_element(self, element_id):
        """Simulate pressing 'enter' key on the element

        Args:
             element_id: target element
        """
        return self.press_key_on_element(element_id, "13")

    @keyword
    def press_key_on_element(self, element_id, key_code):
        """Dispatches KEY_DOWN and KEY_UP keyboard events to the element.

        Args:
             element_id: target element
             key_code: key code to dispatch. See this for the available key codes
                http://help.adobe.com/en_US/AS2LCR/Flash_10.0/help.html?content=00000520.html
        """
        key_down = self.sf_api_commands.do_flex_key_down(element_id, key_code)
        key_up = self.sf_api_commands.do_flex_key_up(element_id, key_code)
        if key_up == "true" and key_down == "true":
            return "true"
        return "{} {}".format(key_down, key_up)

    @keyword
    def press_space_on_element(self, element_id):
        """Simulate pressing 'space bar' key on the element

        Args:
             element_id: target element
        """
        return self.press_key_on_element(element_id, "32")

    @keyword
    def select(self, element_id, item_to_select):
        """Select item from compatible element.

        Args:
            element_id: the value of the elements id property.
            item_to_select: the visible value of the item to select
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_select(element_id, item_to_select)

    @keyword
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

    @keyword
    def select_combobox_item_by_label(self, element_id, item_to_select):
        """Select item from a combobox by label

        Args:
            element_id: the value of the elements id property.
            item_to_select: the visible value of the item to select
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_select_combo_by_label(element_id, item_to_select)

    @keyword
    def select_combobox_item_by_label_from_data_grid(self, element_id, row_index, column_index, item_to_select):
        """Select a value from a combo box inside a data grid

        Args:
             element_id: data grid id
             row_index: data grid row
             column_index: data grid column
             item_to_select: value of the label in the combo box to select
        """
        return self.sf_api_commands.do_flex_data_grid_select_combo_by_label(element_id, row_index, column_index,
                                                                            item_to_select)

    @keyword
    def select_data_grid_index(self, element_id, index_to_select):
        """Select the given row from a data grid

        Args:
             element_id: data grid id
             index_to_select: index of the row to select
        """
        return self.sf_api_commands.do_flex_select_data_grid_index(element_id, index_to_select)

    @keyword
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

    @keyword
    def select_tree_item(self, element_id, property_name, *search_words):
        """Select an item from tree that is in a data grid

        Example:
            Tree
                |_node:item1
                |          |_node:item1.1
                |_node:item2
                           |_node:item2.1
                           |_node:item2.2
        select_tree_item('Tree', 'node', 'item2', 'item2.2');

        results in row 'node:item2.2' to be selected.

        Args:
             element_id: data grid id
             property_name: name of the property to match to
             search_words: list of values for the property
        """
        return self.sf_api_commands.do_flex_select_tree_item(element_id, property_name, *search_words)

    @keyword
    def set_checkbox_value(self, element_id, value):
        """Set checkbox value to true or false.

        Args:
            element_id: the value of the elements id property.
            value: true for checked, false for unchecked
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_checkbox(element_id, "true" if value else "false")

    @keyword
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

    @keyword
    def set_data_grid_checkbox_value(self, element_id, row_index, column_index, value):
        """Set the state of a check box component that is in a data grid cell

        Args:
             element_id: data grid id
             row_index: row of the check box cell
             column_index: column of the check box cell
             value: check or not
        """
        return self.sf_api_commands.do_flex_data_grid_checkbox(element_id, row_index, column_index,
                                                               "true" if value else "false")

    @keyword
    def set_focus(self, element_id):
        """Set focus to the element.

        Args:
            element_id: the value of the elements id property.
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_set_focus(element_id)

    @keyword
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

    @keyword
    def set_radiobutton_value(self, element_id, state=True):
        """Set radiobutton value to true or false.

        Args:
            element_id: the value of the elements id property.
            state: true for checked, false for unchecked
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_radio_button(element_id, "true" if state else "false")

    @keyword
    def set_stepper_value(self, element_id, value):
        """Set the value of a NumericStepper.

        Args:
            element_id: the value of the elements id property.
            value: the value to set. Must be valid for the specific stepper
        Returns:
            true if command succeeds
        """
        return self.sf_api_commands.do_flex_stepper(element_id, value)

    @keyword
    def wait_for_element_to_exist(self, element_id, timeout):
        """Wait until element exists or timeout occurs

        Args:
            element_id: element to exist
            timeout: number of times to try. Not exact time
        """
        return self.sf_api_commands.do_flex_wait_for_element(element_id, timeout)

    @keyword
    def wait_for_element_to_be_visible(self, element_id, timeout):
        """Wait until element is visible or timeout occurs

        Args:
            element_id: element to become visible
            timeout: number of times to try. Not exact time
        """
        return self.sf_api_commands.do_flex_wait_for_element_visible(element_id, timeout)
