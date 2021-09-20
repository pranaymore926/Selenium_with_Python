import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Launching webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")

#launch URL
driver.get("http://newtours.demoaut.com/")
print(driver.title)

#launch another website
driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(5)
print(driver.title)


driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)



