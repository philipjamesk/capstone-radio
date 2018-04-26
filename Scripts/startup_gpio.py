import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

amp = 12
on = 23
lcd = 18
red = 19
green = 20

### Moved from radio.py ###

# # GPIO Set Up for Rotary Encoder and Switch
# sw = 16 # 16 for Production Radio, 17 for Test Radio
# clk = 6 # 6 for Production Radio, 23 for Test Radio
# dt = 5 # 5 for Production Radio, 27 for Test Radio
# GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(on, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(amp, GPIO.OUT)
GPIO.setup(lcd, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

GPIO.output(amp, GPIO.LOW)
GPIO.output(lcd, GPIO.LOW)
GPIO.output(red, GPIO.LOW)
GPIO.output(green, GPIO.LOW)

try:
    while True:
        # def check_events(current_station):
        #     # Will eventually be replaced with GPI Controls from Rotatry Encoder
        #
        #
        #     if GPIO.input(sw) == False:
        #
        #         sys.exit()
        #     if station_list[current_station].logo.rect.centerx <= 120 or station_list[current_station].logo.rect.centerx >= 200:
        #         radio.stop()
        #         current_station = -1
        #     if current_station == -1:
        #         for station in station_list:
        #             if station.logo.rect.centerx >= 120 and station.logo.rect.centerx <= 200:
        #                 current_station = station_list.index(station)
        #                 playStation(current_station)
        #     return current_station
        #
        # # 
        # def rotation_decode(clk):
        #     # read both of the switches
        #     Switch_A = GPIO.input(clk)
        #     Switch_B = GPIO.input(dt)
        #
        #     if (Switch_A == 1) and (Switch_B == 0) :
        #         move_right()
        #         draw_screen(screen)
        #         return
        #     elif (Switch_A == 1) and (Switch_B == 1 ):
        #         move_left()
        #         draw_screen(screen)
        #         return
        #     else:
        #         return
        #
        # GPIO.add_event_detect(clk, GPIO.RISING, callback=rotation_decode, bouncetime=2)

        if (GPIO.input(on)):
            GPIO.output(green, GPIO.LOW)
            GPIO.output(red, GPIO.HIGH)
            GPIO.output(lcd, GPIO.HIGH)
            GPIO.output(amp, GPIO.HIGH)
        else:
            GPIO.output(green, GPIO.HIGH)
            GPIO.output(red, GPIO.LOW)
            GPIO.output(lcd, GPIO.LOW)
            GPIO.output(amp, GPIO.LOW)
        sleep(0.1)
finally:
    GPIO.output(lcd, GPIO.LOW)
    GPIO.output(amp, GPIO.LOW)
    GPIO.cleanup()
