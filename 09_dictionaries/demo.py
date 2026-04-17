# Dictionaries

# empty Dictionaries
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

empty_dict = dict(empty_dict)
print(empty_dict)
print(type(empty_dict))

# dictionary with numeric data 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# dictionary with text data 
data = {"c1":"python","c2":"django","c3":"ai"}
print(data)

# dictionary with mixed data 
data = {1:10,2:20,3:30,"c1":"python","c2":"django","avg":5.5,"passed":True}
print(data)

# Accessing Data In dictionary 
data = {1:10,2:20,3:30,4:40,5:50}
print(data) # all data in dictionary

# first_element = data[0] # KeyError: 0
first_element = data[1]
print(first_element)

last_element = data[5]
print(last_element) 

# Access Individual Data 
data = {1:10,2:20,3:30,4:40,5:50}
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])

# Access Individual Data -> 10k elements 
data = {1:10,2:20,3:30,4:40,5:50,1000:10000}
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])
print(data[1000])
# print(data[9999])

# print(dir(data)) --> __iter__

# Access Individual Data -> 10k elements 
# Loops we can Apply 
data = {1:10,2:20,3:30,4:40,5:50,1000:10000}
for num in data: # Only Keys we can access 
    print(num)
    
for key in data: # Only Keys we can access 
    print(key)
    
for key in data: # Accessing Values With Keys 
    print(data[key])    
    
# Apply Operators -> Requirement: Multiply Each element with 10
data = {1:10,2:20,3:30,4:40,5:50,1000:10000}
for key in data:
    print(data[key] * 10) 
    
# Apply Operations -> Requirement: Each Course Should have First Character Uppercase
data = {"c1":"python","c2":"django","c3":"ai"}
print(data)
for course in data:
    print(data[course].title())
    
# Apply Conditionals -> Requirement: Give Only Even Values
data = {1:10,2:25,3:35,4:40,5:50}
print(data)
for key in data:
    if data[key] % 2 == 0:
        print(data[key])
        
# Duplicates Allowed (Values) & Insertion Order Is Preserved 
data = {1:10,2:20,3:30,4:20,5:50,6:20}
print(data)

# Duplicates Not Allowed (Keys) i.e override old key 
data = {1:10,2:20,1:30,4:20,1:50,6:20}
print(data)

# Keys should be Immutable Objects
data = {("key1"):10,("key2"):20}
print(data)

# Keys should be Immutable Objects
# data = {["key1"]:10,["key2"]:20} # TypeError: unhashable type: 'list'
# print(data)

# Real World Dictionaries Looks Like JSON Data 
# https://media.licdn.com/dms/image/v2/D4D12AQGwOUMYbhUu-A/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1682148646113?e=2147483647&v=beta&t=qeCSY5Ktzx2jkeq7suYaSBV_-OS_18P-yuabrIhNWcU

students = {
    "101": {
        "name": "Ravi",
        "email": "ravi2krishna@gmail.com",
        "courses": ["python","django","ai"],
        "courses_fee": (10000,15000,25000)
    },
    "102": {
        "name": "Krishna",
        "email": "ravi2krishna@gmail.com",
        "courses": ["linux","cloud","devops"],
        "courses_fee": (10000,15000,25000)
    }
}