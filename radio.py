import subprocess
import datetime # for log file

logtime = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
logfile = "~/Documents/Capstone/log" + logtime + ".txt"

stream = input("Please enter a stream to play: ")
stream = "http://media.kcrw.com/pls/kcrwmusic.pls" # to speed things up for now

# mplayer -playlist http://www.abc.net.au/res/streaming/audio/mp3/abc_jazz.pls -cache-min 99 -cache 800 > ~/Documents/Capstone/log.txt 2>&1
p = subprocess.Popen(["mplayer", "-playlist", stream, "-cache-min", "99", "> /Documents/Capstone/log.txt"] )
#print(logfile)


input("Press any to stop stream")
p.kill()


