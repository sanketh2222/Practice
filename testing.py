# i=2
# j=02
# y=int(j)
# print(j)
'''

item_list=[]

#logic to enter items, until enter key is pressed
item=input("Enter item")
while item :
    item=input("Enter item")
    # if not item:
    #     break
    # else:
    #     item_list.append(item)
    item_list.append(item)
item_list.pop()
print(f" items are   {item_list}")
    
# item=input("enter")
# print(item)

'''

import re

# multiple input test
# if cancel in query:then
# inp=["please send a mail", "could you send a mail please"]
# mail_pattern=re.compile(r".*mail.*")
# news_pattern=re.compile(r".*news.*")
# weather_pattern=re.compile(r".*weather.*")
# time_pattern=re.compile(r".*time.*")
# query=input("enter query")
# # print(pattern.match(query))
# print(bool(mail_pattern.findall(query)))
# print(bool(news_pattern.findall(query)))
# print(bool(weather_pattern.findall(query)))
# print(bool(time_pattern.findall(query)))
# pattern=re.compile(r".*who is")
# query="do you know who is soonam kapoor"

# res=pattern.findall(query)
# print(res)
# query=query.replace(str(res[0])," ")

# print(query.strip())

string="ab"
# patt=re.compile(r".*b{1,10}$")
patt=re.compile(r".*b{1,10}.*")
res=patt.findall(string)
print(res)

# if query in inp:
#     print("i got that") 