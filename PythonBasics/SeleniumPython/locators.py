from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service_object = Service()
driver = webdriver.Chrome(options=options,service=service_object)
driver.get("https://rahulshettyacademy.com/angularpractice")

#ID, Xpath,name,linktext, cssselector,classname,name

driver.find_element(By.NAME,"email").send_keys("mrunal@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Mrunal@6890")
driver.find_element(By.ID,"exampleCheck1").click()

# XPATH - //tagname[@attribute = 'Value'] //input[@type='submit] this is custom xpath
#css - tagname[attribute = 'Value'], #id - #inlineRadio1, .className - .alert-success
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Mrunal")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
message= driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello!World")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()