from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
options = webdriver.ChromeOptions()

driver.maximize_window()
WebUrl = ("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query")
driver.get(WebUrl)
delay=5

try:
    #WebDriverWait(driver, delay).until(EC.presence_of_element_located(driver.find_element_by_id('IdOfMyElement')))
    element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "pid"))) #carousel-example-generic
                                                   #invisibility_of_element_located
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")
    

driver.find_element_by_id('pid').send_keys("A280363849")
driver.find_element_by_id('startStation').send_keys("1000-臺北")
driver.find_element_by_id('endStation').send_keys("6000-臺東")
driver.find_element_by_id('normalQty').clear()
driver.find_element_by_id('normalQty').send_keys("2")

driver.find_element_by_id('rideDate1').clear()
driver.find_element_by_id('rideDate1').send_keys("20190608")
driver.find_element_by_id('trainNoList1').send_keys("408")


# *************  locate CheckBox  **************
try:
    CheckBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID ,"recaptcha-anchor"))
        )
except TimeoutException:
    print("Loading took too much time")
CheckBox.click()
#driver.find_element_by_xpath("//*[@id='recaptcha-anchor']/div[1]").click()

driver.find_element_by_xpath("//*[@id='queryForm']/div[4]/input[2]").click()

print(driver.get_cookies())
