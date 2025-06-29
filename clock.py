import time 
import zoneinfo
from datetime import datetime, timezone, timedelta
import sys
import select

def intro():
    print("\nClock App - V1\n\nFeatures:\n1.Timer\n2.Stopwatch\n3.World Clock\n4.Alarm\n")
    pass

def intro_timer():
    print("\nTimer\n\nAvailable time scales:\n1.Hour\n2.Minutes\n3.Seconds\n")
    pass

def intro_stopwatch():
    print("\nStopwatch\n")
    pass

def intro_worldclock():
    print("\nWorld Clock\n")
    pass

def intro_alarm():
    print("\nAlarm\n")
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
    # print("Please press Enter to start the stopwatch. When you want to stop, press Enter again!")
    input("Press Enter to start!")
    stopwatch_start_time = time.time()

    print("Stopwatch Started. Press Enter again to stop.")
    
    while True:
        elapsed_time = time.time() - stopwatch_start_time
        stopwatch_display_time(elapsed_time)
        time.sleep(0.1)

        if stopwatch_is_enter_pressed():
            break
    
    print("\nStopwatch stopped.")
    stopwatch_display_time(elapsed_time, final=True)

def stopwatch_display_time(sec, final=False):
    mins = int(sec // 60)
    hours = int(mins // 60)
    mins = mins % 60
    sec = round(sec % 60, 1)

    formatted_time = f"{hours:02}:{mins:02}:{sec:03.1f}"
    
    
    if final:
        print(f"Time Lapsed = {formatted_time}")
    else:
        print(f"\rTime Lapsed = {formatted_time}", end="", flush=True)

def stopwatch_is_enter_pressed():
    # import sys
    # import select
    # Estes imports aqui dão delay e fazem com que a mensagem não apareça imediatamente...

    if select.select([sys.stdin], [], [], 0)[0]:
        sys.stdin.read(1)  # Consume the Enter key
        return True
    return False

def world_clock():
    #For now, 3 Timezones: Porto, Australia (Melbourne), Los Angeles 
    timezones={
        'Porto, Portugal': "Europe/Lisbon" ,
        'Los Angeles, USA': "America/Los_Angeles",
        'Melbourne, Australia': "Australia/Melbourne" 
}
    
    for city, tz_name in timezones.items():
        tz = zoneinfo.ZoneInfo(tz_name)
        time_in_zone = datetime.now(tz)
        # print(f"The time in {city} is {time_in_zone}.")
        print(f"The time in {city} is {time_in_zone.strftime('%m-%d %H:%M:%S')}.")
    print('')   
    pass

def alarm(set_alarm):
    current_time = datetime.now()
    today_date = datetime.now().date()
    alarm_time = datetime.strptime(set_alarm,"%H:%M").time()
    alarm_datetime = datetime.combine(today_date, alarm_time)
    if alarm_datetime < current_time:
        alarm_datetime += timedelta(days=1) 
    timeleft = alarm_datetime - current_time
    while timeleft.total_seconds() > 0:
        current_time = datetime.now()
        timeleft = alarm_datetime - current_time
        total_seconds = int(timeleft.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"Time left: {hours:02}:{minutes:02}:{seconds:02}", end="\r")
        #print(f"Time left: {timeleft}", end="\r")
        time.sleep(1)

    print("\nAlarm!")

    pass 
    



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
        stopwatch()

    elif feature_select == "3":
        intro_worldclock()
        world_clock()

    elif feature_select == "4":
        intro_alarm()
        set_alarm = input("Please set the timer (for example, 23:30): ") 
        #time_scale = input("Please select the time scale: ")
        #timer_ammount = conv_time_scale_to_seconds(time_scale,t)
        alarm(set_alarm)

    else:
        raise ValueError("Error: Input not valid")


if __name__ == __name__:
    main()
