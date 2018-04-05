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

        #
        self.list_is_not_saved = True

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
            station_buttons[index].Bind(wx.EVT_BUTTON,
                                        lambda event,
                                        index=index:
                                        self.edit_station(index))
            index += 1

        # add system button to panel
        quitButton = wx.Button(panel, label="Quit", pos=(15, 185))
        addButton = wx.Button(panel, label="Add Station", pos=(115, 185))
        saveButton = wx.Button(panel, label="Save", pos=(215, 185))

        quitButton.Bind(wx.EVT_BUTTON, lambda event: self.quit_pressed())
        addButton.Bind(wx.EVT_BUTTON, lambda event: self.add_pressed())
        saveButton.Bind(wx.EVT_BUTTON, lambda event: self.save_pressed())

        spanel.SetSizer(row_sizer)
        spanel.SetupScrolling()

        panel.SetSizer(sizer)
        self.Show()



    def edit_station(self, index):
        self.Close()
        frame = StationEditFrame(None, index)

    def add_pressed(self):
        station_list.append({ 'name' : '', 'address' : '', 'logo' : '' })
        self.Close()
        frame = StationEditFrame(None, -1)

    def save_pressed(self):
        with open('stations.json', 'w') as outfile:
            json.dump(station_list,
                      outfile,
                      sort_keys=True,
                      indent=4,
                      separators=(',', ': '))
        self.list_is_not_saved = False

    def quit_pressed(self):
        if self.list_is_not_saved:
            print("You didn't save!")
        exit()


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

        cancelButton = wx.Button(panel, label="Cancel", pos=(15, 185))
        deleteButton = wx.Button(panel, label="Delete", pos=(115, 185))
        saveStationButton = wx.Button(panel, label="Save", pos=(215, 185))

        cancelButton.Bind(wx.EVT_BUTTON,
                          lambda event: self.station_exit())

        deleteButton.Bind(wx.EVT_BUTTON,
                          lambda event,
                          index=index: self.delete_station(index))

        saveStationButton.Bind(wx.EVT_BUTTON,
                               lambda event,
                               index=index: self.save_station_pressed(index))

        panel.SetSizer(vbox)
        self.Show()

    def save_station_pressed(self, index):
        station_list[index]['name'] = self.name_text.GetValue()
        station_list[index]['address'] = self.address_text.GetValue()
        station_list[index]['logo'] = self.logo_text.GetValue()
        self.station_exit()

    def delete_station(self, index):
        station_list.pop(index)
        self.station_exit()

    def station_exit(self):
        self.Close()
        frame = StationListFrame(None)

def main():
    app = wx.App(False)
    frame = StationListFrame(None)
    app.MainLoop()

if __name__ == '__main__':
    main()
