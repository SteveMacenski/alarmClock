#!/usr/bin/env python

# button thread to check for input and then place hits on appropriate queues

# Steve Macenski (C) 2017

import Queue
import threading

class buttonPresses (threading.Thread):
    def __init__(self, snoozeQue, alarmOffQue):
        threading.Thread.__init__(self)
       
        self.snoozeQue = snoozeQue
        self.alarmOffQue = alarmOffQue
        self.soundAlarmQue = soundAlarmQue


    def stop(self):

        self.stopButtons = True


    def run(self):

        while (self.stopButtons == False):

            # query for inputs for each button TODO

            #if snooze pressed
            # snoozeQue.put(1)
            #if alarm off pressed
            # alarmOffQue.put(1)
            pass
