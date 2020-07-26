from plyer import notification
from bs4 import BeautifulSoup
import requests
import time


def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        timeout=15,
        app_icon=r"C:\Users\SANKETH\PycharmProjects\Practice\Files\favicon.ico"
        
        
    )

# notifyMe("Sanketh", "lets rock and roll")
response=requests.get("https://covidindia.org/")
soup=BeautifulSoup(response.text,'html.parser')
# print("\n")
# print("pretiffy")
# print(soup.prettify())
mydata=[]
for table in soup.find_all('td'):
    #print(table.get_text().split("\n"))
    mydata+=table.get_text().split("\n")
    # mydata.append(table.get_text().split("\n"))
    # print(type(table.get_text()))
    # print(table)
# print(mydata)
# print(len(mydata))
# processed_list=mydata[0:4]
processed_list=[]

# print(processed_list)
# print(149//4)

count=0
for data in range(4,150,4):
    processed_list.append(mydata[count:data])
    # processed_list.append(my)
    # print("count",count)
    # print("data",data)
    count=data

# print(processed_list)
final_list=[]
states=['Karnataka','Maharashtra','Tamil Nadu']
for data in processed_list:
    if data[0] in states:
        # print(data)
        final_list.append(data)
        
print(final_list)
# notify_data=f"State:{final_list[0][0]}\nConfirmed cases-{final_list[0][1]}\n" \
#             f"recoveries-{final_list[0][2]}\n deaths-{final_list[0][3]}"
#1--> confirmed cases
#2--> recoveries
#3--> deaths

# provides notification of each state at a gap of 7 seconds
for i in range(len(final_list)):
    notify_data = f"State:{final_list[i][0]}\nConfirmed cases-{final_list[i][1]}\n" \
                  f"recoveries-{final_list[i][2]}\n deaths-{final_list[i][3]}"
    notifyMe("Corona Outbreak",notify_data)
    time.sleep(7)