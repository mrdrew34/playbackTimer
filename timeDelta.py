#!/usr/bin/env python3.8


reload =  True
while reload == True:

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
    
    calcAnother = input("Would you like to run calculator again? (yes/no)")

    if calcAnother == "yes": reload = True
    elif calcAnother == "no": break


