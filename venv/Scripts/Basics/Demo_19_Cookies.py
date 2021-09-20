#Cookies is piece of info from website saved by browser
#It is a way of remembering users and their interactions with the site storing info in the cookies file in key value pair
#it stores info like username password email
from selenium import webdriver



driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")

driver.get("https://www.amazon.in")
#capture all the cookies created by the browser
cookies = driver.get_cookies()
print(len(cookies))
#print all the cookies captured by webpage
print(cookies)

#Adding new cookie to the browser
cookies = {'name' : 'MyCookie', 'value':'1234567890'}
driver.add_cookie(cookies)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)


#Deleting the cookies
driver.delete_all_cookies()
cookies= driver.get_cookies()
print(len(cookies))
print(cookies)




