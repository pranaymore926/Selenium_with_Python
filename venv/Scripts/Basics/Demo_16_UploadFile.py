import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


time.sleep(3)
#switch to frame
driver.switch_to.frame("frame-one1434677811")

driver.find_element_by_name("RESULT_FileUpload-10").send_keys("C://Users/prana/OneDrive/Pictures/Elon-Musk-High-Quality-Wallpapers.jpg")
driver.close()
