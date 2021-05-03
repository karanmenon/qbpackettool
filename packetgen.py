import os
import sys
import docx2txt 
import re

'''this library is necessary, you must pip install docx2txt #
in your command line so that we can read word documents
'''
folder_addr="/Users/karanmenon/qbpackettool/packets" #put the address of your folder with packets here
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

cat_list=["SCI", "HIST", "GEO", "LIT", "FA", "RMPSS", "GEO", "CE", "MISC."]

distribution={ #define the number of tossups in each category of the packet here
    "SCI":4,
    "HIST":4,
    "LIT":4,
    "FA":3,
    "RMPSS":3,
    "GEO":1,
    "CE":2,
    "MISC.":1,
    "TRASH":1
}

bonus:distribution={ #define the number of bonuses in each category of the packet here
    "SCI":7,
    "HIST":5,
    "LIT":4,
    "FA":1,
    "RMPSS":1,
    "GEO":2,
    "CE":2,
    "MISC.":0,
    "TRASH":2
}

def getTossupList(category): #returns associated question list given tag
    if(category=="SCI"):
        return sci
    elif(category=="HIST"):
        return hist
    elif(category=="LIT"):
        return lit
    elif(category=="FA"):
        return fa
    elif(category=="RMPSS"):
        return rmpss
    elif(category=="GEO"):
        return geo
    elif(category=="CE"):
        return ce
    elif(category=="MISC."):
        return misc
    elif(category=="TRASH"):
        return trash
    else:
        return []
def getBonusList(category): #returns associated bonus list given tag
    if(category=="SCI"):
        return sci_bonus
    elif(category=="HIST"):
        return hist_bonus
    elif(category=="LIT"):
        return lit_bonus
    elif(category=="FA"):
        return fa_bonus
    elif(category=="RMPSS"):
        return rmpss_bonus
    elif(category=="GEO"):
        return geo_bonus
    elif(category=="CE"):
        return ce_bonus
    elif(category=="MISC."):
        return misc_bonus
    elif(category=="TRASH"):
        return trash_bonus
    else:
        return []

#tossup_dict={"SCI":sci, "HIST":hist, "LIT":lit, "FA":fa, "RMPSS":rmpss, "GEO":geo, "CE":ce, "MISC.":misc, "TRASH":trash}
#bonus_dict={"SCI":sci_bonus, "HIST":hist_bonus, "LIT":lit_bonus, "FA":fa_bonus, "RMPSS":rmpss_bonus, "GEO":geo_bonus, "CE":ce_bonus, "MISC.":misc_bonus, "TRASH":trash_bonus}

for file in os.listdir(folder_addr):
    if file.endswith('.docx'):
        files.append(file)
for i in range(len(files)): 
    file_addr=folder_addr+"/"+files[i]
    #print(len(files))
    text=docx2txt.process(file_addr)
    texts=text.split("Bonuses")
    #text="1. dasdsklkdlsamds <HIST, WORLD> Bonus: Guyana <GEO, SA> 2. Kritika <SCI, CHEM> Bonus: Simping <RMPSS, PHIL>"
    all_tossups=re.findall(r"\d\.[^>]*>", texts[0])
    for x in range(len(all_tossups)):
        all_tossups[x]=all_tossups[x][3:]
    all_bonuses=re.findall(r"Bonus:[^>]*>", texts[1])
    #print("Tossups: ", all_tossups[0] , "\n")
    #print("Bonuses: ", all_bonuses[0])
    for j in range(len(all_tossups)):
        category=re.findall(r"<[^<\,]*\,", all_tossups[j])
        for x in range(len(category)):
            category[x]=category[x][1:-1]
        (getTossupList(category[0])).append(all_tossups[j])
    for k in range(len(all_bonuses)):
        category=re.findall(r"<[^<\,]*\," , all_bonuses[k])
        for x in range(len(category)):
            category[x]=category[x][1:-1]   
        (getBonusList(category[0])).append(all_bonuses[k])
#print("Literature: ", lit)
#print("Geography: ", geo)

#for str in cat_list:
