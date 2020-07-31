#shopping mart code
sum=0
count=0
cart={}
while True:
    try:
        user_inp,value=input("Enter item or q").split()#take item and price in single line, q space q to quit or simply q
    except Exception as  e:# handling single q input for quiting
        print("exception occured")
        user_inp="q"
        value=0
        count=1
        print(count) 
    # user_inp=input("Enter item")
    # if user_inp!='q':
    #     value=input("Enter price")
    if user_inp!='q':
        cart.update({user_inp:value})
        # for i in cart.values():
        #         sum+=int(i)
    if user_inp=='q':
        if not bool(cart):
            print("no purchase made")
            break
            
        
        else:
            # print(cart)
           
            print("Order Summary")
            print(bool(cart))
            for key,value in cart.items():
                print(f" item :  {key} ,price :{value}")
                
            print(f" you total bill is   {sum}")
            break
    else:
        # sum+=int(user_inp)
        # print(cart)
        for i in cart.values():
            # print("cart values",i)
            pass
            # print("previous sum",sum)
        sum+=int(i)
        print(f" total bill so far is   {sum}")