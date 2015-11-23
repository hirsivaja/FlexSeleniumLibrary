*** Settings ***

Documentation    Test cases for Flex Selenium library
Library    FlexSeleniumLibrary    ${flash_app_name}    none
Suite Setup    Suite Start
Suite Teardown    Suite Stop
Test Setup    Start

*** Variables ***

${flash_app_url}    http://localhost:8080/flex4test/index.html
${flash_app_name}    Flex4Tester

${browser}    firefox

*** Test Cases ***
Click Button
    ${buttonClicks}=    FP ID Locator    buttonClicks
    ${text}=    FP Get Text Value    ${buttonClicks}
    Should contain    ${text}    Number of clicks: 0
    FP Click    id:'clickButton'
    ${text}=    FP Get Text Value    ${buttonClicks}
    Should contain    ${text}    Number of clicks: 1

Enter Text
    FP Type    id:'alertText'    test
    ${text}=    FP Get Text Value    id:'alertText'
    Should contain    ${text}    test

Get Property
    ${property}=    FP Get Property Value    id:'buttonClicks'    id
    Should be equal   buttonClicks    ${property}
    ${property}=    FP Get Property Value    id:'buttonClicks'    text
    Should be equal   Number of clicks: 0    ${property}

*** Keywords ***
Suite Start
    Open Browser   ${browser}

Suite Stop
    Exit Browser

Start
    Get   ${flash_app_url}
    FP Wait For Flex Ready    10