from ..flexpilotcommands import FlexPilotCommands


class FlexPilotKeywords(object):
    """
    The keywords that manipulate the Flex application using FlexPilot tool.
    
    For more information see:
    https://github.com/mde/flex-pilot/

    Command documentation copied from:
    https://github.com/mde/flex-pilot/wiki/API
    """

    def __init__(self, web_driver=None, flash_object_id=None):
        """Flex keywords

        Args:
            web_driver: WebDriver instance to use sending the calls to Flex application
            flash_object_id: the name of the tested Flex application
        """
        self.flex_pilot_commands = FlexPilotCommands(web_driver, flash_object_id)

    def flex_pilot_locator(self, locator_type, locator_string):
        """
        *attr (automationName etc) 	*value
        id 	howdyButton
        name 	testTextArea
        chain 	name:testTextArea/name:UITextField18
        child 	name:container/child:[2]
        Args:
            locator_type: id, name, child
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
        return

    def flex_pilot_id_locator(self, locator_string):
        return self.flex_pilot_locator("id", locator_string)

    def flex_pilot_name_locator(self, locator_string):
        return self.flex_pilot_locator("name", locator_string)

    def flex_pilot_child_locator(self, parent_locator, number_of_child):
        return "{}/{}".format(parent_locator,self.flex_pilot_locator("child", number_of_child))

    def flex_pilot_chain_locator(self, *flex_pilot_locator):
        return "/".join(flex_pilot_locator)
        
    def fp_assert_display_object(self, locator):
        """
        Assert a display object exists
    
        Args:
            locator: See FlexSeleniumKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_assertDisplayObject", locator)
    
    def fp_assert_property(self, locator, validator):
        """
        Assert a display object 'locator', contains a specified property 'validator' (property pipe value)
    
        Example fp_assertProperty: chain=automationName:test, validator=style.color:blue
    
        Args:
            locator: See FlexSeleniumKeywords.flex_pilot_locator
            validator:
        """
        return self.flex_pilot_commands.call("fp_assertProperty", locator, validator)
    
    def fp_assert_text(self, locator, validator):
        """
        Assert a specified input field 'locator' equals text 'validator'
    
        Args:
            locator: See FlexSeleniumKeywords.flex_pilot_locator
            validator:
        """
        return self.flex_pilot_commands.call("fp_assertText", locator, validator)
    
    def fp_assert_text_in(self, locator, validator):
        """
        Assert a specified input field 'locator' contains text 'validator'
    
        Args:
            locator: See FlexSeleniumKeywords.flex_pilot_locator
            validator:
        """
        return self.flex_pilot_commands.call("fp_assertTextIn", locator, validator)
    
    def fp_check(self, locator):
        """
        Checks the display object (Equivalent to fp_click).
    
        Args:
            locator: See FlexSeleniumKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_check", locator)
    
    def fp_click(self, locator, label=None):
        """
        Clicks display object.
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
            label: optional label, for accordions, button bars etc
        """
        if label is not None:
            return self.flex_pilot_commands.call("fp_click", locator, "'label':'{}'".format(label))
        return self.flex_pilot_commands.call("fp_click", locator)
    
    def fp_date(self, locator):
        """
        Triggers the calendar layout date change on the display object.
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_date", locator)
    
    def fp_drag_drop_to_coordinates(self, locator, x, y):
        """
        Triggers the calendar layout date change on the display object.
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
            x: x-coordinate of the destination
            y: y-coordinate of the destination
        """
        return self.flex_pilot_commands.call("fp_dragDropToCoords", locator, "'coords':'{},{}'".format(x, y))
    
    def fp_drag_drop_elem_to_elem(self, source_locator, destination_locator):
        """
        Triggers the calendar layout date change on the display object.
    
        Args:
            source_locator: see FlexSeleniumKeywords.flex_pilot_locator, the source of the drag
            destination_locator: see FlexSeleniumKeywords.flex_pilot_locator, the destination of the drag
        """
        return self.flex_pilot_commands.call("fp_dragDropElemToElem", source_locator, destination_locator)
    
    def fp_double_click(self, locator):
        """
        Double clicks display object.
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_doubleClick", locator)
    
    def fp_dump(self, locator):
        """
        Dumps the child structure of display object for test building purposes.
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_dump", locator)
    
    def fp_get_object_coordinates(self, locator):
        """
        Gets the coordinates of the display object.
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_getObjectCoords", locator)
    
    def fp_get_property_value(self, locator, attribute_name):
        """
        Gets the value of the property 'attrName' on the display object.
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
            attribute_name: name of the property to get
        """
        return self.flex_pilot_commands.call("fp_getPropertyValue", locator, "'attrName':'{}'".format(attribute_name))
    
    def fp_get_text_value(self, locator):
        """
        Gets the text value of the display object (either the htmlText or label).
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_getTextValue", locator)
    
    def fp_get_version(self):
        """
        Returns the version of FlexPilot currently running.
    
        Returns:
            Version of the FlexPilot
        """
        return self.flex_pilot_commands.call("fp_getVersion")
    
    def fp_lookup_flash(self, locator):
        """
        Looks up a display object in the display list.
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_lookupFlash", locator)
    
    def fp_mouse_out(self, locator):
        """
        Mouses out of display object.
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_mouseOut", locator)
    
    def fp_mouse_over(self, locator):
        """
        Mouses over display object.
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_mouseOver", locator)
    
    def fp_radio(self, locator):
        """
        Selects the radio button display object (Equivalent to fp_click).
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_radio", locator)
    
    def fp_select(self, locator):
        """
        Selects specified combo box display object.
        You can use the following properties in the locator for finding the item in the combo box:
        index, label, text, data, value, or toString.
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
        """
        return self.flex_pilot_commands.call("fp_select", locator)
    
    def fp_type(self, locator, text):
        """
        Types 'text' into the display object found by the locator lookup.
    
        Args:
            locator: see FlexSeleniumKeywords.flex_pilot_locator
            text: text to type
        """
        return self.flex_pilot_commands.call("fp_type", locator, "'text':'{}'".format(text))
