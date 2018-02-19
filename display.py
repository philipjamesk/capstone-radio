#!/usr/bin/env python3

import sys
import pygame

from station import Station

# Make a list of stations
station_list = [Station('KCRW Ecletic 24', 'http://media.kcrw.com/pls/kcrwmusic.pls', 'img/logo/eclectic24_logo.png'),
                Station('triple j', 'http://www.abc.net.au/res/streaming/audio/mp3/triplej.pls', 'img/logo/triplej_logo.png'),
                Station('WUMB', 'http://www.wumb.org/listenlive/links/wumbfast.pls', 'img/logo/wumb_logo.png'),
                Station('TSF Jazz', 'http://statslive.infomaniak.ch/playlist/tsfjazz/tsfjazz-high.mp3/playlist.pls', 'img/logo/tsfjazz_logo.png'),
                Station('Double J', 'http://www.abc.net.au/res/streaming/audio/mp3/dig_music.pls', 'img/logo/doublej_logo.png')]



def play():
    #vInitialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((320,240))
    # Make a background
    bg_color = (255, 128, 255)

    # Start the main loop for the radio app
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Add background color to screen
        screen.fill(bg_color)


        # Make the most recently drawn screen visible.
        pygame.display.flip()

play()
