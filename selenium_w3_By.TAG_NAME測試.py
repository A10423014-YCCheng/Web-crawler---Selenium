from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome( service = s )
driver.maximize_window()

url = 'https://www.w3schools.com/html/tryit.asp?filename=tryhtml_images_trulli'
driver.get(url)

driver.switch_to.frame("iframeResult")
element1 = driver.find_element( By.TAG_NAME, 'img' )
url = element1.get_attribute('src')#取得圖檔名稱
print(url)
driver.quit()

import requests
r = requests.get(url) #到圖片網頁去
with open('test.jpg','wb') as f :
    f.write(r.content) #存檔



