from selenium import webdriver
# browser exposes an executable file
# Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()

driver.get("https://www.rokomari.com/book")

driver.close ()