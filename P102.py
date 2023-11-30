import os
import shutil

from_dir = 'C:/Users/pidik/downloads/t'
to_dir = 'C:/Users/pidik/OneDrive/Desktop'
list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    name,ext = os.path.splitext(i)
    if(ext == ''):
        continue
    if(ext in ['.txt','.doc','.pdf','.docx']):
        path1 = from_dir + '/' + i
        path2 = to_dir + '/' + 'Document_Files_code'
        path3 = to_dir + '/' + 'Document_Files_code' + '/' + i
        if os.path.exists(path2):
            print('Moving' + i)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('Moving' + i)
            shutil.move(path1,path3)