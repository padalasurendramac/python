from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.headless = True
# below for incognito
#options.add_argument('--incognito')# while using incognito use false
#same options.add_argument('--headless") instend of options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)


driver.get('http://amazon.in')
print(driver.title)