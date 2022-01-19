#!//usr/bin/python3

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

#Loop through every file in currecnt directory

for csvfile in os.listdir('.'):
    if not csvfile.endswith('.csv'):
        continue
    print('Removing header from ' + csvfile + '...')

    #Read from csv file and skip 1st line
    csvRow = []
    csvFileObj = open(csvfile)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRow.append(roww)
    csvFileObj.close()

    #Write out csv file
    csvFileObj = open(os.path.join('headerRemoved', csvfile), 'w')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRow:
        csvWriter.writerow(row)
    csvFileObj.close()    
