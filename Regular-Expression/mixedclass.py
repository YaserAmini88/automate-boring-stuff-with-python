#!/usr/bin/python3

import re

xmasRegex = re.compile(r'\d+\s\w+') # Matches : digit + space + one or more letter/digit/underscore
output = xmasRegex.findall('12 monkeys, 11pipers, 10 lords, 9 maids')
print("Output of mixed classes: " + str(output))
