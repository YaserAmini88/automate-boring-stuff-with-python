#!/usr/bin/python3

#This is a project for matching emails and phone numbers with Regex

import re
import pyperclip

protocolRegex = re.compile(r'''(
        https?://               #matches http and https
        (?:w{3}\.)?             #matches www-dot
        [a-zA-Z0-9_-]+          #domain name
        \.                      #dot
        [a-zA-Z]{2,3}           #extension 
        )''', re.VERBOSE)


#Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []

for website in protocolRegex.findall(text):
    matches.append(website) 


#Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses were found.')
