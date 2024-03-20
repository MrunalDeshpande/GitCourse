from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_object = Service()
driver = webdriver.Chrome(service=service_object,options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice")

print(driver.title)