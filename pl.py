from pytube import Playlist
from pytube import YouTube 

import os 
def download(link):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path='.')
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 
    print(yt.title + " has been successfully downloaded.")

playlist_url = str(input("Enter playlist link:   "))
pl = Playlist(playlist_url)
 
video_links = pl.video_urls

for link in video_links:
    download(link)
