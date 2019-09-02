from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import requests
from bs4 import BeautifulSoup
import certifi
import html5lib  #pure-python library for parsing HTML
import prettytable as pt #build tabel
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
driver.maximize_window()
from WebScraping import WebdriverLoad
from WebScraping import go_into_iframe

#-------------------------------------Physical Memory----------------------------------------------
def Memory(soup):
##    print('\n--------I am Soup--------\n');print(soup)
    
    TableName= ('memoryTableSMBios')
    table = soup.find('table', {'id': TableName})   
    trs = table.find_all('tr')

##    print('\n\n--------I am trs -------------\n');print(trs)

    rows = list();title=list();
    for tr in trs:
        title.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('th')])
        rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])

    Technology = title[0].index('Technology')   #----find Technology colume
    memory = title[0].index('Size')
    RNVDIMM_Memory=list();RDIMM_Memory=list();
    for i in range(1,len(rows)):
        if rows[i][Technology] == 'RNVDIMM':
            RNVDIMM_Memory.append(rows[i][memory])
        elif rows[i][Technology] == 'RDIMM':
            RDIMM_Memory.append(rows[i][memory])
        
    return(RNVDIMM_Memory,RDIMM_Memory)
#-----------------------------------------Storage--------------------------------------------------------
def Storage(soup):

    storage_ID= ('div_physical_view_0')
    table = soup.find(id = storage_ID)
    
    trs = table.find_all('tr')
    rows = list();storage=list()
    for tr in trs:
        rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])
    
    for i in range(1,len(rows)):
        if rows[i]:  #--jump if string is empty
            if rows[i][0] == 'Capacity':
                storage.append(rows[i][1])
    return(storage)
            
#-----------------------------------------check disk size--------------------------------------------------------
def check_disk_size(RNVDIMM_Memory,RDIMM_Memory,storage):

    RDIMM_memory = list(map(int, ''.join([x if x.isdigit() else ' ' for x in str(RDIMM_Memory)]).split()))  # extract number from string   
    if RNVDIMM_Memory == []:
        total_memory = RDIMM_memory
        
    else:
        RNVDIMM_memory = list(map(int, ''.join([x if x.isdigit() else ' ' for x in str(RNVDIMM_Memory)]).split())) # extract number from string
        total_memory = RNVDIMM_memory+RDIMM_memory
        
    total_storage = list(map(int, ''.join([x if x.isdigit() else ' ' for x in str(storage)]).split())) # extract number from string

    Total_memory=sum(total_memory);Total_storage=sum(total_storage)
    
    print('disk size = VMs X 20 + VMs X 2 + VMs X 150 / 1024 GB')
    print('total storage is ',Total_storage,'GB')
    VMs_storage = int(str(Total_storage))*1024/(20*1024+2*1024+150)
    print('you can deploy up to ',int(VMs_storage),' VMs according to storage ')

    print('total memory is ',Total_memory,'MB')
    VMs_memory = int(str(Total_memory))/1024/2
    print('you can deploy up to ',int(VMs_memory),' VMs according to memory ')
    
#------------------------------------------main-----------------------------------------------------------------

UserName = ("Administrator")
UserPass = ("Compaq123")

tb1 = pt.PrettyTable()
tb1.field_names = ["IP", "RNVDIMM", "NV_Num", "RDIMM", "RD_Num", "Storage", "Storage_Num"]


##Input1 = input("a. Gen 10\nb. Gen 8/9:\n")
##Input2 = input("Input iLo IP:\n")

Input2='10.10.101.33'
Input1 = 'a'
if  Input1 == 'a':

    WebUrl = ('https://'+Input2+'/')
    driver.get(WebUrl)
                   
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='appFrame']"))
    WebdriverLoad(driver,"//*[@id='username']")
    driver.find_element_by_xpath("//*[@id='username']").send_keys(UserName)
    driver.find_element_by_id('password').send_keys(UserPass)
    driver.find_element_by_xpath("//*[@id='login-form__submit']").click()
      
    driver.switch_to.default_content()
    #---------------------------Memory---------------------------     
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='appFrame']"))
    WebdriverLoad(driver,"//*[@id='tabset_sysInfo']")
    driver.find_element_by_xpath("//*[@id='tabset_sysInfo']").click()
    driver.find_element_by_xpath("//*[@id='tab_mem']").click()

    soup = go_into_iframe(driver,WebUrl,"//*[@id='memoryTableSMBios']")
    [RNVDIMM_Memory,RDIMM_Memory]=Memory(soup)

    #------------------Switch to main window and go to storage-----------------------
    driver.close() # close tab
    driver.switch_to_window(driver.window_handles[0])
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='appFrame']"))
    driver.find_element_by_xpath("//*[@id='tab_storage']").click()

    soup = go_into_iframe(driver,WebUrl,"//*[@id='physical_ctrl_0']")
    driver.find_element_by_xpath("//*[@id='drive_view_0']/li/table/tbody/tr/td[3]").click() # go to physical view
    WebdriverLoad(driver,"//*[@id='physicalContent_0']/ul/li[3]/ul/li/ul/li/table/tbody/tr[9]/td[2]/span/span")

##    #------------------------First click to get dropdown active---------------------------
##    gno_eur = driver.find_element_by_xpath("//*[@id='physicalContent_0']/ul/li[3]/ul/li/a")
##    hover = ActionChains(driver).move_to_element(gno_eur)
##    hover.perform()
##    time.sleep(1)
##    # After choice drop-down click on element
##    gno_click = driver.find_element_by_xpath("//*[@id='physicalContent_0']/ul/li[3]/ul/li/a")
##    gno_click.click()
    #-----------------------------------------------------------------------------------
    storage=Storage(soup)
    
    #------------------------check disk size---------------------------
    tb1.add_row([Input2,RNVDIMM_Memory,len(RNVDIMM_Memory),min(RDIMM_Memory),len(RDIMM_Memory),min(storage),len(storage)])            
    print(tb1)

    check_disk_size(RNVDIMM_Memory,RDIMM_Memory,storage)
    
##    driver.close()
    

    
