from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome( service = s )

url = 'https://www.w3schools.com/html/tryit.asp?filename=tryhtml_id_css'
driver.get(url)

driver.switch_to.frame('iframeResult')

element1 = driver.find_element( By.ID, 'myHeader' )
print(element1.tag_name)
print(element1.text)