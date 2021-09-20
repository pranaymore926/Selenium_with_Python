import openpyxl
import Demo_18_c_DataDrivenTest_XLUtil
from selenium import webdriver



driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")


path = 'C:\\Users\prana\Downloads\WriteData.xlsx'

rowCount =  Demo_18_c_DataDrivenTest_XLUtil.getRowCount(path, 'Sheet1')

print(rowCount)


for r in range(2, rowCount+1):
    userName = Demo_18_c_DataDrivenTest_XLUtil.readData(path, 'Sheet1',r,1 )
    passWord = Demo_18_c_DataDrivenTest_XLUtil.readData(path,'Sheet1', r,2)
    driver.get("http://newtours.demoaut.com/")
    driver.maximize_window()

    driver.find_element_by_name("userName").send_keys(userName)
    driver.find_element_by_name("password").send_keys(passWord)
    driver.find_element_by_id("login").click()
    driver.close()