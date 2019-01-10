from __future__ import unicode_literals
import os
import webvtt
import youtube_dl
import subprocess

class Clip:

    def __init__(self, name, sub_name):
        self.name = name
        self.sub_name = sub_name

    def get_data(self):
        return self.name, self.sub_name

    def get_sub_name(self):
        return self.sub_name

    #currently works but I have not et it up to remove files yet
    def check_for_string(self):
        with open(self.sub_name, 'r') as f:
            data = f.read()
            if "boosted" in data:
                print("Passed")
            else:
                print("bad " + " " + self.sub_name)
                os.remove(self.sub_name)

    def download_clip(self):
        word = "booste"
        prevline = "blah"
        i = 0
        for caption in webvtt.read(self.sub_name):
            for line in caption.text.split("\n"):
                if line == " ":
                    continue
                elif line != prevline and word in line:
                    print(caption.start + " -----> " + caption.end)
                    print(line)
                    prevline = line
                    i+=1
                    title = self.clean_title()
                    subprocess.call("ffmpeg -i $(youtube-dl -f bestvideo[ext=mp4]+audio[ext=mp4]/mp4 --get-url " + self.name + ") -ss " + caption.start + " -to " + caption.end + " " + title + str(i) + ".mp4", shell=True)
                    # subprocess.call("youtube-dl -f bestvideo[ext=mp4]+audio[ext=mp4]/mp4 " + "https://www.youtube.com/watch?v=tSCoVPoCt1U", shell=True)
                    # print("youtube-dl -f bestvideo[ext=mp4]+audio[ext=mp4]/mp4 " + self.name)
                    print(self.name)
                    print(self.sub_name)
                    print(i)

    def clean_title(self):
        title = self.sub_name
        title_edited = title.replace(" ", "").split(".")[0]
        print(title_edited)
        return title_edited

    def download_subs(self):
        ydl_opts = {
            'skip_download': True,
            'forcetitle': True,
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitlesformat': 'vtt',
            'allsubtitles': False,
            'writeautomaticsub': True,
            'postprocessors': [{
                'key': 'FFmpegMetadata',
            }],
        }
        print("----------------------------------------")
        #builds the subtitle name for the constructor
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.name)
            i = info['id']
            t = info['title']
            sub =t + "-" + i + ".en.vtt"
            self.sub_name = sub 
            ydl.download([str(self.name)])

