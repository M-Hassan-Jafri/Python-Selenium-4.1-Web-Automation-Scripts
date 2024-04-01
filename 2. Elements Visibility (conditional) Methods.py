from selenium import webdriver
from selenium.webdriver.common.by import By   # By class provides support for element(s)'
                                              # properties selection
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
print(driver.title)
time.sleep(4)

# find_element() method for interacting with web elements through different HTML properties
searchBar = driver.find_element(By.CLASS_NAME,"wikipedia-search-input")

print(searchBar.is_displayed())   # is_displayed() function to find whether the element is visible
print(searchBar.is_enabled())     # is_enabled() function to find whether the element is enabled

genderCheckBox = driver.find_element(By.ID,"male")
print(genderCheckBox.is_selected())  # is_selected() function to find whether the element is selected
                                     # usually this method is used for checkboxes, radio buttons etc.
time.sleep(22)
