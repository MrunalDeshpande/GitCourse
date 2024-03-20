from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggies = []

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service_obj=Service()
driver =webdriver.Chrome(options=options,service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")

for element in veggieWebElements:
    browserSortedVeggies.append(element.text)
originalBrowserSortedList = browserSortedVeggies.copy()
browserSortedVeggies.sort()
assert browserSortedVeggies == originalBrowserSortedList
