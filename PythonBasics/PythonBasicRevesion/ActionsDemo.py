from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service_obj= Service()
driver = webdriver.Chrome(options=options,service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
actions= ActionChains(driver)
# actions.double_click(driver.find_element(By.))
# actions.context_click()
# actions.drag_and_drop()
actions.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
actions.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
actions.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
