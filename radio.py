#!/usr/bin/env python3

import sys
import os
import time
import pickle
import json

import RPi.GPIO as GPIO

import pygame
import vlc

from station import Station
from logo import Logo

# Make a list of stations
station_list = []
os.putenv('SDL_FBDEV', '/dev/fb1')
screen = pygame.display.set_mode((320,240), pygame.FULLSCREEN)
playlist = vlc.MediaList()
radio = vlc.MediaListPlayer()

# GPIO Set Up for Rotary Encoder and Switch
sw = 17
clk = 19
dt = 20
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main_loop():
    # Put all the initial settings here
    pygame.display.init()
    pygame.mouse.set_visible(False)
    screen_rect = screen.get_rect()


    # find path to folder and change directory
    os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))

    # unpickle last saved playing station otherwise play index 0
    try:
        current_station = pickle.load(open("current_station.pickle", "rb" ))
    except:
        current_station = 0

    # import station list from JSON file
    json_data = open("stations.json").read()
    data = json.loads(json_data)

    # double check that the current_station is still in the station list
    if current_station >= len(data):
        current_station = 0

    # load stations into station list
    for item in data:
        station = Station(item['address'], item['logo'], screen, item['name'])
        station_list.append(station)
        if station_list.index(station) == current_station:
            station.is_playing = True

    # add stations to MediaList
    for station in station_list:
        playlist.add_media(station.address)

    # Set radio MediaList
    radio.set_media_list(playlist)

    # Place logos according to initial playing station
    place_logos(current_station)

    # play current station
    for station in station_list:
        if station.is_playing:
            playStation(station_list.index(station))

    draw_screen(screen, screen_rect)

    while True:
        # This is where pygame will listen for keypresses, update the logos
        # and flip the screen
        # draw_logos(logos, screen)
        time.sleep(.1)
        current_station = check_events(current_station, screen_rect)

def check_events(current_station, screen_rect):
    # Will eventually be replaced with GPI Controls from Rotatry Encoder


    if GPIO.input(sw) == False:
        if v == 'escape':
             sys.exit()
        if station_list[current_station].logo.rect.centerx <= 120 or station_list[current_station].logo.rect.centerx >= 200:
            radio.stop()
            current_station = -1
        if current_station == -1:
            for station in station_list:
                if station.logo.rect.centerx >= 120 and station.logo.rect.centerx <= 200:
                    current_station = station_list.index(station)
                    playStation(current_station)
    return current_station


def move_right():
    for station in station_list:
        station.logo.changex(25)

def move_left():
    for station in station_list:
        station.logo.changex(-25)

def place_logos(current_station):
    """Initially places the logos based on the current_station."""
    x = 160 - (current_station * 100)
    for station in station_list:
        station.logo.setx(x)
        x += 100

def draw_screen(screen, screen_rect):
    # Set the background color
    bg_color = (232, 222, 199)
    screen.fill(bg_color)

    # Add the rest to the display
    dial_marks = pygame.image.load('img/display/radio-marks.png')
    red_line = pygame.image.load('img/display/red-line.png')
    dial_marks_rect = dial_marks.get_rect()
    red_line_rect = red_line.get_rect()
    dial_marks_rect.centerx = screen_rect.centerx
    dial_marks_rect.centery = screen_rect.centery
    red_line_rect.centerx = screen_rect.centerx
    red_line_rect.centery = screen_rect.centery

    # Add station logos to screen
    for station in station_list:
        station.logo.blitme()

    # Add dial marks and red line to screen
    screen.blit(dial_marks, dial_marks_rect)
    screen.blit(red_line, red_line_rect)


    pygame.display.flip()

# Play a stream
def playStation(station):
    radio.play_item_at_index(station)
    pickleStation(station)

# Pickle the current station
def pickleStation(current_station):
    pickle.dump(current_station, open( "current_station.pickle", "wb" ))

def rotation_decode(clk):
    # read both of the switches
    Switch_A = GPIO.input(clk)
    Switch_B = GPIO.input(dt)

    if (Switch_A == 1) and (Switch_B == 0) :
        move_right()
        return

    elif (Switch_A == 1) and (Switch_B == 1 ):
        move_left()
        return
    else:
        return

# run the main loop
GPIO.add_event_detect(clk, GPIO.RISING, callback=rotation_decode, bouncetime=2)
main_loop()
