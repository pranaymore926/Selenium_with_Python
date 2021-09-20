import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
driver.maximize_window()


driver.get("https://opensource-demo.orangehrmlive.com/")

#userName xpath
driver.find_element_by_id("txtUsername").send_keys("admin")
#password
driver.find_element_by_id("txtPassword").send_keys("admin123")
#login button
driver.find_element_by_id("btnLogin").click()



admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
user_mang = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")


#to do mouse hover action use ActionChains class

actions = ActionChains(driver)

actions.move_to_element(admin).move_to_element(user_mang).move_to_element(users).perform()




