#! python3
import os
import pprint

# Way 1
def RemoveZip(filenames):
    FileNum = len(filenames)
    RemoveZipfilenames=[]
    for i in range (FileNum):
        Allfile= filenames[i].split('.zip')[0]
        RemoveZipfilenames.append(Allfile)
    return(RemoveZipfilenames)

mypath = 'C:\\Users\\Administrator\\Downloads\\Spring56\\4.25.57-1589764625'
(_, _, filenames) = next(os.walk(mypath))
pprint.pprint(filenames) # print all file name (include .zip)
RemoveZipfilenames = RemoveZip(filenames)
pprint.pprint(RemoveZipfilenames) # print all file name (remove .zip)

# Use .bat way2
# files_path = [os.path.abspath(x) for x in os.listdir()]
# pprint.pprint(files_path)

# Read JSON
