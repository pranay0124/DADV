import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Filmfare_Awards")

table = pd.DataFrame(columns = ['Nominee','Category','Award','Year'])

tabdata = driver.find_elements_by_xpath('//*[@id="mw-content-text"]/div/table[2]')

lis = []
# List<WebElement> rows = driver.findElements(By.xpath("//table[@class='wikitable']/tbody/tr"));
TogetRows = driver.find_element_by_xpath("//table[@class='wikitable']/tbody")
rows = TogetRows.find_element_by_tag_name("tr")

print(rows)
# //*[@id="mw-content-text"]/div/table[2]/tbody/tr[1]
# //*[@id="mw-content-text"]/div/table[2]/tbody/tr[3]