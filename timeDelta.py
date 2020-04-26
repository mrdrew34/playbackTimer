#!/usr/bin/env python3.8


reload =  True
while reload == True:
    # Get the times from the user
    hours = abs(float(input('How many hours is the video? ')))
    minutes = abs(int(input('How many minutes is the video? ')))
    seconds = abs(int(input('How many seconds is the video? ')))
    speed = abs(float(input('What is the new speed? ')))

    # convert minutes to hours
    minToHr = minutes / 60.0
    
    # convert seconds to hours
    secToHr = seconds / 3600.0
    
    # add the total hours
    totalHr = hours + minToHr + secToHr
    
    # calculate the relative speed (1 / speed change)
    relativeSpeed = float(1/speed)
    
    # calculate change in hours due to speed change
    newHr = totalHr * relativeSpeed
    
    # find minutes remaining
    hrToMin = (newHr - int(newHr)) * 60
    
    # find seconds remaining
    minToSec = (hrToMin - int(hrToMin)) * 60
    
    # Calculate the amount of time saved (work in progress)
    DiffHr = totalHr - newHr
    print(DiffHr)
    deltaHr = (DiffHr - int(DiffHr)) / 60
    print(deltaHr)
    deltaHrToMin = (deltaHr - int(deltaHr)) * 3600
    print(deltaHrToMin)
    deltaMinToSec = (deltaHrToMin - int(deltaHrToMin)) * 60
    print(deltaMinToSec)

    print('The total time now is',int(newHr),'hour(s)',int(hrToMin),'minute(s)',int(round(minToSec)),'second(s).')
    print('You have saved',int(DiffHr),'hour(s)',int(deltaHrToMin),'minute(s)',int(round(deltaMinToSec)),'second(s).')
    calcAnother = input("Would you like to run calculator again? (yes/no)").casefold()


    if calcAnother == 'yes': reload = True
    elif calcAnother == 'y': reload = True
    elif calcAnother != 'yes': break
