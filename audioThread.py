#!/usr/bin/env python

# thread to handle inputs from alarms and buttons to start and stop alarms and mp3

#Steve Macenski (c) 2017

import Queue
import threading

class audio(threading.Thread):

    def __init__(self, snoozeQ, alarmoffQ, soundAlarmQ):
        threading.Thread.__init__(self)
        self.snoozeQ = snoozeQ
        self.alarmoffQ = alarmoffQ
        self.soundAlarmQ = soundAlarmQ

        self.stop = False


    def stop(self):
        self.stop = True


    def run(self):

    while (self.stop == False):
        # while still going, look for threads needing work

        snooze_hit = self.snoozeQ.get(False)
        alarmoff_hit = self.alarmoffQ.get(False)
        go_off = self.soundAlarmQ.get(False)

        if go_off:
            #TODO call play mp3 for alarm
            pass
        if smooze_hit:
            #TODO end alarm mp3 and play mp3 of news
            pass
        if alarmoff_hit:
            #TODO end alarm mp3 and  play mp3 of weather 
            pass



