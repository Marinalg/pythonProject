from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


driver = Chrome("./chromedriver")
driver.get("https://vanongo.com/retail-supermarkets/")
driver.maximize_window()

element: WebElement = driver.find_element(By.XPATH, "//li[@class='pagination-link next-link']/a[./span[text()='next']]")
sleep(1)
element.click()



sleep(7)
driver.quit()