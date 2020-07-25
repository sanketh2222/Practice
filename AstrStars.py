n=int(input("Enter No/n"))
choice=input("T/F")

while 1:
    if choice.lower()=="t":
        for i in range(n):
            print("*"*n)
            n=n-1
    else:
        for j in range(n+1):
            print("*"*j)
            j=j+1

def print_stud(normal,d):
    print(normal)
    for i in d:
        print(i,end=" ")
