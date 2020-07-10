from pyautogui import typewrite
from threading import Thread
import time
from pygame import mixer
import datetime

datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'

mixer.init()
water_qty=0

def getdate():
    import datetime
    return time.asctime(time.localtime(time.time()))

# time.asctime(time.localtime(time.time()))

def water():
    water = datetime.datetime.now()
    # water2 = datetime.datetime.now()
    diff = datetime.datetime.strptime(str(water), datetimeFormat)
    print(diff.minute, diff.second)
    if (diff.hour == 21 and diff.minute >= 57 and diff.second >= 0):
        print(f" time is 4 pm {getdate()} exiting the program")
        #print(f"total water consumed for {diff.day} is {water_qty}")
        with open("HealthLog1.txt", "a") as water1:
            Content = f"\n\ntotal water consumed for {getdate()} is {water_qty}\n"
            water1.write(Content)
        exit(0)
    else:
        time.sleep(10)  # 20 minutes --> 1200
        print(f"Entering else condition @{diff.minute} and {diff.second}")
        water2 = datetime.datetime.now()
        diff = datetime.datetime.strptime(str(water2), datetimeFormat) \
               - datetime.datetime.strptime(str(water), datetimeFormat)

        print(diff.seconds)
        return diff.seconds


while 1:
    wat = water()
    if wat == 10:
        print("water condition")
        mixer.music.load("water.mp3")
        mixer.music.play()

        first = 'waiting...'


        def t():
            time.sleep(5)#wait for 5 seconds for input
            if first == 'waiting...':
                typewrite('n')
                typewrite(['enter'])


        T = Thread(target=t)
        T.start()

        first = input("Drank?Y/N")
        if first.lower() == "y":
            with open("HealthLog1.txt", "a") as water1:
                Content = f"Drank water at [{getdate()}] \n"
                water1.write(Content)
        else:
            pass