import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
driver.maximize_window()


driver.get("https://www.valueresearchonline.com/funds/")

rows = len(driver.find_elements_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr"))
cols = len(driver.find_elements_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr[1]/td"))

print(rows)
print(cols)

#
# for r in range(1,rows+1):
#     for c in range(1, cols+1):
#         driver.find_element_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr["+str(r)+"]/td["+str(c)+"]")

#print name of mutual fund and 1 year return
time.sleep(5)
for r in range(1,rows+1):
    name_of_MF = driver.find_element_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr["+str(r)+"]/td[1]").text
    return_of_1_year = driver.find_element_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr["+str(r)+"]/td[7]").text
    print(f"{name_of_MF} has given {return_of_1_year} in last one year")
