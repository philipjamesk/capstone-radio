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

        # add system button to panel
        quitButton = wx.Button(panel, label="Quit", pos=(15, 185))
        addButton = wx.Button(panel, label="Add Station", pos=(115, 185))
        saveButton = wx.Button(panel, label="Save", pos=(215, 185))

        quitButton.Bind(wx.EVT_BUTTON, quit_pressed)
        addButton.Bind(wx.EVT_BUTTON, add_pressed)
        saveButton.Bind(wx.EVT_BUTTON, save_pressed)

        spanel.SetSizer(row_sizer)
        spanel.SetupScrolling()

        panel.SetSizer(sizer)
        self.Show()

class StationEditFrame(wx.Frame):
    def __init__(self, parent, index):
        wx.Frame.__init__(self, parent)
        self.SetSize(320, 240)
        self.index = index
        panel = wx.Panel(self)

        wx.StaticText(panel, label=station_list[self.index]['name'])

        cancelButton = wx.Button(panel, label="Cancel && Exit", pos=(15, 185), size=(120, 20))
        saveStationButton = wx.Button(panel, label="Save && Exit", pos=(185, 185), size=(120, 20))

        cancelButton.Bind(wx.EVT_BUTTON, lambda event: cancel_pressed(self))
        saveStationButton.Bind(wx.EVT_BUTTON, save_station_pressed)

        self.Show()

def main():
    app = wx.App(False)
    frame = StationListFrame(None)
    app.MainLoop()

def edit_station(frame, index):
    frame.Close()
    print(index)
    frame = StationEditFrame(None, index)

def quit_pressed(event):
    print("Quit Pressed")
    exit()

def add_pressed(event):
    print("Add Pressed")

def save_pressed(event):
    with open('stations.json', 'w') as outfile:
        json.dump(station_list, outfile, sort_keys=True, indent=4, separators=(',', ': '))

def cancel_pressed(frame):
    frame.Close()
    frame = StationListFrame(None)

def save_station_pressed(event):
    pass


if __name__ == '__main__':
    main()
