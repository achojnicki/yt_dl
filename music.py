from urllib.parse import urlparse, parse_qs, parse_qsl
import json
import subprocess
import os

with open('history.json','r', encoding='utf-8') as file:
	history=json.load(file)


urls=[]
songs={}
ready=[]

for page in history:

	p=page['url']
	x=urlparse(p)
	params=parse_qs(x.query)

	if (x.hostname=='youtube.com' or x.hostname=='www.youtube.com') and 'v' in params: 
		v=params['v'][0]
		if v not in songs:
			song={"url":v, "num": 1}
			songs[v]=song
			print(song)
		else:
			songs[v]["num"]=songs[v]["num"]+1
			print(songs[v])





for song in songs:
	if songs[song]['num']>5:
		ready.append(songs[song]['url'])


print(ready)

os.chdir('music')


for song in ready:
	subprocess.run(['py','-m','yt_dlp',f'https://youtube.com/watch?v={song}'])