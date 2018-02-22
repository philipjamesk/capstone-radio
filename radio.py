## Pygame is temporarily turned off for this version

import pygame
import os
import subprocess
import controls as controls
from station import Station
from logo import Logo

# Building Display right in radio for now.
# from display import Display

# Initialize Pygame
pygame.init()

# Make a list of stations
station_list = [Station('KCRW Ecletic 24', 'http://media.kcrw.com/pls/kcrwmusic.pls', 'img/logos/eclectic24_logo.png'),
                Station('triple j', 'http://www.abc.net.au/res/streaming/audio/mp3/triplej.pls', 'img/logos/triplej_logo.png'),
                Station('WUMB', 'http://www.wumb.org/listenlive/links/wumbfast.pls', 'img/logos/wumb_logo.png'),
                Station('TSF Jazz', 'http://statslive.infomaniak.ch/playlist/tsfjazz/tsfjazz-high.mp3/playlist.pls', 'img/logos/tsfjazz_logo.png'),
                Station('Double J', 'http://www.abc.net.au/res/streaming/audio/mp3/dig_music.pls', 'img/logos/doublej_logo.png')]


# Print list of stations
def listStations():
    print('Your station choices are:')
    i = 0
    for station in station_list:
        print(str(i) + ". " + station.name)
        i = i + 1

# Play a stream
def playStation(stream):
    playing_station = subprocess.Popen(["mplayer", "-playlist", stream, "-cache-min", "99"])
    return playing_station


# Close stream
def stopPlaying(playing_station):
    playing_station.kill()

def play():
    # Initialize game and create a screen object.
    pygame.init()
    os.putenv('SDL_FBDEV', '/dev/fb1')
    screen = pygame.display.set_mode((320,240), pygame.NOFRAME, pygame.FULLSCREEN)
    # Make a background
    bg_color = (232, 222, 199)

    station = 2

    # Start the main loop for the radio app
    while True:

        # Watch for keyboard and mouse events
        command = controls.check_events(station)
        if command == 'right':
            station = station + 1
        elif command == 'left':
            station = station - 1

        if station < 0:
            station = 0
        if station >= len(station_list):
            station = len(station_list) - 1

        # for station in station_list:

        # Add logos
        logo = Logo(screen, station_list[station].logo)

        # Add background color to screen
        screen.fill(bg_color)
        logo.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

play()
