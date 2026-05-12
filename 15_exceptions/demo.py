# Exception Handling 

# When No Errors -> Nothing To Handle 
print("Program Execution Started")

num1 = 10
num2 = 5

print("Result: ", num1/num2)

print("Program Execution Completed")

print("=" * 50)

# print("Program Execution Started")

# num1 = 10
# num2 = "5"

# print("Result: ", num1/num2)# TypeError: unsupported operand type(s) for /: 'int' and 'str'

# print("Program Execution Completed")

# When Error Occurs -> Handle Exceptions with try & catch

print("Program Execution Started")

num1 = 10
num2 = "5"

try:
    print("Result: ", num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'
except:
    print("WARNING! Don't Divide Numerics With Strings")

print("Program Execution Completed")

print("=" * 50)

# When No Error Occurs -> Everything works as expected, Handle Exceptions with try & catch

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ", num1/num2) 
except:
    print("WARNING! Don't Divide Numerics With Strings")

print("Program Execution Completed")

print("=" * 50)

# print("Program Execution Started")

# num1 = 10
# num2 = 0

# print("Result: ", num1/num2) # ZeroDivisionError: division by zero

# print("Program Execution Completed")

# print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ", num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! We Got An Error - Check Below Link For More Info")
    print("https://en.wikipedia.org/wiki/Division_by_zero")

print("Program Execution Completed")

print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ", num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! We Got An Error - Check Below Link For More Info")
    print("https://en.wikipedia.org/wiki/Division_by_zero")

print("Program Execution Completed")

print("=" * 50)

# When we Come Across Multiple Errors 
print("Program Execution Started")

# data = [1,2,'three',0,4]
# data = [1,2,0,4]
data = [1,2,4]

for num in data:
    print(1/num) 
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
print("Program Execution Completed")

print("=" * 50)

# When we Come Across Multiple Errors 
print("Program Execution Started")

data = [1,2,'three',0,4]

for num in data:
    try:
        print(1/num) 
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    except:
        print("OOPS! Something Went Wrong")
print("Program Execution Completed")

print("=" * 50)

# When we Come Across Multiple Errors 
print("Program Execution Started")

data = [1,2,'three',0,4]

for num in data:
    try:
        print(1/num) 
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    except TypeError:
        print("OOPS! Dividing String With Numerics is not supported")
    except ZeroDivisionError:
        print("OOPS! We Got An Error - Check Below Link For More Info")
        print("https://en.wikipedia.org/wiki/Division_by_zero")
        
print("Program Execution Completed")

print("=" * 50)

# else: used to keep the code that should run, if No Exception was raised in try block
# when there is no error with else block 

print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ", num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! We Got An Error - Check Below Link For More Info")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else: 
    print("Calculation Was Successful")

print("Program Execution Completed")

print("=" * 50)

# when there is no error with else block 

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ", num1/num2) # Verifying Login Credentials 
except:
    print("OOPS! We Got An Error - Check Below Link For More Info")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else: 
    print("Calculation Was Successful") # Then Only Check OTP

print("Program Execution Completed")

print("=" * 50)

# finally - Run this code for sure 

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ", num1/num2) # Verifying Login Credentials 
except:
    print("OOPS! We Got An Error - Check Below Link For More Info")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else: 
    print("Calculation Was Successful") # Then Only Check OTP
finally:
    print("Closing All Opened File Streams & Database Connections")
    print("Program Execution Completed")

print("=" * 50)

# finally - Run this code for sure 

print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ", num1/num2) # Verifying Login Credentials 
except:
    print("OOPS! We Got An Error - Check Below Link For More Info")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else: 
    print("Calculation Was Successful") # Then Only Check OTP
finally:
    print("Closing All Opened File Streams & Database Connections")
    print("Program Execution Completed")

print("=" * 50)

# Create Custom Exceptions 
class MyCustomError(Exception):
    pass 

age = int(input("Enter Age: "))
if age < 18:
    print("You Cannot Vote")
else:
    print("You Can Vote")
    
# Create Custom Age Exception
class UnderAgeError(Exception):
    pass 

# Voting App with Custom Age Exception
age = int(input("Enter Age: "))
if age < 18:
    print("You Cannot Vote")
    # raise UnderAgeError # UnderAgeError
else:
    print("You Can Vote")
    
# Voting App with Custom Age Exception and Message
age = int(input("Enter Age: "))
if age < 18:
    print("You Cannot Vote")
    # raise UnderAgeError("Below 18 Cannot Vote") # UnderAgeError: Below 18 Cannot Vote
else:
    print("You Can Vote")

class IDError(Exception):
    pass     

# Voting App with Multiple Custom Exceptions and Message
# age = int(input("Enter Age: "))
# if age < 18:
#    raise UnderAgeError("Below 18 Cannot Vote") # UnderAgeError: Below 18 Cannot Vote 
# else:
#     has_id = input("Do You have ID ? (yes/no) ")
#     if has_id != "yes":
#         raise IDError("Without ID Cannot Vote")
# print("You Can Vote")

# Voting App with Multiple Custom Exceptions and Message -> Handle Exceptions
age = int(input("Enter Age: "))
try:
    if age < 18:
        raise UnderAgeError("Below 18 Cannot Vote") # UnderAgeError: Below 18 Cannot Vote 
    else:
        has_id = input("Do You have ID ? (yes/no) ")
        if has_id != "yes":
            raise IDError("Without ID Cannot Vote")
except UnderAgeError:
    print("You are not 18 yet")
except IDError:
    print("Carrying ID is mandatory")
else:
    print("You Can Vote")
finally:
    print("Program Closed")