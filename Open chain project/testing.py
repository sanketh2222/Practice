import  json
import requests
import os
import pandas as pd
import xlwings as xl

#url="https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    #https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY
url="https://jsonplaceholder.typicode.com/todos"
# url="https://www.google.com"
# r=requests.get(url).json()
# print(r)
pd.set_option("display.max_rows", 1010)
pd.set_option("display.max_columns", 1010)
# pd.set_option('max_colwidth', 40)
pd.set_option('display.width', 400)
# pd.set_option()
dict={
    "sanketh":1,
    "elon":2,
    "musk":3
}

for i in dict:
    print(i)#prints only keys by default
    
# if os.path.exists("option_chain3.json"):
#     os.remove("option_chain3.json")
# resp=requests.get(url).json()

# print(type(resp))
# print(resp)


# excel_file="chaindata.xlsx"
# wb=xl.Book(excel_file)
# single_sheet=wb.sheets("oidata")

# with open("option_chain4.json") as f:
#     data=f.read()
#     data1=json.loads(data)#type cast into dict
#     print(type(data1))
    
    
# ce_values= [value["CE"] for value in data1["filtered"]["data"] ]
# pe_values= [value["PE"] for value in data1["filtered"]["data"] ]
# ce=pd.DataFrame(ce_values).sort_values("strikePrice")


# print(ce)
# single_sheet.range("A2").value=ce


# single_sheet.clear_contents()
# single_sheet.range("A1").options(index=False).value=ce
# ce_data=[]
from datetime import datetime
file_data=datetime.now().strftime("%d_%m")
file_name=f"option_data_{file_data}.json" 
print(file_name)
# print(data)


# wb.close()
# file=open("test.json","a")
# for i in data1["filtered"]["data"]:
#     print(type(i))
#     file.write(json.dumps(i["CE"],indent=4,sort_keys=True))
#     file.write("next item\n")
#     ce_data.append(i)
    
# # print(ce_data[0])
# # print(ce_data[1])
# file.close()

# print(pe_values)
 
# print(type(data_dict))
# print(data_dict)