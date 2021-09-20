import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#driver.current_window_handle
#driver.window_handles

driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
# driver.maximize_window()

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//div/a/*[@class ='btn btn-info']").click()
print(driver.current_window_handle)
#current window handle --> CDwindow-A23C737F8DF4F7A27884FB3046E6CA46
handles = driver.window_handles
#child window --> CDwindow-1951C0ECE4F25744E65A49C0EC6E4ED8


for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()

#closes all browser window
#driver.quit()