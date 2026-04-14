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