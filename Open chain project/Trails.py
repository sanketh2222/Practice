# import json
# d={
#     "sanketh":2,
#     "elon":111,
#     "musk":3,
#     "ala":14
# }
# file=open("file.json","w")
# json.dump(d,file,indent="")
# print(json.dumps(d,indent="",sort_keys=True))

# import requests
# from bs4 import BeautifulSoup

# myHtmlData = requests.get('https://www.mohfw.gov.in/')

# soup = BeautifulSoup(myHtmlData.text, 'html.parser')
# myDatastr= ""
# for tr in soup.find_all('tbody')[0].find_all('tr'):
#     myDatastr += tr.get_text()

# print(myDatastr)

for cookie in session_cookie:
    if cookie=="bm_sv":
        with open("file1.txt","a") as f:
            f.write(json.dumps(cookie_dict[cookie],indent=""))
            print("\n")

with open("file1.txt") as f:
    data=f.read()
    