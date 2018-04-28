#!/usr/bin/env python3

import sys
import os
from subprocess import call

import json

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Editor(object):
    def __init__(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        # find path to folder and change directory
        os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
        # load the station list array from the JSON file
        self.station_list = json.loads(open("stations.json").read())
        self.station_frame = StationListFrame(self.root, self.station_list)
        self.root.mainloop()


class StationListFrame(Frame):
    def __init__(self, root, station_list):
        Frame.__init__(self, root)
        self.pack()
        self.root = root
        self.station_list = station_list

        # track whether the list has been saved in Frame was created
        self.list_is_saved = False

        # add canvas for station edit buttons for scrolling
        self.canvas=Canvas(self, highlightthickness=0)
        self.frame=Frame(self.canvas)
        self.myscrollbar=Scrollbar(self,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.myscrollbar.set)

        self.myscrollbar.pack(side="right",fill="y")
        self.canvas.pack()
        self.canvas.create_window((0,0),window=self.frame,anchor='nw')

        def myfunction(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=320,height=200)

        self.frame.bind("<Configure>",myfunction)

        for station in self.station_list:
            ttk.Button(self.frame,
                       text="Edit: " + station['name'],
                       command=lambda index=self.station_list.index(station): self.edit_station(index),
                       width=30).pack()

        self.line = Frame(self, height=1, width=320, background="black")
        self.line.pack()

        self.bottomrow = Frame(self, pady=5)
        self.bottomrow.pack()



        self.save_button = ttk.Button(self.bottomrow,
                           text="Save",
                           command=self.save_pressed)
        self.add_button = ttk.Button(self.bottomrow,
                          text="Add Station",
                          command=self.add_pressed)
        self.quit_button = ttk.Button(self.bottomrow,
                           command=self.quit_pressed,
                           text="Quit")
        self.save_button.pack(side=LEFT)
        self.add_button.pack(side=LEFT)
        self.quit_button.pack(side=LEFT)

    def edit_station(self, index):
        self.pack_forget()
        self.destroy()
        StationEditFrame(self.root, index, self.station_list)
        pass

    def add_pressed(self):
        self.station_list.append({ 'name' : '', 'address' : '', 'logo' : '' })
        self.list_is_saved = False
        self.pack_forget()
        StationEditFrame(self.root, -1, self.station_list)

    def save_pressed(self):
        with open('stations.json', 'w') as outfile:
            json.dump(self.station_list,
                      outfile,
                      sort_keys=True,
                      indent=4,
                      separators=(',', ': '))
        self.list_is_saved = True

    def quit_pressed(self):
        # Check is the list has been saved since being edited
        if self.list_is_saved:
            self.editor_quit()
        else:
            self.savewarning = messagebox.askyesnocancel("Save Station List?",
                               "Press 'Yes' to Save & 'No' to Quit without Saving.")
            if self.savewarning:
                self.save_pressed()
                self.editor_quit()
            elif self.savewarning == False:
                self.editor_quit()

    def editor_quit(self):
        self.root.quit()

class StationEditFrame(Frame):
    def __init__(self, root, index, station_list):
        Frame.__init__(self, root)
        self.configure(width=320, height=240)
        self.pack(expand=TRUE)
        self.root = root
        self.index = index
        self.station_list = station_list

        station = {'name': self.station_list[index]['name'],
                   'address': self.station_list[index]['address'],
                   'logo': self.station_list[index]['logo']}

        name_label = ttk.Label(self, text="Station name:")
        self.name_entry = ttk.Entry(self)
        self.name_entry.insert(0, station['name'])
        name_label.pack(fill=X)
        self.name_entry.pack(fill=X)

        address_label = ttk.Label(self, text="Station Address:")
        self.address_entry = ttk.Entry(self, width=32)
        self.address_entry.insert(0, station['address'])
        address_label.pack(fill=X)
        self.address_entry.pack(fill=X)

        logo_label = ttk.Label(self, text="Station Logo:")
        self.logo_entry = ttk.Entry(self)
        self.logo_entry.insert(0, station['logo'])
        logo_label.pack(fill=X)
        self.logo_entry.pack(fill=X)

        line = Frame(self, height=2, width=320,background="black")
        line.pack(fill=BOTH, pady=10)

        bottom_row = ttk.Frame(self)
        bottom_row.pack(side=BOTTOM, fill=BOTH, pady=10)

        save_button = ttk.Button(bottom_row,
                      text="Save",
                      command=lambda index=self.index: self.save_station(index))
        delete_button = ttk.Button(bottom_row,
                        text="Delete Station",
                        command=lambda index=self.index: self.delete_station(index))
        cancel_button = ttk.Button(bottom_row,
                        text="Cancel",
                        command=self.station_exit)

        save_button.pack(side=LEFT)
        delete_button.pack(side=LEFT)
        cancel_button.pack(side=LEFT)


    def save_station(self, index):
        self.station_list[index]['name'] = self.name_entry.get()
        self.station_list[index]['address'] = self.address_entry.get()
        self.station_list[index]['logo'] = self.logo_entry.get()
        self.station_exit()

    def delete_station(self, index):
        self.station_list.pop(index)
        self.station_exit()

    def station_exit(self):
        self.destroy()
        StationListFrame(self.root, self.station_list)

def main():
    editor = Editor()

if __name__ == '__main__':
    main()
