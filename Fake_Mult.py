'''
Problem -8

Rohan Das Is A Fraud:

Rohan das is a fraud by nature.

Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.

Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!

So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.

Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.

Note: Rohan’s function returns a list of numbers like this
'''

import  random

num=random.randint(1,10)
print(num)

# lst=[table*i for i in range(1,11)]
# print(lst)
def fakeMult(table):
    lst=[table*i for i in range(1,11)]
    lst[num]+=2
    return lst

table=5# table= input("Enter table")
res=fakeMult(table)#res=fakeMult(table)

print(res)

def iscorrect(table,numbers):
    correct=True
    count=0
    for i in numbers:
        if i % table != 0:
            print(i)
            print(f"index is {count}")
            correct=False
        else:
            count += 1

    return correct

result=iscorrect(table,res)
print(result)