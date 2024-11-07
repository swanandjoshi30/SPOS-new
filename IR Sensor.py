import RP1.GPIO as GPIO
import time

sensor 16 #36(18)
led 12 #32(16)
buzzer 18 #12(6)

GPIO.setmode (GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.output (led, False)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.output (buzzer, False)

print ("IR Sensor Ready...")
print("")

try:
    while True:

        if GPIO.input(sensor): 
            GPIO.setwarnings(True)
            GPIO.output (led, True)
            GPIO.output (buzzer, True)
            print ("Object detected")
            while GPIO.input (sensor):
                time.sleep(0.2)

        else:
            GPIO.output (led, False) 
            GPIO.output (buzzer, False) 
            print("Object not detected")

except Keyboardinterrupt: 
    GPIO.cleanup()