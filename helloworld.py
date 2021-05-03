import os
import sys
import docx2txt
folder_addr=""

for path in pathlib.Path("a_directory").iterdir():
    if path.is_file():
        current_file=open(path, "r")
print "Hello World"