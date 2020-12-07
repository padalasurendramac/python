from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(10)

