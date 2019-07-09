import urllib2, csv
from bs4 import BeautifulSoup
outfile = open('ut_legislators.csv','w')
writer = csv.writer(outfile)

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for l in letters:
	url = "https://le.utah.gov/asp/roster/complist.asp?letter=" + l
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')

	table = soup.find('table', {'class': 'UItable'})
	rows = table.find_all('tr')

	for row in rows:
		data = []
		cells = row.find_all('td')

		for cell in cells:
			data.append(cell.text.encode('utf-8').strip())
		if len(data) > 0:
			writer.writerow(data)

outfile.close()