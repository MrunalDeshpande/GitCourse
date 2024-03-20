from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service_obj= Service()
driver=webdriver.Chrome(options=options,service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
# CSS Selector Syntax:tagname[attribute='value'],#id,.classname

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Mrunal Deshpande")
# driver.find_element(By.NAME,"name").send_keys("Mrunal Deshpande")



# Static Drop down
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element(By.NAME,"email").send_keys("mrunal@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Mrunal@6890")
driver.find_element(By.ID,"exampleCheck1").click()

#Xpath Syntax: //tagname[@attribute='value']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message= driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello!Mrunal")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
