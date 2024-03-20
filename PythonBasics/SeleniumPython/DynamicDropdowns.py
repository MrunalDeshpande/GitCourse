import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service_object = Service()
driver = webdriver.Chrome(options=options,service=service_object)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text =="India":
        country.click()
        break
# print(driver.find_element(By.ID,"autosuggest").text)
# print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"