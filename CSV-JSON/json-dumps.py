#!/usr/bin/python3
#json.dumps() will translate a python value into a string of json-formatted data

import json

pythonValue = {'isCat': True, 'miceCaught': 9, 'name': 'Zophie', 'felinIQ': None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)
