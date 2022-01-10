#!/usr/bin/python3

#This is a project for matching emails and phone numbers with Regex

import re
import pyperclip

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?
        (\s|-|\.)?
        (\d{3})
        (\d|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
        )''', re.VERBOSE)


emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+       
        @                       
        [a-zA-Z0-9.-]+          
        (\.[a-zA-Z]{2,4})   
        )''', re.VERBOSE)

#Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]]) #group1=area code, group3=first 3 digits, group5=last 4 digits
    if groups[8] != '':                                   #group8 = extension
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])                          #group0=matches the entire regex


#Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses were found.')
