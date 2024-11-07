import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT) #16(32)

try:
    while True:
        print("Led On")
        GPIO.output(12,GPIO.HIGH)
        time.sleep(1)
        print("Led Off")
        GPIO.output(12,GPIO.LOW)
        time.sleep(2)
except:
    GPIO.cleanup()