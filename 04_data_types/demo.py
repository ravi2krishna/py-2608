# Data Types 

# Numeric Types 
data = 10
print(type(data))

data = -10
print(type(data))

data = 10.5
print(type(data))

data = -10.5
print(type(data))

# data = 3 + i5 # a + ib # NameError
# print(type(data))

data = 3 + 5j # a + bj
print(type(data))

data = True 
print(type(data))

data = False
print(type(data))

data = None 
print(type(data))

data = "python"
print(type(data))

# Complex Data Types 

# List 
data = [10,20,30,40,50]
print(type(data))

# Tuple 
data = (10,20,30,40,50)
print(type(data))

# Set 
data = {10,20,30,40,50}
print(type(data))

# Frozenset
data = frozenset({10,20,30,40,50})
print(type(data))

# Dictionary 
# Just like english dictionary word: explanation 
data = {"course":"python","time":7,"duration":60}
print(type(data))
print(data)

# Custom Data Type
class Student: # Class Creation i.e Blue Print
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_gpa = 9.3
    student_enrolled_courses = ["Python","DevOps","AI"]    
    
data = Student() # Object Creation
print(type(data))
print(data)
print(data.student_email)
print(data.student_enrolled_courses)

print("=================")

# Type Conversion / Implicit Conversion [ Automatic ]
n1 = 10 # int 
n2 = 5.5 # float 
sum = n1 + n2 # int / float 
print(sum) # 15.5 NO DATA LOSS
print(type(sum))

# Type Casting / Explicit Conversion [ Manual ]
price = 1120.85 # float 
print(price)
print(type(price))
round_off_price =  int(price) # int -> datatype(value) 
print(round_off_price)
print(type(round_off_price))

# Some User In a Web Page Was Filling Some Form (Text Boxes) that will be Strings 
rating = "5"
# Convert rating to int
rating = int(rating)
if rating >= 4: # TypeError: '>=' not supported between instances of 'str' and 'int'
    print("Positive Feedback")
else:
    print("Negative Feedback")
    
