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

        vbox = wx.BoxSizer(wx.VERTICAL)

        name_box = wx.BoxSizer(wx.HORIZONTAL)
        name_label = wx.StaticText(panel, label='Name:')
        name_box.Add(name_label, flag=wx.RIGHT, border=8)
        self.name_text = wx.TextCtrl(panel, value=station_list[index]['name'])
        # self.name_text.Bind(wx.E)
        name_box.Add(self.name_text, proportion=1)
        vbox.Add(name_box, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        address_box = wx.BoxSizer(wx.HORIZONTAL)
        address_label = wx.StaticText(panel, label='Address:')
        address_box.Add(address_label, flag=wx.RIGHT, border=8)
        self.address_text = wx.TextCtrl(panel, value=station_list[index]['address'])
        address_box.Add(self.address_text, proportion=1)
        vbox.Add(address_box, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        logo_box = wx.BoxSizer(wx.HORIZONTAL)
        logo_label = wx.StaticText(panel, label='Logo:')
        logo_box.Add(logo_label, flag=wx.RIGHT, border=8)
        self.logo_text = wx.TextCtrl(panel, value=station_list[index]['logo'])
        logo_box.Add(self.logo_text, proportion=1)
        vbox.Add(logo_box, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        cancelButton = wx.Button(panel, label="Cancel && Exit", pos=(15, 185), size=(120, 20))
        saveStationButton = wx.Button(panel, label="Save && Exit", pos=(185, 185), size=(120, 20))

        cancelButton.Bind(wx.EVT_BUTTON, lambda event: cancel_pressed(self))
        saveStationButton.Bind(wx.EVT_BUTTON, lambda event, index=index: self.save_station_pressed(index))

        panel.SetSizer(vbox)
        # self.Bind(wx.EVT_TEXT, self.on_type_event)
        self.Show()

    def save_station_pressed(self, index):
        station_list[index]['name'] = self.name_text.GetValue()
        station_list[index]['address'] = self.address_text.GetValue()
        station_list[index]['logo'] = self.logo_text.GetValue()
        self.Close()
        frame = StationListFrame(None)

def main():
    app = wx.App(False)
    frame = StationListFrame(None)
    app.MainLoop()

def edit_station(frame, index):
    frame.Close()
    frame = StationEditFrame(None, index)

def quit_pressed(event):
    exit()

def add_pressed(event):
    print("Add Pressed")

def save_pressed(event):
    with open('stations.json', 'w') as outfile:
        json.dump(station_list, outfile, sort_keys=True, indent=4, separators=(',', ': '))

def cancel_pressed(frame):
    frame.Close()
    frame = StationListFrame(None)

# def save_station_pressed(frame, index, station):
#     print(station)
#     pass

if __name__ == '__main__':
    main()
