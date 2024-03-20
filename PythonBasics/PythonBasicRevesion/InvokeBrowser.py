#PracticeWebsite
# https://opensource-demo.orangehrmlive.com/web/index.php/auth/log
# https://www.saucedemo.com/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service() #Selenium Manager
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractis")
# driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
