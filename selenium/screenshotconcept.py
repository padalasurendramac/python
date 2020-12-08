from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.reddit.com/')
#driver.get_screenshot_as_file('test1.png')
#screenshot (above) full

'''full screenshot'''
S = lambda X: driver.execute_script('return.document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('redd.png');