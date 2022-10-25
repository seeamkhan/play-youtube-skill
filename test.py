import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import pafy
#import vlc
from vlc import Instance
import time


#music_name = "Linkin Park Numb"
music_name = "James likhte parina kono gan"
query_string = urllib.parse.urlencode({"search_query": music_name})
formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
print('1:')
print(formatUrl)

search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
print('2:')
print(search_results)
#clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
#print('3:')
#print(clip)
clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
print('4:')
print(clip2)

#inspect = BeautifulSoup(clip.content, "html.parser")
#print('5:')
#print(inspect)
#yt_title = inspect.find_all("meta", property="og:title")
#print('6:')
#print(yt_title)

#for concatMusic1 in yt_title:
    #pass
#    print('7: ' + concatMusic1['content'])

#subprocess.Popen(
#"start /b " + "path\\to\\mpv.exe " + clip2 + " --no-video --loop=inf --input-ipc-server=\\\\.\\pipe\\mpv-pipe > output.txt",
#shell=True)

#url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
#url = "https://www.youtube.com/watch?v=Ii2AK1QvuHY"
url = clip2
video = pafy.new(url)
best = video.getbest()
playurl = best.url

#Instance = vlc.Instance()
player = Instance().media_player_new()
Media = Instance().media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()
time.sleep(30)
#player.pause()
#time.sleep(10)
#player.resume()
#time.sleep(10)
player.stop()
