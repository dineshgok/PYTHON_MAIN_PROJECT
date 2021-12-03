import pandas as pd
from nameparser import HumanName as np

name=pd.read_excel("Dinesh_Exercise1.xlsx",sheet_name="Name Parsing")
alldata=name["Name"]

allnames=[]
title1=[]
firstname=[]
middlename=[]
lastname=[]
for i in alldata:
    names= np(i)
    allnames.append(i)
    title1.append(names.title)
    firstname.append(names.first)
    middlename.append(names.middle)
    lastname.append(names.last)
df=pd.DataFrame(list(zip(allnames,title1,firstname,middlename,lastname)),columns=['Name','Title','Firstname','Middlename','Lastname'])
writer = pd.ExcelWriter(r'dineshNameParsing.xlsx', engine='xlsxwriter')
df.to_excel(writer,index=False)
writer.save()
writer.close()