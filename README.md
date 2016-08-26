# docx-to-image

How to use this: 
1. Install Python 3.5 or better (configure python path)
2. Make a new folder
3. Place this script into this folder
4. Copy all docx you want to recover to the same folder this script is
5. Run script.
6. Wait.

Your images will be at /imgs and your original docx at /backup_docx.

This script will only recover a image per docx, but this shouldn't be an issue because I wrote this to recover some images Google Drive converted to docx.

How this script works:
1. Backup all your docx to /backup_docx
2. Rename all .docx in main folder to .zip
3. Extract all .zip to /temp
4. Search for a image01.jpg
5. Rename image01.jpg to match .docx filename
6. Move this jpg file to /imgs
7. Move all zips to /zips
8. Delete /zips and /temp folders

Please enjoy this.

I won't be updating this code.
Feel free to improve it and share with other people too. :)
