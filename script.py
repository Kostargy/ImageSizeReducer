import os
import sys
from PIL import Image
import argparse

def main():

        parser = argparse.ArgumentParser(description='Description of your program')
        parser.add_argument('-p','--path', help='Image Directory', required=True)
        parser.add_argument('-s','--size', help='Maximum image size in bytes',type=check_int, required=True)
        args = parser.parse_args()

        walk_dir = args.path
        global limit
        limit = args.size

        ## Directory iteration
        for root, subdirs, files in os.walk(walk_dir):
            for someImage in files:

                filename , ext = os.path.splitext(someImage)
                p = os.path.abspath(os.path.join(root,someImage))

                if ext == ( ".jpg" or ".png"):
                    image=Image.open(p)
                    to_python(image,p,filename)


def check_int(value):
    ivalue=int(value)
    if ivalue < 0 or ivalue > 200000000:# 200MB
            raise argparse.ArgumentTypeError("Invalid image size: %s Bytes" % value)

    return ivalue


def to_python(image,path,filename):
        ##limit = 500000
        img = Image.open(path)
        width, height = img.size
        ratio = float(width) / float(height)
        quality = 100
        while  os.path.getsize(path) > limit:
            width -= 100
            quality -= 10
            if width < 0:
                return
            height = int(width / ratio)
            ##print("image width: ", width," height: ",height)
            img.resize((width, height), Image.ANTIALIAS)
            img.save(path, "JPEG", quality=quality)
            image.file = open(path)
            # reset the file pointer to the beginning so the while loop can read properly
            image.file.seek(0)
        return


if __name__ == '__main__':
    main()
