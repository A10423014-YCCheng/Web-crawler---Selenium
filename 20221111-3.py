#開啟天瓏網路書店並搜尋’selenium’相關書籍
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome( service = s )

url = 'https://www.tenlong.com.tw/'
driver.get(url)

str = '/html/body/div[3]/nav[1]/nav/div/form/input[2]' #Copy full Xpath取得
search_field = driver.find_element( By.XPATH, str ) #使用By.XPATH方式
search_field.send_keys('selenium') #輸入selenium到對應位置
search_field.submit() #提交
