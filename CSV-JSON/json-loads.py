#!/usr/bin/python3

import json

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felinIQ": null}' #json strings always use double quotes.
jsonDataPythonValue = json.loads(stringOfJsonData)
print(jsonDataPythonValue)
