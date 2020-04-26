#!/usr/bin/env python3.8


hours = float(input('How many hours is the video? '))
minutes = int(input('How many minutes is the video? '))
seconds = int(input('How many seconds is the video? '))
speed = float(input('What is the new speed? '))
        
# hrToSec = hours * 3600
minToHr = minutes / 60.0
# print(minToHr)
secToHr = seconds / 3600.0
# print(secToHr)
totalHr = hours + minToHr + secToHr
# print(totalHr)
relativeSpeed = float(1/speed)
newHr = totalHr * relativeSpeed
# print(newHr)
# print(int(newHr))
hrToMin = (newHr - int(newHr)) * 60
# print(int(hrToMin))
minToSec = (hrToMin - int(hrToMin)) * 60
# print(int(round(minToSec)))
Diff = totalHr - newHr
# print(Diff)



print('The total time now is',int(newHr),'hour(s)',int(hrToMin),'minute(s)',int(round(minToSec)),'second(s).')
input()
    
# if reload == 'no' or '':
    # break
# reload = input('Would you like to continue? (yes/no)')

# print('Which has saved',int(hours - newHr),'hour(s)', int(minutes - hrToMin),'minute(s)',int(seconds-minToSec),'second(s).')
# print(secsToHr)
# secsToMin = ((secsToHr - round(secsToHr)) * 60.0)
# print(secsToMin)
# finalSecs = ((secsToMin - round(secsToMin)) * 60.0)
# print(round(secsToMin))
# print(finalSecs)


# print('The total time is now ', round(secsToMin) , ' minute(s) and ', round(finalSecs), ' seconds.')
# print('This saves ',hours - secsToHr, ' hour(s) ',minutes - secsToMin,' minutes and ',round(seconds - finalSecs),'seconds.')

# input("Press enter to exit: ")
