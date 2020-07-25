import os
import smtplib
def solider(path):
    count=1
    os.chdir(path)
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    txt_files = [file for file in onlyfiles if file[-3:] == "txt"]
    jpg_files = [file for file in onlyfiles if file[-3:].lower()=="jpg"]
    for jpg in jpg_files:
        os.rename(jpg,f"{count}.jpg")
        count+=1

    for file in txt_files:
        os.rename(file,file.capitalize())




path=os.path.join(os.getcwd(),"Files")
os.chdir(path)
os.listdir(path)
solider(path)