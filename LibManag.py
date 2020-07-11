
#new lib management
import  datetime
def getdate():
    now = datetime.datetime.now()
    now = now.strftime("%d-%B")
    return  now
#
class Library:
    def __init__(self,name):
        self.name=name
        self.lst={}
        self.id=100
        with open("BookList.txt") as b:
            content=b.readlines()
        for line in content:
           if line.__contains__("\n"):
               self.lst.update({str(self.id):{"BookTitle": line[0:len(line)-2],
                                  "Lend Date":getdate(),
                                  "LenderName":"",
                                  "Count":int(line[-2])}})
           else:
              self.lst.update({str(self.id): {"BookTitle": line[0:len(line) - 1],
                                  "Lend Date": getdate(),
                                  "LenderName": "",
                                  "Count": int(line[-1])}})
           self.id += 1





    def lend_books(self,name,choice):
         self.cname=name
         self.bid=choice
         print(self.lst)
         if self.lst[self.bid]['Count']==0:
            #print(self.lst[choice]["BookTitle"]+"is not available\n")
            print(f"{self.lst[choice]['BookTitle']} is not available\n")
            print(f"Book already availed by {self.lst[choice]['LenderName']} on {self.lst[choice]['Lend Date']}")
         else:
            count=self.lst[self.bid]['Count']-1
            self.lst[self.bid]['Count']=count
            self.lst[self.bid]["Lend Date"]=getdate()
            self.lst[self.bid]["LenderName"]=self.cname
            print("Book issues sucessfully\n")

         print("upated!!")
         print(self.lst)

    def add_books(self,no_of_books,name):
        self.no_of_books=no_of_books#check if we need to initialize name as self.name
        self.name=name
        book_no = 1
        # print((self.no_of_books + 1) > 1)
        # print(self.id)
        # print(self.lst)
        while self.no_of_books:
            print(f"Book No# {book_no}")
            book_name = input("Book Title?\n")
            count = int(input("Number of copies to be added?"))
            print(self.id)
            print(type(self.id))
            print(str(self.id))
            book_no += 1
            self.lst.update({str(self.id): {"BookTitle": book_name, "Lend Date": getdate(),
                                "LenderName": "NA", "DonorName": self.name, "Count": count}})
            self.no_of_books -= 1
            self.id+=1
        # print(self.lst)
        with open("updated_list.txt", "a") as f:
            f.write(str(self.lst))


    def display_avail_books(self):
        book_no=1
        for book in self.lst:
            if self.lst[book]["Count"]!=0:
                print(f"{book_no} --> {self.lst[book]['BookTitle']}")
                book_no+=1

    def display_all_books(self):
        book_no=1
        for book in self.lst:
                print(f"{book_no} --> {self.lst[book]['BookTitle']}")
                book_no+=1
#
#

    def return_books(self,name,bid):
        self.name=name
        self.bid=bid
        if self.lst[self.bid]['LenderName']==self.name:
            self.lst[self.bid]['Count']+=1
            self.lst[self.bid]['LenderName']=''
            print(f"{self.lst[bid]['BookTitle']} returned sucessfully!!\n")
        else:
            print(f"{self.bid} is not availed by you!!")
#
name=input("Your Name?")
#choice=input("Please enter Book ID")
lib1=Library("MyLib")
while 1:
    print(f"{name}  logged in\n")
    key_input=input("What to do? q for quit")

    if key_input.lower()=="l":
        choice = input("Please enter Book ID")
        lib1.lend_books(name,choice)
    elif key_input.lower()=="a":
        # add books function
        no_of_books = int(input("Number of Books?\n"))  # sample 3
        #name = input("Your Name")
        lib1.add_books(no_of_books,name)

    elif key_input.lower()=="d":
        display_choice=input("Display Only Available?Y/N")
        if display_choice=="y":
            lib1.display_avail_books()
        else:
            lib1.display_all_books()
    elif key_input.lower()=="o":
        print(f"{name} logged off")
        name=input("Next Customer Login Name")
    elif key_input.lower()=="r":
        book_choice=input("Enter Book id to return\n")
        lib1.return_books(name,book_choice)
    elif key_input.lower()=="q":
        print("Thank you")
        break