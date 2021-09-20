import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
# driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com")

driver.implicitly_wait(10)

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)

#closes alert by clicking on OK button
driver.switch_to_alert().accept()

#closes alert by clicking on Cancel button

#driver.switch_to_alert().dismiss()
