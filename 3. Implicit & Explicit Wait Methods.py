import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
print(driver.title)

driver.implicitly_wait(0)     # This method is used to wait for all the elements on a webpage
                              # until their visibility (with a maximum waiting time limit)

NBWButton = driver.find_element(By.XPATH,'//*[@id="HTML4"]/div[1]/button')

NBWButton.click()             # This method clicks the element

try:
    WBWait = WebDriverWait(driver, 1)    # WebDriverWait class instance is used for explicit wait
    WBWait.until(EC.presence_of_element_located((By.ID, "field2")))   # self-explaining methods
    print("I got the Field2")
    time.sleep(4)

except TimeoutException:
    print("I couldn't found the Field2")

finally:
    driver.quit()

# WBWait.click()
time.sleep(2)
