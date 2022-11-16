from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome( service = s )
driver.maximize_window()

url = 'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_button_name'
driver.get(url)

driver.switch_to.frame("iframeResult")
element1 = driver.find_elements( By.NAME, 'subject' )

print(len(element1))
print(element1[0].text)
print(element1[1].text)
element1[0].click()

driver.quit()


