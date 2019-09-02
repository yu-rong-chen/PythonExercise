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


#----------------------------------------等待頁面加載--------------------------------------------------------------
def WebdriverLoad(driver,WebPage):
    delay=5
    try:
        element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, WebPage)))
                                                           #invisibility_of_element_located
##        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
        #Explicit Waits
        #This waits up to delay=5 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds.
        #WebDriverWait by default calls the ExpectedCondition every 500 milliseconds until it returns successfully.
        #https://kkboxsqa.wordpress.com/2017/06/16/the-difference-between-implicit-wait-and-explicit-wait/

    #time.sleep(5)             #Explicit Waits(basic) 強制睡5秒
    #driver.implicitly_wait(5) #Implicit Waits
          #設置了一個最長等待時間，如果在規定時間內網頁加載完成，則執行下一步，否則一直等到時間截止，然後執行下一步。
          #注意這裡有一個弊端，那就是程序會一直等待整個頁面加載完成

def go_into_iframe(driver,WebUrl,Xpath):

    disqus_iframe=driver.find_element_by_tag_name('iframe')
    iframe_url = disqus_iframe.get_attribute('src')
    print(iframe_url)

    WebUrl  = iframe_url
    
    main_window = driver.current_window_handle # save main_window
    driver.execute_script("window.open();")    # open new blank tab
    driver.switch_to_window(driver.window_handles[1]) # switch to the new window which is second in window_handles array
    driver.get(WebUrl)
    WebdriverLoad(driver,Xpath)

    html = driver.page_source #To get the HTML for the whole page
    
    page = driver.execute_script('return document.body.outerHTML') 
    soup = BeautifulSoup(''.join(page), 'html5lib')      #對html標籤進行解釋及分類的解析器
    title = driver.title;print('Title is: ' + title)
    return(soup)

