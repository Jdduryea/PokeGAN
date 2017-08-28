#!/usr/bin/python
from PIL import Image
import numpy as np
import os, sys

def process(dirs, path):
	"""
	Takes all the png images in the chosen directories, resizes them to 64 x 64 
	and converts the images to RGB
	"""
    for image_file in dirs:
        if os.path.isfile(path + image_file):
        	im = Image.open(path+item)
        	f, e = os.path.splitext(path + image_file)

        	#Resize image
        	imResize = im.resize((64,64), Image.ANTIALIAS)

        	#Convert to RGB
        	rgb_im = imResize.convert('RGB')
    		#pic = np.asarray(rgb_im)
        	rgb_im.save(f + "_resized.png", 'PNG', quality=90)

#Example Path "C:\Users\user\PokeGAN\Images\Generation 5\\black-white\\"

path = ""
directories = os.listdir( path )
print(directories)

resize(directories, path)