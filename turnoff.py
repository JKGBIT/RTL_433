#!/usr/bin/env python
# rtl_433 -f 315M -F json | python rtl_2_led.py 
import RPi.GPIO as GPIO
import time
import sys
import json
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

a = 18
b = 23
c = 17
d = 22

GPIO.setup(a,GPIO.OUT)
GPIO.setup(b,GPIO.OUT)
GPIO.setup(c,GPIO.OUT)
GPIO.setup(d,GPIO.OUT) 

GPIO.output(a,False)
GPIO.output(b,False)
GPIO.output(c,False)
GPIO.output(d,False)

GPIO.cleanup()
