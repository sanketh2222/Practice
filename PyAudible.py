import pyttsx3
import PyPDF2
import os

os.chdir("C://Users/SANKETH/PycharmProjects/Practice/Files")
# path=os.chdir("C://Users/SANKETH/PycharmProjects/Practice/Files")
b=input("which book do you want to read today?")
print(f"reading {b}.pdf for you\n")
book=open(f"{b}.pdf","rb")

pdf=PyPDF2.PdfFileReader(book)
print(pdf.numPages)
speak=pyttsx3.init()
rate = speak.getProperty('rate')   # getting details of current speaking rate
print (rate)
rate=speak.setProperty('rate',125) #seting up the voice rate
voices = speak.getProperty('voices')
speak.setProperty('voice', voices[1].id)# change to female voice 0--> Male 1 --> Female
# speak.say("Hellow Sanketh")
# speak.runAndWait()
for page in range(1,47):
    pageno=pdf.getPage(page)
    text=pageno.extractText()
    speak.say(text)
    speak.runAndWait()