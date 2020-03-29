from bs4 import BeautifulSoup
import requests
import pandas

r = requests.get("https://en.wikipedia.org/wiki/Filmfare_Awards") #Fetch HTML Page
soup = BeautifulSoup(r.text, "html.parser") #Parse HTML
soup.prettify()
alltable = soup.findAll('table')

gnani = 1
for table in alltable:
	tabledata = table.tbody.findAll("tr")

	headings = []
	for head in tabledata[0].findAll("th"):
		headings.append(head.text.replace("\n",""))

	rows = []
	for tr in table.findAll('tr'):
		lis = []
		for td in tr.findAll('td'):
			lis.append(td.text.replace("\n", ""))
		rows.append(lis)

	# rows = [tr.findAll('td') for tr in table.findAll('tr')]

	with open('result'+str(gnani)+'.csv', 'a') as f:
		f.write(", ".join(str(e) for e in headings))

	for it in rows:
		with open('result'+str(gnani)+'.csv', 'a') as f:
		    f.write(", ".join(str(e).replace('<td>','').replace('</td>','') for e in it) + '\n')

	gnani = gnani+1


