from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):

        # //a[contains(@href,'shop')] and a[href*='shop'] -CSS
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        chekoutPage = CheckoutPage(self.driver)
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        products = CheckoutPage.getCardTitles()

        for product in products:
            productName = product.find_element(By.XPATH, 'div/h4/a').text
            if productName == "Blackberry":
                product.find_element(By.XPATH, 'div/button').click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in successText
        self.driver.close()
