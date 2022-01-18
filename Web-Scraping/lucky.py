#!/usr/bin/python3

import requests
import sys
import webbrowser
import bs4

print('Googling...')
response = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
#print(response.url)
response.raise_for_status()

#Retrieve top search result links.
soup = bs4.BeautifulSoup(response.text, features="lxml")

#Open a browser tab for each result.
linkElems = soup.select('a')
print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
