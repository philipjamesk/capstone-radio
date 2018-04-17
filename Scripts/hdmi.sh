#!/bin/bash
# Changing 99-pitft.conf to out to the PiTFT screen

sudo cp ~/Scripts/hdmi.conf /usr/share/X11/xorg.conf.d/99-pitft.conf
sudo shutdown -r now
