import pyttsx3
import PyPDF2
import os
from threading import Thread
from pygame import mixer
from gtts import gTTS 
from time import sleep
from io import BytesIO

path=os.path.join(os.getcwd(),"Files")
os.chdir(path)
print(os.listdir())
# path=os.chdir("C://Users/SANKETH/PycharmProjects/Practice/Files")
b=input("which book do you want to read today?")
print(f"reading {b}.pdf for you\n")
book=open(f"{b}.pdf","rb")

mixer.init()

# pdf=PyPDF2.PdfFileReader(book)
# print(pdf.numPages)
# size=pdf.numPages
# speak=pyttsx3.init()
# rate = speak.getProperty('rate')   # getting details of current speaking rate
# print ("current rate is ",rate)
# rate=speak.setProperty('rate',125) #seting up the voice rate
# voices = speak.getProperty('voices')
# speak.setProperty('voice', voices[1].id)# change to female voice 0--> Male 1 --> Female
# # speak.say("Hellow Sanketh")
# speak.runAndWait()

def t():
            # time.sleep(10)  # wait for 5 seconds for input
            # if second == 'waiting...':
            #     typewrite('n')
            #     typewrite(['enter'])
        print("reading from a thread")
        for page in range(0,size):
            pageno=pdf.getPage(page)
            print("page is ",page)
            print("pageno is ",pageno)
            text=pageno.extractText()
            speak.save_to_file(str(text) , 'test.mp3')
            print("saved file")
        #     speak.say(text)
            print("saying")
        #     with open("logs.txt","a") as l:
        #         l.write(str(page))
        #     speak.runAndWait()


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
#         b=input("enter choice")
def onStart(name):
       print('starting', name)
def onWord(name, location, length):
   print('word', name, location, length)
def onEnd(name, completed):
   print('finishing', name, completed)
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()
# print("entering atomic")
# for page in range(0,1):
#         pageno=pdf.getPage(page)
#         print("page is ",page)
#         # print("pageno is ",pageno)
#         text=pageno.extractText()
#         with open("logs1.txt","a") as f:
#                 f.writelines(text)
        # speak.say(text)
        
        # myobj = gTTS(text=text, lang='en', slow=False) 
        # myobj.save(f"welcome{page}.mp3")
        # print("saying")
        # mixer.music.load(f"welcome{page}.mp3")
        # mixer.music.play()
        # sleep(3)
        
        # mixer.music.load("eye.mp3")
        # speak.runAndWait()
    