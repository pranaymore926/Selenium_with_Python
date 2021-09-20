from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Launching webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.fullscreen_window()

#Opening url will take some time so wait for sometime
driver.implicitly_wait(10)

#print(driver.title)


assert "Frames & windows" in driver.title

practise_site_link = driver.find_element_by_link_text('Practice Site')
print(practise_site_link.is_displayed())
practise_site_link.click()

driver.close()

