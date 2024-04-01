from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()
driver.implicitly_wait(22)

GenderRadioButton = driver.find_element(By.ID, "male")
GenderRadioButton.click()
time.sleep(4)

DayCheckBox = driver.find_element(By.ID, "saturday")
DayCheckBox.click()
time.sleep(4)

# "Select" class is used to select the options of a DropDown list by using its various methods
CountryDropDownList = Select(driver.find_element(By.ID, "country"))

CountryDropDownList.select_by_visible_text("China")
time.sleep(2)
CountryDropDownList.select_by_value("brazil")  # Value of the DropDown option in HTML
time.sleep(2)
CountryDropDownList.select_by_index(5)
time.sleep(2)

print("Test passed successfully!")