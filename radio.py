## Pygame is temporarily turned off for this version

import pygame
import subprocess
from station import Station

# Building Display right in radio for now.
# from display import Display

# Initialize Pygame
pygame.init()

# Make a list of stations
station_list = [Station('KCRW Ecletic 24', 'http://media.kcrw.com/pls/kcrwmusic.pls', 'img/logo/eclectic24_logo.png'),
                Station('triple j', 'http://www.abc.net.au/res/streaming/audio/mp3/triplej.pls', 'img/logo/triplej_logo.png'),
                Station('WUMB', 'http://www.wumb.org/listenlive/links/wumbfast.pls', 'img/logo/wumb_logo.png'),
                Station('TSF Jazz', 'http://statslive.infomaniak.ch/playlist/tsfjazz/tsfjazz-high.mp3/playlist.pls', 'img/logo/tsfjazz_logo.png'),
                Station('Double J', 'http://www.abc.net.au/res/streaming/audio/mp3/dig_music.pls', 'img/logo/doublej_logo.png')]


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

listStations()
choice = input('Please select a station or press "q" to quit: ')
if choice.lower() == 'q':
    sys.exit()
elif station_list[int(choice)]:
    playing_station = playStation(station_list[int(choice)].address)
    print('You are listening to ' + station_list[int(choice)].address)
