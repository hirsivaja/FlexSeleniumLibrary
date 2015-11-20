*** Settings ***

Documentation    Test cases for Flex Selenium library
Library    FlexSeleniumLibrary    ${flash_app_name}    none
Suite Setup    Suite Start
Suite Teardown    Suite Stop
Test Setup    Start

*** Variables ***

${flash_app_url}    http://localhost:8080/flex3test/index.html
${flash_app_name}    Flex3Tester

${browser}    firefox

*** Test Cases ***
Click Button
    Click    buttonBar    Buttons view
    Click    clickButton
    ${text}=    Get Text    buttonClicks
    Should be equal    Number of clicks: 1     ${text}
    Click    clickButton
    ${text}=    Get Text    buttonClicks
    Should be equal    Number of clicks: 2     ${text}
    Click    clickButton
    ${text}=    Get Text    buttonClicks
    Should be equal    Number of clicks: 3     ${text}
    Click    buttonBar    DataGrid view
    ${visible}=    Is visible    dataGrid
    Should be true     ${visible}

Enter Text
    Click    buttonBar    Buttons view
    Enter text    alertText    test
    ${text}=    Get Text    alertText
    Should be equal   test    ${text}
    Enter text    alertText    ing    True
    ${text}=    Get Text    alertText
    Should be equal   testing    ${text}
    Enter text    alertText    reset    False
    ${text}=    Get Text    alertText
    Should be equal   reset    ${text}

Get Property
    Click    buttonBar    Buttons view
    ${property}=    Get Property    buttonClicks    id
    Should be equal   buttonClicks    ${property}
    ${property}=    Get Property    buttonClicks    text
    Should be equal   Number of clicks: 0    ${property}
    ${property}=    Get Property    alertText    className
    Should be equal   TextInput    ${property}
    ${property}=    Get Property    buttonClicks    name
    Should be equal   buttonClicks    ${property}

*** Keywords ***
Suite Start
    Open Browser   ${browser}

Suite Stop
    Exit Browser

Start
    Get   ${flash_app_url}
    Sleep    1