# Functional Programming 

# Without Functions 

num1 = 10
num2 = 5

# Math Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 20)

# Another User wants to calculate for 20 & 5
num1 = 20
num2 = 5

# Math Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 20)


# Another User wants to calculate for 200 & 50
num1 = 200
num2 = 50

# Math Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 20)

# With Functions 
def math_ops():
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

# User 1 -> 10 & 5
num1 = 10
num2 = 5
math_ops()
print("=" * 20)

# User 2 -> 20 & 5
num1 = 20
num2 = 5
math_ops()
print("=" * 20)

# User 3 -> 200 & 50
num1 = 200
num2 = 50
math_ops()
print("=" * 20)

# Why not this 
# math_ops(10,5) # TypeError: math_ops() takes 0 positional arguments but 2 were given

# With Parameters 
def math_ops(num1, num2):
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
    
# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'num1' and 'num2'
math_ops(10,5)
print("=" * 20)
math_ops(20,5)
print("=" * 20)
math_ops(200,50)
print("=" * 20)

# Positional Arguments 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
    
employee_info("hyderabad","ravi","ravi2krishna@gmail.com") # incorrect order
employee_info("ravi","ravi2krishna@gmail.com","hyderabad") # correct order
print("=" * 20)


# Keywords Arguments 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
    
employee_info("hyderabad","ravi","ravi2krishna@gmail.com") # incorrect order    
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi2krishna@gmail.com") 

print("=" * 20)

# Without Default Arguments 
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
   
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi2krishna@gmail.com",org_name="Google")  
employee_info(emp_location="pune",emp_name="krishna",emp_email="ravi2krishna@gmail.com",org_name="Google")  
employee_info(emp_location="delhi",emp_name="mike",emp_email="mike@gmail.com",org_name="Google")  

    
print("=" * 20)

# With Default Arguments -> Org Name is Always Google i.e Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name="Google"):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")

employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi2krishna@gmail.com")  
employee_info(emp_location="pune",emp_name="krishna",emp_email="ravi2krishna@gmail.com")  
employee_info(emp_location="delhi",emp_name="mike",emp_email="mike@gmail.com")  
# If an argument is provided, it overrides the default -> works for META 
employee_info(emp_location="new york",emp_name="Mark",emp_email="mark@gmail.com",org_name="META")  

print("=" * 20)

# Placement Requirement: Default arguments must always be placed after any non-default arguments
# Non-default argument follows default argument
# def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile):
#     print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")

def employee_info(emp_name,emp_email,emp_location,emp_mobile,org_name="Google"):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    
def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile="+91"):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")

# Arbitrary Positional Arguments

def add_numbers_one(n1):
    print(n1) 

def add_numbers_two(n1,n2):
    print(n1,n2)  

def add_numbers_three(n1,n2,n3):
    print(n1,n2,n3) 

def add_numbers_ten(n1,n2,n3,n10):
    print(n1,n2,n3,n10) 

add_numbers_one(10)
add_numbers_two(10,20)
add_numbers_three(10,20,30)
add_numbers_ten(10,20,30,100)

print("=" * 20)

def add_numbers(*nums):
    print(nums)  
    
add_numbers(10)   
add_numbers(10,20)   
add_numbers(10,20,30)   
add_numbers(10,20,30,40,50,60,70,80,90,100)   

print("=" * 20)

def add_numbers(*nums):
    total = 0
    for num in nums:
        total += num  
    print(f"Total Sum is {total}")
    
add_numbers(10)   
add_numbers(10,20)   
add_numbers(10,20,30)   
add_numbers(10,20,30,40,50,60,70,80,90,100)   

print("=" * 20)
# Real world use case can be ecommerce application product cart 

# Arbitrary Keywords Arguments
# def profile_fname(fname):
#     print(fname)

def profile(**info):
    print(info)
# profile(fname)    
profile(fname="Ravi")
profile(fname="Ravi",lname="Krishna")
profile(fname="Ravi",lname="Krishna",email="ravi2krishna@gmail.com")

print("=" * 20)

# Real world use case -> jan=3000,feb=4000,mar=2000 
# Requirement: Total Transactions Value and Number Of Transactions Made 
def bank_transactions(**transactions):
    print(transactions)
    total = 0
    transaction_count = 0
    for transaction in transactions:
        total += transactions[transaction]
        transaction_count += 1
    print(f"Total Transactions Value is {total} for {transaction_count} Transactions")
        
bank_transactions(jan=3000,feb=4000,mar=2000)
bank_transactions(jan=3000,feb=4000,mar=2000,apr=5000,may=6000,june=9000)

print("=" * 20)

# Without return 
def add(a,b):
    a + b 
    
add(10,20)
print(add(10,20))

# With return 
def add(a,b):
    return a + b 

print(add(10,20))

# function composition
def sub(c,d,e): # add c & d, then minus e => c + d - e
    return add(c,d) - e

print(sub(3,4,5))

# return - make sure it's the last part of statement to be executed
def add(a,b):
    print("Calculation Started")
    return a + b 
    print("Calculation Completed") # Code is structurally unreachable
    
print(add(200,100))    

# multiple return statements - first return will be considered
def math_ops(num1, num2):
    return num1 + num2 
    return num1 - num2 
    return num1 * num2 
    return num1 / num2 

print(math_ops(1,2))

# multiple returns are present - with conditionals you can control the flow 
def math_ops(num1, num2, operator):
    if operator == "+":
        return num1 + num2 
    elif operator == "-":
        return num1 - num2 
    elif operator == "*":
        return num1 * num2 
    elif operator == "/":
        return num1 / num2 
    else:
        return "Invalid Operator"

print(math_ops(20,10,"+"))
print(math_ops(20,10,"*"))
print(math_ops(20,10,"@"))

# Local Scope
def add():
    la = 10 # local variable - declared "inside the function" 
    lb = 20 # local variable - declared "inside the function" 
    print(la)
    print(lb)

add()

# we cannot use local variable outside the function    
# print(la) # NameError: name 'la' is not defined

# Parameters we are passing to the functions, are also local variables  
def add(la,lb): # local variable - declared "inside the function" 
    print(la)
    print(lb)

add(40,50)

# we cannot use local variable outside the function    
# print(la) # NameError: name 'la' is not defined

# Global Scope
ga = 100 # global variable
def add(la,lb): # local variable - declared "inside the function" 
    print(la)
    print(lb)
    print(ga) # global variable, accessed within function 
    
add(80,90)
print(ga) # global variable, accessed outside function 

# name conflicts
ga = 500 # global variable
def add(la,lb,ga): # local variable - declared "inside the function" 
    print(la)
    print(lb)
    print(ga) # local variable, given preference first 

add(10,20,30)
print(ga)

# name conflicts
ga = 100 # global variable
def add(la,lb,ga): # local variable - declared "inside the function" 
    print(la)
    print(lb)
    print(ga) # local variable, given preference first 
    print(globals()['ga']) # global variable, accessed within function 

add(40,50,60)

# global variables outside the function 
count = 0
print(count)
count +=1 
print(count)

# global variables inside the function 
count = 0
print(count)
def increment():
    global count 
    count += 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    return count 

print(increment())


# Without lambda function i.e Regular functions 
def add(a,b):
    return a+b 
print(add(200,300))

# With lambda function
# lambda arguments:expression
lambda a,b:a+b 
print((lambda a,b:a+b)(100,200)) # One liner function

# Without lambda function
def is_even_num(num):
    if num % 2 == 0:
        return True 
    else:
        return False
    
print(is_even_num(11))
print(is_even_num(10))

# With lambda function
# lambda arguments:expression
lambda num:num % 2 == 0
print((lambda num:num % 2 == 0)(100))
print((lambda num:num % 2 == 0)(101))

# Without lambda 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}") 
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi2krishna@gmail.com") 

# With lambda function
# lambda arguments:expression
print((lambda emp_name,emp_email,emp_location:print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}"))(emp_location="hyderabad",emp_name="ravi",emp_email="ravi2krishna@gmail.com"))


# Without Higher Order Function - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5]   ==>     [1,4,9,16,25]
def square_list(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num*num)
    return squared_list

print(square_list([1,2,3,4,5]))


# With Higher Order Function - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5]   ==>     [1,4,9,16,25]
# syntax ==> map(function, iterable)
map((lambda num:num*num), [1,2,3,4,5])
print(map((lambda num:num*num), [1,2,3,4,5]))
print(list(map((lambda num:num*num), [1,2,3,4,5])))
