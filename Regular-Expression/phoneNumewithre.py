#!/usr/bin/python3

import re

phoneNumRegex = re.compile(r'(\d\d)-\d\d\d\d-\d\d\d\d') # \d stands for decimal
message = phoneNumRegex.search("You can call me with this number: 98-2234-3345.")
print("Area code of number is: " + "(" + message.group(1) + ")")
print("Phone number found: " + message.group())
