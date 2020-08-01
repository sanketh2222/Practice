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

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 172)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # change to female voice 0--> Male 1 --> Female

def speak(text):
    engine.say(text)
    engine.runAndWait()



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
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(user_name, password)
        # TODO: Send email here
        server.sendmail(user_name, rec, f"Subject: {sub}\n\n {msg}")
        print(f"mail sent to {to} sucessfully! ")
        speak(f"mail sent to {to} sucessfully! ")

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


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
    res = con1.index(r"[")
    # removing junk contents
    if r"[" in con1:
        con1 = con1[0:res]
    speak(head1)
    speak(con1)
    print(url)


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

    elif "wikipedia" in query.lower():
        query.replace("wikipedia", "")
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
        break

    elif "read the news" in query:
        news(0)
        speak("Next Up\n")
        news(1)
        speak("Next Up\n")
        news(2)

    elif "the weather like" in query:
        proc = list(query.split(" "))
        print(proc)
        print(len(proc))
        city = proc[len(proc) - 1]
        print(city)
        weather(city)
        
    elif "weather" in query:
        speak("which city?")
        city=Listen().lower()
        print(city)
        weather(city)

    elif "send a mail" in query:
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






