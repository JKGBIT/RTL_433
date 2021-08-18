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

def led(leds):
        for x in leds:
            GPIO.output(x,True)
        time.sleep(1)
        for x in leds:
            GPIO.output(x,False)


def get_rtl_433_data():
     while True:
        line = sys.stdin.readline()
        if not line:
            break
        else:
            try:
                data = json.loads(line)
                i = data["cmd"]
                print(data)
                if(i == 3):
                    print("A")
                    leds = [a]
                elif(i == 12):
                    print("B")
                    leds = [b]
                elif(i == 48):
                    print("C")
                    leds = [c]
                elif(i == 192):
                    print("D")
                    leds = [d]
                elif(i == 15 or i == 7):
                    print("A+B")
                    leds = [a,b]
                elif(i == 51):
                    print("A+C")
                    leds = [a, c]
                elif(i == 195):
                    print("A+D")
                    leds = [a, d]
                elif(i == 60):
                    print("B+C")
                    leds = [b, c]
                elif(i == 204 or i == 196):
                    print("B+D")
                    leds = [b, d]
                elif(i == 240):
                    print("C+D")
                    leds = [c, d]
                else:
                    print("OOPS")
                    leds = []
                    
                if not leds:
                    break
                led(leds)

            except:
                print("Something went wrong")
                GPIO.cleanup()

if __name__ == "__main__":
    get_rtl_433_data()
