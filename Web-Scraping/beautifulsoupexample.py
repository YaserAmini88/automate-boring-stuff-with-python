#!/usr/bin/python3

import bs4
import requests

response = requests.get('http://nostarch.com')
try:
    response.raise_for_status()
except Exception as e:
    print('An error occured while downloading html: ', e)
    exit(1)
else:
    noStarchSoup = bs4.BeautifulSoup(response.text, features="html.parser")
    print(type(noStarchSoup))
finally:
    print('-' * 50)
    exampleFile = open('example.html')
    exampleSoup = bs4.BeautifulSoup(exampleFile, features="html.parser")
    print(type(exampleSoup))
    exampleFile.close()
