# Nested Conditionals 

# inner condition is only checked if the outer condition is true

if True:
    print("1")
if True:
    print("This is not Nested Condition")
    
if True:
    print("1")
    if True:
        print("This is Nested Condition")
        
if False:
    print("1")
    if True:
        print("This is Nested Condition")
        
# Nested Conditionals Use Case
age = int(input("Enter Your Age: "))
if age >= 18:
    has_id = input("Do You Have ID (yes/no): ")
    if has_id == "yes":
        print("You Can Vote")
    else:
        print("You Cannot Vote Without ID")
else:
    print("You Cannot Vote With Under Age")