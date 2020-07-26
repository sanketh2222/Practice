from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r"C:\Users\Kush\Desktop\c.ico",
        timeout=10

    )
def getData(url):
    r = requests.get(url)
    return r.text


# myHtmlData = getData('https://www.mohfw.gov.in/')
myHtmlData = requests.get('https://www.mohfw.gov.in/')

soup = BeautifulSoup(myHtmlData.text, 'html.parser')
myDatastr= ""
for tr in soup.find_all('tbody')[0].find_all('tr'):
    myDatastr += tr.get_text()

print(myDatastr)

'''
if __name__ == '__main__':

    while True:
        # notifyme("Corona Update", "lets stop this togther")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDatastr= ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDatastr += tr.get_text()
        myDatastr = myDatastr[1:]
        itemList = myDatastr.split("\n\n")

        # for i in itemList:
        #     print(i)

        states = ['Delhi']
        for item in itemList[0:29]:
            datalist = item.split('\n')
            # print(datalist)
            if datalist[1] in states:
                nTitle = 'Cases of COVOID-19'
                nText = f"State - {datalist[1]}\nTotal case: {datalist[2]}\n Cured: {datalist[3]}\n Deaths: {datalist[4]}"
                print(nText)
        #         notifyme(nTitle, nText)
        #         time.sleep(2)

'''