from PIL import Image
from image2gif import writeGif
import os

import imageio
directory = str(input()) # where ur all images are 
gif_file_name=str(input())
with imageio.get_writer(gif_file_name+'.gif', mode='I') as writer:
    for filename in os.listdir(directory):
        image = imageio.imread(filename)
        writer.append_data(image)
