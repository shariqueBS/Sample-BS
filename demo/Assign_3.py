import pytest
from selenium.webdriver.common.by import By
import time


def test_pricing_toggle(selenium):
    selenium.get('https://www.browserstack.com')

    selenium.maximize_window()
    print(selenium.title)
    time.sleep(3)
    link = selenium.find_element(By.LINK_TEXT,'Pricing')
    link.click()
    time.sleep(3)
    btn = selenium.find_element(By.CLASS_NAME,'switch-wrap')
    btn.click()
    time.sleep(3)
    btn.click()
    time.sleep(3)

    assert selenium.title == 'Hey bro'


   
