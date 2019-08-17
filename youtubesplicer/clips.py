from __future__ import unicode_literals
import os
import re
import webvtt
import youtube_dl
import subprocess

class Clip:
    def __init__(self, name, sub_name):
        self.name = name
        self.sub_name = sub_name

    #getter method for title and subtile name
    def get_data(self):
        return self.name, self.sub_name

    #getter for subtitle name
    def get_sub_name(self):
        return self.sub_name

    def check_for_string(self, keyword):
        with open(self.sub_name, 'r') as f:
            data = f.read()
            if keyword in data:
                return True
            else:
                os.remove(self.sub_name)
                return False

    def download_clip(self, keyword):
        prevline = ""
        i = 0
        for caption in webvtt.read(self.sub_name):
            for line in caption.text.split("\n"):
                if line == " ":
                    continue
                elif line != prevline and keyword in line:
                    prevline = line
                    output = self.clean_title()
                    i+=1
                    subprocess.call("ffmpeg -i $(youtube-dl -f 22+audio[ext=mp4]/mp4 --get-url " + self.name + ") -ss " + caption.start + " -to " + caption.end + " " + output + str(i) + ".mp4", shell=True)

    #clean title of spaces and special characters for export name
    def clean_title(self):
        title = self.sub_name
        title_edited = title.replace(" ", "").split(".")[0]
        re.sub("[^a-zA-Z0-9]+", "", title_edited)
        return title_edited

    def download_subs(self):
        ydl_opts = {
            'skip_download': True,
            'forcetitle': True,
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitlesformat': 'vtt',
            'allsubtitles': False,
            'postprocessors': [{
                'key': 'FFmpegMetadata',
            }],
        }

        #builds the subtitle name for the constructor
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.name)
            sub = info['title'] + "-" + info['id'] + ".en.vtt"
            re.sub("[^a-zA-Z0-9]+", "", sub)
            self.sub_name = sub 
            ydl.download([str(self.name)])

