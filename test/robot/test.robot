*** Settings ***
Documentation     Test cases for Flex Selenium library
Suite Setup       Suite Start
Suite Teardown    Suite Stop
Test Setup        Start
Library           FlexSeleniumLibrary    ${flash_app_name}
Library           String

*** Variables ***
${flash_app_url}    http://localhost:8080/flex3test/index.html
${flash_app_name}    Flex3Tester
${browser}        firefox
${buttons_view}    0
${radio_buttons_view}    1
${combo_box_view}    2
${check_box_view}    3
${date_view}      4
${data_grid_view}    5
${tab_navigator_view}    6
${stepper_view}    7
${mouse_view}     8
${tree_view}      9
${button_bar}     buttonBar

*** Test Cases ***
Add Notification
    Select Index    ${button_bar}    ${buttons_view}
    Add Notification    This is a test.
    ${name}=    Get Property    text=This is a test.    name
    Should Contain    ${name}    Label

Click
    Select Index    ${button_bar}    ${buttons_view}
    Click    clickButton
    ${number_of_clicks}=    Get Text    buttonClicks
    Should Be Equal    ${number_of_clicks}    Number of clicks: 1
    Click    clickButton
    ${number_of_clicks}=    Get Text    buttonClicks
    Should Be Equal    ${number_of_clicks}    Number of clicks: 2
    Click    clickButton
    ${number_of_clicks}=    Get Text    buttonClicks
    Should Be Equal    ${number_of_clicks}    Number of clicks: 3
    Click    buttonBar    DataGrid view
    Ensure Visibility    dataGrid    ${True}

Click Alert
    Select Index    ${button_bar}    ${buttons_view}
    Click    alertButton
    ${alert_visible}=    Is Alert Visible
    Should Be True    ${alert_visible}
    Click Alert    OK
    ${alert_visible}=    Is Alert Visible
    Should Not Be True    ${alert_visible}

Click Data Grid Column Header
    Select Index    ${button_bar}    ${data_grid_view}
    ${label}=    Get Data Grid Cell Label    dataGrid    0    0
    Should Be Equal    ${label}    Element1
    Click Data Grid Column Header    dataGrid    0
    Click Data Grid Column Header    dataGrid    0
    ${label}=    Get Data Grid Cell Label    dataGrid    0    0
    Should Be Equal    ${label}    Element3

Click Data Grid Item By Label
    Select Index    ${button_bar}    ${data_grid_view}
    Select By Matching On Field    dataGrid    attribute1    Element2
    ${selected_item}=    Get Text    selectedGridItem
    Should Be Equal    ${selected_item}    Selected item: Element = Element2, 2, false
    Click Data Grid Item By Label    dataGrid    2    false
    ${selected_item}=    Get Text    selectedGridItem
    Should Be Equal    ${selected_item}    Selected item: Element = Element2, 2, true

Click Data Grid Ui Component
    Select Index    ${button_bar}    ${data_grid_view}
    Select By Matching On Field    dataGrid    attribute1    Element2
    ${selected_item}=    Get Text    selectedGridItem
    Should Be Equal    ${selected_item}    Selected item: Element = Element2, 2, false
    Click Data Grid Ui Component    dataGrid    1    2
    ${selected_item}=    Get Text    selectedGridItem
    Should Be Equal    ${selected_item}    Selected item: Element = Element2, 2, true

Click Menu Bar Component
    Click Menu Bar Component    menuBar    0    0    0
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Clicked: Buttons view
    Click Alert    OK
    Click Menu Bar Component    menuBar    0    1    0
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Clicked: Radio buttons view
    Click Alert    OK
    Click Menu Bar Component    menuBar    1    0    0
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Clicked: About
    Click Alert    OK

Click Selected Data Grid Item
    Select Index    ${button_bar}    ${data_grid_view}
    ${selected_item}=    Get Text    selectedGridItem
    Should Be Equal    '${selected_item}'    'Selected item: '
    Select Data Grid Index    dataGrid    2
    ${selected_item}=    Get Text    selectedGridItem
    Should Be Equal    '${selected_item}'    'Selected item: '
    Click Selected Data Grid Item    dataGrid
    ${selected_item}=    Get Text    selectedGridItem
    Should Be Equal    ${selected_item}    Selected item: Element = Element3, 3, true

Create Dropdown Event
    Select Index    ${button_bar}    ${combo_box_view}
    Create Dropdown Event    comboBox

Create Mouse Down Event
    Select Index    ${button_bar}    ${mouse_view}
    Create Mouse Down Event    mouseEventCatcher
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Mouse event: mouseDown
    Click Alert    OK

Create Mouse Event
    Select Index    ${button_bar}    ${mouse_view}
    Create Mouse Event    mouseEventCatcher    mouseOut
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Mouse event: mouseOut
    Click Alert    OK

Create Mouse Move Event
    Select Index    ${button_bar}    ${mouse_view}
    Create Mouse Move Event    mouseEventCatcher    200    200
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Mouse event: mouseMove
    Click Alert    OK

Create Mouse Over Event
    Select Index    ${button_bar}    ${mouse_view}
    Create Mouse Over Event    mouseEventCatcher
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Mouse event: mouseOver
    Click Alert    OK

Create Mouse Roll Out Event
    Select Index    ${button_bar}    ${mouse_view}
    Create Mouse Roll Out Event    mouseEventCatcher
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Mouse event: rollOut
    Click Alert    OK

Create Mouse Roll Over Event
    Select Index    ${button_bar}    ${mouse_view}
    Create Mouse Roll Over Event    mouseEventCatcher
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Mouse event: rollOver
    Click Alert    OK

Create Mouse Up Event
    Select Index    ${button_bar}    ${mouse_view}
    Create Mouse Up Event    mouseEventCatcher
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Mouse event: mouseUp
    Click Alert    OK

Double Click
    Select Index    ${button_bar}    ${mouse_view}
    Double Click    dataGrid1
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Mouse event: doubleClick
    Click Alert    OK

Double Click Data Grid Component
    Select Index    ${button_bar}    ${mouse_view}
    Double Click Data Grid Component    dataGrid1    0    0
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Mouse event: doubleClick

Drag Element To

Ensure Enabled State
    Select Index    ${button_bar}    ${buttons_view}
    Ensure Enabled State    ${button_bar}    ${True}
    Ensure Enabled State    disabledButton    ${False}

Ensure Exists
    Ensure Exists    ${button_bar}    ${True}
    Ensure Exists    none_bar    ${False}

Ensure Visibility
    Select Index    ${button_bar}    ${buttons_view}
    Ensure Visibility    clickButton    ${True}
    Ensure Visibility    invisibleButton    ${False}

Enter Date
    Select Index    ${button_bar}    ${date_view}
    Enter Date    dateField    20.11.2011
    ${date}=    Get Text    selectedDate
    Should Be Equal    ${date}    Selected date: 20/11/2011

Enter Date To Data Grid Cell

Enter Text
    Click    buttonBar    Buttons view
    Enter text    alertText    test
    ${text}=    Get Text    alertText
    Should be equal    test    ${text}
    Enter text    alertText    ing    ${True}
    ${text}=    Get Text    alertText
    Should be equal    testing    ${text}
    Enter text    alertText    reset    ${False}
    ${text}=    Get Text    alertText
    Should be equal    reset    ${text}

Exists
    Select Index    ${button_bar}    ${buttons_view}
    ${exists}=    Exists    ${button_bar}
    Should Be True    ${exists}
    ${exists}=    Exists    clickButton
    Should Be True    ${exists}
    ${exists}=    Exists    notButton
    Should Not Be True    ${exists}

Expand Data Grid Elements

Get Alert Text
    Select Index    ${button_bar}    ${buttons_view}
    Click    alertButton
    ${alert_text}=    Get Alert Text
    Should Be Equal    Alert! The world has ended!    ${alert_text}

Get Api Version
    ${api_version}=    Get Api Version
    Should Be Equal    ${api_version}    28

Get Child Elements
    ${children}=    Get Child Elements    viewStack    ${True}    ${False}
    Should Contain    ${children}    viewStack
    Should Contain    ${children}    buttons
    ${children}=    Get Child Elements    viewStack    ${False}    ${False}
    Should Not Contain    ${children}    viewStack
    Should Contain    ${children}    buttons
    ${children}=    Get Child Elements    viewStack    ${True}    ${True}
    Should Contain    ${children}    viewStack
    Should Contain    ${children}    buttons
    Should Not Contain    ${children}    radioButtons
    ${children}=    Get Child Elements    viewStack    ${False}    ${True}
    Should Not Contain    ${children}    viewStack
    Should Contain    ${children}    buttons
    Should Not Contain    ${children}    radioButtons

Get Combobox Selected Item
    Select Index    ${button_bar}    ${combo_box_view}
    ${selected_item}=    Get Combobox Selected Item    comboBox
    Should Be Equal    ${selected_item}    Element = Element1, 1, true
    Select Combobox Item By Label    comboBox    Element = Element2, 2, false
    ${selected_item}=    Get Combobox Selected Item    comboBox
    Should Be Equal    ${selected_item}    Element = Element2, 2, false
    Select Combobox Item By Label    comboBox    Element = Element3, 3, true
    ${selected_item}=    Get Combobox Selected Item    comboBox
    Should Be Equal    ${selected_item}    Element = Element3, 3, true

Get Combobox Values
    Select Index    ${button_bar}    ${combo_box_view}
    ${values}=    Get Combobox Values    comboBox
    Should Contain    ${values}    Element = Element2, 2, false

Get Component Info
    Select Index    ${button_bar}    ${buttons_view}
    ${info}=    Get Component Info    clickButton
    @{list}=    Split String    ${info}    ,
    Length Should Be    ${list}    4

Get Data Grid Cell Label
    Select Index    ${button_bar}    ${data_grid_view}
    ${value}=    Get Data Grid Cell Label    dataGrid    0    0
    Should Be Equal    Element1    ${value}
    ${value}=    Get Data Grid Cell Label    dataGrid    2    0
    Should Be Equal    Element3    ${value}

Get Data Grid Cell Value
    Select Index    ${button_bar}    ${data_grid_view}
    ${value}=    Get Data Grid Cell Value    dataGrid    1    1
    Should Be Equal    2    ${value}
    ${value}=    Get Data Grid Cell Value    dataGrid    2    0
    Should Be Equal    Element3    ${value}

Get Data Grid Component Label
    Select Index    ${button_bar}    ${data_grid_view}
    ${label}=    Get Data Grid Component Label    dataGrid    1    2
    Should Be Equal    ${label}    3

Get Data Grid Field Count
    Select Index    ${button_bar}    ${data_grid_view}
    ${count}=    Get Data Grid Field Count    dataGrid    ${True}
    Should Be Equal    3    ${count}
    ${count}=    Get Data Grid Field Count    dataGrid    ${False}
    Should Be Equal    3    ${count}

Get Data Grid Field Data Fields
    Select Index    ${button_bar}    ${data_grid_view}
    @{fields}=    Get Data Grid Field Data Fields    dataGrid    ${True}
    Should Contain    ${fields}    attribute1
    @{fields}=    Get Data Grid Field Data Fields    dataGrid    ${False}
    Should Contain    ${fields}    attribute3

Get Data Grid Field Label By Row Index
    Select Index    ${button_bar}    ${data_grid_view}
    ${value}=    Get Data Grid Field Label By Row Index    dataGrid    attribute1    1
    Should Be Equal    Element2    ${value}
    ${value}=    Get Data Grid Field Label By Row Index    dataGrid    attribute2    2
    Should Be Equal    3    ${value}

Get Data Grid Field Value By Row Index
    Select Index    ${button_bar}    ${data_grid_view}
    ${value}=    Get Data Grid Field Value By Row Index    dataGrid    attribute1    1
    Should Be Equal    Element2    ${value}
    ${value}=    Get Data Grid Field Value By Row Index    dataGrid    attribute2    2
    Should Be Equal    3    ${value}

Get Data Grid Field Values
    Select Index    ${button_bar}    ${data_grid_view}
    @{values}=    Get Data Grid Field Values    dataGrid    1
    Should Contain    ${values}    2
    @{values}=    Get Data Grid Field Values    dataGrid    2
    Should Contain    ${values}    false

Get Data Grid Row Count
    Select Index    ${button_bar}    ${data_grid_view}
    ${count}=    Get Data Grid Row Count    dataGrid
    Should Be Equal    3    ${count}

Get Data Grid Row Index By Field Label
    Select Index    ${button_bar}    ${data_grid_view}
    ${index}=    Get Data Grid Row Index By Field Label    dataGrid    attribute1    Element3
    Should Be Equal    2    ${index}
    ${index}=    Get Data Grid Row Index By Field Label    dataGrid    attribute2    2
    Should Be Equal    1    ${index}

Get Data Grid Row Index By Field Value
    Select Index    ${button_bar}    ${data_grid_view}
    ${index}=    Get Data Grid Row Index By Field Value    dataGrid    attribute1    Element3
    Should Be Equal    2    ${index}
    ${index}=    Get Data Grid Row Index By Field Value    dataGrid    attribute2    2
    Should Be Equal    1    ${index}

Get Data Grid Values
    Select Index    ${button_bar}    ${data_grid_view}
    @{values}=    Get Data Grid Values    dataGrid    ${True}
    Should Contain    ${values}[0]    Element1
    @{values}=    Get Data Grid Values    dataGrid    ${False}
    Should Contain    ${values}[1]    false

Get Date
    Select Index    ${button_bar}    ${date_view}
    Enter Date    dateField    20.01.2001
    ${date}=    Get Date    dateField
    Should Be Equal    ${date}    20/01/2001

Get Error String
    Select Index    ${button_bar}    ${buttons_view}
    ${error}=    Get Error String    errorButton
    Should Be Equal    ''    '${error}'
    Click    errorButton
    ${error}=    Get Error String    errorButton
    Should Be Equal    I have an error!    ${error}

Get Global Position
    ${position}=    Get Global Position    buttonBar
    @{coordinates}=    Split String    ${position}    ,
    Length Should Be    ${coordinates}    2

Get Number Of Selected Items
    Select Index    ${button_bar}    ${data_grid_view}
    Select By Matching On Field    dataGrid    attribute1    Element3
    ${number}=    Get Number Of Selected Items    dataGrid
    Should Be Equal    1    ${number}
    Select By Matching On Field    dataGrid    attribute1    Element2    ${True}
    ${number}=    Get Number Of Selected Items    dataGrid
    Should Be Equal    2    ${number}

Get Path For Locator
    Select Index    ${button_bar}    ${buttons_view}
    ${path}=    Get Path For Locator    viewStack/clickButton
    Should Contain    ${path}    viewStack

Get Properties
    Select Index    ${button_bar}    ${buttons_view}
    ${values}=    Get Properties    clickButton    id    name    label
    Should Be Equal    ${values}    clickButton,clickButton,Click

Get Property
    Click    buttonBar    Buttons view
    ${property}=    Get Property    buttonClicks    id
    Should be equal    buttonClicks    ${property}
    ${property}=    Get Property    buttonClicks    text
    Should be equal    Number of clicks: 0    ${property}
    ${property}=    Get Property    alertText    className
    Should be equal    TextInput    ${property}
    ${property}=    Get Property    buttonClicks    name
    Should be equal    buttonClicks    ${property}

Get Selected Item At Index
    Select Index    ${button_bar}    ${data_grid_view}
    Select By Matching On Field    dataGrid    attribute1    Element3
    ${selected_index}=    Get Selection Index    dataGrid
    Should Be Equal    ${selected_index}    2
    Select By Matching On Field    dataGrid    attribute1    Element2    ${True}
    ${selected_item}=    Get Selected Item At Index    dataGrid    0
    Should Be Equal    ${selected_item}    Element = Element3, 3, true
    ${selected_item}=    Get Selected Item At Index    dataGrid    1
    Should Be Equal    ${selected_item}    Element = Element2, 2, false

Get Selection Index
    Select Index    ${button_bar}    ${combo_box_view}
    ${index}=    Get Selection Index    comboBox
    Should Be Equal    0    ${index}
    Select Index    comboBox    2
    ${index}=    Get Selection Index    comboBox
    Should Be Equal    2    ${index}

Get Stepper Value
    Select Index    ${button_bar}    ${stepper_view}
    ${value}=    Get Stepper Value    stepper
    Should Be Equal    0    ${value}
    Set Stepper Value    stepper    10
    ${value}=    Get Stepper Value    stepper
    Should Be Equal    10    ${value}
    Set Stepper Value    stepper    30
    ${value}=    Get Stepper Value    stepper
    Should Be Equal    30    ${value}

Get Tab Labels
    Select Index    ${button_bar}    ${tab_navigator_view}
    ${tab_labels}=    Get Tab Labels    tabNavigator
    Should Be Equal    ${tab_labels}    Tab 1,Tab 2,Tab 3

Get Text
    Select Index    ${button_bar}    ${buttons_view}
    ${text}=    Get Text    buttonClicks
    Should Be Equal    ${text}    Number of clicks: 0
    ${text}=    Get Text    clickButton
    Should Be Equal    ${text}    Click

Is Alert Visible
    Select Index    ${button_bar}    ${buttons_view}
    Click    alertButton
    ${alert_visible}=    Is Alert Visible
    Should Be True    ${alert_visible}
    Click Alert    OK
    ${alert_visible}=    Is Alert Visible
    Should Not Be True    ${alert_visible}

Is Checkbox Checked
    Select Index    ${button_bar}    ${check_box_view}
    ${checked}=    Is Checkbox Checked    checkBox
    Should Be True    ${checked}
    Set Checkbox Value    checkBox    ${False}
    ${checked}=    Is Checkbox Checked    checkBox
    Should Not Be True    ${checked}
    Set Checkbox Value    checkBox    ${True}
    ${checked}=    Is Checkbox Checked    checkBox
    Should Be True    ${checked}

Is Checkbox In Data Grid Checked
    Select Index    ${button_bar}    ${data_grid_view}
    ${checked}=    Is Checkbox In Data Grid Checked    dataGrid    0    2
    Should Be True    ${checked}
    ${checked}=    Is Checkbox In Data Grid Checked    dataGrid    1    2
    Should Not Be True    ${checked}
    ${checked}=    Is Checkbox In Data Grid Checked    dataGrid    2    2
    Should Be True    ${checked}

Is Enabled
    Select Index    ${button_bar}    ${buttons_view}
    ${enabled}=    Is Enabled    clickButton
    Should Be True    ${enabled}
    ${enabled}=    Is Enabled    disabledButton
    Should Not Be True    ${enabled}

Is Function Defined
    ${exists}=    Is Function Defined    getFlexAPIVersion
    Should Be True    ${exists}
    ${exists}=    Is Function Defined    getFlexSizeOfTheMoon
    Should Not Be True    ${exists}

Is Label In Combo Data
    Select Index    ${button_bar}    ${combo_box_view}
    ${found}=    Is Label In Combo Data    comboBox    Element = Element3, 3, true
    Should Be True    ${found}
    ${found}=    Is Label In Combo Data    comboBox    Element = Element3, 3, false
    Should Not Be True    ${found}

Is Radiobutton Checked
    Select Index    ${button_bar}    ${radio_buttons_view}
    Set Radiobutton Value    radioButton3
    ${radio1_checked}=    Is Radiobutton Checked    radioButton1
    Should Not Be True    ${radio1_checked}
    ${radio2_checked}=    Is Radiobutton Checked    radioButton2
    Should Not Be True    ${radio2_checked}
    ${radio3_checked}=    Is Radiobutton Checked    radioButton3
    Should Be True    ${radio3_checked}
    Set Radiobutton Value    radioButton2
    ${radio1_checked}=    Is Radiobutton Checked    radioButton1
    Should Not Be True    ${radio1_checked}
    ${radio2_checked}=    Is Radiobutton Checked    radioButton2
    Should Be True    ${radio2_checked}
    ${radio3_checked}=    Is Radiobutton Checked    radioButton3
    Should Not Be True    ${radio3_checked}
    Set Radiobutton Value    radioButton3
    ${radio1_checked}=    Is Radiobutton Checked    radioButton1
    Should Not Be True    ${radio1_checked}
    ${radio2_checked}=    Is Radiobutton Checked    radioButton2
    Should Not Be True    ${radio2_checked}
    ${radio3_checked}=    Is Radiobutton Checked    radioButton3
    Should Be True    ${radio3_checked}

Is Text Present
    Select Index    ${button_bar}    ${buttons_view}
    ${present}=    Is Text Present    buttonClicks    Number of clicks: 0
    Should Be True    ${present}
    ${present}=    Is Text Present    buttonClicks    Number of clicks: 1
    Should Not Be True    ${present}
    ${present}=    Is Text Present    buttonClicks    Number of clicks
    Should Be True    ${present}

Is Visible
    Select Index    ${button_bar}    ${buttons_view}
    ${visible}=    Is Visible    clickButton
    Should Be True    ${visible}
    ${visible}=    Is Visible    invisibleButton
    Should Not Be True    ${visible}

Press Enter On Element
    Select Index    ${button_bar}    ${mouse_view}
    Press Enter On Element    keyboardEventCatcher
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Key event: keyUp, 13
    Click Alert    OK

Press Key On Element
    Select Index    ${button_bar}    ${mouse_view}
    Press Key On Element    keyboardEventCatcher    66
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Key event: keyUp, 66
    Click Alert    OK

Press Space On Element
    Select Index    ${button_bar}    ${mouse_view}
    Press Space On Element    keyboardEventCatcher
    ${alert_text}=    Get Alert Text
    Should Be Equal    ${alert_text}    Key event: keyUp, 32
    Click Alert    OK

Select
    Select Index    ${button_bar}    ${combo_box_view}
    ${selected_item}=    Get Combobox Selected Item    comboBox
    Should Be Equal    ${selected_item}    Element = Element1, 1, true
    Select    comboBox    Element = Element2, 2, false
    ${selected_item}=    Get Combobox Selected Item    comboBox
    Should Be Equal    ${selected_item}    Element = Element2, 2, false

Select By Matching On Field
    Select Index    ${button_bar}    ${data_grid_view}
    Select By Matching On Field    dataGrid    attribute1    Element3
    ${selected_index}=    Get Selection Index    dataGrid
    Should Be Equal    ${selected_index}    2
    Select By Matching On Field    dataGrid    attribute1    Element2    ${True}
    ${selected_item}=    Get Selected Item At Index    dataGrid    0
    Should Be Equal    ${selected_item}    Element = Element3, 3, true
    ${selected_item}=    Get Selected Item At Index    dataGrid    1
    Should Be Equal    ${selected_item}    Element = Element2, 2, false

Select Combobox Item By Label
    Select Index    ${button_bar}    ${combo_box_view}
    ${selected_item}=    Get Combobox Selected Item    comboBox
    Should Be Equal    ${selected_item}    Element = Element1, 1, true
    Select Combobox Item By Label    comboBox    Element = Element2, 2, false
    ${selected_item}=    Get Combobox Selected Item    comboBox
    Should Be Equal    ${selected_item}    Element = Element2, 2, false
    Select Combobox Item By Label    comboBox    Element = Element3, 3, true
    ${selected_item}=    Get Combobox Selected Item    comboBox
    Should Be Equal    ${selected_item}    Element = Element3, 3, true

Select Combobox Item By Label From Data Grid

Select Data Grid Index
    Select Index    ${button_bar}    ${data_grid_view}
    ${selected_item}=    Get Text    selectedGridItem
    Should Be Equal    '${selected_item}'    'Selected item: '
    Select Data Grid Index    dataGrid    2
    ${selected_item}=    Get Text    selectedGridItem
    Should Be Equal    '${selected_item}'    'Selected item: '
    Click Selected Data Grid Item    dataGrid
    ${selected_item}=    Get Text    selectedGridItem
    Should Be Equal    ${selected_item}    Selected item: Element = Element3, 3, true

Select Index
    Select Index    ${button_bar}    ${buttons_view}
    ${visible}=    Is Visible    buttonClicks
    Should Be True    ${visible}
    Select Index    ${button_bar}    ${check_box_view}
    ${visible}=    Is Visible    checkBox
    Should Be True    ${visible}
    Select Index    ${button_bar}    ${data_grid_view}
    ${visible}=    Is Visible    dataGrid
    Should Be True    ${visible}
    Select Index    dataGrid    1
    Select Index    dataGrid    2    ${True}
    ${item1}=    Get Selected Item At Index    dataGrid    0
    ${item2}=    Get Selected Item At Index    dataGrid    1
    Should Be Equal    ${item1}    Element = Element2, 2, false
    Should Be Equal    ${item2}    Element = Element3, 3, true

Select Tree Item
    Select Index    ${button_bar}    ${tree_view}
    Select Tree Item    tree    node    Node1
    ${selected_item}=    Get Text    selectedTreeItem
    Should Be Equal    ${selected_item}    Selected item: Node1
    Select Tree Item    tree    node    Node1Item1
    ${selected_item}=    Get Text    selectedTreeItem
    Should Be Equal    ${selected_item}    Selected item: Node1Item1
    Select Tree Item    tree    node    Node1Item3SubItem2
    ${selected_item}=    Get Text    selectedTreeItem
    Should Be Equal    ${selected_item}    Selected item: Node1Item3SubItem2

Set Checkbox Value
    Select Index    ${button_bar}    ${check_box_view}
    ${checked}=    Is Checkbox Checked    checkBox
    Should Be True    ${checked}
    Set Checkbox Value    checkBox    ${False}
    ${checked}=    Is Checkbox Checked    checkBox
    Should Not Be True    ${checked}
    Set Checkbox Value    checkBox    ${True}
    ${checked}=    Is Checkbox Checked    checkBox
    Should Be True    ${checked}

Set Data Grid Cell Value
    Select Index    ${button_bar}    ${data_grid_view}
    Set Property    dataGrid    editable    true
    Set Data Grid Cell Value    dataGrid    0    0    test
    Set Data Grid Cell Value    dataGrid    0    1    123
    ${cell_value}=    Get Data Grid Cell Value    dataGrid    0    0
    Should Be Equal    ${cell_value}    test
    ${cell_value}=    Get Data Grid Cell Value    dataGrid    0    1
    Should Be Equal    ${cell_value}    123

Set Data Grid Checkbox Value
    Select Index    ${button_bar}    ${data_grid_view}
    ${cell_value}=    Get Data Grid Cell Value    dataGrid    0    2
    Should Be Equal    ${cell_value}    true
    Set Data Grid Checkbox Value    dataGrid    0    2    ${False}
    ${cell_value}=    Get Data Grid Cell Value    dataGrid    0    2
    Should Be Equal    ${cell_value}    false

Set Focus
    Select Index    ${button_bar}    ${buttons_view}
    ${visible}=    Is Visible    invisibleButton
    Should Not Be True    ${visible}
    Set Focus    invisibleButton
    ${visible}=    Is Visible    invisibleButton
    Should Be True    ${visible}
    Set Focus    clickButton
    ${visible}=    Is Visible    invisibleButton
    Should Not Be True    ${visible}

Set Property
    ${visible}=    Get Property    ${button_bar}    visible
    Should Be Equal    true    ${visible}
    Set Property    ${button_bar}    visible    false
    ${visible}=    Get Property    ${button_bar}    visible
    Should Be Equal    false    ${visible}

Set Radiobutton Value
    Select Index    ${button_bar}    ${radio_buttons_view}
    Set Radiobutton Value    radioButton3
    ${radio1_checked}=    Is Radiobutton Checked    radioButton1
    Should Not Be True    ${radio1_checked}
    ${radio2_checked}=    Is Radiobutton Checked    radioButton2
    Should Not Be True    ${radio2_checked}
    ${radio3_checked}=    Is Radiobutton Checked    radioButton3
    Should Be True    ${radio3_checked}

Set Stepper Value
    Select Index    ${button_bar}    ${stepper_view}
    ${value}=    Get Stepper Value    stepper
    Should Be Equal    0    ${value}
    Set Stepper Value    stepper    10
    ${value}=    Get Stepper Value    stepper
    Should Be Equal    10    ${value}
    Set Stepper Value    stepper    30
    ${value}=    Get Stepper Value    stepper
    Should Be Equal    30    ${value}

Wait For Element To Be Visible
    Go To    ${flash_app_url}
    Wait For Element To Exist    ${button_bar}    10

Wait For Element To Exist
    Go To    ${flash_app_url}
    Wait For Element To Be Visible    ${button_bar}    10

*** Keywords ***
Suite Start
    Open Browser    ${EMPTY}    ${browser}
    Maximize Browser Window

Suite Stop
    Close Browser

Start
    Go to    ${flash_app_url}
    Is Enabled    buttonBar
