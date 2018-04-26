#!/usr/bin/env python3

import subprocess
from wifi import Cell, Scheme

cells = Cell.all('wlan0')

unique_cells = []
for cell in cells:
    not_a_member = True
    for uc in unique_cells:
        if uc.ssid == cell.ssid:
            not_a_member = False
    if not_a_member:
        unique_cells.append(cell)


for cell in unique_cells:
    print("{}: {}".format(str(unique_cells.index(cell)), cell.ssid))

network_choice = int(input("Please Select a Network -> "))
cell = unique_cells[network_choice]

if cell.encrypted:
    print(cell.encryption_type)
    passkey = input("Please enter a passkey for {} > ".format(cell.ssid))
else:
    passkey = None

wpa_supplicant = open('/etc/wpa_supplicant/wpa_supplicant.conf', 'a+')
wpa_supplicant.write("\nnetwork={{\n\tssid=\"{}\"\n\tpsk=\"{}\"\n}}".format(cell.ssid, passkey))

# subprocess.call('wpa_cli -i wlan0 reconfigure')
