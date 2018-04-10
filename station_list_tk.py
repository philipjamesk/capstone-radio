# #!/usr/bin/env python3
#
import sys
import os
import platform                    ### <---- For testing only
from subprocess import call

import json

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# find path to folder and change directory
os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
# load the station list array from the JSON file
station_list = json.loads(open("stations.json").read())

class StationListFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.pack()

        # track whether the list has been saved in Frame was created
        self.list_is_not_saved = True

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

        for station in station_list:
            ttk.Button(self.frame,
                       text="Edit: " + station['name'],
                       command=lambda index=station_list.index(station): self.edit_station(index),
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
        print(station_list[index]['name'])
        pass

    def add_pressed(self):
        station_list.append({ 'name' : '', 'address' : '', 'logo' : '' })
        # self.pack_forget()
        # frame = StationEditFrame(None, -1)
        print("Add pressed")

    def save_pressed(self):
        with open('stations.json', 'w') as outfile:
            json.dump(station_list,
                      outfile,
                      sort_keys=True,
                      indent=4,
                      separators=(',', ': '))
        self.list_is_not_saved = False
        print("Save pressed")

    def quit_pressed(self):
        # print("Quit pressed")
        # self.pack_forget()

        if self.list_is_not_saved:
            self.savewarning = messagebox.askyesnocancel("Save Station List?",
                               "Press 'Yes' to Save & 'No' to Quit without Saving.")

            if self.savewarning:
                self.save_pressed()
                sys.exit()
            elif self.savewarning == False:
                sys.exit()
#
#
# class StationEditFrame(wx.Frame):
#     def __init__(self, parent, index):
#         wx.Frame.__init__(self, parent)
#         self.SetSize(320, 240)
#         self.index = index
#         panel = wx.Panel(self)
#
#         vbox = wx.BoxSizer(wx.VERTICAL)
#
#         name_box = wx.BoxSizer(wx.HORIZONTAL)
#         name_label = wx.StaticText(panel, label='Name:')
#         name_box.Add(name_label, flag=wx.RIGHT, border=8)
#         self.name_text = wx.TextCtrl(panel, value=station_list[index]['name'])
#         # self.name_text.Bind(wx.E)
#         name_box.Add(self.name_text, proportion=1)
#         vbox.Add(name_box, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
#
#         address_box = wx.BoxSizer(wx.HORIZONTAL)
#         address_label = wx.StaticText(panel, label='Address:')
#         address_box.Add(address_label, flag=wx.RIGHT, border=8)
#         self.address_text = wx.TextCtrl(panel, value=station_list[index]['address'])
#         address_box.Add(self.address_text, proportion=1)
#         vbox.Add(address_box, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
#
#         logo_box = wx.BoxSizer(wx.HORIZONTAL)
#         logo_label = wx.StaticText(panel, label='Logo:')
#         logo_box.Add(logo_label, flag=wx.RIGHT, border=8)
#         self.logo_text = wx.TextCtrl(panel, value=station_list[index]['logo'])
#         logo_box.Add(self.logo_text, proportion=1)
#         vbox.Add(logo_box, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
#
#         cancelButton = wx.Button(panel, label="Cancel", pos=(15, 185))
#         deleteButton = wx.Button(panel, label="Delete", pos=(115, 185))
#         saveStationButton = wx.Button(panel, label="Save", pos=(215, 185))
#
#         cancelButton.Bind(wx.EVT_BUTTON,
#                           lambda event: self.station_exit())
#
#         deleteButton.Bind(wx.EVT_BUTTON,
#                           lambda event,
#                           index=index: self.delete_station(index))
#
#         saveStationButton.Bind(wx.EVT_BUTTON,
#                                lambda event,
#                                index=index: self.save_station_pressed(index))
#
#         panel.SetSizer(vbox)
#         self.Show()
#
#     def save_station_pressed(self, index):
#         station_list[index]['name'] = self.name_text.GetValue()
#         station_list[index]['address'] = self.address_text.GetValue()
#         station_list[index]['logo'] = self.logo_text.GetValue()
#         self.station_exit()
#
#     def delete_station(self, index):
#         station_list.pop(index)
#         self.station_exit()
#
#     def station_exit(self):
#         self.Close()
#         frame = StationListFrame(None)
#
# def exit_station_list():
#     call(["python3", "radio.py"])
#     sys.exit()
#
def main():
    root = Tk()

    if platform.system() == 'Darwin':
        root.geometry("320x240")
    else:
        root.attributes("-fullscreen", True)
    station_frame = StationListFrame(None)
    root.mainloop()

if __name__ == '__main__':
    main()
