from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

#driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
#login  https://username:password@doman.com/login
driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

driver.find_element(By.NAME, 'upfile').send_keys('c:\\Users\\LENOVO\\Desktop\\text.doc')
driver.find_element(By.XPATH, '//input[@type='submit']').click()