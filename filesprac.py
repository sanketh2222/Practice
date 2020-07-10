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


#output
# func 20
#my func 70
# my func 20
#70


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
count=1



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

#------------Polymorphysim example plus operatore behaves differently based on parameters

# print(5+6)
# print("5" + "6")

# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

#----------------overriding
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


#-- Diamond shape inheritence problem solved by python

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
#first perference is given to __str and next goes for __repr
#cntl+D duplicates a line
# print(e1.name)

#serach for mapping operators for functions in python for operator overloading
#e.g adding salaries of 2 classes

#---abstract method

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

#--------------getters and setters
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


#--------Library Managemnet

# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input
# class Library:
#     lend={}
#     @classmethod
#     def __init__(self,name,args):
#         self.name=name
#         self.list=args
#         self.avail=args
#
#
#     def update(self,bname):
#         print(bname)
#
#
#
#     @classmethod
#     def lend_book(cls,cname,bname):
#         if bname in cls.lend.keys():
#             print(f"SORRY {cname}\n{bname} is already taken by {cls.lend[bname]}\nWe have other books for you")
#
#         # print(cls.avail)
#         #cls.update(bname)
#         else:
#             cls.lend[bname] = cname  # update dict
#             print(f"\n{bname} Book availed successfully by {cname}!!")
#
#         # cls.avail.remove(f"{bname}")
#
#
#
#     def add_books(self,args):
#         self.list.append(args)
#         print("books added sucessfully\n")
#
#     def display_all_books(self):
#         print("available books are\n")
#         for i in self.list:
#             print(i)
#
#     @classmethod
#     def display_avail_books(cls):
#         print("available books are\n")
#         for i in cls.avail:
#             print(i,"\n")
#
#
#     @classmethod
#     def return_book(cls,bname,cname):
#         cls.avail.append(bname)
#         del cls.lend[bname]
#         print(f"\n{bname} book returned successfully by {cname}")
#
#
#
#
#
# lst=['Rich Dad Poor Dad','Chanakya Neti','Bhagwat Gita','Chicken Soup for Chicken Soul',
#      'How to win friends and influence people']
# d={
# 'Rich Dad Poor Dad':2,
# 'Chanakya Neti':1,
# 'Bhagwat Gita':1,
# 'Chicken Soup for Chicken Soul':1,
# 'How to win friends and influence people':1
#
# }
# L=Library("mylib",lst)
# # L.avail=lst
# print(L.avail)
# # L.avail.remove('a')
# # print(L.avail)
# L.display_all_books()
# L.lend_book("Sanketh",'Chanakya Neti')
# # print(L.lend)
# L.lend_book("Vishal",'Chanakya Neti')
# L.return_book("Chanakya Neti","Sanketh")
# L.lend_book("Vishal",'Chanakya Neti')
# # print(type(L.list))
# # L.add_books("Book1")
# # print(L.list)
# # d={}
# # print(type(d))
# # print(L.list)
# # print(L.name)
#
#

string="hello"
# for i in dir(string):
#     print(i)
# import random
# import  inspect
# class Employee:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         self.email = f"{fname}.{lname}@codewithharry.com"
#         self.midname=f"{fname}"
#
#
# # for key, data in inspect.getmembers(random, inspect.isclass):
# #     print('{} : {!r}'.format(key, data))
#
# for k,v in inspect.getmembers(Employee):
#       if k.startswith('__')==False:print (k,v)


# del hindustani_supporter.email
# print(hindustani_supporter.email)
# hindustani_supporter.email = "Harry.Perry@codewithharry.com"
# print(hindustani_supporter.email)
import datetime

# def getdate():
#     now = datetime.datetime.now()
#     now = now.strftime("%d-%B")
#     return  now
#
# with open("BookList.txt") as b:
#     content=b.readlines()
#
# print(content)
# # print(type(content))
# for i in content:
#     #print(i.find("\n"))#15,16,22
#     if i.__contains__("\n"):
#         print(i[-2],i[0:len(i)-2],"\n")
#         # print(i[0:len(i)-2])
#     else:
#       print(i[-1],i[0:len(i)-1])
#       # print(i[0:len(i)-1])
#
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
#                            "LenderName":"NA",
#                            "DonorName":"NA",
#                             "Count":int(line[-2])}})
#     else:
#         d.update({str(id): {"BookTitle": line[0:len(line) - 1],
#                             "Lend Date": getdate(),
#                             "LenderName":"NA",
#                             "DonorName":"NA",
#                             "Count": int(line[-1])}})
#     id += 1
#
# print(d)
# with open("dict.txt","a") as f:
#     f.write(str(d))
# print(d['101']['Count'])
# print(type(d['101']['Count']))

# print(id,"Id no\n")
#
# #add books function
# no_of_books=int(input("Number of Books?\n"))#sample 3
# name=input("Your Name")
# book_no=0
# print((no_of_books+1)>1)
# while no_of_books:
#     print(f"Book No# {book_no}")
#     book_name=input("Book Title?\n")
#     count=int(input("Number of copies to be added?"))
#     book_no+=1
#     d.update({str(id):{"BookTitle":book_name,"Lend Date":getdate(),
#                            "LenderName":"NA","DonorName":name,"Count":count}})
#     no_of_books-=1
#     id += 1
#
# with open("updated_list.txt","a") as f:
#     f.write(str(d))

#display available function
d={
   '100': {'BookTitle': 'Chanakya Neti ', 'Lend Date': '07-July', 'Count': 1},
   '101': {'BookTitle': 'Bhagwat Gita   ', 'Lend Date': '07-July', 'Count': 2},
   '102': {'BookTitle': 'Think and grow rich  ', 'Lend Date': '07-July', 'Count': 1},
   '103': {'BookTitle': 'Chicken Soup for Chicken Soul ', 'Lend Date': '07-July', 'Count': 1}
}

for i,j in d.items():
    print(d[i]['Count'])
    #print(type(i))



