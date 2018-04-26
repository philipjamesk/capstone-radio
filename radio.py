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


class Radio():
    """Creates a Radio class, this will contain the vlc player and the
        pygame display."""
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((320,240), pygame.FULLSCREEN)
        self.playlist = vlc.MediaList()
        self.player = vlc.MediaListPlayer()

        # GPIO Set Up for Rotary Encoder and Switch
        self.sw = 16 # 16 for Production Radio, 17 for Test Radio
        self.clk = 6 # 6 for Production Radio, 23 for Test Radio
        self.dt = 5 # 5 for Production Radio, 27 for Test Radio
        self.on = 23

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.on, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # find path to folder and change directory
        os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))

        # unpickle last saved playing station otherwise play index 0
        try:
            current_station = pickle.load(open("current_station.pickle", "rb" ))
        except:
            current_station = 0

        # import station list from JSON file
        self.json_data = open("stations.json").read()
        self.data = json.loads(self.json_data)

        # double check that the current_station is still in the station list
        if current_station >= len(self.data):
            current_station = 0

        # load stations into station list
        self.station_list = []
        for item in self.data:
            station = Station(item['address'], item['logo'], self.screen, item['name'])
            self.station_list.append(station)
            if self.station_list.index(station) == current_station:
                station.is_playing = True

        # add stations to MediaList
        for station in self.station_list:
            self.playlist.add_media(station.address)

        # Set player MediaList
        self.player.set_media_list(self.playlist)

        # Place logos according to initial playing station
        self.place_logos(current_station)

        # play current station
        for station in self.station_list:
            if station.is_playing:
                self.playStation(self.station_list.index(station))

        pygame.mouse.set_visible(False)
        self.draw_screen()
        GPIO.add_event_detect(self.clk,
                              GPIO.RISING,
                              callback=self.rotation_decode,
                              bouncetime=2)
        playing = True
        while playing:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
            current_station = self.check_events(current_station)
            time.sleep(.1)

    def check_events(self, current_station):
        # Will eventually be replaced with GPI Controls from Rotatry Encoder


        if GPIO.input(self.sw) == False:
            sys.exit()

        if GPIO.input(self.on) == False:
            self.player.stop()

        if self.station_list[current_station].logo.rect.centerx <= 120 or self.station_list[current_station].logo.rect.centerx >= 200:
            self.player.stop()
            current_station = -1

        if current_station == -1:
            for station in station_list:
                if station.logo.rect.centerx >= 120 and station.logo.rect.centerx <= 200:
                    current_station = self.station_list.index(station)
                    self.playStation(current_station)
        return current_station

    def rotation_decode(self, clk):
        # read both of the switches
        Switch_A = GPIO.input(self.clk)
        Switch_B = GPIO.input(self.dt)

        if (Switch_A == 1) and (Switch_B == 0) :
            move_right()
            self.draw_screen()
            return
        elif (Switch_A == 1) and (Switch_B == 1 ):
            move_left()
            self.draw_screen()
            return
        else:
            return

    def move_right(self):
        for station in self.station_list:
            station.logo.changex(25)

    def move_left(self):
        for station in self.station_list:
            station.logo.changex(-25)

    def place_logos(self, current_station):
        """Initially places the logos based on the current_station."""
        x = 160 - (current_station * 100)
        for station in self.station_list:
            station.logo.setx(x)
            x += 100

    def draw_screen(self):
        # Set the background color
        bg_color = (232, 222, 199)
        self.screen.fill(bg_color)
        screen_rect = self.screen.get_rect()
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
        for station in self.station_list:
            station.logo.blitme()

        # Add dial marks and red line to screen
        self.screen.blit(dial_marks, dial_marks_rect)
        self.screen.blit(red_line, red_line_rect)

        pygame.display.flip()

    # Play a stream
    def playStation(self, station):
        self.player.play_item_at_index(station)
        self.pickleStation(station)

    # Pickle the current station
    def pickleStation(self, current_station):
        pickle.dump(current_station, open( "current_station.pickle", "wb" ))


def main():
    radio = Radio()

if __name__ == '__main__':
    main()
