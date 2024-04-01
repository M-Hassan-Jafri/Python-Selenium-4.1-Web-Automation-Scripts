from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Getting the ChromeDriver in webdriver variable to work with
                             # Chrome automation

driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()
driver.implicitly_wait(20)

Name = driver.find_element(By.ID, 'name')
Name.send_keys("Syed Muhammad Hassan Jafri")  # This method types in the input fields
time.sleep(2)

'''The Code below this comment is correct but its incomplete. I'll complete this after the FRAMES
   topic'''

GenderM = driver.find_element(By.CSS_SELECTOR, "#q2 > table > tbody > tr:nth-child(1) > td > label")
GenderM.click()
time.sleep(2)

DoB = driver.find_element(By.ID,"RESULT_TextField")
DoB.clear()
DoB.send_keys("07/14/2001")
time.sleep(2)

Job = driver.find_element(By.ID, "RESULT_RadioButton-3")
Job.click()
JobSelect = driver.find_element(By.XPATH, '//*[@id="RESULT_RadioButton-3"]/option[2]')
JobSelect.click()
time.sleep(2)

driver.find_element(By.NAME,"Submit").click()
time.sleep(5)



