#!/usr/bin/env python3

import sys
import os
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
        img = PhotoImage(file = "pi_radio_splash.gif")
        label = Label(image = img)
        label.pack()
        label.after(3000, self.self_destruct)
        self.root.mainloop()

    def self_destruct(self):
        messagebox.showwarning("No Network", "You do not appear to be connected to the internet.")
        print("Kablamo")
        sys.exit()

def main():
    splash_screen = SplashScreen()

if __name__ == '__main__':
    main()

