import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
# driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


#is_selected method can be used to find if the radiobutton or CheckBoxes are selected or not
#worked with radio Button
# status =  driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
# print("Is selected or not", status)
# time.sleep(5)
# wait = WebDriverWait(driver,10)
# wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="RESULT_RadioButton-7_0"]'))).click()
#
#
# status =  driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
# print("Is selected or not", status)

#working with the checkbixes
#selecct sunday  checkbox
time.sleep(10)
driver.find_element_by_id('RESULT_CheckBox-8_0').click()
time.sleep(10)
#selct saturday
driver.find_element_by_id('RESULT_CheckBox-8_6').click()




status =driver.find_element_by_id('RESULT_CheckBox-8_0').is_selected()
print(status)





driver.close()