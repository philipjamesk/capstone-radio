import os
import json
import wx


station_list = json.loads(open("stations.json").read())

class StationListFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.SetSize(320, 240)
        panel = wx.Panel(self)
        gs = wx.GridSizer(len(station_list), 2, -1, -1)
        print(len(station_list))
        for station in station_list:
            print(station['name'])
            panel.SetSizer(gs)
        self.Show()

def main():
    app = wx.App(False)
    frame = StationListFrame(None)
    app.MainLoop()

if __name__ == '__main__':
    main()
