import pandas as pd
import xlsxwriter
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
writer = pd.ExcelWriter(r'ballardspahr.xlsx', engine='xlsxwriter')
maindata.to_excel(writer,index=False)
writer.save()
writer.close()