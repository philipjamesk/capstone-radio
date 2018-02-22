import os
import sys
import pygame

from station import Station

station_list = [Station('KCRW Ecletic 24',
                    'http://media.kcrw.com/pls/kcrwmusic.pls',
                    'img/logos/eclectic24_logo.png'),
                Station('triple j',
                    'http://www.abc.net.au/res/streaming/audio/mp3/triplej.pls',
                    'img/logos/triplej_logo.png'),
                Station('WUMB',
                    'http://www.wumb.org/listenlive/links/wumbfast.pls',
                    'img/logos/wumb_logo.png'),
                Station('TSF Jazz',
                    'http://statslive.infomaniak.ch/playlist/tsfjazz/tsfjazz-high.mp3/playlist.pls',
                    'img/logos/tsfjazz_logo.png'),
                Station('Double J',
                    'http://www.abc.net.au/res/streaming/audio/mp3/dig_music.pls',
                    'img/logos/doublej_logo.png')]
