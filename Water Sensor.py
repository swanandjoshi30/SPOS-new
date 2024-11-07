import RPi.GPIO as GPIO         # Import library

# Initalize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setup(16, GPIO.IN)         # Set GPIO 16 as input for water level sensor signal 36(18)
GPIO.setup(26, GPIO.OUT)         # Set GPIO 6 as output for LED 37(22)

try:
    while True:
        if (GPIO.input(16)):
            GPIO.output(26, True)    # Turn ON LED if water detected
        else:
            GPIO.output(26, False)   # Keep LED OFF if no water detected
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program exited by user.")