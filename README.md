# docx-to-image<BR>
<BR>
How to use this:<BR>
1. Install Python 3.5 or better (configure python path)<BR>
2. Make a new folder<BR>
3. Place this script into this folder<BR>
4. Copy all docx you want to recover to the same folder this script is<BR>
5. Run script.<BR>
6. Wait.<BR>
<BR>
Your images will be at /imgs and your original docx at /backup_docx.<BR>
<BR>
This script will only recover a image per docx, but this shouldn't be an issue because I wrote this to recover some images Google Drive converted to docx.<BR>
<BR>
How this script works:<BR>
1. Backup all your docx to /backup_docx<BR>
2. Rename all .docx in main folder to .zip<BR>
3. Extract all .zip to /temp<BR>
4. Search for a image01.jpg<BR>
5. Rename image01.jpg to match .docx filename<BR>
6. Move this jpg file to /imgs<BR>
7. Move all zips to /zips<BR>
8. Delete /zips and /temp folders<BR>
<BR>
Please enjoy this.<BR>
<BR>
I won't be updating this code.<BR>
Feel free to improve it and share with other people too. :)<BR>
