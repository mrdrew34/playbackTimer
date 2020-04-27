#!/usr/bin/env python3.8


reload =  True
while reload == True:
    #### User Inputs ####
    hours = abs(float(input('How many hours is the video? ')))
    minutes = abs(int(input('How many minutes is the video? ')))
    seconds = abs(int(input('How many seconds is the video? ')))
    speed = abs(float(input('What is the new speed? ')))
    if speed < 0:
        print('Speed must be greater than 0')

    #### Time Conversions to Hours ####
    # convert minutes to hours
    minToHr = minutes / 60.0    
    # convert seconds to hours
    secToHr = seconds / 3600.0

    #### Time Totals ####
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
        
    #### Calculate changes in time####    
    # Calculate the amount of time saved
    DiffHr = totalHr - newHr
    # Calculate change in hours
    deltaHr = (DiffHr - int(DiffHr)) / 60
    # Calculate change in minutes
    deltaHrToMin = (deltaHr - int(deltaHr)) * 3600
    # Calculate change in seconds
    deltaMinToSec = (deltaHrToMin - int(deltaHrToMin)) * 60
    
    #### Print Calculation Outputs ####
    
    print('\nThe total time now is',int(newHr),'hour(s)',int(hrToMin),'minute(s)',int(round(minToSec)),'second(s).')
    if (DiffHr or deltaHrToMin or deltaMinToSec) < 0:
<<<<<<< HEAD
        print('\n******Taking',abs(int(DiffHr)),'hour(s)',abs(int(deltaHrToMin)),'minute(s)',abs(int(round(deltaMinToSec))),'second(s) longer.******')
    else:
        print('\n******You have saved',int(DiffHr),'hour(s)',int(deltaHrToMin),'minute(s)',int(round(deltaMinToSec)),'second(s).******')
=======
        print('Taking',abs(int(DiffHr)),'hour(s)',abs(int(deltaHrToMin)),'minute(s)',abs(int(round(deltaMinToSec))),'second(s) longer.')
    else:
        print('You have saved',int(DiffHr),'hour(s)',int(deltaHrToMin),'minute(s)',int(round(deltaMinToSec)),'second(s).')
>>>>>>> 98c286c... Finalizing time difference
    calcAnother = input('\nWould you like to run calculator again? (yes/no)').casefold()

    #### Try Again? ####
    if calcAnother == 'yes': reload = True
    elif calcAnother == 'y': reload = True
    elif calcAnother != 'yes': break

    ### Exceptions and negative values need to be addressed ###
