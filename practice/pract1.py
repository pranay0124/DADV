from bs4 import BeautifulSoup
import requests
r = requests.get("https://en.wikipedia.org/wiki/Filmfare_Awards") #Fetch HTML Page
soup = BeautifulSoup(r.text, "html.parser") #Parse HTML
soup.prettify()#for good seperation of tags
# My_table = soup.find('table',{'class':'wikitable'})
# print(My_table)
# links = My_table.findAll('a')
# print(links)
# print("===========================================")
# names = []
# for link in links:
	# names.append(link.get('title'))
# print(names)
	#
	#
soup = BeautifulSoup(r.text, 'html.parser')
names = []
for row in soup.findAll('table')[1].tbody.findAll('tr')[1:]:
    first_column = row.findAll('td')[0]
    new = first_column.findAll('a')
    for link in new:
	    names.append(link.get('title'))
# print(names)


import pandas as pd
df = pd.DataFrame()
df['names'] = names
print(df)
