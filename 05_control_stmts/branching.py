# Branching Structures / Statements (Jump Statements)

for num in range(1,11):
    print(num)

print("========")    

# break - helps you exit the loops
for num in range(1,11):
    # stop the loop when num is 5
    if num == 5:
        break 
    print(num)

print("========") 
    
# continue - helps you skip the current iteration 
for num in range(1,11):
    # skip the iteration when num is 5
    if num == 5:
        continue 
    print(num)
    
print("========")

# pass - acts as a placeholder, does nothing
# Requirement - To Perform Some Operations In Future
# When Salary is above 25000, we want to do something 
# That something as of now we have no idea 
# emp_salary = 15000
# if emp_salary > 25000: # IndentationError: expected an indented block after 'if' statement on line 31
    
emp_salary = 15000
if emp_salary > 25000: 
    pass # _______ 

# Other Operations To Work On 
print("Working With Next Feature / Functionality")

# After 6 Months 
# When Salary is above 25000, we want to do something 
# something is Promoted To Senior Employee
emp_salary = 35000
if emp_salary > 25000: 
    print("Promoted To Senior Employee - Additional Benefits") 

print("========")
   
# When Working With OOP 
# class Employee: # IndentationError: expected an indented block after class definition on line 50

class Employee:
    pass

class Manager:
    pass

class Developer:
    pass