from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys  #open tab  Not work!!
import time
import requests
from bs4 import BeautifulSoup
import certifi
import html5lib  #pure-python library for parsing HTML
import prettytable as pt
import os #ask for current working directory
import openpyxl

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
driver.maximize_window()
mypath='C:\\Users\\Administrator\\Pictures\\test\\iLoresource.xlsx'
wb = openpyxl.Workbook()
sheet=wb.get_sheet_by_name('Sheet')

#----------------------------------------等待頁面加載--------------------------------------------------------------
def WebdriverLoad(driver,WebPage):
    delay=20
    while True:
        try:
            element = WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, WebPage)))
                                                            #invisibility_of_element_located
            break
    ##        print ("Page is ready!")
        except TimeoutException:
            raise Exception("Loading took too much time!")
            continue
#-------------------------------------Physical Memory------------------------------------------------------------
def Memory(driver,WebUrl):

    disqus_iframe=driver.find_element_by_tag_name('iframe')
    iframe_url = disqus_iframe.get_attribute('src')
    print(iframe_url)

    WebUrl  = iframe_url

    driver.get(WebUrl)
    WebdriverLoad(driver,"//*[@id='memoryTableSMBios']")

    html = driver.page_source #To get the HTML for the whole page

    page = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(''.join(page), 'html5lib')      #對html標籤進行解釋及分類的解析器
##    print('\n--------I am Soup--------\n');print(soup)


                        #對html標籤進行解釋及分類的解析器
##    verify=("C:/Users/chenyur/Python/Python36/Lib/site-packages/certs.pem")
##    res = requests.get(WebUrl,verify=False)
##    soup2 = BeautifulSoup(res.text,features="html5lib")   # only show <html><head></head><body></body></html>
##    print('\n--------I am Soup 2--------\n');print(soup2)
##    https://stackoverflow.com/questions/35905517/how-to-get-innerhtml-of-whole-page-in-selenium-driver#


    TableName= ('memoryTableSMBios')
    table = soup.find('table', {'id': TableName})
    trs = table.find_all('tr')

##    print('\n\n--------I am trs -------------\n');print(trs)

    rows = list();title=list();
    for tr in trs:
        title.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('th')])
        rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])

##    print('\n\n--------I am rows -------------\n');print(rows)
##    print('\n\n--------I am title -------------\n');print(title)
    Technology = title[0].index('Technology')
    memory = title[0].index('Size')
    RNVDIMM_Memory=list();RDIMM_Memory=list();
    for i in range(1,len(rows)):
        if rows[i][Technology] == 'NVDIMM-N':
            RNVDIMM_Memory.append(rows[i][memory])
        elif rows[i][Technology] == 'RDIMM':
            RDIMM_Memory.append(rows[i][memory])

    title = driver.title
    print('Title is: ' + title)

    return(RNVDIMM_Memory,RDIMM_Memory)


#-------------------------------------Network------------------------------------------------------------
def Network(driver,WebUrl):

    disqus_iframe=driver.find_element_by_tag_name('iframe')
    iframe_url = disqus_iframe.get_attribute('src')
    # print(iframe_url)

    WebUrl  = iframe_url

    driver.get(WebUrl)
    WebdriverLoad(driver,"//*[@id='tbl_network_ports']")

    html = driver.page_source #To get the HTML for the whole page

    page = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(''.join(page), 'html5lib')      #對html標籤進行解釋及分類的解析器
    # print('\n--------I am Soup--------\n');print(soup)

    TableName= ('tbl_network_ports')
    table = soup.find('table', {'id': TableName})
    trs = table.find_all('tr')

    # print('\n\n--------I am trs -------------\n');print(trs)

    rows = list();title=list()
    for tr in trs:
        title.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('th')])
        rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])

    # print('\n\n--------I am rows -------------\n');print(rows)
    # print('\n\n--------I am title -------------\n');print(title)
    Status = title[1].index('Status')
    Port = title[1].index('Port')
    IPv6 = title[1].index('IPv6 Address')

    StatusOK=list()
    for i in range(2,len(rows)):
        StatusOK.append([rows[i][Status],rows[i][Port:IPv6]])

    title = driver.title
    return StatusOK

#------------------------------------------main-----------------------------------------------------------------

UserName = ("Administrator")
UserPass = ("Compaq123")

tb1 = pt.PrettyTable()
tb1.field_names = ["IP", "RNVDIMM", "NV_Num", "RDIMM", "RD_Num"]
##Input = input("Choose sersion\na. Gen 8 and 9\nb. Gen 10:\n")
Input='b'
if  Input == 'a':
    CWD=os.getcwd()
    F1 = open(CWD+"\\Gen89.txt")
    Gen89 = F1.readline()

    WebdriverLoad(driver,Login)
    driver.find_element_by_xpath(Login).send_keys(UserName);Login = login.readline()
    driver.find_element_by_xpath(Login).send_keys(UserPass);Login = login.readline()
    driver.find_element_by_xpath(Login).click();Login = login.readline()

elif Input == 'b':
    i=0
    #Question = input('')
    CWD=os.getcwd()
    F2 = open(CWD+"\\iLO.txt")
    Gen10 = F2.readline()
    # Gen10 = input("Please input IP:\n")

    while Gen10:
        print(Gen10)
        i=i+1
        # WebUrl  = 'https://'+Gen10+'/'
        WebUrl  = Gen10
        driver.get(WebUrl)

        driver.find_element_by_xpath("//*[@id='details-button']").click()
        WebdriverLoad(driver,"//*[@id='proceed-link']")
        driver.find_element_by_xpath("//*[@id='proceed-link']").click()

        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='appFrame']"))
        WebdriverLoad(driver,"//*[@id='username']")
        driver.find_element_by_xpath("//*[@id='username']").send_keys(UserName)
        driver.find_element_by_id('password').send_keys(UserPass)
        driver.find_element_by_xpath("//*[@id='login-form__submit']").click()

        driver.switch_to.default_content()

        time.sleep(5)
        WebdriverLoad(driver,"//*[@id='appFrame']")
        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='appFrame']"))
        WebdriverLoad(driver,"//*[@id='tabset_sysInfo']")
        driver.find_element_by_xpath("//*[@id='tabset_sysInfo']").click()
        driver.find_element_by_xpath("//*[@id='tab_mem']").click()

        [RNVDIMM_Memory,RDIMM_Memory]=Memory(driver,WebUrl)
        #------------------------Network-----------------------------
        driver.get(WebUrl)
        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='appFrame']"))
        WebdriverLoad(driver,"//*[@id='tabset_sysInfo']")
        driver.find_element_by_xpath("//*[@id='tabset_sysInfo']").click()
        driver.find_element_by_xpath("//*[@id='tab_nic']").click()
        Netdata=Network(driver,WebUrl)

        tb1.add_row([Gen10,RNVDIMM_Memory,len(RNVDIMM_Memory),RDIMM_Memory[0],len(RDIMM_Memory)])

        sheet['A'+str(i)]= str(Gen10)
        sheet['B'+str(i)] = str(Netdata)
        wb.save(mypath)

        Gen10 = F2.readline()

    print(tb1)
    driver.close()
    F2.close()

elif Input == 'c':
    i=0
    #Question = input('')
    CWD=os.getcwd()
    F2 = open(CWD+"\\iLO.txt")
    Gen10 = F2.readline()
    #Gen10 = input("Please input IP:\n")
    while Gen10:
        print(Gen10)
        i=i+1;
        #WebUrl  = 'https://'+Gen10+'/'
        WebUrl  = Gen10
        driver.get(WebUrl)

        driver.find_element_by_xpath("//*[@id='details-button']").click()
        WebdriverLoad(driver,"//*[@id='proceed-link']")
        driver.find_element_by_xpath("//*[@id='proceed-link']").click()

        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='appFrame']"))
        WebdriverLoad(driver,"//*[@id='username']")
        driver.find_element_by_xpath("//*[@id='username']").send_keys(UserName)
        driver.find_element_by_id('password').send_keys(UserPass)
        driver.find_element_by_xpath("//*[@id='login-form__submit']").click()
        Gen10 = F2.readline()
        #-----open tab:
        main_window = driver.current_window_handle
        driver.execute_script("window.open();")
        driver.switch_to_window(driver.window_handles[i])
        #webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform() #Not work
    F2.close()
    Exitdriver = input("Do you want to close all windows?\n")
    if Exitdriver == 'yes':
        driver.close()
