import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import datetime
import time
import requests
import json
import smtplib, ssl
import re


mail_pattern=re.compile(r".*mail.*")
news_pattern=re.compile(r".*news.*")
weather_pattern=re.compile(r".*weather.*")
time_pattern=re.compile(r".*time.*")


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 172)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # change to female voice 0--> Male 1 --> Female



mail_pattern=re.compile(r".*mail.*")
news_pattern=re.compile(r".*news.*")
weather_pattern=re.compile(r".*weather.*")
time_pattern=re.compile(r".*time.*")
wiki_search=re.compile(r".*who is.*")
wiki_search1=re.compile(r".*wikipedia.*")

def speak(text):
    engine.say(text)
    engine.runAndWait()

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

with open("credentials.txt") as f:
    user_name = f.readline().strip()  # remove strailing spaces from string
    password = f.readline()


def mail(to, sub, msg):
    mail_dict = {
        "sanket": "ssankethboss061@gmail.com",
        "elon musk": "sankeths94@gmail.com"
    }
    rec = mail_dict.get(to)
    # print(to)
    # print(sub)
    # print(msg)
    # print(user_name)
    # print(len(user_name))
    # user_name = "sherlock.holmes8907891"

    # print(len(user_name))
    # print(len(password))

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:

        speak("are you sure you want to send the mail")
        choice=Listen()
        if choice.lower()=="yes":
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(user_name, password)
            # TODO: Send email here
            server.sendmail(user_name, rec, f"Subject: {sub}\n\n {msg}")
            print(f"mail sent to {to} sucessfully! ")
            speak(f"mail sent to {to} sucessfully! ")
            server.quit()
        else:
            speak("ok,i am cancelling the mail")


    except Exception as e:
        # Print any error messages to stdout
        print(e)




class count:
    def __init__(self):
        times = 1





def weather(city):
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=134b6fda987e9204b5cea01d566a247a")
    weather_data = json.loads(response.text)
    print(weather_data)
    speak(f"its {weather_data['weather'][0]['description']} in {city}")
    speak(f"feels like {round(int(weather_data['main']['temp_min']) - 273.15)}  degrees in {city}")
    speak(f"humidity is  {weather_data['main']['humidity']}  percent")
    speak(f"wind speed is  {weather_data['wind']['speed']}")





def greet_user():
    speak("Whats Your Name?")
    name = Listen()
    while name == "None":
        name = Listen()
    print(type(name))
    name = name.split(sep=" ")
    print(type(name))
    print(name)
    name = name[len(name) - 1]
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
    # print(type(con1))
    print(con1)
    if head1!=None:
        speak(head1)
        print(url)


    if con1!=None:
        res = con1.index(r"[")
        # removing junk contents
        if r"[" in con1:
            con1 = con1[0:res]
        print(con1)
        speak(con1)





name = greet_user()
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
    query = Listen()
    while query == "None":
        query = Listen()
    print(query)
    print("before condition")
    if "the time" in query:
        now = datetime.datetime.now()
        now = now.strftime("%I:%M:%S %p")
        speak(f"the time is {now}")

    elif "wikipedia" or "who is" in query.lower():
        if "wikipedia" in query:
            query.replace("wikipedia", "")
        else:
            query = query.replace("who is", "").strip()
        try:
            speak(wikipedia.summary(query, sentences=2))
            print(wikipedia.summary(query, sentences=2))
        except wikipedia.exceptions.PageError as e:
            print("Wiki not found")

    elif "browse" in query:
        query = query.split(sep=" ")
        index = query.index("browse")
        content = query[index + 1]
        print(content)
        if content.lower() == "youtube":
            # https://www.youtube.com/results?search_query=python
            speak("What to watch on youtue?")
            content = Listen()
            webbrowser.open(f"https://www.youtube.com/results?search_query={content}")
        else:
            webbrowser.open(f"http://{content}.com")

    elif "stop" in query:
        print("breaking\n")
        exit(0)

    elif bool(news_pattern.findall(query)):
        news(0)
        speak("Next Up\n")
        news(1)
        speak("Next Up\n")
        news(2)

    # elif "the weather like" in query:
    #     proc = list(query.split(" "))
    #     print(proc)
    #     print(len(proc))
    #     city = proc[len(proc) - 1]
    #     print(city)
    #     weather(city)
    #     continue
        
    elif bool(weather_pattern.findall(query)):
        speak("which city?")
        city=Listen().lower()
        print(city)
        weather(city)

    elif bool(mail_pattern.findall(query)):
        speak("to whom?")
        print("to whom?")
        to = Listen().lower()

        speak("whats the subject?")
        print("whats the subject?")
        sub = Listen()
        if "cancel" in sub.lower():
            speak("ok cancelling the mail")
            continue
        speak("say the message that you want to send")
        print("say the message that you want to send")
        msg = Listen()
        mail(to, sub, msg)

    else:
        speak("I didnt catch you there!!")

#
# text="hello i am Zira!, how can i help you"
# speak(text)






