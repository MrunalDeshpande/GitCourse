from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service_object = Service()
driver = webdriver.Chrome(options=options,service=service_object)
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)