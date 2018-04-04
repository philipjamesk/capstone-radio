import os
import json
import wx
import wx.lib.scrolledpanel as sp

station_list = json.loads(open("stations.json").read())

class StationListFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.SetSize(320, 240)
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # add scrolled panel for list of stations
        spanel = sp.ScrolledPanel(panel)
        spanel.SetSize(320, 180)
        row_sizer = wx.BoxSizer(wx.VERTICAL)

        # add edit station buttons
        index = 0
        station_buttons = []
        for station in station_list:
            btn = wx.Button(spanel, label="Edit: " + station['name'])
            station_buttons.append(btn)
            row_sizer.Add(btn, 0, wx.EXPAND)
            station_buttons[index].Bind(wx.EVT_BUTTON, lambda event, index=index: edit_station(self, index))
            index += 1

        b_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # add system button to panel
        quitButton = wx.Button(panel, label="Quit", pos=(15, 185))
        addButton = wx.Button(panel, label="Add Station", pos=(115, 185))
        saveButton = wx.Button(panel, label="Save", pos=(215, 185))

        quitButton.Bind(wx.EVT_BUTTON, quit_pressed)
        addButton.Bind(wx.EVT_BUTTON, add_pressed)
        saveButton.Bind(wx.EVT_BUTTON, save_pressed)

        # b_sizer.Add(quitButton, 0, wx.EXPAND)
        # b_sizer.Add(addButton, 0, wx.EXPAND)
        # b_sizer.Add(saveButton, 0, wx.EXPAND)


        spanel.SetSizer(row_sizer)
        spanel.SetupScrolling()

        # sizer.Add(row_sizer)
        sizer.Add(b_sizer)

        panel.SetSizer(sizer)
        self.Show()


def main():
    app = wx.App(False)
    frame = StationListFrame(None)
    app.MainLoop()

def edit_station(frame, index):
    station_list.remove(station_list[index])
    frame.Close()
    main()

def quit_pressed(event):
    print("Quit Pressed")
    exit()

def add_pressed(event):
    print("Add Pressed")

def save_pressed(event):
    print("Save Pressed")
    print(json.dumps(station_list, sort_keys=True, indent=4, separators=(',', ': ')))
    with open('stations.json', 'w') as outfile:
        json.dump(station_list, outfile, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    main()
