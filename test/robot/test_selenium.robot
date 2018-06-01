*** Settings ***

Documentation    Test cases for Flex Selenium library
Library    FlexSeleniumLibrary    ${flash_app_name}
Suite Setup    Suite Start
Suite Teardown    Suite Stop
Test Setup    Start

*** Variables ***

${flash_app_url}    http://www.google.com
${flash_app_name}    ${EMPTY}

${browser}    firefox

*** Test Cases ***
Google test
    Input text    lst-ib    test
    Press key    lst-ib    \\13
    Wait until page contains    Test - Wikipedia

*** Keywords ***
Suite Start
    Open Browser   about:blank    ${browser}
    Maximize Browser Window

Suite Stop
    Close Browser

Start
    Go to   ${flash_app_url}
    Wait until element is enabled    lst-ib