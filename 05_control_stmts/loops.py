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

# for loop 
prices_products = [1000,1500,2000,2500,10000] 
# Some Offer is running -> Provide a discount of 500 on each product 
# In list we have index which starts from zero, and keeps going on 
print(prices_products)
# print(prices_products[index])
print(prices_products[0])
print(prices_products[1])
# Prices After Discount
print("Prices After Discount")
print(prices_products[0] - 500)
print(prices_products[1] - 500)
print(prices_products[2] - 500)
print(prices_products[3] - 500)
print(prices_products[4] - 500)

# Say we have 1000 products 
# print(prices_products[999] - 500)

print("==============")

# for loop -> 1000 products 
prices_products = [1000,1500,2000,2500,10000,12000,15000,18000,20000] 
for price in prices_products:
    print(price)

print("Prices After Discount")
for price in prices_products:
    print(price - 500)

    
# Say Hello
print("Hello")

# Now Say Hello 10 Times 
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

# Now Say Hello 1000 Times 

for num in range(0,5,1):
    print(num)
    
for num in range(10,15,1):
    print(num)
    
for num in range(5):
    print(num)
    
for num in range(2,5):
    print(num)

for num in range(5,50,5):
    print(num)
    
for num in range(1,10,1):
    print(num)
    
for num in range(1,10,-1):
    print(num)
    
for num in range(10,1,-1):
    print(num)
    
# Now Say Hello 1000 Times 
for num in range(1,1001,1):
    print("Hi: ", num)
