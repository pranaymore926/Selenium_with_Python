import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
driver.maximize_window()


driver.get("https://testautomationpractice.blogspot.com/")

#double click on below element
element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

#actionChain syntax to double click
actions = ActionChains(driver)
actions.double_click(element).perform()