import time, csv, requests, datetime, random
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# chromeOptions = Options()
# chromeOptions.add_experimental_option("prefs", {"download.default_directory": "E:\\DADV\\Exam\\Download"})

# To download apple stocks data
# driver = webdriver.Chrome(options = chromeOptions)
# driver.get("https://finance.yahoo.com/quote/AAPL/history?period1=1519842600&period2=1544639400&interval=1d&filter=history&frequency=1d")
# driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span').click()

# driver.find_element_by_class_name('C($linkColor) Fz(14px)').innerHTML = "Mar 01, 2018 - Dec 13, 2018"
# driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div/div/span').innerHTML = "Mar 01, 2018 - Dec 13, 2018"


#to download S&P 100
# r = requests.get("https://en.wikipedia.org/wiki/S%26P_100")
# soup = BeautifulSoup(r.text, "html.parser")
# soup.prettify()
# table = soup.findAll('table')[2] 

# tabledata = table.tbody.findAll("tr")
# headings = []
# for head in tabledata[0].findAll("th"):
# 	headings.append(head.text.replace("\n",""))


# rows = []
# for tr in table.findAll('tr'):
# 	lis = []
# 	for td in tr.findAll('td'):
# 		lis.append(td.text.replace("\n", ""))
# 	rows.append(lis)


# with open('SP100.csv', 'a') as f:
# 	f.write(", ".join(str(e) for e in headings))

# for it in rows:
# 	with open('SP100.csv', 'a', encoding="utf-8") as f:
# 	    f.write(", ".join(str(e).replace('<td>','').replace('</td>','').replace(',','') for e in it) + '\n')


#to download sp100 companies
# sp100 = pd.read_csv("SP100.csv")
# symbols = sp100["Symbol"]

# chromeOptions = Options()
# chromeOptions.add_experimental_option("prefs", {"download.default_directory": "E:\\DADV\\Exam\\100_Day"})
# driver = webdriver.Chrome(options = chromeOptions)

# for each in symbols:
#     driver.get("https://finance.yahoo.com/quote/"+each+"/history?period1=1519842600&period2=1544639400&interval=1d&filter=history&frequency=1d")
#     driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span').click()
#     time.sleep(3)

# for each in symbols:
# 	driver.get("https://finance.yahoo.com/quote/"+each+"/history?period1=1519842600&period2=1544639400&interval=1d&filter=history&frequency=1wk")
# 	driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span').click()

# for each in symbols:
# 	driver.get("https://finance.yahoo.com/quote/"+each+"/history?period1=1519842600&period2=1544639400&interval=1d&filter=history&frequency=1mo")
# 	driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span').click()



# #to download S&P 500
# r = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
# soup = BeautifulSoup(r.text, "html.parser")
# soup.prettify()
# table = soup.findAll('table')[0] 

# tabledata = table.tbody.findAll("tr")
# headings = []
# for head in tabledata[0].findAll("th"):
# 	headings.append(head.text.replace("\n",""))


# rows = []
# for tr in table.findAll('tr'):
# 	lis = []
# 	for td in tr.findAll('td'):
# 		lis.append(td.text.replace("\n", ""))
# 	rows.append(lis)


# with open('SP500.csv', 'a') as f:
# 	f.write(", ".join(str(e) for e in headings))

# for it in rows:
# 	with open('SP500.csv', 'a', encoding="utf-8") as f:
# 	    f.write(", ".join(str(e).replace('<td>','').replace('</td>','').replace(',','') for e in it) + '\n')