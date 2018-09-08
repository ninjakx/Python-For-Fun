##################################################################
'''               AUTOMATIC FILE ARRANGER                      '''
'''Script to arrange the file according to their extension type'''
##################################################################


import os
import shutil
from os.path import splitext

source=''  #Put path to ur directory 

for i in sorted(os.listdir(source)):
    #print(i)
    filename,ext=splitext(i)
    #print(filename,ext)
       
    if ext=='' or str(ext).split('.')[1].isdigit():
        continue
    extension=(str(ext).split('.')[1]).lower()
    directory=source+extension

    #print(directory)
    
    if not os.path.exists(directory):
        os.makedirs(directory) 
        shutil.move(source+i,directory) 
    else:
        shutil.move(source+i,directory)

print("done")
