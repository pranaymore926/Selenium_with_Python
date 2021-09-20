from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#import explicit package
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Launching webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.expedia.com/")




List_of_fav_link = driver.find_element_by_link_text("List of favorites")
List_of_fav_link.click()
print(driver.title)

driver.back()


wait = WebDriverWait(driver, 20)
add_flight_checkbox =  wait.until(EC.element_to_be_selected(By.ID, 'add-flight-switch'))
add_flight_checkbox.click()

#select check box
#add_a_flight_checkBox = driver.find_element_by_id("add-flight-switch")
# driver.find_element_by_id("").click()
# add_a_flight_checkBox = driver.find_element(By.ID, "add-flight-switch").click()
#print(f"add a flight checkbox is displayed,{add_a_flight_checkBox.is_displayed()}")
#add_a_flight_checkBox.click()








driver.close()
