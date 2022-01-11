#!/usr/bin/python3

import os

#Returns absolute path
print(os.path.abspath('.'))

#Checks for absolute path
print(os.path.isabs('/root/myDir'))

path = '/etc/apache2/apache2.conf'
print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.split(path))
print(path.split(os.path.sep))

path2 = '/root'
print(os.path.getsize(path2))
print(os.listdir(path2))
