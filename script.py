import os
import sys
from PIL import Image
walk_dir = "/home/kostargy//Desktop/python/image"


def to_python(image,path,filename):
        limit = 500000
        img = Image.open(path)
        width, height = img.size
        ratio = float(width) / float(height)
        quality = 100
        while  os.path.getsize(p) > limit:
            width -= 100
            quality -= 10
            if width < 0:
                return
            height = int(width / ratio)
            ##print("image width: ", width," height: ",height)
            img.resize((width, height), Image.ANTIALIAS)
            img.save(path, "JPEG", quality=quality)
            image.file = open(p)
            # reset the file pointer to the beginning so the while loop can read properly
            image.file.seek(0)
        return


## Directory iteration
for root, subdirs, files in os.walk(walk_dir):
    for someImage in files:
        filename , ext=os.path.splitext(someImage)
        p=os.path.abspath(os.path.join(root,someImage))
        if ext==".jpg":
            image=Image.open(p)
            to_python(image,p,filename)
