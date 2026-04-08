# Indentation

print("Hello")
print("Python")
# print("Ravi") # IndentationError: unexpected indent

# Indentation defines the structure and hierarchy of "code blocks"

# if condition 
# if True:
# print("Student Passed") # IndentationError: expected an indented block after 'if' statement on line 10

if True:
 print("Student Passed")

if True:
 print("Statement 1")    
 print("Statement 2")    
 print("Statement 3")    
 print("Statement N")    
 
# "consistent" indentation
if True:
  print("Statement 1")    
  print("Statement 2")    
  print("Statement 3") # IndentationError: unexpected indent 
  print("Statement N") 
  
# "consistent" indentation -> Recommended Way Using Tab i.e 4 Spaces 
if True:
    print("Statement 1")    
    print("Statement 2")    
    print("Statement 3")    
    print("Statement N")    
    
if False:
    print("Let's see if this code runs")

# if condition
if 5 > 2:
    print("yes 5 > 2 is correct")
    
# if condition
if 5 < 2:
    print("yes 5 < 2 is correct") 
    
num = -10
if num > 0:
    print("given num is positive")
if num < 0:
    print("given num is negative")
    
# if else 
num = 10
if num > 0:
    print("given num is positive")
else:
    print("given num is negative")
    
# input() Function
name = input("What is your name: ")
print(name)
print("Welcome "+name) # concatenation 
print("Welcome name") # This is static
print(f"Welcome {name}") # Interpolation -> This should be dynamic

# if else condition dynamic
num = input("Enter Number: ")
num = int(num) # Type Casting
if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print(f"given {num} is positive")
else:
    print(f"given {num} is negative")

# Voting App
age = int(input("Enter Your Age: "))
if age >= 18:
    print("You Can Vote")
else:
    print(f"You Can Vote as you are still {age}")

# Conditional Expression
# value_if_true if condition else value_if_false 
age = int(input("Enter Your Age Again: "))
status = "You Can Vote" if age >= 18 else "You Cannot Vote" 
print(status)

# elif ladder 
marks = int(input("Enter Marks: "))
if marks >= 35:
    print("PASSED")
else:
    print("FAILED")   
    
# check for grades      
marks = int(input("Enter Marks: "))
if marks >= 90:    
    print("A Grade")
elif marks >= 75:    
    print("B Grade")
elif marks >= 60:    
    print("C Grade")        
elif marks >= 50:    
    print("D Grade")
elif marks >= 35:    
    print("E Grade")
else:
    print("FAILED")   

# match-case 
error_code = int(input("What Error Code Did You See: "))
match error_code:
    case 403:
        print("Forbidden Error")
    case 404:
        print("Not Found Error")
    case 502:
        print("Bad Gateway Error")
    case _:
        print("Unknown Error")

user_role = input("Enter Your Role: ")
match user_role:
    case "lead" | "manager":
        print("You have Read, Write & Delete Access")
    case "developer" | "tester":
        print("You have Only Read & Write Access")
    case "guest":
        print("You have Only Read Access")
    case _:
        print("Access Denied")
        


