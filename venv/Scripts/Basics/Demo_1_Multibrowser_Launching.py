from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\software\\geckodriver-v0.29.1-win64.\\geckodriver.exe")

driver.get("http://newtours.demoaut.com/")
print(driver.title) #returns title
print(driver.current_url) # returns current Url
#print(driver.page_source)  # return html code of page
driver.close()
