import os
import sys
import docx2txt 
'''this library is necessary, you must pip install docx2txt 
in your command line so that we can read word documents
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

sci_bonus=[]
hist_bonus=[]
lit_bonus=[]
fa_bonus=[]
rmpss_bonus=[]
geo_bonus=[]
ce_bonus=[]
misc_bonus=[]
trash_bonus=[]

for file in os.listdir(folder_addr):
    if file.endswith('.docx'):
        files.append(file)
for i in range(len(files)):
    all_tossups=[]
    all_bonuses=[]
    text=docx2txt.process(files[i])


