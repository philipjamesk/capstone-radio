import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

amp = 12
on = 23
lcd = 18
red = 19
green = 20

GPIO.setup(on, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(amp, GPIO.OUT)
GPIO.setup(lcd, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

# Assume button is off to start and set all outputs accordingly
last_state = 0
GPIO.output(amp, GPIO.LOW)
GPIO.output(lcd, GPIO.LOW)
GPIO.output(red, GPIO.LOW)
GPIO.output(green, GPIO.HIGH)



try:
    while True:
        current_state = (GPIO.input(on))
        if current_state is not last_state:
            if (current_state):
                GPIO.output(green, GPIO.LOW)
                GPIO.output(red, GPIO.HIGH)
                GPIO.output(lcd, GPIO.HIGH)
                GPIO.output(amp, GPIO.HIGH)
            else:
                GPIO.output(green, GPIO.HIGH)
                GPIO.output(red, GPIO.LOW)
                GPIO.output(lcd, GPIO.LOW)
                GPIO.output(amp, GPIO.LOW)
            last_state = current_state
        sleep(0.1)

finally:
    GPIO.output(lcd, GPIO.LOW)
    GPIO.output(amp, GPIO.LOW)
    GPIO.cleanup()
