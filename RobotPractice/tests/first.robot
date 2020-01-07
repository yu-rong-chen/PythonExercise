*** Settings ***
Documentation  This is some basic info about the whole suite
Library   SeleniumLibrary  
Library   FindElement.py

*** Variables ***

*** Test Cases ***
User must sign in to check out
    [Documentation]  This is some bais info about the test
    [Tags]  Smoke  
    Calls python Keywords
    # driver.get(WebUrl)
    # Open Browser  https://10.10.124.12/#/job/show/overview/r/rest/vtc/jobs/1  chrome    
#     wait until page contains element  xpath=//*[@id="hp-login-user"]
#     Input Text  xpath=//*[@id="hp-login-user"]  Administrator
#     Input Text  xpath=//*[@id="hp-login-password"]  Compaq123
#     Click Button  xpath=//*[@id="hp-login-button"]
#     wait until page contains element  xpath=//*[@id="hp-main-menu-control"]
# User need to add Repository
#     wait until page contains element  xpath=//*[@id="hp-main-menu"]/div/ul
#     # $(URL)  =  Findhref
#     # Input Text  //*[@id='hp-main-menu']/div/ul/li[2]/ul/li[1]/a  $(URL)
#     Calls python Keywords
        
*** Keywords ***
Calls python Keywords
    Open Browser  https://10.10.124.7/#/job/show/overview/r/rest/vtc/jobs/9  chrome
    # FindElement.Getdriver
    # ${driver}=   FindElement.Getdriver
    # ${WebUrl}=   Get Location

#     ${href_url}=   Findhref   //*[@id='hp-main-menu']/div/ul/li[2]/ul/li[1]/a   ${WebUrl}   ${driver}
#     # Open Browser  href_url  chrome
#     # Findhref(xpath=//*[@id='hp-main-menu']/div/ul/li[2]/ul/li[1]/a)
