#!/usr/bin/python3

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no group
output = phoneNumRegex.findall('Cell: 455-555-9999 Work: 222-345-7777')
print("All numbers extracted with findall function: " + str(output))
