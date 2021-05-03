import os
import sys
import docx2txt 
import re

'''this library is necessary, you must pip install docx2txt #
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

tossup_dict={"SCI":sci, "HIST":hist, "LIT":lit, "FA":fa, "RMPSS":rmpss, "GEO":geo, "CE":ce, "MISC.":misc, "TRASH":trash}
bonus_dict={"SCI":sci_bonus, "HIST":hist_bonus, "LIT":lit_bonus, "FA":fa_bonus, "RMPSS":rmpss_bonus, "GEO":geo_bonus, "CE":ce_bonus, "MISC.":misc_bonus, "TRASH":trash_bonus}
'''
for file in os.listdir(folder_addr):
    if file.endswith('.docx'):
        files.append(file)
for i in range(len(files)): 
    text=docx2txt.process(files[i])
'''
text="1. dasdsklkdlsamds <HIST, WORLD> Bonus: Guyana <GEO, SA> 2. Kritika <SCI, CHEM> Bonus: Simping <RMPSS, PHIL>"
all_tossups=re.findall(r"\d\.[^\.>]*>", text)
for x in range(len(all_tossups)):
    all_tossups[x]=all_tossups[x][3:]
all_bonuses=re.findall(r"Bonus:[^>]*>", text)
print("Tossups: ", all_tossups , "\n")
print("Bonuses: ", all_bonuses)

for j in range(len(all_tossups)):
    category=re.findall(r"<[^<\,]\,", all_tossups[j])
    for x in range(len(category)):
        category[x]=category[x][1:-1]
    tossup_dict[category].append(all_tossups[j])
for k in range(len(all_bonuses)):
    category=re.findall(r"<[^<\,]\," , all_bonuses[k])
    for x in range(len(category)):
        category[x]=category[x][1:-1]
    bonus_dict[category].append(all_bonuses[k])
    


