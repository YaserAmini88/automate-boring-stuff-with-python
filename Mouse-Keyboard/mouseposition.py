#!/usr/bin/python3

import pyautogui

print('Press Ctrl+C to quit')

try:
    while True:
       #Get and print mouse coordinates.
       x,y = pyautogui.position()
       positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
       print(positionStr, end='') # end='' prevents default new line being added.
       print('\b' * len(positionStr), end='', flush=True) # \b = backspace
except KeyboardInterrupt:
    print('\nDone')
