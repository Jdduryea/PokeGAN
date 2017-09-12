#!/usr/bin/python
from PIL import Image
import numpy as np
import os, sys

def process(dirs, path, gen_name):
    """
    Takes all the png images in the chosen directories, resizes them to 64 x 64 
    and converts the images to RGB
    """
    final_images_path = "\Desktop\PokeGAN\Images\Gen 5 Processed\\"
    for image_file in dirs:
        if os.path.isfile(path + image_file):
            im = Image.open(path+image_file)
            f, e = os.path.splitext(image_file) 

            #Convert to RGBA to use as a mask 
            rgba_im = im.convert('RGBA')

            # White colour (r,g,b,a)
            whitened = Image.new('RGBA', rgba_im.size, (255,255,255,255)) 

            #Paste rgba_im on top of a new image to mask alpha channel and effectively whiten it
            whitened.paste(rgba_im, mask=rgba_im) 

            #Resize image
            imResize = whitened.resize((96,96), Image.ANTIALIAS)


            imResize.save(final_images_path + f + gen_name + "_resized.png", 'PNG', quality=90)

#Example Path "C:\Users\user\PokeGAN\Images\Generation 5\\black-white\\"

def delete(dirs,path):
    for image_file in dirs:
        if "resized" in (path + image_file) and os.path.isfile(path + image_file):
            os.remove(path + image_file)


path = ""
gen_name = "_bw_"
directories = os.listdir( path )

process(directories, path, gen_name)

#delete(directories, path)