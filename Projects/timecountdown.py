import time
import sys
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f'\r{timeformat}',end='\r')
        time.sleep(1)
        t -= 1
    print("goodbye")
countdown(10)
