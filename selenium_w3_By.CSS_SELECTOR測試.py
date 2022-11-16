from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome( service = s )
driver.maximize_window() # 打開的網頁佔滿整個螢幕

url = 'https://www.w3schools.com/cssref/tryit.asp?filename=trycss_display'
driver.get(url)

driver.switch_to.frame("iframeResult")
element = driver.find_element( By.CSS_SELECTOR , 'body > div:nth-child(3) > p' )#copy selector body > div:nth-child(5) > p
print(element.tag_name)
print(element.get_attribute('textContent'))#網頁上沒顯示的文字取得方法
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
