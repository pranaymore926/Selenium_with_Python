import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
driver.maximize_window()


driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button_right_click  = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

#use ActionsChains class and pass driver as parameter
actions = ActionChains(driver)

#to right click use below method
actions.context_click(button_right_click).perform()


driver.close()



