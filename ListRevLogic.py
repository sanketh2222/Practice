lst=[1,2,3,4,5,6,7]
lst2=lst.copy() # OR List2=lst[:]
size=len(lst)-1
size1=len(lst)
i=0
print(i<=size+1)
while size1:
    print(i,size)
    lst[i]=lst2[size]
    i+=1
    size-=1
    size1-=1

print(lst)