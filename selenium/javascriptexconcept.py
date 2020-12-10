from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #this is like ec=expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://amazon.in/')

# storing value in best_sellers
best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')
# below method for execute script
#driver.execute_script("arguments[0].click();", best_sellers)
# javascript for (document.title)
#title = driver.execute_script("return document.title;")
#print(title)
# below script for refresh
#driver.execute_script("history.go(0);")
# alert pop script
#driver.execute_script("alert('hello test');")

#innertext of page find with help of javascript
#inner_text = driver.execute_script("return document.documentElement.innerText;")
#print(inner_text)

#form = driver.find_element(By.ID, 'hs-login')
# high lighting the element
#driver.execute_script("arguments[0].style.border = '3px solid red'", form)

#below script for scroll fullly down
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

#click on forgot and scroll method
#forgot_pwd = driver.find_element(By.ID, 'Forgot Password?')
#driver.execute_script("arguments[0].scrollIntoView(true);", forgot_pwd)

# user browser information get 
#print(driver.execute_script("return navigator.userAgent;"))

#js script for enter value
driver.execute_script("document.getElementById('username').value='suendra';")