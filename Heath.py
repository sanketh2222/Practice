# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client
import  time
time.clock()
print(time.clock())
print("1: Harry\n2: Sejal\n3: Elon\n")
client=int(input("Enter Choice no.\n"))
ch=int(input("1: Push Data\n2: Retrive Data"))
print("What to do? Diet/Execr(D/E)")
choice=input()
dfiles=["1","harryD.txt","sejalD.txt","muskD.txt"]
xfiles=["1","harryE.txt","sejalE.txt","muskE.txt"]


#Writing the data for diet
while ch==1:
    if choice.lower()=="d":
        with open(str(dfiles[client]),mode="a") as d:
            plan=input("Enter Diet Plan")
            #diet=str(getdate())+"       "+plan+"\n"
            diet=f"[{getdate()}]      {plan} \n"
            d.write(diet)
            more=input("More Data push? Y/N")
            if more.lower()=="n":
                break
    elif choice.lower()=="e":
        with open(str(xfiles[client]),mode="a") as d:
            plan=input("Enter Exercise Plan")
            exer=str(getdate())+"       "+plan+"\n"
            print(exer)
            exer=d.write(exer)
            more = input("More Data push? Y/N")
            if more.lower() == "n":
                print(time.clock())
                break

if ch==2:
    if choice.lower()=="d":
        with open(dfiles[client]) as inp:
            content=inp.read()
        print(content)
    else:
        with open(xfiles[client]) as inp:
            content=inp.read()
        print(content)

# exer=open("HarryEx.txt","+")



