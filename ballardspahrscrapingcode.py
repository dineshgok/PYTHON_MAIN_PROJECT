
import requests
from bs4 import BeautifulSoup
import pandas as pd
baseurl= "https://www.ballardspahr.com/People"
url="https://www.ballardspahr.com/People?Services=%7BB160CF7E-CBE1-4342-85FF-FF2A86B7A235%7D"
headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
res = requests.get(url=baseurl, headers=headers)
soup = BeautifulSoup(res.content, 'lxml')
servicedata=[]
namedata=[]
officedata=[]
roledata=[]
emaildata=[]
telenumberdata=[]
faxnumberdata=[]
pagelink=[]
services=[]
for option in soup.find('select', {'title':'Filter by Services'}).find_all('option'):
    if option.get('value'):
        services.append((option.get('value'), option.text))
for service_id, service_name in services[1:6]:
        service_url =baseurl+f"?Services={service_id}"
        res = requests.get(url=service_url, headers=headers)
        soup = BeautifulSoup(res.content, 'lxml')
        for option in soup.find('select',{'title':'Filter by Offices'}).find_all('option')[1:]:
            if option.get('value'):
                office_id = option.get('value')
                for page_num in range(5):
                    full_url = f"https://www.ballardspahr.com/sitecore/api/people/search?lang=en&sc_apikey=%7B8BEE2997-A9B1-4874-A4C3-7EBA04C493EC%7D&page={page_num}&Services={service_id}&Offices={office_id}"
                    res = requests.get(full_url, headers=headers)
                    if res.ok:
                        for i in res.json()['Results']:
                            person_url = i['url']
                            final_url = f"https://www.ballardspahr.com/sitecore/api/layout/render/jss?lang=en&sc_apikey=%7B8BEE2997-A9B1-4874-A4C3-7EBA04C493EC%7D&item={person_url}"
                            res = requests.get(url=final_url, headers=headers)
                            json_object = res.json()['sitecore']['route']
                            servicesname=service_name
                            servicedata.append(servicesname)
                            name=json_object['name']
                            namedata.append(name)
                            role=json_object['placeholders']['content'][0]['placeholders']['aside'][0]['fields']['Title']['fields']['Name']['value']
                            roledata.append(role.strip('()'))
                            email=json_object['placeholders']['content'][0]['placeholders']['aside'][0]['fields']['Email']['value']               
                            emaildata.append(email.strip('()'))
                            office=option.text
                            officedata.append(office)
                            telenumber=json_object['placeholders']['content'][0]['placeholders']['aside'][1]['placeholders']['related-offices'][0]['fields']['OfficeNumber']['value']
                            telenumberdata.append(telenumber.strip('()'))
                            faxnumber=json_object['placeholders']['content'][0]['placeholders']['aside'][1]['placeholders']['related-offices'][0]['fields']['FaxNumber']['value']
                            faxnumberdata.append(faxnumber.strip('()'))
                            pageurl=baseurl.strip('/People')+person_url
                            pagelink.append(pageurl)
maindata = pd.DataFrame()
maindata['SNO'] = maindata.index + 1
maindata.set_index('SNO',inplace=True)
maindata['SERVICES'] =servicedata
maindata['NAME'] =namedata
maindata['ROLE'] =roledata
maindata['EMAIL'] = emaildata
maindata['OFFICES'] =officedata
maindata['TELEPHONE_NUMBER'] =telenumberdata
maindata['FAX_NUMBER'] =faxnumberdata
maindata['PAGE_URL'] =pagelink
maindata
