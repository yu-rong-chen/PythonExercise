class FindElement:
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'
    
    def  Findhref(self,Locator,WebUrl,driver):
        driver.get(WebUrl)
        disqus_href=driver.find_element_by_xpath(Locator)
        href_url = disqus_href.get_attribute('href')
        print(href_url)
        driver.get(href_url)
        # print(self)
        # print('\n',Locator)
        # print('\n',WebUrl)
        return href_url
    
    def Getdriver():
        from selenium import webdriver
        print('Nice to meet you')
        # driver = webdriver.Chrome()
        # return driver


    def play_button(self):
        print("Pressed Play")