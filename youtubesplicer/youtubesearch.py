from __future__ import unicode_literals
from clips import Clip
import os
import webvtt
import youtube_dl
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--linksfile", help = "path to the text file of YouTube links")
parser.add_argument("-c", "--keyword", help = "Your keyword to search for")
args = parser.parse_args()

links = args.linksfile
keyword = args.keyword

with open(links, 'r') as file:
    linkarr = file.readlines()
    
num_lines=len(open(links).readlines()) -1 

def main():
    objs = []
    for i in range(num_lines):
        objs.append(Clip(linkarr[i], " "))
        objs[i].download_subs()
        if not objs[i].check_for_string(keyword):
        	i+=1
        else:
            objs[i].download_clip(keyword)
			

if __name__ == '__main__':
	main()