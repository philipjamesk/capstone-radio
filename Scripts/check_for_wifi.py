#!/usr/bin/env python3

from wifi import Cell, Scheme

network_map = Cell.all('wlan0')
network_set = set()
for network in network_map:
    network_set.add(network)

network_array = []
for network.ssid in network_set:
    network_array.append(network.ssid)
    print(str(network_array.index(network.ssid)) + ": " + network.ssid)

network_to_join = int(input("Select a Newtork -> "))

# if
