import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import datetime
import time
import requests
import json

engine=pyttsx3.init('sapi5')
engine.setProperty('rate',172)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)# change to female voice 0--> Male 1 --> Female

class count:
    def __init__(self):
        times=1

def speak(text):
    engine.say(text)
    engine.runAndWait()

def weather(city):
    response=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=134b6fda987e9204b5cea01d566a247a")
    weather_data=json.loads(response.text)
    print(weather_data)
    speak(f"its {weather_data['weather'][0]['description']} in {city}")
    speak(f"feels like {round(int(weather_data['main']['temp_min'])-273.15)}  degrees in {city}")
    speak(f"humidity is  {weather_data['main']['humidity']}  percent")
    speak(f"wind speed is  {weather_data['wind']['speed']}")


def Listen():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak now")
        audio=r1.listen(source)#opens/starts the microphone
        try:
            text=r1.recognize_google(audio,language="en-in")# get the text or content that you just spoke
        except Exception as e:
            print("I did not hear that")
            return "None"
            # speak("i did not hear that")
        print(text)
        return text



def greet_user():
    speak("Whats Your Name?")
    name=Listen()
    while name=="None":
        name=Listen()
    print(type(name))
    name=name.split(sep=" ")
    print(type(name))
    print(name)
    name=name[len(name)-1]
    speak(f"hello {name} how may i help you?")
    return name

def news(count):
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=0f984866c30c4880967285aa463f328e')
    # c= count()
    # print()
    response = requests.get(url)
    # f=open("file1.txt","a")
    # f.write(str(response.json()))
    news = response.json()
    # print(response.json())
    print(news['articles'][count]['description'])
    head1 = news['articles'][count]['description']
    con1 = news['articles'][count]['content']
    url = news['articles'][count]['url']
    res = con1.index(r"[")
    # removing junk contents
    if r"[" in con1:
        con1 = con1[0:res]
    speak(head1)
    speak(con1)
    print(url)

name=greet_user()
# print(name)


while 1:
    # r1=sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("speak now")
    #     audio=r1.listen(source)#opens/starts the microphone
    #     try:
    #         query=r1.recognize_google(audio)# get the text or content that you just spoke
    #     except Exception as e:
    #         print("did not hear that")
    #         return
    # print(query)
    # print(name)
    query=Listen()
    while query=="None":
        query=Listen()
    print(query)
    print("before condition")
    if "the time" in query:
        now = datetime.datetime.now()
        now = now.strftime("%I:%M:%S %p")
        speak(f"the time is {now}")

    elif "wikipedia" in query.lower():
        query.replace("wikipedia","")
        try:
            speak(wikipedia.summary(query,sentences=2))
            print(wikipedia.summary(query,sentences=2))
        except wikipedia.exceptions.PageError as e:
            print("Wiki not found")

    elif "browse" in query:
        query=query.split(sep=" ")
        index=query.index("browse")
        content=query[index+1]
        print(content)
        if content.lower()=="youtube":
            #https://www.youtube.com/results?search_query=python
            speak("What to watch on youtue?")
            content=Listen()
            webbrowser.open(f"https://www.youtube.com/results?search_query={content}")
        else:
            webbrowser.open(f"http://{content}.com")

    elif "stop" in query:
        print("breaking\n")
        break

    elif "read the news" in query:
        news(0)
        speak("Next Up\n")
        news(1)
        speak("Next Up\n")
        news(2)

    elif "how is the weather like" in query:
        proc=list(query.split(" "))
        print(proc)
        print(len(proc))
        city=proc[len(proc)-1]
        print(city)
        weather(city)

    else:
        speak("I didnt catch you there!!")

#
# text="hello i am Zira!, how can i help you"
# speak(text)






