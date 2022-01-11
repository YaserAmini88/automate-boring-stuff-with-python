#!/usr/bin/python3

import os

print(os.getcwd())

#change directory
os.chdir('/root')
print(os.getcwd())

os.makedirs('/root/myDir')
