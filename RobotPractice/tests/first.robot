*** Settings ***
Documentation  This is some basic info about the whole suite
Library  Selenium2Library

*** Variables ***

*** Test Cases ***
User must sign in to check out
    [Documentation]  This is some basic info about the test
    [Tags]  Robot 
    Open Browser  https://robotframework.org/  chrome
    Close Browser 

*** Keywords ***