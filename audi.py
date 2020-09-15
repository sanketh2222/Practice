# # Import the required module for text 
# # to speech conversion 
# import gtts
# import gtts
# from pygame import mixer
# import time

# # This module is imported so that we can 
# # play the converted audio 
# import os 


# path=os.path.join(os.getcwd(),"Files")
# os.chdir(path)
# print(os.listdir())


# mixer.init()
# # The text that you want to convert to audio 
# mytext = 'Welcome to geeksforgeeks!'

# # Language in which you want to convert 
# language = 'en'

# # Passing the text and language to the engine, 
# # here we have marked slow=False. Which tells 
# # the module that the converted audio should 
# # have a high speed 
# myobj = gtts.gTTS(text=mytext, lang=language, slow=False) 

# # Saving the converted audio in a mp3 file named 
# # welcome 
# # myobj.save("welcome.mp3") 
# for i in range(5):
#     mixer.music.load(f"welcome{i}.mp3")
#     mixer.music.set_volume(0.7)
#     mixer.music.play()
#     time.sleep(5)

# Playing the converted file 
# os.system("mpg321 welcome.mp3") 

import pyttsx3
import PyPDF2
import os
from threading import Thread
from pygame import mixer
from gtts import gTTS 
from time import sleep
import pyttsx3

path=os.path.join(os.getcwd(),"Files/tests")
os.chdir(path)
print(os.listdir())
# path=os.chdir("C://Users/SANKETH/PycharmProjects/Practice/Files")
# b=input("which book do you want to read today?")
# print(f"reading {b}.pdf for you\n")
# book=open(f"{b}.pdf","rb")

mixer.init()

speak=pyttsx3.init()
rate = speak.getProperty('rate')   # getting details of current speaking rate
print ("current rate is ",rate)
rate=speak.setProperty('rate',125) #seting up the voice rate
voices = speak.getProperty('voices')
speak.setProperty('voice', voices[1].id)# change to female voice 0--> Male 1 --> Female

# pdf=PyPDF2.PdfFileReader(book)
# print(pdf.numPages)
# size=pdf.numPages
# speak=pyttsx3.init()
# rate = speak.getProperty('rate')   # getting details of current speaking rate
# print ("current rate is ",rate)
# rate=speak.setProperty('rate',125) #seting up the voice rate
# voices = speak.getProperty('voices')
# speak.setProperty('voice', voices[1].id)# change to female voice 0--> Male 1 --> Female
# speak.say("Hellow Sanketh")
# speak.runAndWait()

# def t():
#             # time.sleep(10)  # wait for 5 seconds for input
#             # if second == 'waiting...':
#             #     typewrite('n')
#             #     typewrite(['enter'])
#         print("reading from a thread")
#         for page in range(0,size):
#             pageno=pdf.getPage(page)
#             print("page is ",page)
#             print("pageno is ",pageno)
#             text=pageno.extractText()
#             speak.say(text)
#             print("saying")
#             with open("logs.txt","a") as l:
#                 l.write(str(page))
#             speak.runAndWait()


# T = Thread(target=t)
# T.start()
# ch=input("waiting for inp.")   
# print(f" the choice is   {ch}")
# if ch=="e":
#     print("exiting")
#     exit(1)
#     print("exit done")
# # print("page is",page) 
        
# if b.__contains__("cn"):
#     print("entering cn")
#     # for page in range(1,46):
#     #     pageno=pdf.getPage(page)
#     # text=pageno.extractText()
#     # speak.say(text)
#     # speak.runAndWait()
#     for page in range(0,size):
#         # print("read next page?")
#         speak.say(f"read next page?")
#         choice=input("next page?")
#         pageno=pdf.getPage(page)
#         print("page is ",page)
#         print("pageno is ",pageno)
#         text=pageno.extractText()
#         speak.say(text)
#         print("saying")
#         with open("logs.txt","a") as l:
#                 l.write(str(page))
#         speak.runAndWait()
# else:
#     print("entering atomic")
#     for page in range(0,size):
#         pageno=pdf.getPage(page)
#         print("page is ",page)
#         print("pageno is ",pageno)
#         text=pageno.extractText()
#         speak.say(text)
#         print("saying")
#         speak.runAndWait()

print("entering atomic")
# for page in range(0,2):
#         pageno=pdf.getPage(page)
#         print("page is ",page)
#         # print("pageno is ",pageno)
#         text=pageno.extractText()
#         with open("logs.txt","a") as f:
#                 f.write(str(text))
#         # speak.say(text)
        
#         myobj = gTTS(text=text, lang='en', slow=True) 
#         myobj.save(f"welcome{page}.mp3")
#         print("saying")
#         mixer.music.load(f"welcome{page}.mp3")
#         mixer.music.play()
#         sleep(3)
        
        # mixer.music.load("eye.mp3")
        # speak.runAndWait()
# counter=0
# file=open("logs.txt")
# Content = file.read() 
# CoList = Content.split("\n") 
# text=""    
# for i in CoList: 
#     if i: 
#         counter += 1
# start=0
# print(f" total lines is   {counter}")          
# with open("logs.txt","r") as f:
#     for i in range(counter+1):
#         if i%4!=0:
#             text=text+f.readline()
#             # print(f" text is   {text}")
#             start=1
#         if start!=0 and i%4==0:
#              with open("test.txt","a") as t:
#                 t.write(str(text))   
#                 start=3
                
#         if start==3:
#             print(f" value of i is   {i}")   
#             myobj = gTTS(text=text, lang='en', slow=Truecontent=""
count=1
count2=0
start=0
content=""
file=open("check.txt","a")
with open("logs.txt") as f:
    text=f.readlines()
    print(type(text))
    # text=list(text)
    text.remove("\n")
    size=len(text)
    print("size of text is ",len(text))
    for word in text:
        # count+=1
        if count%4!=0:
            content+=word
        #     file.write(word)
            count+=1
        #     print(count)#75
            if count>size:
                    file.write(content)
                    myobj = gTTS(text=content, lang='en', slow=False) 
                    myobj.save(f"welcome{count}.mp3")
        #     if count>count2:
        #             file.write(content)
        # count+=1
        else:
                # print("entering else ")
                # count+=1
                content+=word
                count+=1
                count2=count#5,9,13,17
                # print(f" count is   {count}")#73
                
                file.write(content)
                myobj = gTTS(text=content, lang='en', slow=True) 
                myobj.save(f"welcome{count}.mp3")
                content=""
                
                # print(f" count is   {count}")
                # print(content)
                # myobj = gTTS(text=content, lang='en', slow=False) 
                # myobj.save(f"welcome{count}.mp3")
#             myobj.save(f"welcome{i}.mp3")
#             start=2
#             text=""
     
# for line in range(counter+1):
#     myobj.save(f"welcome{line}.mp3")
#     print("saying")
#     mixer.music.load(f"welcome{line}.mp3")
#     mixer.music.play()

# mixer.music.load(f"welcome40.mp3")
# mixer.music.play()
# sleep(5)