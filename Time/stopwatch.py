#!/usr/bin/python3

import time

print("Press Enter to begin. Afterwards, press Enter to click the stopwatch. Press ctrl+c to quit")
input()      #press enter to begin
print("Started...")
startTime = time.time()
lastTime = startTime
lapNum = 1

#start tracking the lap time
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print("Lap #%s: %s (%s)" % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()   #reset the last lap time
except KeyboardInterrupt:
    #Handle the ctrl+c exception to keep its error message from displaying
    print('\nDone.')
