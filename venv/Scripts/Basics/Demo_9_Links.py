
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
# driver.maximize_window()

driver.get("https://www.amazon.in/")

driver.implicitly_wait(10)

links_list = driver.find_elements(By.TAG_NAME, 'a')
print("Count of all links : ",len(links_list))

# for link in links_list:
#     print (link.text)

#driver.find_element(By.LINK_TEXT, "Account & Lists").click()
driver.find_element_by_partial_link_text("Account").click()

print("Link clicked")

driver.quit()