#!/usr/bin/pyhton3

#Change all american-style dates to european-style dates: MM-DD-YYYY -> DD-MM-DDDD

import os
import re
import shutil

datePattern = re.compile(r'''^(.*?)       #all text before the date
        ((0|1)?\d)-                       #one or two digits for the month
        ((0|1|2|3)?\d)-                   #one or two digits fo the day
        ((19|20)\d\d)                     #four digits for the year
        (.*?)$                            #all text after the date
        '''), re.VERBOSE)


for amerFilename is os.listdir('.'):
    mo = datePattern.search(amerFilename)

    #Skip files without date
    if mo == None:
        continue

    #Get different parts of filename
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(3)
    yearPart   = mo.group(4)
    afterPart  = mo.group(5)

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print('Renaming "%s" to "%s"...' %(amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)
