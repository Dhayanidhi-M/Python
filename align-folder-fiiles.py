import os,shutil

#add new file extentions and folder name - extention:folderName
#example - 'txt':text-dir - (txt - externtion , text-dir - folderName) 
file_align ={'txt':'text-dir',
             'csv':'csv-dir',
             'py':'python-dir',
            'MP4':'Record-dir',
            'mp4':'Record-dir'
            }
# source folder path
folder_path = "C:/Recordings"  #use your custom folder

#function to move the files to respective folder
def createOrPlaceFile(item,ext):
    if os.path.exists(folder_path+"/"+file_align[ext]) and os.path.isdir(folder_path+"/"+file_align[ext]):
        shutil.move(folder_path+"/"+item,folder_path+"/"+file_align[ext])
    else:
        os.makedirs(folder_path+"/"+file_align[ext])
        shutil.move(folder_path+"/"+item,folder_path+"/"+file_align[ext])

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Print the list of files
for item in files:
    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path):
        ext = os.path.splitext(item)[1][1:]
        if ext in list(file_align.keys()):
            createOrPlaceFile(item,ext)
