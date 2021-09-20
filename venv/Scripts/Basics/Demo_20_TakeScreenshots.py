from selenium import webdriver
import Demo_20_Utility


driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")

driver.maximize_window()
driver.get("https://www.amazon.in")
TIME = Demo_20_Utility.current_time()
driver.save_screenshot(TIME+".png")

driver.close()