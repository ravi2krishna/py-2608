# Looping Structures / Statements (Iteration Statements)

# while loop 

# while True: # this forms an infinite loop
#     print("Repeat.....")
    # to terminate above loop use control + c 
    
while False:
    print("Repeat.....")
    
# Counters 
count = 1
while count <= 5:
    print("Count is: ",count)
    count += 1
    
# Use While when we don't know number of Iterations/Repetitions in advance

# You Found a lost phone, trying to break passcode
# Tell me at which attempt phone will be unlocked ?

actual_pin = "2345"
user_given_pin = ""

while user_given_pin != actual_pin:
    user_given_pin = input("Enter PIN: ")
print("Phone Unlocked")    


 