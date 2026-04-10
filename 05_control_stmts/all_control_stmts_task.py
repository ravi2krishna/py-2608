# Simulate Authentication Functionality ATM / OTP / Passwords etc 
correct_pin = 2345

attempts = 3

# print(len(correct_pin))
# correct_pin = 2345
# pin_str = str(correct_pin)
# print(len(pin_str))


while attempts > 0:
    print(f"You Have {attempts} Attempts Left")
    user_pin = int(input("Enter Pin: "))
    
    if(len(str(user_pin))) != 4:
        print("Transaction Failed - Pin Must be 4 Digit Number")
        attempts -= 1
        continue
    
    if user_pin == correct_pin:
        print("Transaction Success")
        break 
    else:
        print("Transaction Failed - Incorrect Pin")
        attempts -= 1

else:
    print("Maximum attempt reached, Try after 24 Hours")