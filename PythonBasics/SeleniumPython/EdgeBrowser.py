from selenium import webdriver
from selenium.webdriver.edge.service import Service

service_object = Service()
driver = webdriver.Edge(service=service_object)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.minimize_window()
driver.back()
driver.refresh()
driver.close()