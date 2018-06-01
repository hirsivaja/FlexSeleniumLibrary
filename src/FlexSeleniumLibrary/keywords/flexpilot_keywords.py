from ..flexpilotcommands import FlexPilotCommands
from SeleniumLibrary.base import keyword, LibraryComponent


class FlexPilotKeywords(LibraryComponent):
    """
    The keywords that manipulate the Flex application using FlexPilot tool.
    
    For more information see:
    https://github.com/mde/flex-pilot/

    Command documentation copied from:
    https://github.com/mde/flex-pilot/wiki/API
    """

    def __init__(self, ctx, flash_object_id=None):
        """Flex keywords

        Args:
            ctx: The Selenium context we are using
            flash_object_id: the name of the tested Flex application
        """
        LibraryComponent.__init__(self, ctx)
        self.flex_pilot_commands = FlexPilotCommands(ctx, flash_object_id)

    @keyword
    def fp_locator(self, locator_type, locator_string):
        """
        Generates a locator string from the parameters

        Locator strings can also be generated manually.

        type        example
        ----------------------------
        id 	        id:'howdyButton'
        name 	    name:'testTextArea'
        chain 	    name:'testTextArea'/name:'UITextField18'
        child 	    name:'container'/child:[2]
        attribute   label:'OK'
                    automationName:'testButton7'

        Args:
            locator_type: id, name, child, custom
            locator_string: unique locator for the element
        Returns:
            FlexPilot locator as string
        """
        if locator_type == "id":
            return "id:'{}'".format(locator_string)
        elif locator_type == "name":
            return "name:'{}'".format(locator_string)
        elif locator_type == "child":
            return "child:[{}]".format(locator_string)
        elif locator_type == "custom":
            return locator_string
        raise AssertionError("Unknown locator type: {}".format(locator_type))

    @keyword
    def fp_id_locator(self, locator_string):
        """
        Generates a id locator string from the parameter

        Args:
            locator_string: id of the element
        Returns:
            FlexPilot locator as string
        """
        return self.fp_locator("id", locator_string)

    @keyword
    def fp_name_locator(self, locator_string):
        """
        Generates a name locator string from the parameter

        Args:
            locator_string: name of the element
        Returns:
            FlexPilot locator as string
        """
        return self.fp_locator("name", locator_string)

    @keyword
    def fp_child_locator(self, parent_locator, number_of_child):
        """
        Generates a child locator string from the parameter

        Args:
            parent_locator: locator for the element parent
            number_of_child: number of child of the parent
        Returns:
            FlexPilot locator as string
        """
        return "{}/{}".format(parent_locator, self.fp_locator("child", number_of_child))

    @keyword
    def fp_chain_locator(self, *flex_pilot_locator):
        """
        Generates a chain locator string from the parameters

        Args:
            flex_pilot_locator: the locators to chain
        Returns:
            Locators chained to one
        """
        return "/".join(flex_pilot_locator)

    @keyword
    def fp_assert_display_object(self, locator):
        """
        Assert a display object exists
    
        Args:
            locator: See FlexPilotKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_assertDisplayObject", locator)

    @keyword
    def fp_assert_property(self, locator, validator):
        """
        Assert a display object 'locator', contains a specified property 'validator' (property pipe value)
    
        Example fp_assertProperty: chain=automationName:test, validator=style.color:blue
    
        Args:
            locator: See FlexPilotKeywords.flex_pilot_locator
            validator:
        """
        return self.flex_pilot_commands.call("fp_assertProperty", locator, "validator:'{}'".format(validator))

    @keyword
    def fp_assert_text(self, locator, validator):
        """
        Assert a specified input field 'locator' equals text 'validator'
    
        Args:
            locator: See FlexPilotKeywords.flex_pilot_locator
            validator:
        """
        return self.flex_pilot_commands.call("fp_assertText", locator, "validator:'{}'".format(validator))

    @keyword
    def fp_assert_text_in(self, locator, validator):
        """
        Assert a specified input field 'locator' contains text 'validator'
    
        Args:
            locator: See FlexPilotKeywords.flex_pilot_locator
            validator:
        """
        return self.flex_pilot_commands.call("fp_assertTextIn", locator, "validator:'{}'".format(validator))

    @keyword
    def fp_check(self, locator):
        """
        Checks the display object (Equivalent to fp_click).
    
        Args:
            locator: See FlexPilotKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_check", locator)

    @keyword
    def fp_click(self, locator, label=None):
        """
        Clicks display object.
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
            label: optional label, for accordions, button bars etc
        """
        if label is not None:
            return self.flex_pilot_commands.call("fp_click", locator, "'label':'{}'".format(label))
        return self.flex_pilot_commands.call("fp_click", locator)

    @keyword
    def fp_date(self, locator):
        """
        Triggers the calendar layout date change on the display object.
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_date", locator)

    @keyword
    def fp_drag_drop_to_coordinates(self, locator, x, y):
        """
        Drags a display object 'locator' to a specified x,y.
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
            x: x-coordinate of the destination
            y: y-coordinate of the destination
        """
        return self.flex_pilot_commands.call("fp_dragDropToCoords", locator, "'coords':'{},{}'".format(x, y))

    @keyword
    def fp_drag_drop_elem_to_elem(self, source_locator, destination_locator):
        """
        Drags a display object to the coordinates of the display object 'destination_locator'.
    
        Args:
            source_locator: see FlexPilotKeywords.flex_pilot_locator, the source of the drag
            destination_locator: see FlexPilotKeywords.flex_pilot_locator, the destination of the drag
        """
        return self.flex_pilot_commands.call("fp_dragDropElemToElem", source_locator, destination_locator)

    @keyword
    def fp_double_click(self, locator):
        """
        Double clicks display object.
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_doubleClick", locator)

    @keyword
    def fp_dump(self, locator):
        """
        Dumps the child structure of display object for test building purposes.
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_dump", locator)

    @keyword
    def fp_get_object_coordinates(self, locator):
        """
        Gets the coordinates of the display object.
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_getObjectCoords", locator)

    @keyword
    def fp_get_property_value(self, locator, attribute_name):
        """
        Gets the value of the property 'attrName' on the display object.
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
            attribute_name: name of the property to get
        """
        return self.flex_pilot_commands.call("fp_getPropertyValue", locator, "'attrName':'{}'".format(attribute_name))

    @keyword
    def fp_get_text_value(self, locator):
        """
        Gets the text value of the display object (either the htmlText or label).
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_getTextValue", locator)

    @keyword
    def fp_get_version(self):
        """
        Returns the version of FlexPilot currently running.
    
        Returns:
            Version of the FlexPilot
        """
        return self.flex_pilot_commands.call("fp_getVersion")

    @keyword
    def fp_lookup_flash(self, locator):
        """
        Looks up a display object in the display list.
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_lookupFlash", locator)

    @keyword
    def fp_mouse_out(self, locator):
        """
        Mouses out of display object.
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_mouseOut", locator)

    @keyword
    def fp_mouse_over(self, locator):
        """
        Mouses over display object.
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_mouseOver", locator)

    @keyword
    def fp_radio(self, locator):
        """
        Selects the radio button display object (Equivalent to fp_click).
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_radio", locator)

    @keyword
    def fp_select(self, locator):
        """
        Selects specified combo box display object.
        You can use the following properties in the locator for finding the item in the combo box:
        index, label, text, data, value, or toString.
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_select", locator)

    @keyword
    def fp_type(self, locator, text):
        """
        Types 'text' into the display object found by the locator lookup.
    
        Args:
            locator: see FlexPilotKeywords.flex_pilot_locator
            text: text to type
        """
        return self.flex_pilot_commands.call("fp_type", locator, "'text':'{}'".format(text))

    @keyword
    def fp_wait_for_flex_ready(self, timeout):
        """
        Wait for the application to load

        Args:
            timeout: time to wait for the application to load
        """
        self.flex_pilot_commands.wait_for_flex_application_to_load(int(timeout))

    @keyword
    def fp_wait_for_flex_object(self, locator, timeout):
        """
        Wait for the flex object to appear

        Args:
            locator: The object to look for
            timeout: time to wait for the object to appear
        """
        self.flex_pilot_commands.wait_for_flex_object(locator, int(timeout))
