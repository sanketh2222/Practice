import re
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
res= fact(560)
# print(res)
res=str(res)
# res="5000050000"

#logic to calculate the number of trailling zeros without any error
pattern=re.compile(r'[0]{1,200}$')

print(pattern)
print(pattern.findall(res))
print(type(pattern.findall(res)))
result=pattern.findall(res)
print(len(result[0].split("0"))-1)
# 000
# 000
# 000
# 000
# 000
# 0
#logic to calculate the number of trailling zeros,with error 

        

# lst=a.split("0")
# print(lst)
# print(lst.count(''))
# print(fact(70))

# find the trailing number of zeros in factorial, without calculating the factorial
def trailcount(num):
    count=0
    i=5
    while(num//i!=0):
     count+=int(num/i)
     i=i*5
    
    return count

print(trailcount(560))