from tkinter import *
from tkinter import ttk
import os
import time


root = Tk()
root.title("Clock App")

mainframe = ttk.Frame(root)
# mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

button = ttk.Button(root, text="Timer", command="buttonpressed", width= 30)
button.grid()
button = ttk.Button(root, text="Stopwatch", command="buttonpressed", width= 30)
button.grid()
button = ttk.Button(root, text="World Clock", command="buttonpressed", width= 30)
button.grid()
button = ttk.Button(root, text="Alarm", command="buttonpressed", width= 30)
button.grid()

# button.grid(row=5, sticky=S)

# se eu quisesse trocar o texto do button
# button.configure(text="Start here!")

""" EXAMPLE TUTORIAL
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
"""






"""
def intro():
    print("\nCountdown - V1\n\nAvailable time scales:\n1.Hour\n2.Minutes\n3.Seconds\n")
    pass

def conv_time_scale_to_seconds(time_scale, t):
    if time_scale == "1":
        countdown_ammount = t * 60 * 60
    elif time_scale == "2":
        countdown_ammount = t * 60
    elif time_scale == "3":
        countdown_ammount = t
    else:
        print("Error: Input not valid!")
        # raise ValueError("Error: Input not valid!")
        exit()
    return countdown_ammount

def countdown(countdown_ammount):
    while countdown_ammount:
        hours, remainder = divmod(countdown_ammount, 3600)
        mins, secs = divmod(remainder, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        # print(f"Time Left: {countdown_ammount}")
        print(f"Time Left: {timer}", end="\r")
        time.sleep(1)
        countdown_ammount -=1 


    print("\nTimer finished!")
    pass

def main():
    intro() # Na teoria, isto nao precisava de ser uma funcao...
    time_scale = input("Please select the time scale: ")
    t = int(input("Please set the countdown: "))
    countdown_ammount = conv_time_scale_to_seconds(time_scale,t)
    countdown(countdown_ammount)



if __name__ == __name__:
    main()

"""
root.mainloop()
