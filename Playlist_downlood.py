# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:19:42 2023

@author: Image903
"""

import re
from pytube import Playlist

DOWNLOAD_DIR = 'Path to the downlaod folder'

playlist = Playlist('Playlist url')

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    
print("Number of Videos : "+ str(len(playlist.videos)))
      
vid_download = len(playlist.videos);
vid_skipped = 0
vid_num=1

for video in playlist.videos:
    try:
         print("Downloading : " + str(vid_num) )
         vd = video.streams.get_highest_resolution()
         vd.download(DOWNLOAD_DIR)
        
         vid_num = vid_num+1
         
    except Exception:
        vid_download=vid_download-1
        vid_skipped = vid_skipped +1
        print("Age restricted or invalid url: Skipped...")
        pass
    
print("Total Videos Downloaded : " + str(vid_download))
print("Total Videos Skipped : " + str(vid_skipped))
