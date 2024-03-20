from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service_object = Service("H:\SeleniumWithPython\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service = service_object)
# driver.get("https://rahulshettyacademy.com")

#Chrome Driver = Chrome Browser
service_object = Service() #selenium Manager
driver = webdriver.Chrome(service = service_object)# Invoking Browser
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.minimize_window()
driver.back()
driver.refresh()
driver.close()

