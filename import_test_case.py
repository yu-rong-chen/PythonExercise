import openpyxl
# There are five tools
mypath='C:\\Users\\Administrator\\Pictures\\test\\testcase.xlsx'
wb = openpyxl.Workbook()
sheet=wb.get_sheet_by_name('Sheet')

tool=['Xorsyst, ','BigVM, ','MaxMem, ','XorPMEM, ','vMotion_Migration, ','vMotion_Migration_XorPMEM, ','Live_Migration, ','Storage_Migration, ',\
    'POLX, ','MaxCPU, ','SCX, ']
Memory=['8GB','4GB','4GB','32GB','16GB','32GB','16GB','16GB','4GB','4GB','8GB']
Host=['ESXi series, ','Hyper-V series, ']
guest=['windows and linux (EX,W2K19 and RH82)','windows (W2K19)']
summary_txt='non-zero'

for i in range (0,11):
    try:
        for j in range (0,6):
            if tool[i] == 'Xorsyst, 'or tool[i] == 'XorPMEM, 'or tool[i] =='MaxMem, ':
                defaultMEMTEST=['AUTO','7','0','NULL','re-use VM','Unknown']
            elif tool[i] == 'BigVM, 'or tool[i] == 'Live_Migration, 'or tool[i]=='Storage_Migration, ' or tool[i]=='vMotion_Migration, 'or tool[i]=='vMotion_Migration_XorPMEM, ':
                defaultMEMTEST=['1','AUTO','0','NULL','re-use VM','Unknown']
            elif tool[i] == 'POLX, 'or tool[i] =='MaxCPU, 'or tool[i] == 'SCX, ':
                defaultMEMTEST=['NULL','re-use VM','Unknown']
        #--Priority-------------------------------------------------------------------------
            if (i==0 and j==0) or (i==1 and j==0) or (i==10 and j==0):
                Priority='RAT'
            elif (i==2,10) and j==0:
                Priority='FAST'
            else:
                if defaultMEMTEST[j] == 'Unknown':
                    Priority='TOFT3'
                else:
                    Priority='TOFT'
        #---Test Item Host version-----------------------------------------------------------------------
            if tool[i] == 'Xorsyst, 'or tool[i] == 'BigVM, 'or tool[i]=='MaxMem, 'or tool[i] =='XorPMEM, 'or tool[i]=='POLX, ' or tool[i] =='SCX, 'or tool[i]=='MaxCPU, 'or tool[i]=='vMotion_Migration, 'or tool[i]=='vMotion_Migration_XorPMEM, ':
                version=0
            elif tool[i] == 'Live_Migration, 'or tool[i]=='Storage_Migration, ':
                version=1
        #-----Test  Item ----------------------------------------------------------
            if defaultMEMTEST[j]=='re-use VM':
                Test_Item=str('Use the default MEMTEST value, '+tool[i])+str(Host[version])+'Set Memory TEST as default "'\
                        +str(defaultMEMTEST[0])+'",both '+str(guest[version])+', enable re-use VM'
            elif defaultMEMTEST[j]=='Unknown':
                Test_Item=str('Use the default MEMTEST value, '+tool[i])+str(Host[version])+'Set Memory TEST as default "'\
                        +str(defaultMEMTEST[0])+'",both '+str(guest[version])+', shutdownVM during Test waiting'
            elif defaultMEMTEST[j]=='AUTO':
                Test_Item=str('Use case 5:  Assign AUTO in scenario, '+tool[i])+str(Host[version])+'Set Memory TEST as "'\
                        +str(defaultMEMTEST[j])+'",both '+str(guest[version])
            elif defaultMEMTEST[j]=='1':
                Test_Item=str('Use case 4:  Assign any integer in scenario, '+tool[i])+str(Host[version])+'Set Memory TEST as "'\
                        +str(defaultMEMTEST[j])+'",both '+str(guest[version])
            elif defaultMEMTEST[j]=='7':
                Test_Item=str('Use case 4:  Assign any integer in scenario, '+tool[i])+str(Host[version])+'Set Memory TEST as "'\
                        +str(defaultMEMTEST[j])+'",both '+str(guest[version])
            elif defaultMEMTEST[j]=='0':
                Test_Item=str('Use case 3:  Assign 0 in scenario - disable MEMTEST, '+tool[i])+str(Host[version])+'Set Memory TEST as "'\
                        +str(defaultMEMTEST[j])+'",both '+str(guest[version])
            elif defaultMEMTEST[j]=='NULL':
                if tool[i] == 'POLX, 'or tool[i] =='MaxCPU, 'or tool[i] == 'SCX, ':
                    Test_Item=str('Use case 2: MEMTEST in Hidden -  disabled key, '+tool[i])+str(Host[version])+'Set Memory TEST as "'\
                            +str(defaultMEMTEST[j])+'",both '+str(guest[version])
                else:
                    Test_Item=str('Use case 1:  Enter empty in scenario - disable MEMTEST, '+tool[i])+str(Host[version])+'Set Memory TEST as "'\
                            +str(defaultMEMTEST[j])+'",both '+str(guest[version])
            
        #---Expect results------------------------------------------------------------------------
            if defaultMEMTEST[j] == 'NULL':
                Expect_Result='1. check MEMTEST in "source_scenario.txt" is MEMTEST:""'\
                            +'. 2. check MEMTEST column in "summary.txt" is 0'\
                            +'. 3. MEMTEST value in "xorsystsetup" is not exist'
            elif defaultMEMTEST[j] == 'AUTO':
                Expect_Result='1. check MEMTEST in "source_scenario.txt" is '+defaultMEMTEST[j]\
                            +'. 2. check MEMTEST column in "summary.txt" is '+summary_txt\
                            +'. 3. MEMTEST value in "xorsystsetup" is the same as "summary.txt"'
            elif defaultMEMTEST[j] == 're-use VM':
                if tool[i] == 'POLX, ' or tool[i]=='MaxCPU, 'or tool[i]=='SCX, ':
                    Expect_Result='1. check MEMTEST in "source_scenario.txt" is MEMTEST:""'\
                                +'. 2. check MEMTEST column in "summary.txt" is 0'\
                                +'. 3. MEMTEST value in "xorsystsetup" is not exist' 
                else:
                    Expect_Result='1. check MEMTEST in "source_scenario.txt" is '+defaultMEMTEST[0]\
                                +'. 2. check MEMTEST column in "summary.txt" is '+summary_txt\
                                +'. 3. MEMTEST value in "xorsystsetup" is the same as "summary.txt"'
            elif defaultMEMTEST[j] == 'Unknown':
                if tool[i]=='POLX, ' or tool[i]=='MaxCPU, 'or tool[i]=='SCX, ':
                    Expect_Result='1. check MEMTEST in "source_scenario.txt" is MEMTEST:""'\
                                +'. 2. check MEMTEST column in "summary.txt" is Unknown'
                else:
                    Expect_Result='1. check MEMTEST in "source_scenario.txt" is '+defaultMEMTEST[0]\
                                +'. 2. check MEMTEST column in "summary.txt" is '+defaultMEMTEST[j]
            else:
                Expect_Result='1. check MEMTEST in "source_scenario.txt" is '+defaultMEMTEST[j]\
                            +'. 2. check MEMTEST column in "summary.txt" is '+defaultMEMTEST[j]\
                            +'. 3. MEMTEST value in "xorsystsetup" is the same as "summary.txt"'
        #-----Steps--------------------------------------------------------------------------------    
            if defaultMEMTEST[j] == 'AUTO':
                Steps='1. Set Memory TEST as "'+defaultMEMTEST[j]\
                    +'". 2. VM memory larger than '+Memory[i]
            elif defaultMEMTEST[j] == 're-use VM':
                Steps='1. Set Memory TEST as "'+defaultMEMTEST[0]\
                    +'". 2. VM memory larger than '+Memory[i]\
                    +'. 3. Complete job. 4. Enable re-reuse VM bottom and execute again.'
            elif defaultMEMTEST[j] == 'Unknown':
                Steps='1. Set Memory TEST as "'+defaultMEMTEST[0]\
                    +'". 2. VM memory larger than '+Memory[i]\
                    +'. 3.Shut down VM during test waiting'
            else:
                Steps='1. Set Memory TEST as "'+defaultMEMTEST[j]
        #-----Save to excel------------------------------------------------------------------------
            sheet_id=str(6*i+j+1)
            sheet['A'+sheet_id]= str(tool[i])
            sheet['B'+sheet_id]= int(sheet_id)+1926
            sheet['C'+sheet_id]= Priority 
            sheet['D'+sheet_id]= 'MEMTEST configuration verification'
            sheet['E'+sheet_id]= Test_Item
            sheet['F'+sheet_id]= str(Expect_Result)
            sheet['G'+sheet_id]= str(Steps)
            wb.save(mypath)
    except Exception:
            print('default is NULL')
            continue
