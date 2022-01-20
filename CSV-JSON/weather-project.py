#!/usr/bin/python3

import requests
import json
import sys

if len(sys.argv) < 2: #first argument of sys.argv is the name of the script itself
    print("Usage: python3 weather-ptoject.py location")
    sys.exit()
location = ' '.join(sys.argv[1:]) #everything after first argument which is the name of the script


#Download the json data from weatherapi.com
url = 'http://api.weatherapi.com/v1/current.json?key=30588d7023f14fee99e83550222001&q=%s' % (location)
response = requests.get(url)
response.raise_for_status()
#print(response.text)

#Load json data to a python variable
weatherData = json.loads(response.text)
w = weatherData['current']['condition']['text']
s = weatherData['current']['wind_mph']
print('Current weather of %s is: ' % (location) + w )
print('Wind speed is: ', s)
