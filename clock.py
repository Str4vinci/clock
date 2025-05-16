import time 
from datetime import datetime
import pytz


def intro():
    print("\nClock App - V1\n\nFeatures:\n1.Timer\n2.Stopwatch\n3.World Clock\n4.Alarm\n")
    pass

def intro_timer():
    print("\nTimer\n\nAvailable time scales:\n1.Hour\n2.Minutes\n3.Seconds\n")
    pass

def intro_stopwatch():
    print("\nStopwatch\n\nAvailable time scales:\n1.Hour\n2.Minutes\n3.Seconds\n")
    pass

def intro_worldclock():
    print("\nWorld Clock\n\nAvailable time scales:\n1.Hour\n2.Minutes\n3.Seconds\n")
    pass

def intro_alarm():
    print("\nAlarm\n\nAvailable time scales:\n1.Hour\n2.Minutes\n3.Seconds\n")
    pass

def conv_time_scale_to_seconds(time_scale, t):
    if time_scale == "1":
        timer_ammount = t * 60 * 60
    elif time_scale == "2":
        timer_ammount = t * 60
    elif time_scale == "3":
        timer_ammount = t
    else:
        print("Error: Input not valid!")
        # raise ValueError("Error: Input not valid!")
        exit()
    return timer_ammount

def timer(timer_ammount):
    while timer_ammount:
        hours, remainder = divmod(timer_ammount, 3600)
        mins, secs = divmod(remainder, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(f"Time Left: {timer}", end="\r")
        time.sleep(1)
        timer_ammount -=1 


    print("\nTimer finished!")
    pass


def stopwatch():
    pass

def world_clock():
    #For now, 3 Timezones: Porto, Australia (Melbourne), Los Angeles 
    tz_porto = 
    timezones={
        'Porto, Portugal': 
        'Los Angeles, USA'
        'Melbourne, Australia'
        
    

def main():
    intro() # Na teoria, isto nao precisava de ser uma funcao...
    feature_select= (input("Please select the feature: "))
    if feature_select == "1":
        intro_timer()
        time_scale = input("Please select the time scale: ")
        t = int(input("Please set the timer: "))
        timer_ammount = conv_time_scale_to_seconds(time_scale,t)
        timer(timer_ammount)
    elif feature_select == "2":
        intro_stopwatch()

    elif feature_select == "3":
        intro_worldclock()

    elif feature_select == "4":
        intro_alarm()

    else:
        raise ValueError("Error: Input not valid")


if __name__ == __name__:
    main()
