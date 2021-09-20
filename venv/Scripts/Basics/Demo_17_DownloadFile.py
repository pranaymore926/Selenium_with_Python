import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#the downloads will be downloaded at default location. Hence to give desired location we need to import below package
from selenium.webdriver.chrome.options import Options

#specify download location of files
#download scenario is different from chromebrowser in firefox browser. in firefox browser it will show download pop up
# fp = webdriver.FirefoxProfile()
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk" , "text/plain,application/pdf")
#fp.set_preference("browser.download.manager.showWhenStarting", False)
#fp.set_preference("browser.download.dir","C:\Downloadedfiles")
#fp.set_preference("browser.download.folderList",2)
#fp.set_preference("pdfjs.disabled", True)
#driver=webdriver.Firefox(firefox_profile=fp,executable_path='.\geckodriver')



chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory":"C:\Downloadedfiles"})

#pass above created chromeOptions as parameter to intialize the driver
driver = webdriver.Chrome(executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe", chrome_options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#download text file
driver.find_element_by_xpath("//*[@id='textbox']").send_keys("What is mobile Number ? Karu kya dial number")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()


#download pdf file
driver.find_element_by_id("pdfbox").send_keys("What is mobile Number in pdf ? Karu kya dial number?")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()


