from __future__ import unicode_literals
from clips import Clip
import os
import webvtt
import youtube_dl

with open("links.txt", 'r') as file:
    links = file.readlines()

objs = []
for i in range(1):
    objs.append(Clip(links[i], " "))
    objs[i].download_subs()
    objs[i].check_for_string()
    objs[i].download_clip()