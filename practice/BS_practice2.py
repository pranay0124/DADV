from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://en.wikipedia.org/wiki/Filmfare_Awards"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
print(soup)

data = []
table = soup.find('table', attrs={'class':'lineItemsTable'})
# table_body = table.find('tbody')

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

print(data)