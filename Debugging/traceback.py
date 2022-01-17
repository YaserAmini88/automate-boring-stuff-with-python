#!/usr/bin/python3

import traceback

try:
    raise Exception('This is the error message')
except:
    errorFile = open('log.txt', 'w')
    errorFile.write(traceback.format_exec())
    errorFile.close()
    print('The traceback info was written in log.txt file.')

