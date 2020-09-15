
from pygame import mixer
import datetime
import time
from pyautogui import typewrite
from threading import Thread


water_qty = 0


def getdate():
    import datetime
    return time.asctime(time.localtime(time.time()))


# time.asctime(time.localtime(time.time()))


datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'

mixer.init()


mixer.music.set_volume(0.7)
now = datetime.datetime.now()
now = now.strftime("%d-%B")


def water():
    water = datetime.datetime.now()
    # water2 = datetime.datetime.now()
    diff = datetime.datetime.strptime(str(water), datetimeFormat)
    print(diff.minute, diff.second)
    if (diff.hour == 2 and diff.minute >= 59 and diff.second >= 0):
        print(f" time is 4 pm {getdate()} exiting the program")
        print(f"total water consumed for {diff.day} is {water_qty}")
        with open("HealthLog.txt", "a") as water1:
            Content = f"\n\ntotal water consumed for {now} is {water_qty}\n"
            water1.write(Content)
        exit(0)
    else:
        time.sleep(1200)  # 20 minutes --> 1200
        print(f"Entering else condition @{diff.minute} and {diff.second}")
        water2 = datetime.datetime.now()
        diff = datetime.datetime.strptime(str(water2), datetimeFormat) \
               - datetime.datetime.strptime(str(water), datetimeFormat)

        print(diff.seconds)
        return diff.seconds/60


def phy():
    water = datetime.datetime.now()
    # water2 = datetime.datetime.now()
    diff = datetime.datetime.strptime(str(water), datetimeFormat)
    print(diff.minute, diff.second)
    if (diff.hour == 2 and diff.minute >= 59 and diff.second >= 0):
        print(f" time is 4 pm {getdate()} exiting the program")
        print(f"total water consumed for {diff.day} is {water_qty}")
        with open("HealthLog.txt", "a") as water1:
            Content = f"\n\ntotal water consumed for {now} is {water_qty}\n"
            water1.write(Content)
        exit(0)
    else:
        time.sleep(900)  # 15 minutes --> 900 with dependency
        print(f"Entering else condition @{diff.minute} and {diff.second}")
        water2 = datetime.datetime.now()
        diff = datetime.datetime.strptime(str(water2), datetimeFormat) \
               - datetime.datetime.strptime(str(water), datetimeFormat)

        print(diff.seconds)
        return diff.seconds/60


def eye():
    water = datetime.datetime.now()
    # water2 = datetime.datetime.now()

    diff = datetime.datetime.strptime(str(water), datetimeFormat)
    print(diff.minute, diff.second)
    if (diff.hour == 2 and diff.minute >= 59 and diff.second >= 0):
        print(f" time is  {getdate()} exiting the program")
        # print(f"total water consumed for {diff.day} is {water_qty}")
        with open("HealthLog.txt", "a") as water1:
            Content = f"\n\ntotal water consumed for {now} is {water_qty}\n"
            water1.write(Content)
        exit(0)
    else:
        time.sleep(600)  # 10 minutes with dependency of water function--> value 600
        water2 = datetime.datetime.now()
        diff = datetime.datetime.strptime(str(water2), datetimeFormat)\
               - datetime.datetime.strptime(str(water), datetimeFormat)

        print(diff.seconds)
        return diff.seconds/60


class once:
    count = 1
    start = 1

    def __init__(self):
        self.count = 1


var = once.count
start = once.start
print(var)
check = 0

while 1:
    water2 = datetime.datetime.now()
    diff = datetime.datetime.strptime(str(water2), datetimeFormat)
    if start == 1:
        start = 2
        print(f"\nStarted at {diff.minute} minutes and {diff.second} \n")

    if water_qty >= 3.4:
        check = 1

    wat = water()
    print(check, "before condition\n")
    if wat == 20 and check == 0:
        print("water condition")
        mixer.music.load("water.mp3")
        mixer.music.play(-1)
        first = 'waiting...'


        def t():
            time.sleep(10)  # wait for 15 seconds for input
            if first == 'waiting...':
                typewrite('n')
                typewrite(['enter'])


        T = Thread(target=t)
        T.start()
        first = input("Drank?Y/N")
        if first.lower() == "y":
            mixer.music.stop()
            water_qty = water_qty + 0.2
            with open("HealthLog.txt", "a") as water1:
                if var == 1:
                    var = 2
                    Content = f"\nLogs for {now}\nDrank water at [{getdate()}] \n"
                    water1.write(Content)
                else:
                    Content = f"Drank water at [{getdate()}] \n"
                    water1.write(Content)
        elif first.lower() == "n":
            mixer.music.stop()

    ey = eye()
    if ey == 10:
        if check == 1:
            time.sleep(1200)  # include the dependency of water once criteria of water is met value--> 1200
        print("eye confition")
        mixer.music.load("eye.mp3")
        mixer.music.play(-1)
        second = 'waiting...'


        # def t():
        #     time.sleep(10)  # wait for 5 seconds for input
        #     if second == 'waiting...':
        #         typewrite('n')
        #         typewrite(['enter'])


        T = Thread(target=t)
        T.start()
        second = input("Done?Y/N")
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

    ph = phy()
    if ph == 10:
        if check == 1:
            time.sleep(1200)  # include the dependency of water once criteria of water is met value--> 1200
        print("physical confition")
        mixer.music.load("phy.mp3")
        mixer.music.play(-1)
        second = 'waiting...'

        def t():
            time.sleep(10)  # wait for 5 seconds for input
            if second == 'waiting...':
                typewrite('n')
                typewrite(['enter'])


        T = Thread(target=t)
        T.start()


        second = input("Will do?Y/N")
        if second.lower() == "y":
            mixer.music.stop()
            with open("HealthLog.txt", "a") as i1:
                if var == 1:
                    var = 2
                    Content = f"\nLog for {now}\nphy exercise done  at [{getdate()}]\n"
                    i1.write(Content) 
                else:
                    Content = f"Eye exercise done  at [{getdate()}]\n"
                    i1.write(Content)
        elif second.lower() == "n":
            mixer.music.stop()
