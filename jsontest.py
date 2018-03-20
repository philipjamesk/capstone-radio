import json
from station import Station
import pygame
screen = pygame.display.set_mode((320,240))
json_data = open('stations.json').read()

data = json.loads(json_data)

station_list = []
for item in data:
    station = Station(item['address'], item['logo'], screen)
    station_list.append(station)

for station in station_list:
    print(str(station.logo.rect.centerx) + " " + station.address)
