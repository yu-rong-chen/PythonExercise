## Regression 
rhel 83:
`robot -L trace:info -d reports  -V variables/ilorest.yaml --include rhel84 suites`

|**test ID**| **expected execute target**| **actual execute target**|**verified result**|
|--|--|--|--|
| 3516950 RHEL83 |Remote | Remote | pass|
| 3516884 SLES12 SP5 |Local|local| pass|
| 3516929 W2K19  |Local|Local|pass|
| 3516905 W2K16  |Remote|Remote|pass|

Prerequisites

    Get iLO FW Version 
        pass criteria: PTA get console output and meet "iLO" regular expression 
        fail: reger to error code: GET_ILO_FIRMWARE_ERROR 
            1. return message has "Current session has expired or is invalid, please login again", refer to error code: ILOREST_TIMEOUT
            2. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
            3. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
            4. other unexpected error message, refer to error code: OUT_OF_EXPECTED

    Get BIOS FW Version 
        pass: return message and meet "System ROM " regular expression 
        fail: refer to error code: GET_BIOS_FIRMWARE_ERROR
            1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
            2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
            3. other unexpected error message, refer to error code: OUT_OF_EXPECTED

    Get Host OS Versions 
        pass: return message and meet "Operating System" regular expression
        fail: return message is empty, refer to error code: GET_HOST_VERSION_ERROR

    Get iLOREST Versions
        pass: return message and meet "RESTful Interface Tool" regular expression
        fail: 
            1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
            2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
            3. other unexpected error message, refer to error code: OUT_OF_EXPECTED
Login

    Pass: return message has "Discovering data...Done"

    Fail: 
        1. lower case of login_mode in yaml not meet 'local' or 'remote', refer to error code:ILOREST_LOGIN_MODE_ERROR
        2. return message has no "Discovering data...Done"
            1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
            2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
            3. other unexpected error message, refer to error code: OUT_OF_EXPECTED

Download and Clear IEL Logs 

    Download IEL:

        Pass: ilorest download iel command excute successfully with no error message
        Fail: 
            1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
            2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
            3. other unexpected error message, refer to error code: OUT_OF_EXPECTED

    Check IEL:
        Pass: Check if IELlog.txt is json format. Show latest IELlog.txt conent in report.
        Fail: 
            1. If IELlog.txt is not json format, refer to error code: DECODE_JSON_FAILED
            2. if IELlog.txt not exist, refer to error code: FILE_CHECK_COMMAND_ERROR

    Clear IEL:
        Pass: return message has "Event log cleared successfully"
        Fail: in contrast with pass
            1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
            2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
            3. other unexpected error message, refer to error code: OUT_OF_EXPECTED
        Download IELclear.txt:
            Pass: ilorest download iel command excute successfully with no error message
            Fail: 
                1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
                2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
                3. other unexpected error message, refer to error code: OUT_OF_EXPECTED

    Check IEL:
        Pass: 1. Check if IELlogclear.txt is json format. 2. “Event log cleared “ should exist in IELlogclear.txt. 
        Fail: in contrast with pass
            1. "Event log cleared " not exist in IELlogclear.txt. refer to error code: ILOREST_CLEAR_IEL_ERROR
            2. If IELlogclear.txt is not json format, refer to error code: DECODE_JSON_FAILED
            3. if IELlogclear.txt not exist, refer to error code: FILE_CHECK_COMMAND_ERROR

Download and Clear IML Logs 

    Download IML:
        Pass: ilorest download iml command excute successfully with no error message
        Fail: 
            1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
            2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
            3. other unexpected error message, refer to error code: OUT_OF_EXPECTED

    Check IML:
        Pass: Check if IMLlog.txt is json format. Show latest IMLlog.txt conent in report.
        Fail: 
            1. If IMLlog.txt is not json format, refer to error code: DECODE_JSON_FAILED
            2. if IMLlog.txt not exist, refer to error code: FILE_CHECK_COMMAND_ERROR

    Clear IML:
        Pass: return message has "IML Cleared."
        Fail: in contrast with pass
            1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
            2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
            3. other unexpected error message, refer to error code: OUT_OF_EXPECTED
        Download IMLlogclear.txt:
            Pass: ilorest download iml command excute successfully with no error message
            Fail: 
                1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
                2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
                3. other unexpected error message, refer to error code: OUT_OF_EXPECTED
    Check IML:
        Pass: Check if IMLlogclear.txt is json format. 2. “IML Cleared' “ should exist in IMLlogclear.txt.
        Fail: 
            1. if IMLlogclear.txt not exist, refer to error code: FILE_CHECK_COMMAND_ERROR
            2. If IMLlogclear.txt is not json format, refer to error code: DECODE_JSON_FAILED
            3. "IML Cleared" not exist in IMLclear.txt. refer to error code: ILOREST_CLEAR_IML_ERROR 

    Insert One Entry to IML
        Pass: return message has "The operation completed successfully."
        Fail: in contrast with pass
            1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
            2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
            3. other unexpected error message, refer to error code: OUT_OF_EXPECTED
        Download IMLlog_insert.txt:
            Pass: ilorest download iml command excute successfully with no error message
            Fail: 
                1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
                2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
                3. other unexpected error message, refer to error code: OUT_OF_EXPECTED
    Check IML:
        Pass: 1. Check if IMLlog_insert.txt is json format. 2. "Add this message as part of testing" exist in IMLinsert.txt.
        Fail: in contrast with pass
            1. if IMLlog_insert.txt not exist, refer to error code: FILE_CHECK_COMMAND_ERROR
            2. If IMLlog_insert.txt is not json format, refer to error code: DECODE_JSON_FAILED
            3. "Add this message as part of testing" not exist in IMLlog_insert.txt. refer to error code: CHECK_IML_INSERT

Download and Clear AHS Logs 

    Download AHS 
        Pass: ilorest download ahs command excute successfully with no error message
        Fail: 
            1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
            2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
            3. other unexpected error message, refer to error code: OUT_OF_EXPECTED

    Check AHS
        Pass: 1. HPE.ahs should exist. 2. The size of HPE.ahs > 0. 
        Fail: in contrast with Pass
            1. HPE.ahs not exist, refer to error code: AHS_FAIL_DOWNLOAD
            2. size of HPE.ahs equal 0, refer to error code: AHS_SIZE_ZERO
            3. other unexpected error message, refer to error code: OUT_OF_EXPECTED

    Clear AHS
        Pass: return message has "One or more properties were changed and will not take effect until the device".
        Fail: in contrast with pass
            1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
            2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
            3. other unexpected error message, refer to error code: OUT_OF_EXPECTED
        Download AHS HPEclear.ahs
            Pass: ilorest download ahs command excute successfully with no error message
            Fail: 
                1. return error message has "ilorest: command not found", refer to error code: ILOREST_NOT_INSTALL
                2. return error message has "Command 'XXX' not found.", refer to error code: ILOREST_COMMAND_ERROR
                3. other unexpected error message, refer to error code: OUT_OF_EXPECTED
    Check AHS
        Pass: 1. HPEclear.ahs should exist. 2. The size of HPEclear.ahs > 0. 
        Fail: in contrast with Pass
            1. HPEclear.ahs not exist, refer to error code: AHS_FAIL_DOWNLOAD
            2. size of HPEclear.ahs equal 0, refer to error code: AHS_SIZE_ZERO
            3. other unexpected error message, refer to error code: OUT_OF_EXPECTED

    Should Not be Equal  ${ahs_size}  ${ahsclear_size}
        Pass: The size of HPE.ahs and HPEclear.ahs should not be equal
        Fail: in contrast with pass

Download Invalid Log Type 

        Pass: show error command: ‘Error: Log opted does not exist!’ 

Clear Invalid Log Type

        Pass: show error command: ‘Error: Log opted does not exist!’ 


