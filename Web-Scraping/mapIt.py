#!/usr/bin/python3

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    #Get address from command line.
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    #Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)    
