import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name =="chrome":
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(4)

    elif browser_name == "firefox":
        # options = webdriver.FirefoxOptions()
        # options.add_experimental_option("detach", True)
        service_obj = Service()
        driver = webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(4)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
