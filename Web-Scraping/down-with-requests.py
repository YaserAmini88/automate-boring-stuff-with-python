#!/usr/bin/python3

import requests

response = requests.get('http://fararu.com')
print('Type of response in requests module: ' + str(type(response)))
print('*' * 50)
print('Status Code: ' + str(response))
print('*' * 50)
print('Length of response: ' + str(len(response.text)))
print('*' * 50)
print(response.text[:200])
print('*' * 50)

response2 = requests.get('http://fararu.com/dodo.txt')
try:
    response2.raise_for_status()
except Exception as exc:
    print('There was a problem:', exc)
else:
    print('Everything went smoothly')
