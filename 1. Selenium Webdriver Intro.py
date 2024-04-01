from selenium import webdriver
import time

driver = webdriver.Chrome()  # Getting the ChromeDriver in webdriver variable to work with
                             # Chrome automation

driver.get("https://www.google.com/")

driver.maximize_window()
time.sleep(1)
driver.minimize_window()
time.sleep(1)
driver.maximize_window()

print(driver.title)
time.sleep(2)

driver.get("https://itsc.usindh.edu.pk/")    # get() method Loads a webpage
print(driver.title)    # title property will get the title of the current webpage
time.sleep(3)    # sleep() method for delaying the execution (wait)

driver.back()    # back() is used for navigating to the previous webpage
print(driver.title)
time.sleep(2)

driver.forward()    # forward() is used for navigating forward to the next webpage
print(driver.title)
time.sleep(2)