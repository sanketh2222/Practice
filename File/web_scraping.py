from bs4 import BeautifulSoup
import requests

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
states=['Karnataka','Maharashtra','Tamil Nadu']
for data in processed_list:
    if data[0] in states:
        print(data)
   

#1--> confirmed cases
#2--> recoveries
#3--> deaths 
# for state in 

# for data in range(0,149):
#     processed_list.append(mydata[0:4])
    