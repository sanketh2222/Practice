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

# def print_stud(normal,d):
#     print(normal)
#     for i in d:
#         print(i,end=" ")
# 
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

#comprehension exercise:
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

# dict1={
#     1:"item1",
#     2:"item2"
# }
# dict2={value,key for key,value in dict1.items()}
# print(dict,"/n",dict2)


# khana = ["roti", "Sabzi", "chawal"]
#
# # for item in khana:
# #     if item=="roti"
#
# for item in khana:
#     if item == "roti":
#         print(f"{item} found")
#         break
#
# else:
#     print("Your item was not found")
from functools import lru_cache

# val=int(input("Cached value"))

# @lru_cache(maxsize=1)
# def some_work(n):
#     print("doing somework")
#     time.sleep(n)
#     print("grand success")
#     return n

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

# def searcher():
#     import time
#     # Some 4 seconds time consuming task
#     book = "This is a book on harry and code with harry and good"
#     time.sleep(4)
#
#     while True:
#         text = (yield)
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


import os
print(os.getcwd())
path=os.chdir("C://Users/SANKETH/PycharmProjects/Practice/Files")
#C:\Users\SANKETH\PycharmProjects\Practice\Files
print(os.getcwd())


count=0
file_list=[]
for i in range(1,6):
    file_list.append(f"file{i}.txt")
    # with open(f"file{i}.txt","a") as f:
    #     f.write("sanketh")


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
def search():
    global count
    dict={}
    for file in file_list:
        with open(file) as f:
            content=f.readlines()
            # print(content)
            # print(count)
            # print(dict)
            dict[file]=content[count].replace("/n","")
    print(dict)
    dict2={value:key for key,value in dict.items()}
    print(dict2)
    time.sleep(4)



    while True:
        text=(yield )
        if text in dict.values():
            print(f"{text} found {dict2[text]}")
        else:
            print(f"{text} not found")

s=search()
s.__next__()
s.send("Musk")
print("after yield")
s.send("Elon")


#
# for file in file_list:
#     with open(file,"a") as f:
#         f.write("")






