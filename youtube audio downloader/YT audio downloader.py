from pytube import YouTube
import pytube
import os
import urllib.request
import json
import urllib

#Taking the title of the video
video_url = input('Enter YouTube video URL: ')
params = {"format": "json", "url": "%s" % video_url}
url = "https://www.youtube.com/oembed"
query_string = urllib.parse.urlencode(params)
url = url + "?" + query_string


with urllib.request.urlopen(url) as response:
    response_text = response.read()
    data = json.loads(response_text.decode())
    title = (data['title'])


#downloading the video
name = pytube.extract.video_id(video_url)
YouTube(video_url).streams.filter(
    only_audio=True).first().download(filename=name)

#grabbing the current working directory
path = os.getcwd() + '\\'

#get the location and name of the downloaded file
location = path + name
nwname = path + title + '.mp3'

#renaming existing file to mp3
os.rename(location, nwname)
