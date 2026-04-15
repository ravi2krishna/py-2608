# String Methods / Operations 

# data = "python"
# print(dir(data))

# Simulate Gmail Functionality 
#              RavI2KRIshnA -> ravi2krishna@gmail.com
email = input("Enter Email ID: ")
print("Original Email: "+email)
# lower(): Converts the entire string to lowercase
formatted_email = email.lower()
print("Transformed Email: "+formatted_email)
# strip() method to remove whitespace from both ends
formatted_email = formatted_email.strip()
print("Transformed Email: "+formatted_email)
# concatenation join strings 
domain = "@gmail.com"
formatted_email = formatted_email + domain
print("Transformed Email: "+formatted_email)


# Simulate PAN Functionality 
# https://www.pan.utiitsl.com/panonline_ipg/forms/csfPan.html/csfPreForm
# https://www.pan.utiitsl.com/PANform/forms/csf/preCSF
pan = input("Enter Your PAN Card ID: ")
print("Original PAN: "+pan) # $ampui9916s

# isalnum(): returns True if all characters in the string are alphanumeric (letters or numbers) 
valid_pan = pan.isalnum()
print(f"Given {pan} is {valid_pan}")

# logics are check for alphanumeric and also for length i.e 10 
if pan.isalnum() and len(pan) == 10:
    print("Original PAN: "+pan)
    # upper(): Converts the entire string to uppercase
    print("Formatted PAN: "+pan.upper())
else:
    print(f"Given PAN {pan} is Invalid")

# Simulate Phone ISD Scenario 
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png
# https://www.businessbloomer.com/wp-content/uploads/2014/11/woocommerce-add-coupon-automatically-to-cart-if-product.png

# startswith() method returns True if the string starts with the specified value, otherwise False.
mobile = input("Enter Mobile Number Starting With ISD Code: ")
india_number = mobile.startswith("+91")
print(f"Indian Number {india_number}")

if mobile.startswith("+91"):
    print("Calling Indian Number - Charged In Rupees")
elif mobile.startswith("+33"):
    print("Calling France Number - Charged In Euros")  
elif mobile.startswith("+1"):
    print("Calling USA Number - Charged In Dollars")      
else:
    print("Invalid Number - Only India, France and USA Supported")

    
# Simulate Email Synchronization 
# endwith() method returns True if the string ends with the specified value, otherwise False.
source_email = input("Enter Source Email ID: ")
source_email_status = source_email.endswith("@gmail.com")
destination_email = input("Enter Destination Email ID: ")
print(f"Email Is Gmail {source_email_status}")
if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("Email Backup Process Started")
else:
    print("Email Backup Process Failed - Source & Destination Didn't Match")
   
    
# Simulate Data Operations Work: CSV Data from a file and perform some operations 
# https://www.datablist.com/learn_images/csv/google_sheet_csv.png
# https://www.slashgear.com/img/gallery/csv-files-explained-what-they-are-and-how-to-open-them/what-are-csv-files-1699455969.jpg
# Name,Email,Age,City,Job_Role
# emp_data = "Johnny,john@apple.com,45,Hyd,Developer"
# Requirement: Display Employee Name & Job Role 
emp_data = "Johnny,john@apple.com,45,Hyd,Developer"
emp_name = emp_data[0]
print("Employee Name: ",emp_name)

emp_name = emp_data[0:6]
print("Employee Name: ",emp_name)

emp_data = "Ravi,ravi@apple.com,45,Hyd,Admin"
emp_name = emp_data[0:6]
print("Employee Name: ",emp_name)

# Using Above Approach we are hard coding logic, which is not good practice 

# split() method is used to break a string into a list of smaller strings 
# based on a specific separator default is space
emp_data = "Johnny john@apple.com 45 Hyd Developer"
emp_data = "Ravi ravi@apple.com 45 Hyd Admin"
emp_data = "Johnny john@apple.com 45 Hyd Developer"
emp_data_extraction = emp_data.split()
print(emp_data_extraction)
print("Employee Name: ",emp_data_extraction[0])

emp_data = "Krishna,ravi2krishna@gmail.com,34,Hyd,Developer"
emp_data_extraction = emp_data.split(",")
print(emp_data_extraction)
print("Employee Name: ",emp_data_extraction[0])
print("Employee Role: ",emp_data_extraction[-1])

# Simulate Amazon Order Email Confirmation Template Based System
order_template = "Hello your order with order_id has been shipped"
order_ids = "AMZ-123,AMZ-234,AMZ-345,AMZ-456,AMZ-567"
order_ids_extracted = order_ids.split(",")
# print(dir(order_id_extracted)) # __iter__
for order_id in order_ids_extracted:
    # replace(): To replace substrings in a Python string -> replace(old, new)
    send_email = order_template.replace("order_id",order_id)
    print(send_email)
    
