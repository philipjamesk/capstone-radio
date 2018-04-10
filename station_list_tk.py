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
        self.root = root

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
        self.pack_forget()
        self.destroy()
        StationEditFrame(self.root, index)
        print(station_list[index]['name'])
        pass

    def add_pressed(self):
        station_list.append({ 'name' : '', 'address' : '', 'logo' : '' })
        self.list_is_saved = False
        self.pack_forget()
        StationEditFrame(self.root, -1)
        print("Add pressed")

    def save_pressed(self):
        with open('stations.json', 'w') as outfile:
            json.dump(station_list,
                      outfile,
                      sort_keys=True,
                      indent=4,
                      separators=(',', ': '))
        self.list_is_saved = True
        print("Save pressed")

    def quit_pressed(self):
        # Check is the list has been saved since being edited
        if self.list_is_saved:
            sys.exit()
        else:
            self.savewarning = messagebox.askyesnocancel("Save Station List?",
                               "Press 'Yes' to Save & 'No' to Quit without Saving.")
            if self.savewarning:
                self.save_pressed()
                sys.exit()
            elif self.savewarning == False:
                sys.exit()

class StationEditFrame(Frame):
    def __init__(self, root, index):
        Frame.__init__(self, root)
        self.configure(width=320, height=240)
        self.pack(expand=TRUE)
        self.index = index

        station = {'name': station_list[index]['name'],
                   'address': station_list[index]['address'],
                   'logo': station_list[index]['logo']}
        name = ''
        address = ''
        logo = ''

        name_label = ttk.Label(self, text="Station name:")
        name_entry = ttk.Entry(self, textvariable=name)
        name_entry.insert(0, station['name'])
        name_label.pack(fill=X)
        name_entry.pack(fill=X)

        address_label = ttk.Label(self, text="Station Address:")
        address_entry = ttk.Entry(self, width=32, textvariable=address)
        address_entry.insert(0, station['address'])
        address_label.pack(fill=X)
        address_entry.pack(fill=X)

        logo_label = ttk.Label(self, text="Station Logo:")
        logo_entry = ttk.Entry(self, textvariable=logo)
        logo_entry.insert(0, station['logo'])
        logo_label.pack(fill=X)
        logo_entry.pack(fill=X)

        ##### Possibly Add Preview of the Logo
        #
        # # image = Image.open("img/logos/eclectic24_logo.png")
        # # image = image.resize((80, 80), PIL.Image.ANTIALIAS)
        # # photo = ImageTk.PhotoImage(image)
        # # photo_label = Label(station_frame, image=photo)
        # # photo_label.pack(side=LEFT)
        #
        ##### Add file picker for choosing logo
        #
        # edit_logo_button = ttk.Button(station_frame, text="Select Logo")
        # edit_logo_button.pack()
        #
        #####

        line = Frame(self, height=2, width=320,background="black")
        line.pack(fill=BOTH, pady=10)

        bottom_row = ttk.Frame(self)
        bottom_row.pack(side=BOTTOM, fill=BOTH, pady=10)

        save_button = ttk.Button(bottom_row, text="Save")
        delete_button = ttk.Button(bottom_row, text="Delete Station")
        quit_button = ttk.Button(bottom_row, text="Quit")

        save_button.pack(side=LEFT)
        delete_button.pack(side=LEFT)
        quit_button.pack(side=LEFT)







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
