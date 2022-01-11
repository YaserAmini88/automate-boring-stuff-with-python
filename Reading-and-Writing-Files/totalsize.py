#!/usr/bin/python3

import os

totalsize = 0
path = '/root'

for filename in os.listdir(path):
    totalsize += os.path.getsize(os.path.join(path, filename))

print(totalsize)    
