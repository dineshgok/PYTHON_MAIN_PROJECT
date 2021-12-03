import pandas as pd
import pycountry


address1=pd.read_excel("Dinesh_Exercise1.xlsx",sheet_name="Address Parsing")
data=address1["full_address"]
new=data.str.split(",", expand = True)

addressline1=new[0]
addressline2=new[1]
newdata=new[2].str.split(" ", expand = True)
addressline3=newdata[1]

address1['zip']=address1["full_address"].str.extract(r'(\d{5}\-?\d{0,4})')
countrydata=[]
for i in da:
    for country in pycountry.countries:
        if country.name in i:
            countrydata.append(country.name)
countries= pd.DataFrame(countrydata)

df=pd.DataFrame(list(zip(data,addressline1,addressline2,addressline3,countries[0],address1['zip'])),columns=['Fulladdress','Address_line1','Addressline2','city','country','zip'])

writer = pd.ExcelWriter(r'dineshaddressParsing.xlsx', engine='xlsxwriter')
df.to_excel(writer,index=False)
writer.save()
writer.close()