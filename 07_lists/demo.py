# Lists 

# empty list
empty_list = []
print(empty_list)
print(type(empty_list))

empty_list = list(empty_list)
print(empty_list)
print(type(empty_list))

# list with numeric data 
data = [10,20,30,40,50]
print(data)

# list with text data 
data = ["python","django","ai"]
print(data)

# list with mixed data 
data = [10,20,30,"python","django",5.5,True]
print(data)

# Accessing Data In Lists 
data = [10,20,30,40,50]
print(data) # all data in list 

first_element = data[0]
print(first_element)

last_element = data[-1]
print(last_element)

# unknown_element = data[10] # IndexError: list index out of range
# print(unknown_element)

# Slicing same as strings
data = [10,20,30,40,50]
print(data)
print(data[1:3:1]) # 20,30 
print(data[0:5:2]) # 10,30,50

# Access Individual Data 
data = [10,20,30,40,50]
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

# Access Individual Data -> 10k elements 
data = [10,20,30,40,50,10000]
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
# print(data[9999])

# Access Individual Data -> 10k elements 
# Loops we can Apply 
data = [10,20,30,40,50,10000]
for num in data:
    print(num)
    
# Apply Operators -> Requirement: Multiply Each element with 10
data = [10,20,30,40,50,10000]
for num in data:
    print(num * 10)

# Apply Operations -> Requirement: Each Course Should have First Character Uppercase
data = ["python","django","ai"]
print(data)
for course in data:
    print(course.title())
    
# Apply Conditionals -> Requirement: Give Only Even Values
data = [10,25,35,40,50]
print(data)
for num in data:
    if num % 2 == 0:
        print(num)

# Duplicates Allowed & Insertion Order Is Preserved 
data = [10,20,30,20,50,20]
print(data)

# List Methods
print(dir(data))