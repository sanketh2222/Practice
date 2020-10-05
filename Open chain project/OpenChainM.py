import  json
import requests
from time import sleep
import os
from selenium import webdriver
import pandas as pd
import xlwings as xl
from datetime import datetime

url="https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"



# file_name=f"option_data_{datetime.now.strftime("%H%M")}" 
# url="https://jsonplaceholder.typicode.com/todos"
# url="https://www1.nseindia.com/homepage/Indices1.json"

headers={
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    
}

cookie_dict={"bm_sv":"D2426C607602C18D0712BD0FF91E0CDA~SyBAu6SxlQm7gsX/wannAR0xHNzleJOqtYtwH87nLaisC9NzRodCjsbbxbzi92PATL08w8eXILBFVDQnCYVKjWHeNDxi2djthfRsSuv1YtPBvIlezLDL4m3dbQoG0DkbTZ4N9SIOREH+ozp9ZdVHG7GMXs2kSayvgfyiQFxENoM"}


# currDir=os.path.dirname(__file__)
mydir=os.getcwd()
# print(currDir)
print(mydir)

if os.path.exists("option_chain5.json"):
    os.remove("option_chain5.json")


if os.path.exists("file.txt"):
    os.remove("file.txt")
    
if os.path.exists("file1.txt"):
        os.remove("file1.txt")

if os.path.exists("file3.txt"):
    os.remove("file3.txt")
    
    
def get_session_cookie():
    driver=webdriver.Chrome(executable_path=os.path.join(mydir,"chromedriver.exe"))
    driver.get("https://www.nseindia.com")
    cookies=driver.get_cookies()
    for cookie in cookies:
        cookie_dict[cookie["name"]]=cookie["value"]
        cookie_dict[cookie["domain"]]=cookie["value"]
        with open("file3.txt","a") as f1:
            f1.writelines(str(cookie))
        with open("file.txt","a") as f:
            f.write(json.dumps(cookie_dict,indent="")) 
            print("\n")
            # print("\n")
    
    driver.quit()
    return cookie_dict
        
            
        
# session_cookie=get_session_cookie()

# for cookie in session_cookie:
#     if cookie=="bm_sv":
#         with open("file1.txt","a") as f:
#             f.write(json.dumps(cookie_dict[cookie],indent=""))
#             print("\n")

# cookie="bm_sv" 
def start_session(status):   
    session=requests.session()
    # session.cookies.set(cookie,cookie_dict[cookie])
    if status==1:
        session_cookie=get_session_cookie()
        for cookie in session_cookie:
            if cookie=="bm_sv" or  "nseappid" in cookie or "nsit" in cookie:
                with open("file1.txt","a") as f:
                    f.write(json.dumps(cookie_dict[cookie],indent=""))
                    print("\n")
                session.cookies.set(cookie,cookie_dict[cookie])
    else:
        for cookie in cookie_dict:
            if cookie=="bm_sv" or  "nseappid" in cookie or "nsit" in cookie:
                session.cookies.set(cookie,cookie_dict[cookie])
    resp=session.get(url,headers=headers)
    return resp#status code

def read_wrire_data():
    with open("option_chain5.json") as f:
        data=f.read()
    data1=json.loads(data)#type cast into dict
    print(type(data1))
    ce_values= [value["CE"] for value in data1["filtered"]["data"] ]
    pe_values= [value["PE"] for value in data1["filtered"]["data"] ]
    ce=pd.DataFrame(ce_values).sort_values("strikePrice")
    excel_file="chaindata.xlsx"
    wb=xl.Book(excel_file)
    single_sheet=wb.sheets("oidata")
    single_sheet.clear_contents()
    single_sheet.range("A1").options(index=False).value=ce
    
def fetch_oi():
    try:
        
        # data = json.loads(str(resp))
        # print(type(resp))
        resp = start_session(0)
        print(resp) 
        print(resp.json()) 
        with open("option_chain5.json","a") as f:
            f.write(json.dumps(resp.json(),indent=4,sort_keys=True))
        print("executing from try")
        read_wrire_data()
        
    except Exception as e:
        print("executing from exception")
        session_cookie=get_session_cookie()
        res=start_session(1)
        # resp=session.get(url,headers=headers)
        print(res)
        with open("option_chain5.json","a") as f:
            f.write(json.dumps(res.json(),indent=4,sort_keys=True))
        read_wrire_data()
    # print(data)
# print(type(data))

# file=open("option_chain3.json","a")
# json.dump(resp,file,indent="")
# file.close()
# print("function executed successfully")

    
# with open("option_chain3.json","w") as f:
#     # f.write(json.dumps(resp,indent=4,sort_keys=True))
#     f.write(str(data))
#     # f.write(str(resp))
#     # print(r)
#     print("function executed successfully")   


# for cookie in cookie_dict:
#     print(cookie)
#     session.cookies.set(cookie,cookie_dict[cookie])
    
# count=0
# def fetch_oi():
#     # r=requests.get(url,headers=headers).json()
#     for cookie in session_cookie:
#         if cookie=="bm_sv":
#             session=requests.session()
#             session.cookies.set(cookie,cookie_dict[cookie])
#             count+=1
        
#     r=session.get(url,headers=headers).json()
#     # print(r)
#     with open("option_chain3.json","a") as f:
#         f.write(json.dumps(r,sort_keys=True,indent=""))
#     # print(r)
#     print("function executed successfully")
    # with open("option_chain1.json","w") as f:
    #     f.write(json.dumps(r))


if __name__ == '__main__':
    fetch_oi()