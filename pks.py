import os
from zipfile import *
os.chdir(r'C:\Users\Prakash\Downloads\ps')
f=ZipFile('file.zip','w',ZIP_DEFLATED)
file=os.listdir(r'C:\Users\Prakash\Downloads\ps')
for n in  file:
    f.write(n)
f.close()
