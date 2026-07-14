import os
import shutil

# Checks if the path variable was already set globally by the GUI
if 'path' not in globals():
    path = input("Enter the path: ")

files = os.listdir(path)
for file in files:

    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)