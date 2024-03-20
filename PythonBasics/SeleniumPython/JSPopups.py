from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "Mrunal"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service_object = Service()
driver = webdriver.Chrome(options=options,service=service_object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()

