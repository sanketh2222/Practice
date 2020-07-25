#comprehension exercise:
list=[]
no=int(input("no of items"))
while int(no)>=1:
    items=input("Enter the items")
    list.append(items)
    no-=1

print(list)
print("1.List comp/n2.Dict comrehension/n3.Set comprehension")

while 1:
    choice = int(input("Choice?"))
    if choice==1:
        listc=[i for i in list]
        print(listc)

    elif choice==2:
        dict={1:f"{i}" for i in list}
        print(dict)
        dict1={value:key for key,value in dict.items()}
        print(dict1)

    else:
        setc=(i for i in list)
        setc1={i for i in list}
        print(setc)
        print(setc1)

    if choice==4:
        break

dict1={
    1:"item1",
    2:"item2"
}
dict2={value,key for key,value in dict1.items()}
print(dict,"/n",dict2)