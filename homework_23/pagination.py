from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = Chrome("./chromedriver")
driver.get("https://reinvently.com/blog/")
driver.maximize_window()

element: WebElement = driver.find_element(By.XPATH, "////a[contains(text(), 'Send')]")
sleep(1)
element.click()