from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome( service = s )
driver.maximize_window()

url = 'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_link_target'
driver.get(url)

driver.switch_to.frame("iframeResult")
element = driver.find_element( By.LINK_TEXT , 'Visit W3Schools.com!' )
print(element.tag_name)#超連結標籤 = a
element.click()#進入網址，打開下一個網頁

driver.quit()






'''
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
'''
