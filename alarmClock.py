#!/usr/bin/env python

# alarm clock for raspberry pi zero, MRP121, 7-segment backpack and wifi

# Steve Macenski (c) 2017
import clockThread
import alarmsThread
import audioThread
import buttonThread
import sys
import exit
import Queue

class alarmClock():
    def __init__(self):
       print "starting up alarm clock . . ."
       self.execute()

       if len(sys.argv) > 1:
           self.args = sys.argv[1]
    
    def execute(self):

        # start up all of the threads and items

        # setup Queue
        snooze_press_audio = Queue.Queue()
        snooze_press_reset = Queue.Queue()
        alarmOff_press = Queue.Queue()
        soundAlarm = Queue.Queue()

        print "starting up clock . . . "
        try:
            displayClock = clockThread.clockThread(setAlarm_press)
            displayClock.setDaemon(True)
            displayClock.start()
        except:
            print "display setup FAILED"
            os._exit(1)

        print "starting up alarms . . ."
        try:
            alarms = alarmsThread.alarms(soundAlarm, snooze_press_reset)
            alarms.setDaemon(True)
            alarms.start()
        except:
            print "alarm functions FAILED"
            os._exit(1)

        print "starting up button sensitivity. . . "
        try:
            buttons = buttonThread.buttonPresses(snooze_press_audio, alarmOff_press)
            buttons.setDaemon(True)
            buttons.start()
            pass
        except:
            print "button threads FAILED"
            os._exit(1)

        print "starting up audio thread. . . "
        try:
            audio = audioThread.audio(snooze_press, alarmOff_press, soundAlarm)
            audio.setDaemon(True)
            audio.start()
        except:
            print "audio thread FAILED"
            os._exit(1)

clock = alarmClock()

