# #!/usr/bin/env python3
#
import sys
import os
import platform                    ### <---- For testing only
from subprocess import call

import json

from tkinter import *
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
        canvas=Canvas(self, highlightthickness=0)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(self,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"),width=320,height=200)

        frame.bind("<Configure>",myfunction)

        for station in station_list:
            ttk.Button(frame,
                       text="Edit: " + station['name'],
                       command=lambda index=station_list.index(station): self.edit_station(index),
                       width=30).pack()



#         # add scrolled panel for list of stations
#         spanel = sp.ScrolledPanel(panel)
#         spanel.SetSize(320, 180)
#         row_sizer = wx.BoxSizer(wx.VERTICAL)
#
#         # add edit station buttons
#         index = 0
#         station_buttons = []
#         for station in station_list:
#             btn = wx.Button(spanel, label="Edit: " + station['name'])
#             station_buttons.append(btn)
#             row_sizer.Add(btn, 0, wx.EXPAND)
#             station_buttons[index].Bind(wx.EVT_BUTTON,
#                                         lambda event,
#                                         index=index:
#                                         self.edit_station(index))
#             index += 1
#
#         # add system button to panel
#         quitButton = wx.Button(panel, label="Quit", pos=(15, 185))
#         addButton = wx.Button(panel, label="Add Station", pos=(115, 185))
#         saveButton = wx.Button(panel, label="Save", pos=(215, 185))
#
#         quitButton.Bind(wx.EVT_BUTTON, lambda event: self.quit_pressed())
#         addButton.Bind(wx.EVT_BUTTON, lambda event: self.add_pressed())
#         saveButton.Bind(wx.EVT_BUTTON, lambda event: self.save_pressed())
#
#         spanel.SetSizer(row_sizer)
#         spanel.SetupScrolling()
#
#         panel.SetSizer(sizer)
#         self.Show()
#
#
    def edit_station(self, index):
        print(station_list[index]['name'])
        pass
#
#     def add_pressed(self):
#         station_list.append({ 'name' : '', 'address' : '', 'logo' : '' })
#         self.Close()
#         frame = StationEditFrame(None, -1)
#
#     def save_pressed(self):
#         with open('stations.json', 'w') as outfile:
#             json.dump(station_list,
#                       outfile,
#                       sort_keys=True,
#                       indent=4,
#                       separators=(',', ': '))
#         self.list_is_not_saved = False
#
#     def quit_pressed(self):
#         if self.list_is_not_saved:
#             dlg = wx.Dialog(self, title="Warning!", size=(300, 180), pos=(10, 20))
#             dlg_panel = wx.Panel(dlg)
#             dlg_sizer = wx.BoxSizer(wx.VERTICAL)
#
#             label = wx.StaticText(dlg_panel,
#                     label="Do you want to save before quitting?")
#
#             dlg_sizer.Add(-1, 10)
#             dlg_sizer.Add(label, -1, wx.ALIGN_CENTER)
#
#             dlg_sizer.Add(-1, 10)
#             button_sizer = wx.BoxSizer(wx.HORIZONTAL)
#
#             noButton = wx.Button(dlg_panel, label="No", size=(70, 30))
#             # cancelButton = wx.Button(dlg_panel, label="Cancel", size=(70,30))
#             yesButton = wx.Button(dlg_panel, label="YES", size=(70, 30))
#
#             noButton.Bind(wx.EVT_BUTTON,
#                           lambda event,
#                           dlg=dlg:
#                           self.no_pressed(dlg))
#
#             # cancelButton.Bind(wx.EVT_BUTTON,
#             #                   lambda event,
#             #                   dlg=dlg:
#             #                   self.cancel_pressed(dlg))
#
#             yesButton.Bind(wx.EVT_BUTTON,
#                            lambda event,
#                            dlg=dlg:
#                            self.yes_pressed(dlg))
#
#             button_sizer.Add(noButton, 0)
#             # button_sizer.Add(cancelButton, 0)
#             button_sizer.Add(yesButton, 0)
#
#             dlg_sizer.Add(button_sizer, -1, wx.ALIGN_CENTER)
#             dlg_panel.SetSizer(dlg_sizer)
#             dlg.ShowModal()
#             dlg.Destroy()
#         else:
#             exit_station_list()
#
#     def no_pressed(self, dlg):
#         dlg.Destroy()
#         exit_station_list()
#
#     # def cancel_pressed(self, dlg):
#     #     dlg.Destroy()
#
#     def yes_pressed(self, dlg):
#         dlg.Destroy()
#         self.save_pressed()
#         self.quit_pressed()
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
