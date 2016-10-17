import os
import warnings
import webbrowser

os.environ['HOME']

path_current= os.getcwd()

lulumix = [l.strip('\r\n').split(',') for l in open(path_current + '/github/python_ebc_2016/day_04/exercise/lulu_mix_16.csv')]
#now remove header: 
lulumix.pop(0)

class Song(object):
     def __init__(self,song, artist, duration):
         self.song=song
         self.artist=artist 
        
         try: 
         	duration=int(duration)
         except ValueError:
         	duration = 0
         	warnings.warn('The song %s by %s had no duration. It is now set to zero' %(self.song, self.artist)) 
         if duration < 0 :
         	raise Exception('the duration was less than zero')
         self.duration=duration
     def pretty_duration(self):
     	time_in_hours=self.duration/3600
     	timeleft=self.duration%3600
     	time_in_min= timeleft/60
     	seconds= timeleft%60
     	print "%i hours %i minutes %i seconds" % (time_in_hours, time_in_min, seconds)
     def play(self):
     	url = 'https://www.youtube.com/results?search_query='
     	webbrowser.open(url + self.artist + "+" + self.song)

songs=[]

for line in lulumix:
	current_song=Song(line[0],line[1],line[2])
	songs.append(current_song)

print songs[3].pretty_duration()





