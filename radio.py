## Pygame is temporarily turned off for this version

# import pygame
import subprocess
from Station import Station

# Initialize Pygame
# pygame.init()

# Make a list of stations
station_list = [Station('KCRW Ecletic 24', 'http://media.kcrw.com/pls/kcrwmusic.pls'),
                Station('triple j', 'http://www.abc.net.au/res/streaming/audio/mp3/triplej.pls'),
                Station('WUMB', 'http://wumb.streamguys1.com/wumb919fast')]


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

# Close stream
def stopPlaying():
    if 'playing_station' in globals():
        playing_station.kill()


radio_on = True
while radio_on:
    listStations()
    choice = input('Please select a station or press "q" to quit: ')
    if choice.lower() == 'q':
        stopPlaying()
        radio_on = False
    elif station_list[int(choice)]:
        print(station_list[int(choice)].address)
