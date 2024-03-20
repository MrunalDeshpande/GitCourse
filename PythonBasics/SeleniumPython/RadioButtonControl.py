from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service_object = Service()
driver = webdriver.Chrome(options=options,service=service_object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
# print(len(radiobuttons))
#
# for radiobutton in radiobuttons:
#     if radiobutton.get_attribute("value") == "radio2":
#         radiobutton.click()
#         assert radiobutton.is_selected()
#         break

radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radiobutton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

