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
