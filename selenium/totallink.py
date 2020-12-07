from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://amazon.com")

print(driver.title)
driver.implicitly_wait(10)
driver.maximize_window()


linkList = driver.find_elements(By.TAG_NAME, "a")
print(len(linkList))
#print(linkList)
for ele in linkList:
#    link_text = ele.text
#    print(link_text)
    print(ele.get_attribute('href'))

imageList = driver.find_elements(By.TAG_NAME, 'img')
print(len(imageList))

for ele in imageList:
    print(ele.get_attribute('src'))