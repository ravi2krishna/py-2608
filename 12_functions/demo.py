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