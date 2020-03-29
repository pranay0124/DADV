import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Windows.html")

#some driver functions
print(driver.title)
print(driver.current_url)

#finding the element by the X-path
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(3)

#to close the driver browser
driver.close() #closes only one tab
driver.quit() #closes all the tabs


#Navigation of pages
driver.get("https://www.youtube.com/")
time.sleep(3)
driver.get("https://leetcode.com/problemset/all/")
time.sleep(3)

driver.back()
driver.forward()


#Conditional Commands
#is_displayed(), is_Enabled(), is_selected() - gives true or false if the element is present or not

