
#!/usr/bin/env python3

import sys
import os
import socket
import subprocess
from time import sleep

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
        label.after(5000, lambda label=label: self.self_destruct(label))
        self.root.mainloop()

    def self_destruct(self, label):
        if (self.is_connected()):
            pass
        else:
            messagebox.showwarning("No Network",
                                   "Please  connect\nto the internet.")
        self.root.quit()

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
