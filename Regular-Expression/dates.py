#!/usr/bin/python3

import re

patterns = re.compile(r'''
        (\d|\d{2}|\d{4})
        (\s|-|\.|\/)
        (\d{2}|\d)
        (\s|-|\.|\/)
        (\d{4}|\d{2})
        ''', re.VERBOSE)

test_dates = u"12/25/0000, 10.21.1955, 10-21-1985"

for groups in patterns.findall(test_dates):
    result = re.sub('groups[5]', 'groups[1]', test_dates)
    print(result)
