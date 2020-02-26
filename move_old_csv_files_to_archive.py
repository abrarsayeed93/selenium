import shutil
import os

source = 'C:\\Users\\asayeed\\Downloads\\'
dest1 = 'C:\\Users\\asayeed\\Downloads\\archive\\'

files = os.listdir(source)

for f in files:
    if f.endswith(".csv"):
        print(f)
        shutil.move(source+f, dest1+f)