name = "Ram Krishna Prasad"
# print(len(name))
# print(name[4])
# print(name[0:4])
# print(name[0:18])
# # print(name[200]) # wrong
# print(name[0:200]) # right
# print(name[0:8])
# print(name[0:8:1])
# print(name[:5])
# print(name[0:])
# print(name[::])
# print(name[::3])
# print(name[::-1]) # Print in reverse order
# print(name[::-2])name = "Ram Krishna Prasad"
# # print(len(name))
# # print(name[4])
# # print(name[0:4])
# # print(name[0:18])
# # # print(name[200]) # wrong
# # print(name[0:200]) # right
# # print(name[0:8])
# # print(name[0:8:1])
# # print(name[:5])
# # print(name[0:])
# # print(name[::])
# # print(name[::3])
# # print(name[::-1]) # Print in reverse order
# print(name[::-2])
# print(name[-3:len(name)])

# num=[i for i in range(1,10)]
# print(num)
# n=input()
# for i in range(1,int(n)):
#     print(i,end=" ")
import os
# path=os.path.join(os.getcwd(),"Files")
# print(path)
# print(os.listdir(path))
# for i in os.listdir(path):
#     print(os.path.splitext(i)[1],end=" ")
# name = "sanketh.png"
# print(name.split("."))
# name[1]
# a=1
# b=a
# d=1
#
# print(a==b)
# print(a==d)
# a=2
# print(b)
# print(a is b)
# print(d is a) # not supposed to return true since d is a new variable and not pointing to a or b

# a=[1,2,3]
# b=a
# print("a",a)
# print("b",b)
# b[0]=2
# print("a",a)
# print("b",b)
# c=[2,2,3]
# print(a==c)
# print(a is c)

# age_year=input("Enter your inp.")
# if len(age_year)==4:
#     if int(age_year)>2020:
#         print("you are not born yet")
#     else:
#         print("you entered year")
#         age=int(age_year)+100
#         if 2020-int(age_year)>=150:
#             print("you seem to be very old")
#             year = int(input("enter year"))
#             age = year - int(age_year)
#             print(f"you will be {age} in year {year} ")
#         else:
#             print(f"you will be 100 in {age}")
#             year=int(input("enter year"))
#             age=year-int(age_year)
#             print(f"you will be {age} in year {year} ")
# else:
#     if int(age_year)==0:
#         print("min age should be 1")
#     elif int(age_year)>=150:
#         print("you seem to be very old")
#         exit(0)
#         # year = int(input("enter year"))
#         # age=year-(2020-int(age_year))
#         # print(f"you will be {age} in year {year}")
#     else:
#         print("you entered your age")
#         year=2020+100-int(age_year)
#         print(f"you will be 100 in {year} ")
#         year=int(input("enter year"))
#         age=year-(2020-int(age_year))
#         print(f"you will be {age} in year {year}")

# try:
#     n=int(input("enter the no of apples"))
#     mn=int(input("enter mx"))
#     mx=int(input("enter mn"))
#     print(mx,mn)
#
#     if mn==mx:
#         print("invalid")
#     else:
#         lst=[i  for i in range(mn,mx+1) if n% i==0]
#     # print(type(mn))
#     # print(mn>=mx)
#     # while mn>=mx:
#     #     if n%mn==0:
#     #         print(f"{mn} is divisble by {n}")
#     #         mn+=1
#     #     else:
#     #         continue
#
#     for i in range(mn,mx+1):
#         if n%i==0:
#             print(f"{i} is a divisor of {n}")
#         else:
#             print(f"{i} is not  a divisor of {n}")
# except ValueError:
#     print("invalid input")


'''

#REVERSING LIST WITH OWN LOGIC
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

'''
# import re
# Sentences = ['This is good', 'python is good', 'python is not python snake','joke','python is best in best']
# query = "is good"# query= input("enter query string")
#
# def matching(sentence,query):
#     score = 0
#     words1=sentence.split(" ")
#     # print(words1)
#     words2=query.split(" ")
#     # print(words2)
#     for word1 in words1:
#         for word2 in words2:
#             if word1==word2:
#                 score+=1
#     return score
#
# # print(matching("python is good","python"))
#
# scores=[(matching(sentence,query)) for sentence in Sentences ]
# # print(scores)
#
#
# sentscore=[ sentscore for sentscore in sorted(zip(scores,Sentences),reverse=True)]
# sentscorelist=[j for i,j in sentscore if i!=0]#to filter the list by excluding 0 score. to find the no. of exact match
# occurance=len(sentscorelist)# no. of match
#
# print(f"{occurance} matched results\n")
# for score,sent in sentscore:
#     if score!=0:
#         print(f"\"{sent}\"  matched with a score of {score}\n")

# print(f"{occurance} matched results")
# for item in sentscorelist:
#     print(f"{item}")
# print(sentscore)
# print(sentscorelist)
# scoremap=tuple(zip(Sentences,scoresent))
# print(scoresent)
# print(scoremap)


# list1=[1,2,3]
# list2=[4,5,6]
# print(tuple(zip(list1,list2)))

# parse=[]
#
# # patt=re.compile(r'')
#
#
# for i in Sentences:
#     parse.append(i.split())
#
# # print(parse)
# query=query.split()
# # print("query")
# # print(query[1])
# # print(len(parse))
# # print(len(parse[2]))
# count=0
# occ=0
# dict={}
#
# for i in range(0,len(parse)):
#     for j in range(len(parse[i])):
#         for z in range(len(query)):
#             if query[z]==parse[i][j]:
#                 count+=1
#     # print(i,"main loop ")
#
#     dict.update({count:i})
#     if count>=1:
#         occ+=1
#     count=0
# print(dict)
# dict1={}
# print(f"{occ} matched results")
# for i in sorted(dict.keys(),reverse=True):
#     if i!=0:
#         print(f"{Sentences[dict.get(i)]} --> {i} ocuurences")
# print(count)
# print(dict)
# lst=[i for i in dict.values()]
# lst.sort(reverse=True)
# print(lst)

# for i,j in range(0,len()):
#     for z in query:
#         if query[z]==parse[i][j]:
#             count+=1

# lst=[4,3,2,1,10]
# lst1=[1,2,3,4,5]
# sort=[sorted(zip(lst1,lst), reverse=True)]#first the list is mapped, then sorted based on the first
# #parameter value in this case lst1
# sort=[sorted(zip(lst,lst1), reverse=True)]
# print(sort)

# import  random
#
# num=random.randint(1,10)
# print(num)
#
# # lst=[table*i for i in range(1,11)]
# # print(lst)
# def fakeMult(table):
#     lst=[table*i for i in range(1,11)]
#     lst[num]+=2
#     return lst
#
# table=5# table= input("Enter table")
# res=fakeMult(table)#res=fakeMult(table)
#
# print(res)
#
# def iscorrect(table,numbers):
#     correct=True
#     count=0
#     for i in numbers:
#         if i % table != 0:
#             print(i)
#             print(f"index is {count}")
#             correct=False
#         else:
#             count += 1
#
#     return correct
#
# result=iscorrect(table,res)
# print(result)


# lst=[i for i in numbers if i%table!=0]
import random
list=[
'Rohan Das',

'Shubham Agarwal',

'Ritesh Arora',

'Ram Charan Teja',
    
'Elon Musk'
]
fname=[]
for i in list:
    fname.append(i.split(" ",1))
fnames=[]
lnames=[]

# print(fname,"\n")


for fn in fname:
    fnames.append(fn[0])

for ln in fname:
    lnames.append(ln[1])

print(fnames)
# print(len(fnames))
print(lnames)
# print(len(lnames))
rand=random.randint(0,len(fnames))

count=0
size=len(fnames)-1
print(f"{size+1} funny names \n")
while count<size+1:
    rand = random.randint(0,size )
    rand1 = random.randint(0, size)
    res = fnames[count] + " " + lnames[rand1]
    print(res)
    count+=1

