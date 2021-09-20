import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
driver.maximize_window()


driver.get("https://www.worldometers.info/geography/flags-of-the-world/")


india_flag = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div/div/div[79]/div/div")

#command for scrolling
#driver.execute_script("arguments[0].scrollIntoView();", india_flag)


#scroll till end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
