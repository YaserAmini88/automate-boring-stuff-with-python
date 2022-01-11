#!/usr/loca/python3

import os

paths = os.path.join('usr','bin','spam')
print(paths)

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('/etc/bbb/', filename))
