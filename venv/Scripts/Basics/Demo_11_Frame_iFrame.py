#working with frame
#switch_to.frame(name)
#switch_to.frame(id)
#we cannot jump directly from one frame to another for that we need to jump to main page first for that we can use below command
#driver.switch_to.default_content()
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
# driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)
driver.switch_to_default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
time.sleep(3)

driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[6]/a")
driver.quit()