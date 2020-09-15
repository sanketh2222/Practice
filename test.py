#import pickle
# from  operator import itemgetter
# from pygame import mixer
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
# diff = datetime.datetime.strptime(str(water2), datetimeFormat) \
#        - datetime.datetime.strptime(str(water), datetimeFormat)

# print(diff.seconds)

#water=water/10

#print(water)

# Starting the mixer
# mixer.init()

# Loading the song
# mixer.music.load("water.mp3")
# mixer.music.load("eye.mp3")

# Setting the volume
# mixer.music.set_volume(0.7)
#
# def water():
#     water = datetime.datetime.now()
#
#     time.sleep(1200)
#     water2 = datetime.datetime.now()
#     diff = datetime.datetime.strptime(str(water2), datetimeFormat) \
#            - datetime.datetime.strptime(str(water), datetimeFormat)
#
#     print(diff.seconds/60)
#     return  diff.seconds/60
#
# def eye():
#     water = datetime.datetime.now()
#
#     time.sleep(1800)
#     water2 = datetime.datetime.now()
#     diff = datetime.datetime.strptime(str(water2), datetimeFormat) \
#            - datetime.datetime.strptime(str(water), datetimeFormat)
#
#     print(diff.seconds/60)
#     return diff.seconds/60
#
# while 1:
#     wat=water()
#     if wat==20:
#         print("water condition")
#         mixer.music.load("water.mp3")
#         mixer.music.play()
#         first=input("Drank?Y/N")
#         if first.lower()=="y":
#             with open("HealthLog.txt","a") as water1:
#                 Content=f"Drank water at [{getdate()}] \n"
#                 water1.write(Content)
#         else:
#             pass
#
#
#     ey=eye()
#     if ey==30:
#         print("eye confition")
#         mixer.music.load("eye.mp3")
#         mixer.music.play()
#         second = input("Done?Y/N")
#         if second.lower()=="y":
#             with open("HealthLog.txt","a") as i1:
#                 Content=f"Eye exercise done  at [{getdate()}]\n"
#                 i1.write(Content)
#         else:
#             pass
#
#




    # Start playing the song

#
#
#
# # infinite loop
# while True:
#
#     print("Press 'p' to pause, 'r' to resume")
#     print("Press 'e' to exit the program")
#     query = input("  ")
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

# print("hello")
# str="hello world"
# string="hello world i am robo speed 1 tera hertz memonery 1 zeta bytes"
# print(string[0::550])
# print(str[:-6])# skip last 6 letters of the string
# print(str[-5:])# get only last 5 letters of the string
# d=input()
# print(int(d))

# d={}
# d["Me"]="hello"
# # print(d)
# d2={
#     "Fname":"Elon",
#     "Lname":"Musk"
# }
# d.update(d2)

# print(d)
# del d["Me"]

# print(d.items())
# d=d.items()
# for a in d:
#     if  a[1]=="Elon":
#         print(a)
#         print(a[0])
#         continue


# while(1):
#       d=int(input("enter no#"))
#   if d>=100:
#       print("congs")
#       break


# while (True):
#     d = input("enter no#")
#     d = int(d)
#     if d == 100:
#         break

    # Code as discussed in the video
# try:
#     f = open("sejalD.txt", "rt")
#     print(f.tell())
#     print(f.readline())
#     print(f.tell())
#     print(f.readline())
#     f.seek(42)
#     print(f.readline())
# except FileNotFoundError as e:
#     print("could not find file")
# f.close()
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
#
# d={
#     "Harry":22,
#     "Elon":48
# }
#
# for i in d.items():
#     print(i,end="\n")# prints dict in tuple form
#
# for i in d.items():
#     print(i,end=" ")# prints in a single line seperated by a single space
#
# print("\n")# same as print(i,end="\n")
#
# for i in d:
#     print(i)# prints only keys


# File reading basics
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)# this content is empty
#f.close()


# def myFunc(e):
#   return len(e)
#
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW',"BB"]
#
# model={
#   ("ford","1","2020"),
#   ("bmw","2","2021")
# }
# k=itemgetter(1)
# print(k)
# cars.sort(key=lambda l:len(l))
# print(cars)
# t=myFunc(cars)
# print(t)


# f = open("harry.txt")
# f.seek(11)
# print(f.tell())
# print(f.readline())
# # print(f.tell())
#
# print(f.readline())
# # print(f.tell())
# f.close()
#

# l=10
#
# def func():
#     global  l #permission to change the global variable
#     l=l+10#global variable modiefied to 20
#     print(l)
#
# func()
# print(l)


# def func():
#     x=20
#     def myfunc():
#         global x
#         x=70
#         print("myfunc",x)#70
#     print("func",x)#20
#     myfunc()
#     print("myfunc()",x)#20
#
# func()#70 and 20
# print(x)#70


# output
# func 20
# my func 70
# my func 20
# 70


# def sample():
#     print("inside sample func")
#     l=5
#     def mysample():
#         print("inside nested mysample func")
#     mysample()
#
# sample()
# print(l)  # cannot access in global scope the locals that are a part of sample() functions. example l and mydef() function


# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
count = 1

# --------------------decorators---------------

# def dec1(func):
#     def exec():
#         print("before exec\n")
#         count=2
#         func()
#         print("after exec\n")
#     return  exec
#
# @dec1
# def myfun():
#     print("My function")
#     print(count)
#
# myfun()

# class Employee:
#     no_of_leaves=8
#
#     def __init__(self,name,age):#constructors
#         self.age=age
#         self.name=name
#
#
#     @classmethod
#     def modify_leaves(cls,num):
#         cls.no_of_leaves=num
#
#
#
# e1=Employee("abc",12)
# print(e1.name)
# # e1.no_of_leaves=34
# # print(e1.__dict__)
# # print(e1.no_of_leaves)
# print(Employee.no_of_leaves)
# e1.modify_leaves(9)
# print(e1.__dict__)
# print(Employee.no_of_leaves)


'''


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

Employee.printgood("Rohan")



#-----------------------Multiple inheritence

class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game =game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class CoolProgramer(Player, Employee):

    language = "C++"
    def printlanguage(self):
        print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgramer("Karan",["Cricket"])
# det = karan.printdetails()
# karan.printlanguage()
# print(det)
print(karan.var)


--- multilevel inheritence


class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

# print(darry.guitar) #wrong
print(harry.isdance())

# electronic device
# pocket gadget
# phone


'''

# ------------Polymorphysim example plus operatore behaves differently based on parameters

# print(5+6)
# print("5" + "6")

# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

# ----------------overriding
# class A:
#     classvar1 = "I am a class variable in class A"
#     def __init__(self):
#         self.var1 = "I am inside class A's constructor"
#         self.classvar1 = "Instance var in class A"
#         self.special = "Special"
#
# class B(A):
#     classvar1 = "I am in class B"
#
#     def __init__(self):#once inint method from class B is overriden then while using class b objects the init method of class a
#         #will not be called
#         self.var1 = "I am inside class B's constructor"
#         #self.classvar1 = "Instance var in class B"
#         super().__init__()
#         print(super().classvar1)
#
# class C:
#     pass
#
# a = A()
# b = B()
# print(b.classvar1)# searches for insatnce variable first, if instance variable not present then prints classvar1 from class variable
# #instance variable always takes the 1st preference
# # print(b.special, b.var1, b.classvar1)
# print(a.classvar1)


# -- Diamond shape inheritence problem solved by python

# class A:
#     def met(self):
#         print("This is a method from class A")
#
# class B(A):
#     def met(self):
#         print("This is a method from class B")
#
# class C(A):
#     def met(self):
#         print("This is a method from class C")
#
# class D(C, B):
#     def met(self):
#         print("This is a method from class D")
#
#
# a = A()
# b = B()
# c = C()
# d = D()
#
# d.met()

# class Employee:
#     no_of_leaves = 8
#
#     #called as constructors
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     #dunder methods all the methodes that start and end with__
#     def __mod__(self, other):
#         return  self.salary % other.salary
#
#     #overriding the division / operator
#     def __truediv__(self, other):
#         return self.salary / other.salary
#
#     #representation of on object print(e1) preference#2 when __str is present
#     def __repr__(self):
#         return f"Employee('{self.name}', {self.salary}, '{self.role}')"
#
#     # representation of on object print(e1) preference#1 Always
#     def __str__(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#
#
#
# #e1=Employee()#throws an error
# e1=Employee("a",5,"inst")
# e2=Employee("b",2,"prog")
# print(e1%e2)
# print(e1)#changes the representation of the employee object e1
# first perference is given to __str and next goes for __repr
# cntl+D duplicates a line
# print(e1.name)

# serach for mapping operators for functions in python for operator overloading
# e.g adding salaries of 2 classes

# ---abstract method

# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod


# class Shape(ABC):
#
#     def __init__(self,height):
#         self.height=height
#     @abstractmethod
#     def printarea(self):
#         return self.height
#
#     @abstractmethod
#     def printlength(self):
#          return 1
#
# class Rectangle(Shape):
#     type = "Rectangle"
#     sides = 4
#     def __init__(self,height):
#         self.length = 6
#         self.breadth = 7
#         self.height=height
#     def printarea(self):
#         return self.length * self.breadth
#
#     def printlength(self):
#         return self.length
#
# rect1 = Rectangle(2)
# print(rect1.printarea())
# print(rect1.height)
# print(Shape.printarea(2))
# s1= Shape()  # throws  an error

# --------------getters and setters
# class Employee:
#     no_of_leaves = 8
#     var = 8
#
#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role
#
#     def printDetails(self):
#         return  self.role
#
# e1=Employee("a",22,"dev")
# print(e1.__dict__)
# print(e1.role)
# print(e1.printDetails())
# e1.role="Snr DEV"
# print(e1.__dict__)
# print(e1.printDetails())
# print(e1.role)

#
# class Employee:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         self.email = f"{fname}.{lname}@codewithharry.com"
#         self.midname=f"{fname}"
#
#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"
#
#     @property# you can call the function without using () eg. no need to call like e1.email() we can say e1.email
#     def email(self):
#         if self.fname==None or self.lname == None:
#             return "Email is not set. Please set it using setter"
#         return f"{self.fname}.{self.lname}@codewithharry.com"
#
#
#     @property#only for checking
#     def mname(self):
#         if self.midname is None:
#             print("please set email or fname")
#
#     @mname.setter
#     def mname(self,name):
#         print("setting mname\n")
#         self.midname=name
#
#
#     # @property
#     # def fname(self, fname):
#     #     self.fname = fname
#     #     if fname is None:
#     #         print("please set email or fname")
#
#     @mname.deleter
#     def mname(self):
#         print("deleting now\n")
#         self.midname=None
#
#
#
#     @email.setter# @email--> name under @property
#     #this method cannot be used to modify the things that are directly taking value at init--> eg. fname and lname
#     #cant be used to set any attribute
#     def email(self, string):
#         print("Setting now...")
#         #self.midname=string
#         names = string.split("@")[0]
#         self.fname,self.lname = names.split(".")[0],names.split(".")[1]
#         # self.lname = names.split(".")[1]
#
#
#     @email.deleter
#     def email(self):
#         print("deleteing now\n")
#         self.fname = None
#         self.lname = None
#
#
#
#
# hindustani_supporter = Employee("Hindustani", "Supporter")
# # nikhil_raj_pandey = Employee("Nikhil", "Raj")
#
# print(hindustani_supporter.email)
#
# hindustani_supporter.fname = "US"
#
# print(hindustani_supporter.email)
# hindustani_supporter.email = "this.that@codewithharry.com"
# print(hindustani_supporter.email)
# print("after changing email\n")
# print(hindustani_supporter.fname)
# print(hindustani_supporter.lname)
# del hindustani_supporter.email
# print(hindustani_supporter.email)
#
#
# print(hindustani_supporter.midname)
# print("before ks\n")
# hindustani_supporter.mname = "ks"
# print("after changing\n")
# print(hindustani_supporter.midname)
# del hindustani_supporter.mname
# print("after deleting mname\n")
# print(hindustani_supporter.mname)


# --------Library Managemnet

# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


# dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input
'''
class Library:
    lend = {}


    def __init__(self, name, args):
        self.name = name
        self.list = args
        #self.avail = args
        self.checkval=3

    # def update(self, bname):
    #     print(bname)

    def lend_book(self,cname,bname):
        if self.checkval==3:
            avail={}
        check=0
        print(self.checkval)
        print("before checkval condition\n")
        if self.checkval==4:
            print("entering checkval condition\n")
            print(avail.items(),"checking avail items\n")#failing here
            print(bname,"checking bname")
            self.checkval=4
            for self.cname,self.bname in avail.items():
                if cname in avail.items() and bname in avail.items():
                    print("you have already availed\n")
                    check=1
            print(check,"check value\n")
            print(avail,"dict list value to check if availed")
        if check==0:
            if self.list.get(bname)==0:
                print(f"books not available")
            else:
                self.checkval=4
                d2={cname:bname}
                avail.update(d2)
                print(avail.items(),"checking avail\n")
                print(self.list.get(bname))
                if self.list.get(bname)>=1:
                     count=self.list.get(bname)-1
                     print(f"\nBook {bname} availed by {cname} Sucessfully")
                     self.list[bname]=count

        print("status")
        print(self.list)


    def add_books(self, args):
        self.list.update(args)
        print("books added sucessfully\n")

    def display_all_books(self):
        print("available books are\n")
        for i in self.list:
            print(i)

    @classmethod
    def display_avail_books(cls):
        print("available books are\n")
        for i in cls.avail:
            print(i, "\n")

    @classmethod
    def return_book(cls, bname, cname):
        cls.avail.append(bname)
        del cls.lend[bname]
        print(f"\n{bname} book returned successfully by {cname}")



lst = ['Rich Dad Poor Dad', 'Chanakya Neti', 'Bhagwat Gita', 'Chicken Soup for Chicken Soul',
       'How to win friends and influence people']
d = {
    'Rich Dad Poor Dad': 2,
    'Chanakya Neti': 2,
    'Bhagwat Gita': 1,
    'Chicken Soup for Chicken Soul': 1,
    'How to win friends and influence people': 1

}
# print(d.get('Chanakya Neti'))
L = Library("mylib", d)
# L.avail=lst
# print(L.avail)
# L.avail.remove('a')
# print(L.avail)
L.display_all_books()
L.lend_book("Sanketh", 'Chanakya Neti')
L.lend_book("Sanketh", 'Chanakya Neti')
#L.lend_book("Vishal", 'Chanakya Neti')
#L.lend_book("Vishal", 'Chanakya Neti')

# print(L.lend)
# L.lend_book("Vishal", 'Chanakya Neti')
# L.return_book("Chanakya Neti", "Sanketh")
# L.lend_book("Vishal", 'Chanakya Neti')

'''


#new lib management
# import  datetime
# def getdate():
#     now = datetime.datetime.now()
#     now = now.strftime("%d-%B")
#     return  now
# #
# class Library:
#     def __init__(self,name):
#         self.name=name
#         self.lst={}
#         self.id=100
#         with open("BookList.txt") as b:
#             content=b.readlines()
#         for line in content:
#            if line.__contains__("\n"):
#                self.lst.update({str(self.id):{"BookTitle": line[0:len(line)-2],
#                                   "Lend Date":getdate(),
#                                   "LenderName":"",
#                                   "Count":int(line[-2])}})
#            else:
#               self.lst.update({str(self.id): {"BookTitle": line[0:len(line) - 1],
#                                   "Lend Date": getdate(),
#                                   "LenderName": "",
#                                   "Count": int(line[-1])}})
#            self.id += 1
#
#
#
#
#
#     def lend_books(self,name,choice):
#          self.cname=name
#          self.bid=choice
#          print(self.lst)
#          if self.lst[self.bid]['Count']==0:
#             #print(self.lst[choice]["BookTitle"]+"is not available\n")
#             print(f"{self.lst[choice]['BookTitle']} is not available\n")
#             print(f"Book already availed by {self.lst[choice]['LenderName']} on {self.lst[choice]['Lend Date']}")
#          else:
#             count=self.lst[self.bid]['Count']-1
#             self.lst[self.bid]['Count']=count
#             self.lst[self.bid]["Lend Date"]=getdate()
#             self.lst[self.bid]["LenderName"]=self.cname
#             print("Book issues sucessfully\n")
#
#          print("upated!!")
#          print(self.lst)
#
#     def add_books(self,no_of_books,name):
#         self.no_of_books=no_of_books#check if we need to initialize name as self.name
#         self.name=name
#         book_no = 1
#         # print((self.no_of_books + 1) > 1)
#         # print(self.id)
#         # print(self.lst)
#         while self.no_of_books:
#             print(f"Book No# {book_no}")
#             book_name = input("Book Title?\n")
#             count = int(input("Number of copies to be added?"))
#             print(self.id)
#             print(type(self.id))
#             print(str(self.id))
#             book_no += 1
#             self.lst.update({str(self.id): {"BookTitle": book_name, "Lend Date": getdate(),
#                                 "LenderName": "NA", "DonorName": self.name, "Count": count}})
#             self.no_of_books -= 1
#             self.id+=1
#         # print(self.lst)
#         with open("updated_list.txt", "a") as f:
#             f.write(str(self.lst))
#
#
#     def display_avail_books(self):
#         book_no=1
#         for book in self.lst:
#             if self.lst[book]["Count"]!=0:
#                 print(f"{book_no} --> {self.lst[book]['BookTitle']}")
#                 book_no+=1
#
#     def display_all_books(self):
#         book_no=1
#         for book in self.lst:
#                 print(f"{book_no} --> {self.lst[book]['BookTitle']}")
#                 book_no+=1
# #
# #
#
#     def return_books(self,name,bid):
#         self.name=name
#         self.bid=bid
#         if self.lst[self.bid]['LenderName']==self.name:
#             self.lst[self.bid]['Count']+=1
#             self.lst[self.bid]['LenderName']=''
#             print(f"{self.lst[bid]['BookTitle']} returned sucessfully!!\n")
#         else:
#             print(f"{self.bid} is not availed by you!!")
# #

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
#print(i[-2] print the character @ -2 index
# for i in content:
#     #print(i.find("\n"))#15,16,22
#     if i.__contains__("\n"):
#         print(i[-2],i[0:len(i)-2],"\n")
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
#     if line.__contains__("\n"):
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

# name=input("Your Name?")
# #choice=input("Please enter Book ID")
# lib1=Library("MyLib")
# while 1:
#     print(f"{name}  logged in\n")
#     key_input=input("What to do? q for quit")
#
#     if key_input.lower()=="l":
#         choice = input("Please enter Book ID")
#         lib1.lend_books(name,choice)
#     elif key_input.lower()=="a":
#         # add books function
#         no_of_books = int(input("Number of Books?\n"))  # sample 3
#         #name = input("Your Name")
#         lib1.add_books(no_of_books,name)
#
#     elif key_input.lower()=="d":
#         display_choice=input("Display Only Available?Y/N")
#         if display_choice=="y":
#             lib1.display_avail_books()
#         else:
#             lib1.display_all_books()
#     elif key_input.lower()=="o":
#         print(f"{name} logged off")
#         name=input("Next Customer Login Name")
#     elif key_input.lower()=="r":
#         book_choice=input("Enter Book id to return\n")
#         lib1.return_books(name,book_choice)
#     elif key_input.lower()=="q":
#         print("Thank you")
#         break
# string="Chanakya Neti 1\n"
# another="Bhagwat Gita 2"
# length=len(string)
# print(string[-2])
# print(another[-1])

# import pyttsx3
# import PyPDF2
# import os
#
# os.chdir("C://Users/SANKETH/PycharmProjects/Practice/Files")
# # path=os.chdir("C://Users/SANKETH/PycharmProjects/Practice/Files")
#
# book=open("cn.pdf","rb")
# pdf=PyPDF2.PdfFileReader(book)
# print(pdf.numPages)
# speak=pyttsx3.init()
# rate = speak.getProperty('rate')   # getting details of current speaking rate
# print (rate)
# rate=speak.setProperty('rate',125)
# voices = speak.getProperty('voices')
# speak.setProperty('voice', voices[1].id)
# # speak.say("Hellow Sanketh")
# # speak.runAndWait()
# for page in range(1,47):
#     pageno=pdf.getPage(page)
#     text=pageno.extractText()
#     speak.say(text)
#     speak.runAndWait()
import os 
from pygame import mixer

import time
# from playsound import playsound

path=os.path.join(os.getcwd(),"Files/tests")
os.chdir(path)
print(os.listdir())
# counter=0
# file=open("sample.txt")
# Content = file.read() 
# CoList = Content.split("\n") 
# # text=""    
# for i in CoList: 
#     if i: 
#         counter += 1
# print(f" total lines is   {counter}")
# content=""
# count=0
# file=open("check.txt","a")
# with open("logs.txt") as f:
#     text=f.readlines()
#     print(type(text))
#     # text=list(text)
#     text.remove("\n")
#     for word in text:
#         if count%4!=0:
#             content+=word
#             file.write(word)
#             count+=1
            
        # file.write("\n")
    # text=str(text)
    # samp=text.replace("\n")
    # file.write(str(text))
    
mixer.init()
import pyttsx3
# engine = pyttsx3.init()
# engine.save_to_file('Hello World' , 'test1.mp3')
# engine.runAndWait()

# for i in range(5,76,4):
#     mixer.music.load(f"welcome{i}.mp3")
#     mixer.music.play()
#     time.sleep((18))
# mixer.music.load("test1.mp3")
# mixer.music.play() 
# time.sleep(5) 
    
# playsound("welcome5.mp3")  
playsound.playsound("test1.mp3") 

