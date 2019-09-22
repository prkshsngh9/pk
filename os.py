import os
from zipfile import *
a=os.walk(r'E:\New folder\New folder')
for m in a:
    print(m)
    print('')
f=ZipFile(a,'w',zip-DEFLATED)
f.write(a)
f.close()
