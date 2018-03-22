#!/usr/bin/env python3

import sys
import os
import pygame
import vlc
import json

from station import Station
from logo import Logo

# Make a list of stations
station_list = []
# current_station = 3                             # will eventually be pickled
screen = pygame.display.set_mode((320,240), pygame.FULLSCREEN)
playlist = vlc.MediaList()
radio = vlc.MediaListPlayer()

def main_loop():
    # Put all the initial settings here
    pygame.init()
    screen_rect = screen.get_rect()
    current_station = 3
    # find path to folder
    path = (os.path.dirname(os.path.realpath(sys.argv[0])))
    print(path)
    # import station list from JSON file
    path_to_json = path + "/stations.json"
    json_data = open(path_to_json).read()

    data = json.loads(json_data)
    for item in data:
        path_to_logo = path + '/' + item['logo']
        station = Station(item['address'], path_to_logo, screen)
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

    draw_screen(screen, screen_rect, path)

    while True:
        # This is where pygame will listen for keypresses, update the logos
        # and flip the screen
        # draw_logos(logos, screen)
        current_station = check_events(current_station, screen_rect, path)

#####  Working here
        # radio_controls()

def check_events(current_station, screen_rect, path):
    # Determine is a key event is a left or right arrow and pass it to the
    # correct movement function
    #
    # Will eventually be replaced with GPI Controls from Rotatry Encoder
    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_RIGHT and station_list[0].logo.rect.centerx <= 160:
                move_right()
            if event.key == pygame.K_LEFT and station_list[-1].logo.rect.centerx >= 160:
                move_left()
            draw_screen(screen, screen_rect, path)
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

def draw_screen(screen, screen_rect, path):
    # Set the background color
    bg_color = (232, 222, 199)
    screen.fill(bg_color)

    # Add the rest to the display
    dial_marks = pygame.image.load(path + '/img/display/radio-marks.png')
    red_line = pygame.image.load(path + '/img/display/red-line.png')
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

# run the main loop
main_loop()
