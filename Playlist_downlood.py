# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:19:42 2023

@author: Image903
"""

import re
from pytube import Playlist

DOWNLOAD_DIR = 'D:\\ML_DL\\Files_ML_DL\\Violence_files\\Violence_classis_Dataset\\Physical_Voilence\\Python_downlaods\\kicks_real_scenes'

playlist = Playlist('https://www.youtube.com/playlist?list=PL7A2BF5EE83A36AC4')

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