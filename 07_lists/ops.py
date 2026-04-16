# List Methods / Operations 

# append(): Adds elements to end of the list
data = [10,20,30,40,50]
print(data)
data.append(60)
print(data)

# extend(): Adds Iterable To List 
data = [10,20,30,40,50]
print(data)
data.extend([60,70,80,90,100])
print(data)

# insert(): Add element at specific position based on index 
data = [10,20,40,50]
print(data)
# data.append(30)
data.insert(2,30)
print(data)

# pop(): Remove an element, by default last element
# If index is provided, removes specific element
data = [10,20,30,40,50]
print(data)
data.pop()
print(data)

data = [10,20,30,40,50]
print(data)
data.pop(0)
print(data)

# remove(): Remove an element, based on value
data = [10,20,30,40,50]
print(data)
# data.remove(0) # ValueError: list.remove(x): x not in list
data.remove(40)
print(data)

# Requirement: Remove all Occurrences Of 10
data = [10,20,30,10,40,50,10]
print(data)
while 10 in data:
    data.remove(10)
print(data)

# clear(): Removes all elements and empties list 
data = [10,20,30,10,40,50,10]
print(data)
data.clear()
print(data)

# index(): Used To get index position of value 
data = [10,20,30,40,50]
print(data)
print(data.index(30))

# count(): Count the number of occurrences 
data = [10,20,30,10,40,50,10]
print(data)
print(data.count(10))

# reverse(): Reverses the list 
data = [10,20,30,40,50]
print(data)
data.reverse()
print(data)

# sort(): Sorts the list, default is Ascending Order 
data = [10,30,20,50,40]
print(data)
data.sort()
print(data)

data = [10,30,20,50,40]
print(data)
data.sort(reverse=True)
print(data)

# copy(): Create a backup copy
data = [10,20,30,40,50]
print(data)
backup_copy = data.copy()
print(backup_copy)

# PAN 
pan = ["AIOKL9967D","IOPVB0054G"]
print(pan)
pan[0] = "ANPKL9967D"
pan[1] = "DFPVB0054G"
print(pan)