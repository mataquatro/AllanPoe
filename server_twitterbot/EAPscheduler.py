#!/usr/local/bin/python2.7

from threading import Timer
import datetime as dt
import random
import os

# This is what will be executed on the defined schedule.
def full_path():
    print dt.datetime.now()
    os.system('/home/gileshc/twitterbot/EAPbot.py')
    
# This accepts number of seconds before executing full_path
def ticktock(tempo):
    t = Timer(tempo, full_path)
    t.start()

# Return a list with the number of seconds used in ticktock.
def gotime():
    timer1 = (random.randint(1,3) * 60)
    timer2 = (random.randint(4, 15) * 60)
    timer3 = (random.randint(3, 7) * 60)
    
    tempos = [timer1, timer2, timer3]
    return tempos

t = gotime()
ticktock(t[0])
ticktock(t[1])
ticktock(t[2])
