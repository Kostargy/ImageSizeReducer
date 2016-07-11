import os
import sys
walk_dir = "/home/kostargy//Desktop/python/imageTest"


for root, subdirs, files in os.walk(walk_dir):
    for infile in files:
        nice, ext=os.path.splitext(infile)
        print("file:",nice," ext: ",ext)
