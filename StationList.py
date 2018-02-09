## Pygame is temporarily turned off for this version

# import pygame
import subprocess
from Station import Station

# Make a list of stations
station_list = [Station('KCRW Ecletic 24', 'http://media.kcrw.com/pls/kcrwmusic.pls'),
                Station('triple j', 'http://www.abc.net.au/res/streaming/audio/mp3/triplej.pls'),
                Station('WUMB', 'http://wumb.streamguys1.com/wumb919fast')]

# Print list of stations
def listSations():
    print('Your station choices are:')
    i = 0
    for station in station_list:
        print(str(i) + ". " + station.name)
        i = i + 1
        print("Press 'Q' to quit.")
