import os
import time

def nudge_effect():
    for i in range(10):
        offset = " " * (i % 2 * 2)  # toggle between 0 and 2 spaces
        print(f"{offset}!!! ALARM !!!", end="\r")
        time.sleep(0.1)
    print("!!! ALARM !!!       ")  # clear extra characters
    
def flash_alarm():
    for i in range(10):
        os.system('clear')  # use 'cls' on Windows
        if i % 2 == 0:
            print("!!! ALARM !!!".center(80))
        time.sleep(0.2)

def main():
    #nudge_effect()
    #print("testeringo")
    flash_alarm()

main()
