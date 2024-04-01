from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()
driver.implicitly_wait(22)

# find_elements() method finds all the elements with the same attribute called by 'By' class
All_Links = driver.find_elements(By.TAG_NAME,"a")

TotalLinks = len(All_Links)  # len() function will count total number of links on the current page
print(f"Total no. of links is: {TotalLinks}")

# time.sleep(4)

# Looping to get all the links' accessible names (link texts)
for li in All_Links:
    print(li.accessible_name)  # 'accessible_name' property is used to get the links' visible texts

time.sleep(2)

# 'LINK_TEXT' attribute is used to find a link on webpage by locating its Text/Accessible name
driver.find_element(By.LINK_TEXT, "orange HRM").click()
time.sleep(4)
driver.back()
time.sleep(2)

# 'PARTIAL_LINK_TEXT' attribute is used to find a link on webpage by locating its partial
# Text/Accessible name
driver.find_element(By.PARTIAL_LINK_TEXT, "Atom").click()
time.sleep(4)
