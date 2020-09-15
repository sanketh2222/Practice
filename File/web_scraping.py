from bs4 import BeautifulSoup
import requests
import re

response=requests.get("https://www.x-rates.com/table/?from=INR&amount=1")
soup=BeautifulSoup(response.text,'html.parser')
# print("\n")
# print("pretiffy")
# print(soup.prettify())
mydata=[]
for table in soup.find_all('td'):
    # print(table.get_text())
    # print(type(table))
    # print(table.get_text().split("\n"))
    # mydata+=table.get_text().split("\n")
    mydata.append(table.get_text())
    # print(type(table.get_text()))
    # print(table)
# print(mydata)
# print(type(mydata))
# print(len(mydata))
processed_list=[]
count=0
size=len(mydata)


with open("testfile.txt","r+") as f:
    f.truncate(0)

f=open("testfile.txt","a")
count=0
for i in range(0,size):
    
    if i%3==0 and i>0:
        # print(mydata[count:i])
        f.write(str(mydata[count:i]))
        f.write("\n")
        # f.writelines(str(mydata[count:i]))
        count=i
    
f.close()  

f=open("testfile.txt")

a=f.readlines()
# a.remove("\n")
# print(a)
size=a.__len__()
dict={}
for i in range(0,size):
    
    if i%3==0 and i>0:
        # print(mydata[count:i])
        
        mydata[count]=mydata[count].lower()
        # print(mydata[0],mydata)
        dict[mydata[count]]=float(mydata[i-1])
        # f.write(str(mydata[count:i]))
        # f.write("\n")
        # f.writelines(str(mydata[count:i]))
        count=i

# print(dict)
countries=[]
for country in dict.keys():
    countries.append(country)
amount=float(input("Enter amount"))
print("available countries\n")
cnt=[cnt for cnt in countries]
cnt.sort()
for i in cnt:
    print(i)
country_inp=input("enter country")
# pattern=re.compile(r'.*indi.*')
pattern=re.compile(f".*{country_inp}.*")
# pattern.findall(countries)
newlist = list(filter(pattern.match, countries)) #searching the matches in a list
print(newlist)
curr=amount*dict.get(newlist[0])

print(f"exchanges rates are {dict.get(newlist[0])}")
print(f"converted currency is {curr}")

f.close()

# for i in dict.keys():
#     # dict[i]=i.lower()
    
# print(dict)
# print(dict)

#writing to file
# for i in range(0,size):
    
#     if i%3==0 and i>0:
#         print(mydata[count:i])
#         f.write(str(mydata[count:i]))
#         f.write("\n")
#         # f.writelines(str(mydata[count:i]))
#         count=i
    
# f.close()  
# processed_list=mydata[0:3]
# print(processed_list)
# processed_list=mydata[4:7]
# print(processed_list)

'''
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
    
'''