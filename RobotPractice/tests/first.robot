*** Settings ***
Documentation  This is some basic info about the whole suite
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
User must sign in to check out
    [Documentation]  This is some bais info about the test
    [Tags]  Smoke  
    Open Browser  https://10.10.124.8/#/job/show/overview/r/rest/vtc/jobs/1  chrome
    SeleniumLibrary.wait until page contains element  xpath=//*[@id="hp-login-user"]
    SeleniumLibrary.Input Text  xpath=//*[@id="hp-login-user"]  Administrator
    SeleniumLibrary.Input Text  xpath=//*[@id="hp-login-password"]  Compaq123
User need to add Repository
    SeleniumLibrary.Click Button  xpath=//*[@id="hp-login-button"]
    SeleniumLibrary.wait until page contains element  xpath=//*[@id="hp-main-menu"]
    # SeleniumLibrary.Click Link  xpath=//*[@id="hp-main-menu"]


*** Keywords ***
