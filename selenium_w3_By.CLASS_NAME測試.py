from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome( service = s )
driver.maximize_window()

url = "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_classes_span"
driver.get(url)

driver.switch_to.frame("iframeResult")
element1 = driver.find_elements( By.CLASS_NAME, 'note' )
print(len(element1))
print(element1[1].text)


