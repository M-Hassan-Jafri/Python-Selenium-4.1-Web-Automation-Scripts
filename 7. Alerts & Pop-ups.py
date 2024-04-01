from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")

driver.maximize_window()
driver.implicitly_wait(22)

driver.find_element(By.ID, "alertButton").click()
time.sleep(1.5)
driver.switch_to.alert.accept()  # 'switch_to' property is used to switch to an alert or popup
time.sleep(4)

driver.find_element(By.XPATH, '//*[@id="confirmButton"]').click()
time.sleep(1.5)
driver.switch_to.alert.dismiss()
time.sleep(4)
