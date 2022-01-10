#!/usr/bin/python3

#This is a project for matching emails and phone numbers with Regex

import re
import pyperclip

phoneRegex = re.compile(r'''(
        (\d{3}|(\d{3}\))?       #area code - because we used '?' this part is optional
        (\s|-|\.)?              #separator - space, hyphen or dot
        (\d{3})                 #first 3 digits
        (\s|-|\.)               #separator
        (\d{4})                 #last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension - optional
        )''', re.VERBOSE)

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+       #username
        @                       # @ symbol
        [a-zA-Z0-9.-]+          # domain name
        (\.[a-zA-Z]{2,4})       # dot-something - for example .com, .org
        )''', re.VERBOSE)

#Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([group[1],group[3],group[5]]) #group1=area code, group3=first 3 digits, group5=last 4 digits
    if group[8] != '':                                #group8 = extension
        phoneNum += ' x' + group[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(group[0])                          #group0=matches the entire regex


#Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses were found.')
