name = "Ram Krishna Prasad"
# print(len(name))
# print(name[4])
# print(name[0:4])
# print(name[0:18])
# # print(name[200]) # wrong
# print(name[0:200]) # right
# print(name[0:8])
# print(name[0:8:1])
# print(name[:5])
# print(name[0:])
# print(name[::])
# print(name[::3])
# print(name[::-1]) # Print in reverse order
# print(name[::-2])name = "Ram Krishna Prasad"
# # print(len(name))
# # print(name[4])
# # print(name[0:4])
# # print(name[0:18])
# # # print(name[200]) # wrong
# # print(name[0:200]) # right
# # print(name[0:8])
# # print(name[0:8:1])
# # print(name[:5])
# # print(name[0:])
# # print(name[::])
# # print(name[::3])
# # print(name[::-1]) # Print in reverse order
# print(name[::-2])
# print(name[-3:len(name)])

# num=[i for i in range(1,10)]
# print(num)
# n=input()
# for i in range(1,int(n)):
#     print(i,end=" ")
import os
# path=os.path.join(os.getcwd(),"Files")
# print(path)
# print(os.listdir(path))
# for i in os.listdir(path):
#     print(os.path.splitext(i)[1],end=" ")
# name = "sanketh.png"
# print(name.split("."))
# name[1]
# a=1
# b=a
# d=1
#
# print(a==b)
# print(a==d)
# a=2
# print(b)
# print(a is b)
# print(d is a) # not supposed to return true since d is a new variable and not pointing to a or b

# a=[1,2,3]
# b=a
# print("a",a)
# print("b",b)
# b[0]=2
# print("a",a)
# print("b",b)
# c=[2,2,3]
# print(a==c)
# print(a is c)

# age_year=input("Enter your inp.")
# if len(age_year)==4:
#     if int(age_year)>2020:
#         print("you are not born yet")
#     else:
#         print("you entered year")
#         age=int(age_year)+100
#         if 2020-int(age_year)>=150:
#             print("you seem to be very old")
#             year = int(input("enter year"))
#             age = year - int(age_year)
#             print(f"you will be {age} in year {year} ")
#         else:
#             print(f"you will be 100 in {age}")
#             year=int(input("enter year"))
#             age=year-int(age_year)
#             print(f"you will be {age} in year {year} ")
# else:
#     if int(age_year)==0:
#         print("min age should be 1")
#     elif int(age_year)>=150:
#         print("you seem to be very old")
#         exit(0)
#         # year = int(input("enter year"))
#         # age=year-(2020-int(age_year))
#         # print(f"you will be {age} in year {year}")
#     else:
#         print("you entered your age")
#         year=2020+100-int(age_year)
#         print(f"you will be 100 in {year} ")
#         year=int(input("enter year"))
#         age=year-(2020-int(age_year))
#         print(f"you will be {age} in year {year}")

# try:
#     n=int(input("enter the no of apples"))
#     mn=int(input("enter mx"))
#     mx=int(input("enter mn"))
#     print(mx,mn)
#
#     if mn==mx:
#         print("invalid")
#     else:
#         lst=[i  for i in range(mn,mx+1) if n% i==0]
#     # print(type(mn))
#     # print(mn>=mx)
#     # while mn>=mx:
#     #     if n%mn==0:
#     #         print(f"{mn} is divisble by {n}")
#     #         mn+=1
#     #     else:
#     #         continue
#
#     for i in range(mn,mx+1):
#         if n%i==0:
#             print(f"{i} is a divisor of {n}")
#         else:
#             print(f"{i} is not  a divisor of {n}")
# except ValueError:
#     print("invalid input")


'''

#REVERSING LIST WITH OWN LOGIC
lst=[1,2,3,4,5,6,7]
lst2=lst.copy() # OR List2=lst[:]
size=len(lst)-1
size1=len(lst)
i=0
print(i<=size+1)
while size1:
    print(i,size)
    lst[i]=lst2[size]
    i+=1
    size-=1
    size1-=1

print(lst)


#15 lines
#problem 4
cases=int(input("Enter no of test cases"))
num=[]
for i in range(cases):
    n=int(input("Enter numbers"))
    num.append(n)

# num=[451,10,2133]
numc=num.copy()
num2=[]
for i in range(len(num)):
    num2.append(str(num))

for i in range(len(num)):
    if num[i]>10:#not considering number 10
        while num2[i][::-1]!=num2[i]:
            num[i]+=1
            num2[i]=str(num[i])
    else:
        num2[i]=num[i]

print(num2)
for i in range(len(num)):
    print(f"palindrome of {numc[i]} is {num2[i]}")

'''
# import re
# Sentences = ['This is good', 'python is good', 'python is not python snake','joke','python is best in best']
# query = "is good"# query= input("enter query string")
#
# def matching(sentence,query):
#     score = 0
#     words1=sentence.split(" ")
#     # print(words1)
#     words2=query.split(" ")
#     # print(words2)
#     for word1 in words1:
#         for word2 in words2:
#             if word1==word2:
#                 score+=1
#     return score
#
# # print(matching("python is good","python"))
#
# scores=[(matching(sentence,query)) for sentence in Sentences ]
# # print(scores)
#
#
# sentscore=[ sentscore for sentscore in sorted(zip(scores,Sentences),reverse=True)]
# sentscorelist=[j for i,j in sentscore if i!=0]#to filter the list by excluding 0 score. to find the no. of exact match
# occurance=len(sentscorelist)# no. of match
#
# print(f"{occurance} matched results\n")
# for score,sent in sentscore:
#     if score!=0:
#         print(f"\"{sent}\"  matched with a score of {score}\n")

# print(f"{occurance} matched results")
# for item in sentscorelist:
#     print(f"{item}")
# print(sentscore)
# print(sentscorelist)
# scoremap=tuple(zip(Sentences,scoresent))
# print(scoresent)
# print(scoremap)


# list1=[1,2,3]
# list2=[4,5,6]
# print(tuple(zip(list1,list2)))

# parse=[]
#
# # patt=re.compile(r'')
#
#
# for i in Sentences:
#     parse.append(i.split())
#
# # print(parse)
# query=query.split()
# # print("query")
# # print(query[1])
# # print(len(parse))
# # print(len(parse[2]))
# count=0
# occ=0
# dict={}
#
# for i in range(0,len(parse)):
#     for j in range(len(parse[i])):
#         for z in range(len(query)):
#             if query[z]==parse[i][j]:
#                 count+=1
#     # print(i,"main loop ")
#
#     dict.update({count:i})
#     if count>=1:
#         occ+=1
#     count=0
# print(dict)
# dict1={}
# print(f"{occ} matched results")
# for i in sorted(dict.keys(),reverse=True):
#     if i!=0:
#         print(f"{Sentences[dict.get(i)]} --> {i} ocuurences")
# print(count)
# print(dict)
# lst=[i for i in dict.values()]
# lst.sort(reverse=True)
# print(lst)

# for i,j in range(0,len()):
#     for z in query:
#         if query[z]==parse[i][j]:
#             count+=1

# lst=[4,3,2,1,10]
# lst1=[1,2,3,4,5]
# sort=[sorted(zip(lst1,lst), reverse=True)]#first the list is mapped, then sorted based on the first
# #parameter value in this case lst1
# sort=[sorted(zip(lst,lst1), reverse=True)]
# print(sort)

# import  random
#
# num=random.randint(1,10)
# print(num)
#
# # lst=[table*i for i in range(1,11)]
# # print(lst)
# def fakeMult(table):
#     lst=[table*i for i in range(1,11)]
#     lst[num]+=2
#     return lst
#
# table=5# table= input("Enter table")
# res=fakeMult(table)#res=fakeMult(table)
#
# print(res)
#
# def iscorrect(table,numbers):
#     correct=True
#     count=0
#     for i in numbers:
#         if i % table != 0:
#             print(i)
#             print(f"index is {count}")
#             correct=False
#         else:
#             count += 1
#
#     return correct
#
# result=iscorrect(table,res)
# print(result)


# lst=[i for i in numbers if i%table!=0]


#weather API development
# import requests
# import json

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
#
# city="chennai"
# response=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=134b6fda987e9204b5cea01d566a247a")
#
# # print(type(response))
#
# weather_data=json.loads(response.text)
#
# # print(weather_data)
# # print(type(weather_data))
# print(f"{weather_data['weather'][0]['description']}")
# print(f"feels like {round(int(weather_data['main']['temp_min'])-273.15)}  degrees in chennai")
# print(f"humidity is  {weather_data['main']['humidity']}  percent")
# print(f"wind speed is  {weather_data['wind']['speed']}")
# # print(weather_data["weather"]["description"])
#
# speak(f"its {weather_data['weather'][0]['description']} in {city}")
# speak(f"feels like {round(int(weather_data['main']['temp_min'])-273.15)}  degrees in {city}")
# speak(f"humidity is  {weather_data['main']['humidity']}  percent")
# speak(f"wind speed is  {weather_data['wind']['speed']}")

# url = ('http://newsapi.org/v2/top-headlines?'
#            'country=in&'
#            'apiKey=d48128f52a774428a589dcab2548c687')
#
# response = requests.get(url)
# # f=open("file1.txt","a")
#  # f.write(str(response.json()))
# news = response.json()
# # print(response.json())
# # print(news['articles'][0]['description'])
# head1 = news['articles'][0]['description']
# con1 = news['articles'][0]['content']
# url = news['articles'][0]['url']
# # print(head1)
# print(con1)
# # print(type(url))
# con2=""
# res=con1.index(r"[")
# if r"[" in con1:
#     con1=con1[0:res]
# print(con1)
    # print(url)


# Reminder and notes function for AI desktop project

import pyttsx3
import speech_recognition as sr
import datetime
import time
from pyautogui import typewrite
from threading import Thread

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 172)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # change to female voice 0--> Male 1 --> Female

now = datetime.datetime.now()
now = now.strftime("%d-%B")


def Listen():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak now")
        audio = r1.listen(source)  # opens/starts the microphone
        try:
            text = r1.recognize_google(audio, language="en-in")  # get the text or content that you just spoke
        except Exception as e:
            print("I did not hear that")
            return "None"
            # speak("i did not hear that")
        print(text)
        return text


def getdate():
    import datetime
    return time.asctime(time.localtime(time.time()))


# query=Listen()
# print(type(query))
# print(query)
query = "set a reminder at tomorrow 12:35 a.m."
query2 = "set a reminder at tomorrow 2:00 p.m."

event=0


# q=input("listening..")
processed_query = query.split(" ")
# print(processed_query)
# print(type(processed_query))
proc = ""
if processed_query.__contains__("tomorrow"):
    data = processed_query.index("tomorrow")
    # print(data)
    proc = processed_query[data:len(processed_query)]
    # print(list(now))  # dd -month
    # print()
    day = int(now[0:2])+1
    # print(day)
    proc[0]=day

print(proc)
if proc[2]=='p.m':
    proc[2]="PM"
else:
    proc[2]="AM"

# print(proc)
rem_date=proc[0]
rem_time=proc[1]+proc[2]
# print(rem_date)
# print(rem_time)
rem_time=str(proc[1])
d=rem_time.split(":")
event=0
rem_hour=int(d[0])
if d[1]=="00":
    d[1]=0
    rem_min=0
rem_min=int(d[1])
# rem_hour=proc[1]
# rem_min=
print(d)



datetimeFormat = '%A, %d %B %Y %I:%M%p'
now1 = datetime.datetime.now()
now1 = now1.strftime(datetimeFormat)
now1=list(now1.split(" "))
#
# print(now1)
#
curr_time=now1[4]
if curr_time[0]==0:
    curr_time=curr_time[1:7]
else:
    curr_time = curr_time[0:7]
curr_day=now1[1]
# print(rem)
print(curr_time)
# print(curr_time[-2:])# AM OR PM of current time
# print(curr_time[0:5])
# curr_time.index(
curr_hour=int(curr_time[0:curr_time.index(":")])
if curr_time[3]!=0:
    curr_min=int(curr_time[3:5])
else:
    curr_time=int(curr_time[4:5])
print(curr_hour)
print(curr_min)
# print(curr_day)

# event=proc[1]

def t():
    # time.sleep(10)  # wait for 15 seconds for input
    # if first == 'waiting...':
    # time
    while 1:
        datetimeFormat = '%A, %d %B %Y %I:%M%p'
        now1 = datetime.datetime.now()
        now1 = now1.strftime(datetimeFormat)
        now1 = list(now1.split(" "))
        curr_time = now1[4]
        if curr_time[0] == 0:
            curr_time = curr_time[1:7]
        else:
            curr_time = curr_time[0:7]
        curr_day = now1[1]
        # print(rem)
        # print(curr_time)
        # print(curr_time[-2:])# AM OR PM of current time
        # print(curr_time[0:5])
        # curr_time.index(
        curr_hour = int(curr_time[0:curr_time.index(":")])
        if curr_time[3] != 0:
            curr_min = int(curr_time[3:5])
        else:
            curr_time = int(curr_time[4:5])
        # print(curr_hour)
        # print(curr_min)

        # print(proc[2])
        # print(curr_time[-2:])
        # print("before condition")
        if proc[2]==curr_time[-2:]:
            # print(rem_hour)#12
            # print(curr_hour)#12
            # print(curr_min)  # 0
            # print(rem_min)#12
            # event=0
            print(event)
            if curr_hour>=rem_hour and curr_min>=rem_min and event==0:
                print("reminding you")
                # event=1
                global event
                event=1
                # event=+1
                break
    #     typewrite('n')
    #     typewrite(['enter'])

while 1:
    event=0
    T = Thread(target=t)
    T.start()
    # q=input("Listening...")
    # print("after input",q)
    q= Listen()
    print("after listening",q)


# count=0
# for i in now1:
#     print(i,count)
#     count+=1