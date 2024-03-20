from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service_object= Service()
driver= webdriver.Chrome(options=options,service=service_object)

driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text