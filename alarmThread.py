#!/usr/bin/env python

# thread for getting alarms from google calendar, checking if time is alarm time, maybe set alarms to go off and handling OR queue out for another thread to do.

# Steve Macenski (C) 2017

import threading
import datetime
import pytz
import time
import Queue

class alarms(threading.Thread):

    def __init__(self, soundQue, snooze_reset):
        threading.Thread.__init__(self)
        self.soundQue = soundQue
        self.stop_alarms = False
        self.snooze_reset = snooze_reset
        self.alarms = get_alarms()


    def get_alarms(self):
        # use google calendar API to get alarms from calendar
        #TODO

        # parse for the keywords "alarm" or "get up" 
        #list.sort() so theyre in order IS CRITICAL 

        return [datetime.datetime.today() - datetime.timedelta(hours = 1)]*2


    def sound_alarm(self):
        self.alarm_on = True
        
        self.soundQue.put("sound alarm")


    def stop(self):
        self.stop_alarms = True


    def run(self):
        
        while (self.stop_alarms == False):
            # calc time, see if matches the current time, at 1AM relook

            if self.snooze_reset.get(false):
                current = datetime.datetime.now()+datetime.timedelta(minutes=9)
                current.replace(second=0, microsecond=0)
                self.alarms.append(current)
                self.alarms.sort()

            if len(self.alarms) > 0:

                timeZone = pytz.timezone("America/Chicago")
                currentTime = datetime.datetime.now(timeZone)

                #truncate seconds and microseconds
                currentTime = currentTime.replace(second=0, microsecond=0)

                for alarm in self.alarms:
                    if alarm == currentTime and self.alarm_on == False:
                        self.sound_alarm()

                    if alarm < currentTime:
                        #old alarm, remove from list for efficiency & allow 
                        # for another alarm to go off
                        self.alarm_on = False
                        self.alarms.remove(alarm)
                
                if (alarm[0] == currentTime - datetime.timedelta(minutes=10)):
                     # if 10 minutes before first alarm, get weather and news
                     #assign to queue for those threads
                     #TODO
                     pass

            if currentTime.hour == 1 and currentTime.minute == 0:
                #get alarms at 1am
                self.alarms = get_alarms()

            time.sleep(1)
