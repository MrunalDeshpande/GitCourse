from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

BrowserSortedVeggies = []
service_object = Service()
driver = webdriver.Chrome(service=service_object)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#Click on Column Header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

# Collect all veggies names ->BrowserSortedVeggiesList (A,B,C)
VeggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in VeggieWebElements:
    BrowserSortedVeggies.append(ele.text)

OriginalBrowserSortedList = BrowserSortedVeggies.copy()

# Sort this BrowserSortedVeggis List => newsortedlist(A,B,C)
BrowserSortedVeggies.sort()

assert BrowserSortedVeggies==OriginalBrowserSortedList







