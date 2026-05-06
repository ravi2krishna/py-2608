# File & Directory Management Using Python 

# Syntax - 1
# file = open("file.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
file = open("14_file_manage/file.txt","r")
print(file)
print(file.closed) # False --> Still Open 
file.close()
print(file.closed) # True --> Now Closed 

print("=" * 50)

# Syntax - 2
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data)
print(file.closed) # Implicitly Closed 

print("=" * 50)

# Reading Data From File 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.read())
    
# Reading Data From File Character wise 
with open("14_file_manage/file.txt","r") as file_data:
    # print(file_data.read())
    for character in file_data.read():
        print(character)
        
# Reading Data From File Word wise 
with open("14_file_manage/file.txt","r") as file_data:
    # print(file_data.read())
    for word in file_data.read().split():
        print(word)
        

# Reading Data From File Line wise 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readline())
    
# Reading Data From File Multiple Lines
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readlines())
    
# Reading Data From File Multiple Lines
with open("14_file_manage/file.txt","r") as file_data:
    for line in file_data.readlines():
        print(line.strip())
        

# Write The Data To File
# Before Writing, Let's create file 
with open("14_file_manage/write.txt","w") as file_data:
    print(file_data)

# Write The Data To File
with open("14_file_manage/write.txt","w") as file_data:
    file_data.write("Hello")
    
# Write The Data To File Multiple Lines
with open("14_file_manage/write.txt","w") as file_data:
    file_data.writelines(['Hello there \n', 'how are you'])
    
# Append Mode 
with open("14_file_manage/write.txt","a") as file_data:
    file_data.writelines(['this is \n', 'new line'])
    
# Create Folder / Directory
directory_name = "14_file_manage/students_data"
# os.mkdir(directory_name)
import os 
# os.mkdir(directory_name)

if not os.path.exists(directory_name):
    os.mkdir(directory_name)

# Create file in students_data directory 
with open("14_file_manage/students_data/students.txt","w") as file_data:
    print(file_data)
    
# Delete File 
os.remove("14_file_manage/students_data/students.txt")

# Delete Empty Directory 
os.rmdir(directory_name)

# Delete Non-Empty Directory 
import shutil
# Deletes the folder and all its contents recursively
shutil.rmtree("14_file_manage/data")

