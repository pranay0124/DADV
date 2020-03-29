import time, csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime
import random
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("https://www.bseindia.com/corporates/List_Scrips.aspx")

# Segment selection
select = Select(driver.find_element_by_id('ContentPlaceHolder1_ddSegment'))
select.select_by_visible_text('Equity')
time.sleep(2)

# Status selection
select1 = Select(driver.find_element_by_id('ContentPlaceHolder1_ddlStatus'))
select1.select_by_visible_text('Active')
time.sleep(2)

driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()
driver.find_element_by_id("ContentPlaceHolder1_lnkDownload").click()
time.sleep(10)

# C:\Users\home\Downloads
code = []
f = open("C:\\Users\\dellg7\\Downloads\\Equity.csv", 'r')
readFile = csv.reader(f)

for row in readFile:
    code.append(row[0])

print(code)
time.sleep(5)

driver.get("https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.aspx?flag=0")

#date
driver.find_element_by_id("ContentPlaceHolder1_txtToDate").click()
time.sleep(3)
x = datetime.datetime.now()
date = str(int(x.strftime("%d")))
year = x.strftime("%Y")
driver.find_element_by_link_text(date).click()
time.sleep(2)
driver.find_element_by_id("ContentPlaceHolder1_txtFromDate").click()
select = Select(driver.find_element_by_class_name("ui-datepicker-year"))
pyear = str(int(year)-1)
select.select_by_visible_text(pyear)
driver.find_element_by_link_text(date).click()
time.sleep(2)

for i in range(0,30):
    random_code = random.choice(code)
    print(random_code)
    #company id
    search = driver.find_element_by_id('ContentPlaceHolder1_smartSearch')
    search.clear()
    search.send_keys(random_code)
    driver.find_element_by_class_name("quotemenu").click()
    #download
    driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()
    time.sleep(3)
    driver.find_element_by_id("ContentPlaceHolder1_btnDownload").click()
    time.sleep(10)

driver.close()