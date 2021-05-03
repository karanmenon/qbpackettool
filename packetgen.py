import os
import sys
import docx2txt 
'''this library is necessary, you must pip install docx2txt 
in your command line so that we can read word docuemtns
'''
folder_addr=""
files=[]
sci=[]
hist=[]
lit=[]
fa=[]
rmpss=[]
geo=[]
ce=[]
misc=[]
trash=[]
for file in os.listdir(folder_addr):
    if file.endswith('.docx'):
        files.append(file)
for i in range(len(files)):
    text=docx2txt.process(files[i])
