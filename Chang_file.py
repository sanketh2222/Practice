import  os

# renaming text files to py files
# file_list=os.listdir()
# print(file_list)
# for file in file_list:
#     file_list=file.split(".")
    
# print(file_list)
# for file in file_list:
#     new_file=file.split(".")
#     os.rename(file,f"{new_file[0]}.py")

files=[]
file_list=os.listdir()
# print(file_list)
# for file in file_list:
#     new_files=new_files.append(file.split("."))
    


new_files=[file.split(".")[0].lower() for file in file_list]
new_files=set(new_files)

for i in new_files:
    if i.__contains__("_"):
        files.append(i.split("_"))
        
print(files)
new_list=[]
for i,j in files:
    new_list.append(i+j)
    
new_list=set(new_list)
print(new_list)
# print(type(new_files))

# os.path="C:/Users/SANKETH/PycharmProjects/Practice"

os.chdir(r"C:\Users\SANKETH\PycharmProjects\Practice")
file_list1=os.listdir()
new_files1={file.split(".")[0].lower() for file in file_list1}
# new_files1=set(new_files1)
print(type(new_files1))



# print(os.getcwd())
print(new_files1)
print(new_files1.intersection(new_list))
common_files=new_files1.intersection(new_list)
list(common_files)

with open(file="file2.txt",mode="a") as f:
    f.write(str(new_files1))    
    f.write(str(new_list))    
    f.write(f"{str(common_files)} were deleted")    

# for file in common_files:
#     os.remove(f"{file}.txt")
    



    

