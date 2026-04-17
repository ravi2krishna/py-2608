# Tuples Methods / Operations 

# index(): Used To get index position of value 
data = (10,20,30,40,50)
print(data)
print(data.index(30))

# count(): Count the number of occurrences 
data = (10,20,30,10,40,50,10)
print(data)
print(data.count(10))

# PAN 
pan = ["AIOKL9967D","IOPVB0054G"] # Lists are Mutable 
print(pan)
pan[0] = "ANPKL9967D"
pan[1] = "DFPVB0054G"
print(pan)

# New Requirement: Do Not Allow Updating AADHAR_ID or PAN_ID
pan = ("AIOKL9967D","IOPVB0054G") # Lists are Mutable 
print(pan)
pan[0] = "ANPKL9967D" # TypeError: 'tuple' object does not support item assignment
pan[1] = "DFPVB0054G"
print(pan)