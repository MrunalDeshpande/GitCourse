from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Headless mode
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service_obj=Service()
driver =webdriver.Chrome(options=chrome_options,service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")