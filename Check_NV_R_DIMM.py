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
import prettytable as pt


driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
driver.maximize_window()

#----------------------------------------等待頁面加載--------------------------------------------------------------
def WebdriverLoad(driver,WebPage):
    delay=5
    try:
        element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, WebPage)))
                                                           #invisibility_of_element_located
##        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
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
        if rows[i][Technology] == 'RNVDIMM':
            RNVDIMM_Memory.append(rows[i][memory])
        elif rows[i][Technology] == 'RDIMM':
            RDIMM_Memory.append(rows[i][memory])
  
    title = driver.title
    print('Title is: ' + title) 
        
    return(RNVDIMM_Memory,RDIMM_Memory)


#------------------------------------------main-----------------------------------------------------------------

UserName = ("Administrator")
UserPass = ("Compaq123")

tb1 = pt.PrettyTable()
tb1.field_names = ["IP", "RNVDIMM", "NV_Num", "RDIMM", "RD_Num"]
##Input = input("Choose sersion\na. Gen 8 and 9\nb. Gen 10:\n")
Input='b'
if  Input == 'a':
    F1 = open("C:/Users/chenyur/Documents/Lynda/PythonExercise/Gen89.txt")
    Gen89 = F1.readline()

    WebdriverLoad(driver,Login)
    driver.find_element_by_xpath(Login).send_keys(UserName);Login = login.readline()
    driver.find_element_by_xpath(Login).send_keys(UserPass);Login = login.readline()
    driver.find_element_by_xpath(Login).click();Login = login.readline()

elif Input == 'b':
    i=0
    #Question = input('')
    F2 = open("C:/Users/chenyur/Documents/Lynda/github/PythonExercise/iLO.txt")
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
  
        driver.switch_to.default_content()
        
        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='appFrame']"))
        WebdriverLoad(driver,"//*[@id='tabset_sysInfo']")
        driver.find_element_by_xpath("//*[@id='tabset_sysInfo']").click()
        driver.find_element_by_xpath("//*[@id='tab_mem']").click()

        [RNVDIMM_Memory,RDIMM_Memory]=Memory(driver,WebUrl)

        tb1.add_row([Gen10,RNVDIMM_Memory,len(RNVDIMM_Memory),RDIMM_Memory[0],len(RDIMM_Memory)])
        
        Gen10 = F2.readline()
    print(tb1)
    driver.close()
    F2.close()

    
