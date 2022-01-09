#!/usr/bin/python3

import re

heroRegex = re.compile(r'Superman|Batman')
message = heroRegex.search('Superman are my favorite heroes')

batRegex = re.compile(r'Bat(man|mobile|woman|bat)')
batmessage = batRegex.search('Batbat lost a wheel')

batRegex2 = re.compile(r'Bat(wo)?man') # ? means that match 'wo' optionally - matching zero or one
mo1 = batRegex2.search("The advantures of Batman")
mo2 = batRegex2.search("The adventures of Batwoman")

batRegex3 = re.compile(r'Bat(wo)*man') # * means match zero or more
Regex3 = batRegex3.search("The adventures of Batwowowowowoman")

batRegex4 = re.compile(r'Bat(wo)+man') # + means match one or more
mo4 = batRegex4.search("The adventures of Batwowowowoman")


repetition1 = re.compile(r'(Ha){3}') # matches = HaHaHa
repetition2 = re.compile(r'(Ha){3,5}') # matches = HaHaHa, HaHaHaHa, HaHaHaHaHa
repetition3 = re.compile(r'(Ha){3,}') # matches = HaHaHa, HaHaHaHa, ...
repetition4 = re.compile(r'(Ha){,3}') # matches = , Ha, HaHa, HaHaHa
mo5 = repetition1.search("HaHaHa")
mo6 = repetition3.search("HaHaHaHaHaHaHaHa")

print("Output is: " + message.group())
print("Output of Bat is: " + batmessage.group())
print("Output of mo1: " + mo1.group())
print("Output of mo2: " + mo2.group())
print("Output of Asterisk: " + Regex3.group())
print("Output of mo4: " + mo4.group())
print("Output of repetition1: " + mo5.group())
print("Output of repetition3: " + mo6.group())
