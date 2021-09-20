import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Launching webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

user_ele = driver.find_element_by_name("userName")

#returns true or false if the element is displayed
print(user_ele.is_displayed())

#returns true or false if the element is enabled or not
print(user_ele.is_enabled())

pass_ele = driver.find_element_by_name("passWord")

#returns true or false if the element is displayed
print(pass_ele.is_displayed())

#returns true or false if the element is enabled or not
print(pass_ele.is_enabled())

user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")


driver.find_element_by_name("login").click()

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print(roundtrip_radio.is_selected())
