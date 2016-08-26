#Python 3.5

import os
import zipfile
import re
import shutil
import glob
from os import listdir
from os.path import isfile, join
print("------\nThis Python script recovers images from your docx!")
print("For now, it can only recover one image per file.")
print("It should be enough to recover images that you uploaded to Google Drive and it converted to docx.")
print("------\nPlease wait, it is working on your files...")

path_main = os.getcwd()
path_temp = path_main+'\\temp'
path_imgs = path_main+'\\imgs'
path_back = path_main+'\\backup_docx'
path_zips = path_main+'\\zips'
items = 0
if not os.path.exists(path_temp):
	os.makedirs(path_temp)
if not os.path.exists(path_imgs):
	os.makedirs(path_imgs)
if not os.path.exists(path_back):
	os.makedirs(path_back)
if not os.path.exists(path_zips):
	os.makedirs(path_zips)

files = [f for f in listdir(path_main) if isfile(join(path_main, f))]
for item in files: 
	filename, file_extension = os.path.splitext(item)
	if file_extension == '.docx':
	
		shutil.copyfile(item, path_back+"\\"+item)
		newname = item.replace("docx","zip", 1)
		os.rename(item,newname)
files2 = [f for f in listdir(path_main) if isfile(join(path_main, f))]

for item in files2: 
	filename, file_extension = os.path.splitext(item)
	if file_extension == '.zip':
		with zipfile.ZipFile(item, "r") as z:
			z.extractall(path_temp+'/'+item)
		

for item in glob.glob(path_temp+'/*/word/media/*.jpg'):
	newitem = item.replace(path_temp+"\\","")
	itemname = newitem.replace(".zip\word\media\image01.jpg","")
	print("Recovered:",itemname)
	mv_img = path_imgs+"\\"+itemname+'.jpg'
	
	#shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
	shutil.move(item, mv_img)

for item in files2: 
	filename, file_extension = os.path.splitext(item)
	if file_extension == '.zip':
		shutil.move(item, path_zips+"\\"+item)

shutil.rmtree(path_temp)
shutil.rmtree(path_zips)

print("------\nDone.\n\nThis script renamed your .docx to .zip.\nBut don't worry, there is a backup /back folder.\nAnd the recovered images are /imgs.\n\nFeel free to delete them all.\n------")
