import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
# driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#use select class to work with dropdown
#select one option from dropdown

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp=Select(element)

#select by Value
drp.select_by_value("Radio-0")

#select by index
drp.select_by_index(2)

#select by visible text
drp.select_by_visible_text("Evening")


#count how many options in dropdown
print(len(drp.options))


#capture all the options from dropdown

for option in drp.options:
    print (option.text)



