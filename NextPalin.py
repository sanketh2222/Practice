#15 lines
#problem 4
cases=int(input("Enter no of test cases"))
num=[]
for i in range(cases):
    n=int(input("Enter numbers"))
    num.append(n)

# num=[451,10,2133]
numc=num.copy()
num2=[]
for i in range(len(num)):
    num2.append(str(num))

for i in range(len(num)):
    if num[i]>10:#not considering number 10
        while num2[i][::-1]!=num2[i]:
            num[i]+=1
            num2[i]=str(num[i])
    else:
        num2[i]=num[i]

print(num2)
for i in range(len(num)):
    print(f"palindrome of {numc[i]} is {num2[i]}")