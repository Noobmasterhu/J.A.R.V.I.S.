#-/-/-/-/-/-/-imports-\-\-\-\-\-\-\-

from androidhelper import sl4a
from time import sleep
#import datetime
import random
from datetime import datetime
droid = sl4a.Android()

#-/-/-/-/-/-/-greet you-\-\-\-\-\-\-\-

hou = datetime.now().hour
mini = datetime.now().minute
time = f"{hou}:{mini}"
s = datetime.strptime(time, "%H:%M")
hour = s.strftime("%I:%M %p")
 
hourt = datetime.now().hour
#mini = datetime.datetime.now().minute

if 5 < hourt < 12:
   droid.ttsSpeak(f"good morning sir. time is {hour}. have a nice day. ")

if 12 < hourt < 17:
   droid.ttsSpeak(f"good noon sir. time is {hour}. how you doing")

if 17 < hourt < 23:
   droid.ttsSpeak(f"good evening sir. time is {hour}. how was your day?")

else:
   droid.ttsSpeak(f"sir it is already {hour}. you should sleep.")

sleep(7)

#-/-/-/-/-/-/-all datas-\-\-\-\-\-\-\-

data= {'hello':'hello sir, ai am JARVIS. your personal assistant','how are you jarvis':'ai am fine sir. how are you.'}
calldata = {'call name':'**********','call name*':'**********'}

#-/-/-/-/-/-/-speech input-\-\-\-\-\-\-\-

txt = droid.recognizeSpeech()
droid.setClipboard(txt.result)
clip = txt.result
print("you said", clip)
#-/-/-/-/-/-/-all paths-\-\-\-\-\-\-\-

path1 ='/storage/emulated/0/bro.jpg'
path2 ='/storage/emulated/0/musik/'
musiks = ['Deadpool.mp3', "ashes.mp3", "wewillrockyou.mp3", "sweetdreams.mp3", "havana.mp3", "kolavari.mp3"]
link = path2 + random.choice(musiks)
#droid.ttsSpeak(f"you said {clip}") #to make bot speak what u said in input
sleep(0)

#-/-/-/-message reply from data-\-\-\-\-

if clip in data:
  droid.ttsSpeak(data[clip])

#-/-/-/-/-/-/-WI-FI on off -\-\-\-\-\-\-\-

elif 'on wi-fi' in clip.lower():
  droid.toggleWifiState(True)
  droid.ttsSpeak("turned on wi-fi")

elif 'off wi-fi' in clip.lower():
  droid.toggleWifiState(False)
  droid.ttsSpeak("turned off wi-fi")

#-/-/-/-/-/-/-take picture-\-\-\-\-\-\-\-

elif 'picture' in clip.lower():
  droid.cameraCapturePicture(path1)
  droid.ttsSpeak("picture saved")

#-/-/-/-/-/-/-music on off-\-\-\-\-\-\-\-

elif 'play music' in clip.lower():
  droid.mediaPlay(link)

elif 'stop music' in clip.lower():
  droid.mediaPlayClose()

#-/-/-/-/-/-/-/-call-\-\-\-\-\-\-\-\-

elif clip.lower() in calldata:
  droid.phoneCallNumber(calldata[clip.lower()])

else:
  droid.ttsSpeak("ai am kind of confused")
