try:
    n=int(input("enter the no of apples"))
    mn=int(input("enter mx"))
    mx=int(input("enter mn"))
    print(mx,mn)

    if mn==mx:
        print("invalid")
    else:
        lst=[i  for i in range(mn,mx+1) if n% i==0]
    # print(type(mn))
    # print(mn>=mx)
    # while mn>=mx:
    #     if n%mn==0:
    #         print(f"{mn} is divisble by {n}")
    #         mn+=1
    #     else:
    #         continue

    for i in range(mn,mx+1):
        if n%i==0:
            print(f"{i} is a divisor of {n}")
        else:
            print(f"{i} is not  a divisor of {n}")
except ValueError:
    print("invalid input")
