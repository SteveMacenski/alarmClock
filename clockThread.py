#!/usr/bin/env python

# Thread for running the alarm clock display time features 
#Steve Macenski (c) 2017

import threading
import sys
import time
import datetime
import pytz
from Adafruit_7Segment import SevenSegment

class displayTime(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

        self.display = SevenSegment(address=0x70)

        self.stop_clock = False

    
    def stop(self):
        # when application closes, stop thread from spinning

        self.display.disp.clear()

        self.stop_clock = True


    def run(self):
        # continue working until it stops

        while (self.stop_clock == False):    
    
            # find the current time and update display
            timeZone = pytz.timezone("America/Chicago")
            currentTime = datetime.datetime.now(timeZone)

            self.display.writeDigit(0, int(currentTime.hour/10)) 
            self.display.writeDigit(1, hour % 10)
            self.display.writeDigit(3, int(minute/10))
            self.display.writeDigit(4, minute % 10)

            time.sleep(1)
