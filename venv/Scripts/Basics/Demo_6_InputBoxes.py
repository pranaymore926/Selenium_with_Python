from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#to find input boxes in webpage
inputboxes = driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputboxes))

#how to provide value into textbox
driver.find_element(By.ID,'RESULT_TextField-1').send_keys("Pranay")
driver.find_element(By.ID , 'RESULT_TextField-2').send_keys("More")

driver.find_element_by_id('RESULT_TextField-3').send_keys("8830732133")


#How to get the status
status1 = driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print("Displayed or not", status1)

status2 = driver.find_element(By.ID,'RESULT_TextField-1').is_enabled()
print("Enabled or not", status2)

driver.close()