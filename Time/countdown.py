#!/usr/bin/python3

import time
import subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')  # end='' adds in the end of print command. by default end is equal to newline
    time.sleep(1)
    timeLeft = timeLeft -1

#subprocess.Popen(['start', 'alarm.wav'], shell=True)    
