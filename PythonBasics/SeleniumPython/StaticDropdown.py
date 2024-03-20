from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service_object= Service()
driver = webdriver.Chrome(options=options,service=service_object)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.select_by_value()
# If there is Select tag there is static dropdown in HTML code then apply all above method relaeated to this static class
