#!/usr/bin/python3

import bs4

soup = bs4.BeautifulSoup(open('example.html'), features="html.parser")
spanElem = soup.select('span')[0]
print('Span Elements: ', spanElem)
print('Span ID: ', spanElem.get('id'))
print('Span attributes: ', spanElem.attrs)
