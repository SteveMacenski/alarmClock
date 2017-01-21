#!/usr/bin/env python

# button thread to check for input and then place hits on appropriate queues

# Steve Macenski (C) 2017

import Queue
import threading
import Adafruit_MPR121.MPR121 as MPR121

class buttonPresses (threading.Thread):
    def __init__(self, snoozeQue, alarmOffQue):
        threading.Thread.__init__(self)
       
        self.snoozeQue = snoozeQue
        self.alarmOffQue = alarmOffQue
        self.soundAlarmQue = soundAlarmQue

        self.cap = MPR121.MPR121()

    def stop(self):

        self.stopButtons = True


    def run(self):
        last_touched = cap.touched()

        while (self.stopButtons == False):
            current_touched = self.cap.touched()

            for i in range(12):

                pin_bit = 1 << i

                if current_touched & pin_bit and not last_touched & pin_bit:
                    if i == 0:
                        # snooze button in 0 slot
                        snoozeQue.put(1)
                    if i == 1:
                        # off button in 1 slot
                        alarmOffQue.put(1)

                last_touched = current_touched
                time.sleep(0.1)
