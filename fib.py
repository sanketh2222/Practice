# def fib(n):
#     val=0
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#        return  fib(n-1)+fib(n-2)
#
# ans=fib(3)
# print(ans)
#import pickle
# from threading import Timer
# import threading
#
# timeout = 5
#
# # t = Timer(timeout, print, ['Sorry, times up'])
# # t.start()
# # prompt = "You have %d seconds to choose the correct answer...\n" % timeout
# # answer = input(prompt)
# # t.cancel()
#
#
#
#
# # try:
# #     answer = input_with_timeout(prompt, 10)
# # except TimeoutExpired:
# #     print('Sorry, times up')
# # else:
# #     print('Got %r' % answer)
#
#
# #ans="n"
# def water_input():
#     def answer():
#         print("no choice")
#
#
#     timeout=2
#     t = Timer(timeout,answer)
#     t.start()
#     prompt = "Drank? Y/N"
#     answer = input(prompt)
#     t.cancel()
#     return answer
#
#
#
# # ans=water_input()
# # if ans=="y":
# #     print("here",ans)
# # else:
# #     print("not entered")
# #need to make use of decorators
# def eye_input():
#     timeout=5
#     t = Timer(timeout, print, ["n"])
#     t.start()
#     prompt = "Done? Y/N"
#     answer = input(prompt)
#     t.cancel()
#     return answer
# ans="y"
# def answer():
#     ans="n"
#     print("timeout")
#     return ans
#
# t= Timer(3,answer)# call the answer function after20 seconds
# t.start()
# if ans=="y":
#     print(ans)
#     try:
#         ans=input("enter something")
#     except TimeoutError:
#         print("timedout")
#     print("cant proceed without enetering")
#     print(ans)
# t.cancel()
# print("you enetered")
import  time
# import  datetime
# def getdate():
#     import datetime
#     return time.asctime(time.localtime(time.time()))
# time.asctime(time.localtime(time.time()))


# datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
# water2 = datetime.datetime.now()
# diff = datetime.datetime.strptime(str(water2), datetimeFormat)
# print(diff.hour)
# print(diff.minute)
# def check_time():
#     while 1:
#         #print("in the main while loop\n")
#         water2 = datetime.datetime.now()
#         diff = datetime.datetime.strptime(str(water2), datetimeFormat)
#         if (diff.hour==16 and diff.minute==29 and diff.second==0):
#             print(f" time is 4 pm {getdate()} exiting the program")
#             exit(0)
#         else:
#             pass





# first=water_input()
# print("here",first.lower())

#
# #import pickle
# from  operator import itemgetter
from pygame import mixer
import datetime
import time
from datetime import timedelta
water_qty=0
def getdate():
    import datetime
    return time.asctime(time.localtime(time.time()))
# time.asctime(time.localtime(time.time()))


datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
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
mixer.init()

# Loading the song
# mixer.music.load("water.mp3")
# mixer.music.load("eye.mp3")

# Setting the volume
mixer.music.set_volume(0.7)
now=datetime.datetime.now()
now=now.strftime("%d-%B")
def water():
    water = datetime.datetime.now()
    #water2 = datetime.datetime.now()
    diff = datetime.datetime.strptime(str(water), datetimeFormat)
    print(diff.minute, diff.second)
    if (diff.hour == 2 and diff.minute >=57 and diff.second >= 0):
        print(f" time is 4 pm {getdate()} exiting the program")
        print(f"total water consumed for {diff.day} is {water_qty}")
        with open("HealthLog.txt", "a") as water1:
            Content = f"\n\ntotal water consumed for {now} is {water_qty}\n"
            water1.write(Content)
        exit(0)
    else:
        time.sleep(30)#20 minutes --> 1200
        print(f"Entering else condition @{diff.minute} and {diff.second}")
        water2 = datetime.datetime.now()
        diff = datetime.datetime.strptime(str(water2), datetimeFormat) \
               - datetime.datetime.strptime(str(water), datetimeFormat)
    
        print(diff.seconds)
        return  diff.seconds


def phy():
    water = datetime.datetime.now()
    # water2 = datetime.datetime.now()
    diff = datetime.datetime.strptime(str(water), datetimeFormat)
    print(diff.minute, diff.second)
    if (diff.hour == 2 and diff.minute >= 57 and diff.second >= 0):
        print(f" time is 4 pm {getdate()} exiting the program")
        print(f"total water consumed for {diff.day} is {water_qty}")
        with open("HealthLog.txt", "a") as water1:
            Content = f"\n\ntotal water consumed for {now} is {water_qty}\n"
            water1.write(Content)
        exit(0)
    else:
        time.sleep(150)  # 15 minutes --> 900 with dependency
        print(f"Entering else condition @{diff.minute} and {diff.second}")
        water2 = datetime.datetime.now()
        diff = datetime.datetime.strptime(str(water2), datetimeFormat) \
               - datetime.datetime.strptime(str(water), datetimeFormat)

        print(diff.seconds)
        return diff.seconds

def eye():
    water = datetime.datetime.now()
    #water2 = datetime.datetime.now()
    
    diff = datetime.datetime.strptime(str(water), datetimeFormat)
    print(diff.minute,diff.second)
    if (diff.hour == 2 and diff.minute >=57 and diff.second >= 0):
        print(f" time is 4 pm {getdate()} exiting the program")
        # print(f"total water consumed for {diff.day} is {water_qty}")
        with open("HealthLog.txt", "a") as water1:
            Content = f"\n\ntotal water consumed for {now} is {water_qty}\n"
            water1.write(Content)
        exit(0)
    else:
        time.sleep(70)  #10 minutes with dependency of water function--> value 600
        water2 = datetime.datetime.now()
        diff = datetime.datetime.strptime(str(water2), datetimeFormat) \
               - datetime.datetime.strptime(str(water), datetimeFormat)
    
        print(diff.seconds)
        return diff.seconds


class once:
    count=1
    start=1
    def __init__(self):
        self.count = 1


var = once.count
start=once.start
print(var)
check=0

while 1:
    water2 = datetime.datetime.now()
    diff = datetime.datetime.strptime(str(water2), datetimeFormat)
    # if (diff.hour == 2 and diff.minute >=20 and diff.second >= 0):
    #     print(f" time is 4 pm {getdate()} exiting the program\n")
    #     print(f"total water consumed for {now} is {water_qty}")
    #     exit(0)
    if start==1:
        start=2
        print(f"\nStarted at {diff.minute} minutes and {diff.second} \n")

    if water_qty>=0.6:
        check=1
        
    wat=water()
    print(check,"before condition\n")
    if wat==30 and check==0:
        print("water condition")
        mixer.music.load("water.mp3")
        mixer.music.play(-1)
        first=input("Drank?Y/N")
        if first.lower()=="y":
            mixer.music.stop()
            water_qty=water_qty+0.2
            with open("HealthLog.txt","a") as water1:
                if var==1:
                    var=2
                    Content=f"\nLogs for {now}\nDrank water at [{getdate()}] \n"
                    water1.write(Content)
                else:
                    Content=f"Drank water at [{getdate()}] \n"
                    water1.write(Content)
        elif first.lower()=="n":
            mixer.music.stop()


    ey=eye()
    if ey==70:
        if check==1:
            time.sleep(30)# include the dependency of water once criteria of water is met value--> 1200
        print("eye confition")
        mixer.music.load("eye.mp3")
        mixer.music.play(-1)
        second = input("Done?Y/N")
        if second.lower()=="y":
            mixer.music.stop()
            with open("HealthLog.txt","a") as i1:
                if var==1:
                    var=2
                    Content = f"\nLog for {now}\nEye exercise done  at [{getdate()}]\n"
                    i1.write(Content)
                else:
                    Content=f"Eye exercise done  at [{getdate()}]\n"
                    i1.write(Content)
        elif second.lower()=="n":
            mixer.music.stop()

    ph=phy()
    if ph == 150:
        if check == 1:
            time.sleep(30)  # include the dependency of water once criteria of water is met value--> 1200
        print("physical confition")
        mixer.music.load("phy.mp3")
        mixer.music.play(-1)
        second = input("Will do?Y/N")
        if second.lower() == "y":
            mixer.music.stop()
            with open("HealthLog.txt", "a") as i1:
                if var == 1:
                    var = 2
                    Content = f"\nLog for {now}\nEye exercise done  at [{getdate()}]\n"
                    i1.write(Content)
                else:
                    Content = f"Eye exercise done  at [{getdate()}]\n"
                    i1.write(Content)
        elif second.lower() == "n":
            mixer.music.stop()






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
#     f.seek(50)
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