# import subprocess
#
# stream = input("Please enter a stream to play: ")
# subprocess.Popen(["mplayer", "-playlist", stream, "-cache-min", "99"])


from Station import Station

station_list = [Station('KCRW Ecletic 24', 'http://media.kcrw.com/pls/kcrwmusic.pls'),
                Station('triple j', 'http://www.abc.net.au/res/streaming/audio/mp3/triplej.pls'),
                Station('WUMB', 'http://wumb.streamguys1.com/wumb919fast')]

print('Your station choices are:')
i = 0
for station in station_list:
  print(str(i) + ". " + station.name)
  i = i + 1


