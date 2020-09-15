# import datetime
# from datetime import timedelta
# now = datetime.datetime.now()
# now1 = now+timedelta(hours=5.5)
# now1=now1.strftime("%I:%M:%S %p")
# now=now.strftime("%I:%M:%S %p")
# # l = now.strftime("%I:%M:%S %p").timedelta(5)
# print(f" time is   {now1}")
# print(f" time is   {now}")import requests
import requests
import json

# url = "https://www.fast2sms.com/dev/wallet?authorization=2Uk4loecxYszb609TPgMH1LySRQVKmEh35iquCvjXaG8wtAJOZnsBmIQXhVzot3Cxj07SZ5E9dlgkU2P"

url = "https://www.fast2sms.com/dev/bulk"

# url="https://www.fast2sms.com/dev/wallet?authorization=2Uk4loecxYszb609TPgMH1LySRQVKmEh35iquCvjXaG8wtAJOZnsBmIQXhVzot3Cxj07SZ5E9dlgkU2P"


Api_key="2Uk4loecxYszb609TPgMH1LySRQVKmEh35iquCvjXaG8wtAJOZnsBmIQXhVzot3Cxj07SZ5E9dlgkU2P"
querystring = {"authorization":Api_key,"sender_id":"SHRLCK","message":"This is test message","language":"english","route":"p",
               "numbers":"8310145281"}

headers = {
    'cache-control': "no-cache"
}


# class Test:
#     var=1
try:
    response = requests.request("GET", url, headers=headers, params=querystring)
except Exception:
    print("failed due to unknown error")
    
    
if response.text.__contains__("true"):
    print("sucessfull")
else:
    print("failed")
# v=Test()
# print(type(v))
# print(v.var)
# dict=response.text
print(response)
print(type(response))
# if response["return"]=="true":
#     print("message sent sucessfully")
# else:
#     print("an unknown error occured")

print(response.text)


