# count=0
# for i in range(1,6):
#     # print("inside condition",i)
#     for j in range(i-1):
#         print(i,end="")
#         # count=2
#     print(i)

# for i in range(1,6):
#     # print("inside condition",i)
#     for j in range(i):
#         print(i,end="")
        # count=2
    # print(i)\
# print((10**(i)//9)*i)
    
import re
import os

string='''
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
'''
pattern1=re.compile(r"head")
pattern2=re.compile(r"\w+=\".*\"")
res=pattern1.findall(string)
res2=pattern2.findall(string)
res=set(res)
print(res2)
ans=[]
for i in range(len(res2)):
    ans.append(res2[i].replace("="," >"))

print(res2)
for i in  res2:
    string.replace(i,"var")
    
print(string)
    
os.mkdir("open")