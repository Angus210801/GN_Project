from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Common.function_Configure import renameAndclose,borwserConfigure,getLocation,getLocation

driver = webdriver.Chrome()
driver.get("http://dkcphweb15/Xpress/31.X.Migration/MDCT/select-devices")

options = borwserConfigure()
global driver
driver = webdriver.Chrome(chrome_options=options)
from Common.function_Basic import windowsPage

windowsPage.clickNextButton()

device = (By.XPATH, "//label[contains(text(),'" + "Engage75" + "')]")
driver.click(*device)
driver.driver.find_element(By.ID, 'btnAdd').send_keys(Keys.ENTER)
driver.driver.find_element(By.XPATH, "//input[@value='NEXT >']").click()