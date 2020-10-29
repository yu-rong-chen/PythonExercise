*** Settings ***
Documentation  This is some basic info about the whole suite
Library   SeleniumLibrary

*** Variables ***
${Login URL}    https://kimconnect.com/how-to-transfer-files-via-ssh-or-winrm/

*** Test Cases ***
User must sign in to check out
    [Documentation]  This is some bais info about the test
    [Tags]  Smoke  
    Calls python Keywords
    
        
*** Keywords ***
Calls python Keywords
    Open Browser    ${Login URL}    chrome
    Input Text  name=s  Hi