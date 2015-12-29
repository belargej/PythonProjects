#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")
assert "Google" in driver.title
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("cnnmoney"+Keys.RETURN)
