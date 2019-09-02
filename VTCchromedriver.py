from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from WebScraping import WebdriverLoad
from bs4 import BeautifulSoup

#""" Python selenium keep browser open """
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True) 

def add_repository(driver,Source,os_type,User,Password):

        page = driver.execute_script('return document.body.outerHTML') 
        soup = BeautifulSoup(''.join(page), 'html5lib')      #對html標籤進行解釋及分類的解析器

        TableName= ('DataTables_Table_0')
        table = soup.find('table', {'id': TableName})   
        trs = table.find_all('tr')

        # # print('\n\n--------I am trs -------------\n');print(trs)

        # rows = list();title=list();
        # for tr in trs:
        #         title.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('th')])
        #         rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])
        
        # print('\n\n--------I am rows -------------\n');print(rows)
        Sourse_id = 0
        token = soup.find('input', {'name':str(Sourse_id)})['value']
        # """ https://stackoverflow.com/questions/46028156/python-beautiful-soup-getting-input-value?rq=1 """
        
        if token != None:
                for Sourse_id in range(0,100,3):
                        token = soup.find('input', {'name':str(Sourse_id)})['value']
                        print(token)
                        if token == '':
                                break
                
        td_num = Sourse_id/3 +1
        XPath_source = "//*[@id='DataTables_Table_0']/tbody/tr/td["+str(int(td_num+1))+"]/input"
        driver.find_element_by_xpath(XPath_source).send_keys(Source)
        XPath_ostype = "//*[@id='DataTables_Table_0']/tbody/tr/td["+str(int(td_num+2))+"]/div/div/div"
        driver.find_element_by_xpath(XPath_ostype).click
        if os_type == 1:
                XPath_linux = "//*[@id='DataTables_Table_0']/tbody/tr/td["+str(int(td_num+2))+"]/div/div/ol/li[1]" 
                driver.find_element_by_xpath(XPath_linux).click
        elif os_type == 2:
                XPath_windows = "//*[@id='DataTables_Table_0']/tbody/tr/td["+str(int(td_num+2))+"]/div/div/ol/li[2]"
                driver.find_element_by_xpath(XPath_windows).click
        XPath_User = "//*[@id='DataTables_Table_0']/tbody/tr/td["+str(int(td_num+3))+"]/input"
        driver.find_element_by_xpath(XPath_User).send_keys(User)
        XPath_Password = "//*[@id='DataTables_Table_0']/tbody/tr/td["+str(int(td_num+4))+"]/input"
        driver.find_element_by_xpath(XPath_Password).send_keys(Password)
        

def repository(ID,Num,f,driver):
        normal_num = 12;NVDIMM_num = 18; """ Be careful Num """
        for line in f:
                Num=Num+1
                if ID == 'a':
                        if Num >1 and Num <=8:
                                PerfectVM_URL = line
                                User = 'root';Password = 'compaq';
                                add_repository(driver,PerfectVM_URL,1,User,Password)
                        elif Num>=9 and Num < normal_num:
                                PerfectVM_URL = line
                                User = 'Administrator';Password = 'compaq';
                                add_repository(driver,PerfectVM_URL,2,User,Password)
                         
                elif ID == 'b':
                        if Num >(normal_num+1) and Num <NVDIMM_num:
                                PerfectVM_URL = line
                                User = 'Administrator';Password = 'compaq';
                                print(PerfectVM_URL)
                                driver.find_element_by_xpath("//*[@id='vtc-scenario-name']").send_keys('UItest')
                        
                elif ID == 'c':
                        if Num >(NVDIMM_num+1) and Num <=22:
                                PerfectVM_URL = line
                                User = 'Administrator';Password = 'compaq';
                                print(PerfectVM_URL)
                        elif Num>=22:
                                PerfectVM_URL = line
                                User = 'root';Password = 'compaq';
                                print(PerfectVM_URL)
                else:print("Print error ID\n")



#------------------------------------------main-----------------------------------------------------------------

##VTC_IP = input("What is your IP?\n")
VTC_IP = '10.10.124.9'
WebUrl  = "https://"+VTC_IP
driver.get(WebUrl)
driver.maximize_window()

UserName = ("Administrator")
UserPass = ("Compaq123")


WebdriverLoad(driver,"//*[@id='hp-login-page']")
driver.find_element_by_id('hp-login-user').send_keys(UserName)
driver.find_element_by_id('hp-login-password').send_keys(UserPass)
driver.find_element_by_id('hp-login-button').click()

WebdriverLoad(driver,"//*[@id='hp-main-menu-control']")


#--------------------------------------setting--------------------------
##driver.find_element_by_xpath("//*[@id='hp-main-menu-control']").click() # click and div id = hp-main-menu-control change site


WebdriverLoad(driver,"//*[@id='hp-main-menu']/div/ul")

disqus_href=driver.find_element_by_xpath("//*[@id='hp-main-menu']/div/ul/li[2]/ul/li[1]/a")

href_url = disqus_href.get_attribute('href')
print(href_url)
WebUrl  = href_url
driver.get(WebUrl)

#----------------------------------Add reposotory-----------------------
WebdriverLoad(driver,"//*[@id='vtc-settings-repository-panel']/div")
WebdriverLoad(driver,"//*[@id='vtc-settings-repository-panel-edit']")
disqus_href=driver.find_element_by_xpath("//*[@id='vtc-settings-repository-panel-edit']")


href_url = disqus_href.get_attribute('href')
print(href_url)
WebUrl  = href_url
driver.get(WebUrl)
WebdriverLoad(driver,"//*[@id='vtc-repository-add']/a")
driver.find_element_by_xpath("//*[@id='vtc-repository-add']/a").click()

Num=0;
# ID = input("Which category ?\n(a)ESXi67U3-normal\n(b)NVDIMM\n(c)MaxCPU\n") 
ID = 'a'
with open ("c:/Users/chenyur/OneDrive - Hewlett Packard Enterprise/Spring/PerfectVM-URL.txt","r") as f:    
        repository(ID,Num,f,driver)

f.close
#--------------------------------------scenario--------------------------
# WebdriverLoad(driver,"//*[@id='hp-main-menu']/div/ul")
# disqus_href=driver.find_element_by_xpath("//*[@id='hp-main-menu']/div/ul/li[1]/ul/li[1]/a")

# href_url = disqus_href.get_attribute('href')
# print(href_url)
# WebUrl  = href_url
# driver.get(WebUrl)

# #-----------------------------------add scenario--------------------------
# WebdriverLoad(driver,"//*[@id='vtc-scenario-page']/div/div[1]")
# disqus_href=driver.find_element_by_xpath("//*[@id='vtc-scenario-page']/div/div[1]/header/h1/div[1]/a")

# href_url = disqus_href.get_attribute('href')
# print(href_url)
# WebUrl  = href_url
# driver.get(WebUrl)

# WebdriverLoad(driver,"//*[@id='vtc-scenario-add-form']/div[1]")
# driver.find_element_by_xpath("//*[@id='vtc-scenario-name']").send_keys('UItest')
# driver.find_element_by_xpath("//*[@id='vtc-add-host']").click()


