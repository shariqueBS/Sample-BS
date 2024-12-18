
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.browserstack.com/")


print(driver.title)
link = driver.find_element(By.LINK_TEXT,'Pricing')
link.click()
btn = driver.find_element(By.CLASS_NAME,'switch-wrap')
btn.click()
WebDriverWait(driver,5)
btn.click()