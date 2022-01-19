#!/usr/bin/python3

import csv

File = open('example.csv')
Reader = csv.reader(File)
Data = list(Reader)
print('Data from CSV file: ')
print('*' * 50)
print(Data)
print('*' * 50)
print('Print Second row -> First column: ', Data[1][0]) # Data[row][col]
print('Print Fifth row -> First column: ', Data[4][0]) # Data[row][col]
