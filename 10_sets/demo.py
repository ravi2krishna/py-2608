# Sets 

# empty set
empty_set = {} # empty curly braces are always dictionaries
print(empty_set)
print(type(empty_set))

empty_set = set(empty_set)
print(empty_set)
print(type(empty_set))

# set with numeric data 
data = {10,20,30,40,50}
print(data)

# set with text data 
data = {"python","django","ai"}
print(data)

# set with mixed data 
data = {10,20,30,"python","django",5.5,True}
print(data)

# Accessing Data In tuples 
# data = {10,20,30,40,50}
# print(data) # all data in tuple 

# first_element = data[0] # TypeError: 'set' object is not subscriptable
# print(first_element)

# last_element = data[-1]
# print(last_element)

# print(dir(data)) # __iter__

# Access Individual Data -> 10k elements 
# Loops we can Apply 
data = {10,20,30,40,50,10000}
for num in data:
    print(num)
    
# Apply Operators -> Requirement: Multiply Each element with 10
data = {10,20,30,40,50,10000}
for num in data:
    print(num * 10)  
    
# Apply Operations -> Requirement: Each Course Should have First Character Uppercase
data = {"python","django","ai"}
print(data)
for course in data:
    print(course.title())
    
# Apply Conditionals -> Requirement: Give Only Even Values
data = {10,25,35,40,50}
print(data)
for num in data:
    if num % 2 == 0:
        print(num)  
        
        
# Duplicates Not Allowed & Insertion Order Is Not Preserved 
data = {10,20,30,20,50,20}
print(data)

print(dir(data))

# frozenset
data = frozenset({10,20,30,40,50})
print(type(data))

# Methods / Operations 
print(dir(data))