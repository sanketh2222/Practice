# n=int(input("Enter No/n"))
# choice=input("T/F")
#
# while 1:
#     if choice.lower()=="t":
#         for i in range(n):
#             print("*"*n)
#             n=n-1
#     else:
#         for j in range(n+1):
#             print("*"*j)
#             j=j+1
#
# def print_stud(normal,d):
#     print(normal)
#     for i in d:
#         print(i,end=" ")

# 
# lst=["a","b","c","d"]
# print_stud(34,lst)

# maps
# def square(a):
#     return  a*a;
#
# def cube(a):
#     return a*a*a
#
# def quad(a):
#     return  a**4
#
# func=[square,cube,quad]
#
# for i in range(4):
#     num=list(map(lambda x:x(i),func))
#     print(num)

# names=["John","Cena","Randy","Orton"]
#
# for i in names:
#     print(i,end=" ")
#
# print("/n")
# a=",".join(names)
# print(a)


# from pygame import mixer
# import pygame
# import datetime
# import time
# from datetime import timedelta
#
# def getdate():
#     import datetime
#     return time.asctime(time.localtime(time.time()))
# # time.asctime(time.localtime(time.time()))
#
#
# datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
# datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
# water = datetime.datetime.now()
# time.sleep(5)
# water2 = datetime.datetime.now()
# diff = datetime.datetime.strptime(str(water2), datetimeFormat) /
#        - datetime.datetime.strptime(str(water), datetimeFormat)

# print(diff.seconds)

#water=water/10

#print(water)

# Starting the mixer
# from pygame import mixer
#
# # Starting the mixer
# mixer.init()
#
# # Loading the song
# mixer.music.load("water.mp3")
#
# # Setting the volume
# mixer.music.set_volume(0.7)
#
# # Start playing the song
# mixer.music.play(-1)
#
# # infinite loop
# while True:
#
#     print("Press 'p' to pause, 'r' to resume")
#     print("Press 'e' to exit the program")
#     query = input(" ")
#
#     if query == 'p':
#
#         # Pausing the music
#         mixer.music.pause()
#     elif query == 'r':
#
#         # Resuming the music
#         mixer.music.unpause()
#     elif query == 'e':
#
#         # Stop the mixer
#         mixer.music.stop()
#         break


# decorators
# class once:
#     count=1
#     def __init__(self):
#         self.count = 1
#
#
# var = once.count
# print(var)
#
# while 1:
#     if var==1:
#         print("var is 1 now changing the value to 2")
#         print("/nexecute only once")
#         var=2
#     else:
#         print("sucessfully changed the value, /n now exiting the loop")
#
#
# print("outside the loop/n")

# d={
#     "a":1,
#     "b":2
# }
# print(d.get("a"))
# print(type(d.get("a")))
# print(type(d.items()))
# print(d.items())
# for key,value in d.items():
#     print(key,value)


import time
import datetime

#
# def getdate():
#     import datetime
#     return time.asctime(time.localtime(time.time()))
# time.asctime(time.localtime(time.time()))

#
# datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
# datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
# water = datetime.datetime.now()
# time.sleep(5)
# water2 = datetime.datetime.now()
# diff = datetime.datetime.strptime(str(water2), datetimeFormat) /
#        - datetime.datetime.strptime(str(water), datetimeFormat)
#
# print(diff)

# new lib management
#previous version wont work for 2 objects
'''
import datetime


def getdate():
    now = datetime.datetime.now()
    now = now.strftime("%d-%B")
    return now


#
class Library:
    def __init__(self, name):
        self.name = name
        self.lst = {}
        self.id = 100
        with open("BookList.txt") as b:
            content = b.readlines()
        for line in content:
            if line.__contains__("/n"):
                self.lst.update({str(id): {"BookTitle": line[0:len(line) - 2],
                                           "Lend Date": getdate(),
                                           "LenderName": "",
                                           "Count": int(line[-2])}})
            else:
                self.lst.update({str(id): {"BookTitle": line[0:len(line) - 1],
                                           "Lend Date": getdate(),
                                           "LenderName": "",
                                           "Count": int(line[-1])}})
            self.id += 1

    def lend_books(self, cname, bid):
        self.cname = cname
        self.bid = bid
        if self.lst[choice]['Count'] == 0:
            # print(self.lst[choice]["BookTitle"]+"is not available/n")
            print(f"{self.lst[choice]['BookTitle']} is not available/n")
            print(f"Book already availed by {self.lst[choice]['LenderName']} on {self.lst[choice]['Lend Date']}")
        else:
            count = self.lst[choice]['Count'] - 1
            self.lst[choice]['Count'] = count
            self.lst[choice]["Lend Date"] = getdate()
            self.lst[choice]["LenderName"] = self.cname
            print("Book issues sucessfully/n")

        print("upated!!")
        print(self.lst)

    def add_books(self, no_of_books, name):
        self.no_of_books = no_of_books  # check if we need to initialize name as self.name

        book_no = 0
        print((self.no_of_books + 1) > 1)
        while no_of_books:
            print(f"Book No# {book_no}")
            book_name = input("Book Title?/n")
            count = int(input("Number of copies to be added?"))
            self.id += 1
            book_no += 1
            self.lst.update({str(id): {"BookTitle": book_name, "Lend Date": getdate(),
                                       "LenderName": "NA", "DonorName": name, "Count": count}})
            no_of_books -= 1
        with open("updated_list.txt", "a") as f:
            f.write(str(self.lst))


#
#
#

# if __name__ == '__main__':
#     lst={
#         "Chankya Neti":2,
#         "Bhagwat Gita":1
#     }

# with open("BookList.txt") as b:
#     content=b.readlines()
#
# print(content)
# # print(type(content))
# print(i[-2] print the character @ -2 index
# for i in content:
#     #print(i.find("/n"))#15,16,22
#     if i.__contains__("/n"):
#         print(i[-2],i[0:len(i)-2],"/n")
#         # print(i[0:len(i)-2])
#     else:
#       print(i[-1],i[0:len(i)-1])
#       # print(i[0:len(i)-1])

# d={}
# with open("BookList.txt") as b:
#     content=b.readlines()
#
# id=100
# for line in content:
#
#     if line.__contains__("/n"):
#         d.update({str(id):{"BookTitle": line[0:len(line)-2],
#                            "Lend Date":getdate(),
#                            "LenderName":"",
#                             "Count":int(line[-2])}})
#     else:
#         d.update({str(id): {"BookTitle": line[0:len(line) - 1],
#                             "Lend Date": getdate(),
#                             "LenderName":"",
#                             "Count": int(line[-1])}})
#     id += 1

# print(d)
# with open("dict.txt","a") as f:
#     f.write(str(d))
# print(d['101']['Count'])
# print(type(d['101']['Count']))

name = input("Your Name?")
# choice=input("Please enter Book ID")
lib1 = Library("MyLib")
while 1:
    key_input = input("What to do? q for quit")

    if key_input.lower() == "l":
        choice = input("Please enter Book ID")
        lib1.lend_books(name, choice)
    elif key_input.lower() == "a":
        # add books function
        no_of_books = int(input("Number of Books?/n"))  # sample 3
        # name = input("Your Name")
        lib1.add_books(no_of_books, name)

    elif key_input.lower() == "q":
        print("Thank you")
        break
'''

# def gen(n):
#     for i in range(n):
#         yield i


# def fact(n):
#         fact = 1
#         for i in range(n):
#             fact=fact*(i+1)
#             yield fact
#
# print(fact(7))
# num=fact(6)
# print(num.__next__())
# print(fact(6).__next__())
# print(num.__next__())

# def fib(n):
#     if n==1 or n==0:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# print(fib(4))
#
# def gen_fib(n):
#     a,b=0,1
#     for i in range(n):
#         a,b=b,a+b
#         yield a
#
#
# print(gen_fib(7).__next__())
# print(gen_fib(7).__next__())
# print(gen_fib(7).__next__())
# print(gen_fib(7).__next__())
#
# def gen_fib(n):
#     a,b=0,1
#     for i in range(n):
#         a,b=b,a+b
#         yield a



# number = 5
# def Factorial_gen(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#         yield fac
#     # return fac
# print(Factorial_gen(number))
# num=Factorial_gen(5)
# print(num.__next__())
# print(num.__next__())

# comprehension exercise:
# list=[]
# no=int(input("no of items"))
# while int(no)>=1:
#     items=input("Enter the items")
#     list.append(items)
#     no-=1
#
# print(list)
# print("1.List comp/n2.Dict comrehension/n3.Set comprehension")
#
# while 1:
#     choice = int(input("Choice?"))
#     if choice==1:
#         listc=[i for i in list]
#         print(listc)
#
#     elif choice==2:
#         dict={1:f"{i}" for i in list}
#         print(dict)
#         dict1={value:key for key,value in dict.items()}
#         print(dict1)
#
#     else:
#         setc=(i for i in list)
#         setc1={i for i in list}
#         print(setc)
#         print(setc1)
#
#     if choice==4:
#         break
#
# dict1={
#     1:"item1",
#     2:"item2"
# }
# dict2={value,key for key,value in dict1.items()}
# print(dict,"/n",dict2)


# khana = ["roti", "Sabzi", "chawal"]
#
# for item in khana:
#     if item=="roti"
#
# for item in khana:
#     if item == "roti":
#         print(f"{item} found")
#         break
#
# else:
#     print("Your item was not found")
# from functools import lru_cache

# val=int(input("Cached value"))
#
# @lru_cache(maxsize=1)
# def some_work(n):
#     print("doing somework")
#     time.sleep(n)
#     print("grand success")
#     return n
#
# try except and finally and else:
# if __name__ == '__main__':
#
#     some_work(3)
#     print("second")
#     print(some_work(3))
#     print("third")
#     print(some_work(3))
#     print(some_work(3))
#
#
# f1 = open("harry.txt")
#
# try:
#     f = open("does2.txt")
#
# except EOFError as e:
#     print("Print eof error aa gaya hai", e)
#
# except IOError as e:
#     print("Print IO error aa gaya hai", e)
#
# else:
#     print("This will run only if except is not running")
#
# finally:
#     print("Run this anyway...")
#     # f.close()
#     f1.close()
#
# print("Important stuff")

# ----coroutines
#
# def searcher():
#     import time
#     # Some 4 seconds time consuming task
#     book = "This is a book on harry and code with harry and good"
#     time.sleep(4)
#
#     while True:# from second time onwards executes from here.
#         text = (yield)# making seracher as a coroutin. Also to received value from send
#         if text in book:
#             print("Your text is in the book")
#         else:
#             print("Text is not in the book")
#
# search = searcher()
# print("search started")
# next(search)
# print("Next method run")
# search.send("harry")
#
# search.close()
# search.send("harry")
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")


# import os
# print(os.getcwd())
# path=os.chdir("C://Users/SANKETH/PycharmProjects/Practice/Files")
# #C:\Users\SANKETH\PycharmProjects\Practice\Files
# print(os.getcwd())
#
#
# count=0
# file_list=[]
# for i in range(1,6):
#     file_list.append(f"file{i}.txt")
#     # with open(f"file{i}.txt","a") as f:
#     #     f.write("sanketh")
#

# for i in range(101,1001):
#     file_list.append(f"file{i}.txt")
#     with open(f"file{i}.txt","a") as f:
#         f.write("sanketh")

# for i in range(1,101):
#     os.remove(f"file{i}.txt")--> delete all files

# list.append("file")
# print(file_list)
# print(os.getcwd())
# try:
#     for file in file_list:
#         # print(file)
#         # print(os.getcwd())
#         with open(file,"a") as f:
#             f.write("sanketh")
#
# except:
#     print(f"{file} file not found")



# file_list=["file1.txt","file2.txt","file3.txt","file4.txt","file5.txt"]
# def search():
#     global count
#     dict={}
#     for file in file_list:
#         with open(file) as f:
#             content=f.readlines()
#             # print(content)
#             # print(count)
#             # print(dict)
#             dict[file]=content[count].replace("/n","")
#     print(dict)
#     dict2={value:key for key,value in dict.items()}
#     print(dict2)
#     time.sleep(4)
#
#
#
#     while True:
#         text=(yield )
#         if text in dict.values():
#             print(f"{text} found {dict2[text]}")
#         else:
#             print(f"{text} not found")
#
# s=search()
# s.__next__()
# s.send("Musk")
# print("after yield")
# s.send("Elon")


#
# for file in file_list:
#     with open(file,"a") as f:
#         f.write("")

#--------OS Module


# import os
# print(dir(os))
# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# f = open("harry.txt")
# print(os.listdir("C://"))
# os.makedirs("This/that")
# os.rename("harry.txt", "codewithharry.txt")
# print(os.environ.get('Path'))
# print(os.path.join("C:/", "/harry.txt"))

# print(os.path.exists("C://Program Files2"))
# print(os.path.isfile("C://Program Files"))

import os
# path=os.path.join(os.getcwd(),"Files")
# os.chdir(path)
# onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
# print(onlyfiles)
#
# txtfiles =[file for file in onlyfiles if file[-3:]=="txt"]
# txtfiles =[file for file in onlyfiles if file[-3:].lower()=="jpg"]
# print(txtfiles)
# string ="tamanna-bhatia-cute-hd-photos-1080p-dwehnq-400x533.JPG"
# print(string.capitalize())
# print(string[-3:].lower())#getting last 3 charecters of the string
# print(onlyfiles)
# def solider(path):
#     count=1
#     os.chdir(path)
#     onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
#     txt_files = [file for file in onlyfiles if file[-3:] == "txt"]
#     jpg_files = [file for file in onlyfiles if file[-3:].lower()=="jpg"]
#     for jpg in jpg_files:
#         os.rename(jpg,f"{count}.jpg")
#         count+=1
#
#     for file in txt_files:
#         os.rename(file,file.capitalize())
#
#
#
#
# path=os.path.join(os.getcwd(),"Files")
# os.chdir(path)
# solider(path)


#--------HTTP Requests


# r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
# print(r.text)
# print(r.status_code)

# url = "https://aws.amazon.com/console/
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)

# string ="Hey jarvis please open youtube for me"
# processed=string.split(sep=" ")
# print(processed.index("open"))
# word=processed.index("open")+1
# print(processed[word])

# now=datetime.datetime.now()
# now=now.strftime("%I:%M:%S %p")
# print(now)

# import wikipedia
#
# print(wikipedia.summary("BeerBiceps"))

import os
# for r,d,f in os.walk("c:\\"):
#     for files in f:
#          if files == "Telegram.exe":
#               print(os.path.join(r,files))

# https://www.google.com/search?q=how+to+improve+skills
import webbrowser
from googlesearch import search
# string="https://www.google.com/search?q="
# another="how to become rich"
# another1=another.replace(" ","+")
# print(another1)
# print(string+another1)
# url=string+another1
# webbrowser.open(url)
# query=googlesearch.search("Elon Musk")
# print(query)
# query = "beer biceps"
#
import json
import requests
import pyttsx3
# f=open("file.json")

# print(f.read())
# data=json.load(f)
# print(type(data))
# print(data["Name"])
# print(data["Age"])
# f.close()

# speak=pyttsx3.init()
# rate = speak.getProperty('rate')   # getting details of current speaking rate
# print (rate)
# rate=speak.setProperty('rate',125) #seting up the voice rate
# voices = speak.getProperty('voices')
# speak.setProperty('voice', voices[1].id)# change to female voice 0--> Male 1 --> Female


# url = ('http://newsapi.org/v2/top-headlines?'
#        'country=in&'
#        'apiKey=0f984866c30c4880967285aa463f328e')
# response = requests.get(url)
# class Counts:
#     times=1
#     def __init__(self):
#         self.times=1
#
# c= Counts()
# print("count class",c.times)
#
# response=requests.get("https://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=0f984866c30c4880967285aa463f328e")
# # f=open("file1.txt","a")
# f2=open("file2.txt","a")
# # f.write(str(response.json()))
# news=response.json()
# print(type(news))#dict

# data=json.dump(news,f2)

#
# print(response.json())
# print(news['articles'][0]['description'])
# head1=news['articles'][0]['description']
# con1=news['articles'][0]['content']
# con1=news['articles'][0]['url']
# # print(type(head1))
# print("content\n")
# print(news['articles'][0]['content'])
# speak.say(head1)
# speak.runAndWait()
#
# speak.say(con1)
# speak.runAndWait()
#
# speak.say("next up")
#
# print("news 2\n")
#
# print(news['articles'][1]['description'])
# print("content\n")
# print(news['articles'][1]['content'])
#
# speak.say(news['articles'][1]['description'])
# speak.runAndWait()
# speak.say(news['articles'][1]['content'])
# speak.runAndWait()
#
# speak.say("next up")
#
# print(news['articles'][2]['description'])
# print("content\n")
# print(news['articles'][2]['content'])
#
#
# speak.say(news['articles'][2]['description'])
# speak.runAndWait()
# speak.say(news['articles'][2]['content'])
# speak.runAndWait()
# f.close()
#f2.close()
# string="hello\n world"
# print(string.splitlines())

import re

string =" My email @gmail contact is ssankethboss061@gmail.com and find sankeths94@gmail.com"
# string1=string.split(" ")
# for i in string1:
#     if i.endswith("@gmail.com"):
#         print(i)

# Email Collector
import re
str ='''
2
'''
# email1
# email2
# email3

str = """

 Email:enquiry@alliance.edu.in   Helpline: +91 80 3093 8100 / 8200 / 4619 9100
 Media  Library  News  Webmail  Careers
 Alliance University
 Conferences
 Admissions Open
 Select Language
UPDATES:
ABOUT US 
WHY AU 
COLLEGES 
FACULTY
INTERNATIONAL PROGRAMS
PROGRAMS
RESEARCH
ADMISSIONS 
PLACEMENTS
CONTACT US
Contact UsHome Contact Us
 Contact Us Back
 Vice-Chancellor
Dr. Pavana Dibbur
 : vc@alliance.edu.in
 : +91 80 3093 8100/4619 9100

 Pro Vice-Chancellor (Academics, Research & Strategy)
Dr. Anubha Singh
 : anubha@alliance.edu.in
 : +91 80 3093 8102

 Registrar
Mr. Madhu Sudan Mishra
 : registrar@alliance.edu.in
 : +91 80 3093 8100/4619 9100

 Registrar (Examination & Evaluation)
Dr. Sajan Mathew
 : registrar.exams@alliance.edu.in
 : +91 80 3093 8141

 Director (Placements)
Mr. Mathew Thankachan
 : placement@alliance.edu.in | mathew.t@alliance.edu.in
 : +91 80 3093 8124 | 98444 72674

 Director (International Affairs)
Mr. Rajen Chatterjee
 : rajen.chatterjee@alliance.edu.in
 : +91 80 3093 8075

 Director (Admissions)
Mr. Abhay Chebbi
 : abhay.chebbi@alliance.edu.in
 : +91 96636 46464

 Human Resources Department
 : hrd@alliance.edu.in
 : +91 80 3093 8210 / 8204

 Student Verification 
Office of Registrar (Examination & Evaluation)
 : edu.verify@alliance.edu.in
 : +91 80 3093 8100 / 8200 | +91 80 4619 9100

 Contacts Info
 ALLIANCE UNIVERSITY
 Central Campus
Chikkahagade Cross, Chandapura - Anekal Main Road, Anekal
Bengaluru – 562 106, Karnataka,   India. [ Get Route Map ]
+91 80 3093 8100/8200/4619 9100 | Fax: +91 80 4619 9099
E-mail : enquiry@alliance.edu.in

 Office of Admissions
UG: +91 9620009825 | 91084 43123 | 91084 42143 | 98806 19618
PG: +91 98860 02500 | 99002 29974 | 90083 16363

 City Campus 1
19th Cross, 7th Main, BTM 2nd Stage, N.S. Palya
Bengaluru – 560 076, Karnataka,   India. [ Get Route Map ]
Tel.: +91 80 26786020 / 21 , 26789749

 City Campus 2
2nd Cross, 36th Main, Dollars Scheme, BTM 1st Stage
Bengaluru – 560 068, Karnataka,   India. [ Get Route Map ]
Tel.: +91 80 26681444 / 4372 | Fax: +91 80 26782048

 CONTACT INFO
 Contact Us
 Enquiry
 Feedback
 Get Route from Address
Quick Course Finder


Find Courses
 SCHOOLS | COLLEGES
 Alliance School of Business
 Alliance College of Engineering and Design
 Alliance School of Law
 Alliance Ascent College
 Planned Academic Units
International Partners

Antwerp Management School
Antwerp Management School
Belgium
Royal Roads University
Royal Roads University
Canada
Beijing Institute of Technology
Beijing Institute of Technology
China
Nanjing University of Aeronautics and Astronautics
Nanjing University of Aeronautics and Astronautics
China
The Sino-British College, USST,
The Sino-British College, USST,
China
INSEEC
INSEEC
France
IPAC School of Management
IPAC School of Management
France
ISEP
ISEP
France
Paris School of Business
Paris School of Business
France
Telecom School of Management
Telecom School of Management
France
Telecom SudParis
Telecom SudParis
France
Toulouse Business School
Toulouse Business School
France
Berlin School of Economics and Law
Berlin School of Economics and Law
Germany
European Business School
European Business School
Germany
University of Applied Sciences
University of Applied Sciences
Germany
Duisenberg School of Finance
Duisenberg School of Finance
The Netherlands
Maastricht School of Management
Maastricht School of Management
The Netherlands
Russian Presidential Academy of National Economy and Public Admi. (RANEPA)
Russian Presidential Academy of National Economy and Public Admi. (RANEPA)
Russia
Togliatti Academy of Management
Togliatti Academy of Management
Russia
Edinburgh Napier University
Edinburgh Napier University
UK
Federation of Schools (FEDE)
Federation of Schools (FEDE)
Switzerland
Swansea Metropolitan University
Swansea Metropolitan University
UK
University of Bedfordshire
University of Bedfordshire
UK
University of Chester
University of Chester
UK
University of Dundee
University of Dundee
UK
Fairleigh Dickinson University
Fairleigh Dickinson University
USA
Georgia State University
Georgia State University
USA
Kennesaw State University
Kennesaw State University
US
Oakland University
Oakland University
USA
San Jose State University
San Jose State University
USA
The University of Memphis
The University of Memphis
USA
Webber International University
Webber International University
USA
 International Programs
 Testimonials
 My two years at Alliance University have groomed me to be a confident individual ready to enter the corporate world and has deepened this confidence by helping me get a job in my dream organization. Alliance with its state of the art facilities, competitive curriculum, varied cultural mix and strong faculty base has motivated and guided m...  Read More

 Kiran Varghese Jacob Kiran Varghese Jacob
Google Google
 Top University in India for MBA LAW Engineering & Arts and the Humanities
Alliance University is a private University established in Karnataka State by Act No.34 of year 2010 and is recognized by the University Grants Commission (UGC), New Delhi... 

About Us
THE UNIVERSITY
GOVERNANCE
CORPORATE SOCIAL RESPONSIBILITY
AACSB
IACBE
NIRF
Useful Links
PROGRAMS & COURSES
INTERNATIONAL PROGRAMS
RESULTS
FEEDBACK
DOWNLOADS
PHOTO GALLERY
Useful Links
STUDENT VERIFICATION
ALLIANCE ADVENTURE CLUB
ANTI-RAGGING POLICY
ROUTE MAP
CONTACT US
2018 © All Rights Reserved.  | Privacy Policy | Terms & Conditions | Disclaimer | Sitemap




"""


# email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+", str)
email = re.findall(r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]+",str)

print(email)


# pattern = re.compile(r'([a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]+)')
# pattern = re.compile(r'\+\w+ \w+ \w+ \w+')#extract phone no
pattern = re.compile(r'\+[1,9]+ \d{2} \d{4} \d{4}')#extract phone no.
match=pattern.findall(str)
print(match)
# string="i"
# pat1=re.compile(r'a+i')
# pat2=re.compile(r'a*i')
# print(pat1.findall(string))
# print(pat2.findall(string))

# patt= re.compile("^s.*@gmail.com$")
# patt2=re.compile("^\s")
# match=patt2.findall(string)
# print(match)
# matches = patt.finditer(string)
# print(type(matches))
# print(patt.findall(string))
# for match in matches:
#     print("matches")
#     print("matches",match)