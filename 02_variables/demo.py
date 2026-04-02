# Variables 

# Assign Data (Store Data)
student_name = "Ravi" # String
student_age = 20 # int 
student_gpa = 9.5 # float 
student_passed = True # Boolean True / False 
STUDENT_AADHAR = None # Absence Of Value 

# Retrieve Data (Get Data)
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)
print(STUDENT_AADHAR)

# Retrieve Data (Get Data) 
# Concatenation: Joining Strings Using + Operator 
print("=========== Student Info ===========")
# print("Student Name: Krishna") # Static
print("Student Name: " + student_name) # Dynamic
# print("Student Age: " + student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age: ", student_age)
print("Student GPA: ", student_gpa)
print("Student PAssed: ", student_passed)
print("Student AADHAR ID: ", STUDENT_AADHAR)
print("=========== Student Info ===========")

# type(): Used to tell Data Type
type(student_name)
print(type(student_name)) # student_name is an object of String Class 
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))
print(type(STUDENT_AADHAR))

# id(): Used to get Memory Address 
id(student_name)
print(id(student_name))
print(id(student_age))
print(id(student_gpa))
print(id(student_passed))
print(id(STUDENT_AADHAR))

print("===================")

# Memory Model In Python 
value_x = 10 
print(id(value_x))

value_y = 100 
print(id(value_y))

value_z = 10 
print(id(value_z))