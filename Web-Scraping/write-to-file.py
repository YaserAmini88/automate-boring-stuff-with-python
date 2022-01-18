#!/usr/bin/python3

import requests

response = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

try:
    response.raise_for_status()
except Exception as e:
    print('The was an error downloading the url you requested: ', e)
    exit(1)
else:
    playFile = open('RomeoAndJuliet.txt', 'wb')  # Open file in binary
    for chunk in response.iter_content(1000):
        playFile.write(chunk)
    playFile.close()    
    print('*' * 50)
    print('Finish writing data to RomeAndJuliet.txt')
