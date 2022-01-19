#!/usr/bin/python3

import csv

File = open('example.csv')
Reader = csv.reader(File)
for row in Reader:
    print('Row #' + str(Reader.line_num) + ' ' + str(row))
