from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service_obj=Service()
driver=webdriver.Chrome(options=options,service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# radios = driver.find_elements(By.XPATH,"//input[@type='radio']")
# print(len(radios))
#
# for radio in radios:
#     if radio.get_attribute("value")== "radio2":
#         radio.click()
#         assert radio.is_selected()
#         break
radios = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radios[1].click()
assert radios[1].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

