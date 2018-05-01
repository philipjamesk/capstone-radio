#!/usr/bin/env python3

import sys
import os
import socket
from subprocess import call
from time import sleep
import json

from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class SplashScreen(object):
    def __init__(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        # find path to folder and change directory
        os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
        img = PhotoImage(file = "img/pi_radio_splash.gif")
        label = Label(image = img)
        label.pack()
        label.after(3000, self.self_destruct)
        self.root.mainloop()

    def self_destruct(self):
        if (self.is_connected()):
            subprocess.Popen(["python3",
                        "/home/pi/Documents/capstone-radio/radio.py"])
        else:
            messagebox.showwarning("No Network", "Please connect to the internet.")
            sys.exit()

    def is_connected(self):
        try:
            # connect to the host -- tells us if the host is actually
            # reachable
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False

def main():
    splash_screen = SplashScreen()

if __name__ == '__main__':
    main()

    import socket
