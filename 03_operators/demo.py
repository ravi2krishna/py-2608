# Operators

# Arithmetic Operators 
num1 = 10
num2 = 5 

print("Sum Of Numbers: ",num1+num2)
print("Difference Of Numbers: ",num1-num2)
print("Product Of Numbers: ",num1*num2)
print("Division Of Numbers: ",num1/num2)
print("Modulus Of Numbers: ",num1%num2)

print("Floor Division Of Numbers: ",num1//num2)
print("Division Of Numbers: ",3/2) # 1.5
print("Floor Division Of Numbers: ",3//2) # 1
print("Exponentiation Of Numbers: ",3**2) # 3 ^ 2 

print("========================")

# Compound Assignment Operators
num = 10 
num = num + 5 # long form 
print(num)

num = 10
num += 5 # short form 
print(num)

 
# Increment & Decrement increase or decrease a variable's value by one
# Increment: Generally used in loops in future sessions
count = 1
print(count)
# count++ # SyntaxError
count += 1
print(count)

# Decrement: Generally used in loops in future sessions
count = 10
print(count)
# count-- # SyntaxError
count -= 1
print(count)

print("========================")

# Comparison Operators 
num1 = 3
num2 = 2 

print(num1 == num2) # False 
print(num1 != num2) # True 
print(num1 > num2) # True

print("========================")

# Logical Operators 
num1 = 4
num2 = 3
num3 = 2
num4 = 1

print(num1 > num2 and num3 > num4) # T and T -> T
print(num1 > num2 and num3 < num4) # T and F -> F

print(num1 > num2 or num3 < num4) # T or F -> T
print(num1 < num2 or num3 < num4) # F or F -> F

print(num1 < num2) # F
print(not num1 < num2) # T

print("========================")

# Membership Operators 
data = "python is interpreted language"
find_word = "java"
status = find_word in data 
print(status) # False

data = "python is interpreted language"
find_word = "python"
status = find_word in data 
print(status) # True

# List Data Type -> Stores Multiple Values []
employee_ids = ["101","102","103","110","1001"]
find_emp_id = "103"
find_emp_id = "105"
status = find_emp_id in employee_ids
print("Employee Found: ",status)

# List Data Type -> Stores Multiple Values []
employee_ids = ["101","102","103","110","1001"]
find_emp_id = "105"
status = find_emp_id not in employee_ids
print("Employee Not Found: ",status)

print("========================")

# Identity Operators
n1 = 10
n2 = 10
n3 = 5

print(id(n1))
print(id(n2))

print(n1 is n2) # id(n1) == id(n2)
print(n1 is not n3)

print("========================")

# Bitwise Operators 
n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
       # 0000000000000001

print(n1 & n2) # 1 

n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
       # 0000000000000111
       
print(n1 | n2) # 7 