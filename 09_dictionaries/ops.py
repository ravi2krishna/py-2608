# Dictionary Methods / Operations 

data = {"a":"apple","b":"banana"}
print(type(data))

# update(): add / update item in dictionary 
print(data)
data.update({"c":"cherry"}) # if key is not present, then adds data 
print(data)

data.update({"a":"apricot"}) # if key is present, then updates data 
print(data)

# pop(): remove an item key 
data = {"a":"apple","b":"banana"}
print(data)
data.pop("a")
print(data)
# data.pop("c") # KeyError: 'c'
# print(data)
# data.pop() # TypeError: pop expected at least 1 argument, got 0

# popitem(): remove last item 
data = {"a":"apple","b":"banana"}
print(data)
data.popitem()
print(data)
# data.popitem("a") # TypeError: dict.popitem() takes no arguments (1 given)

# clear(): Empties Dictionary 
data = {"a":"apple","b":"banana"}
print(data)
data.clear()
print(data)

# get(): used to get value for key 
data = {"a":"apple","b":"banana"}
print(data)
# print(data.get()) # TypeError: get expected at least 1 argument, got 0
print(data.get("b"))
# print(data["c"]) # KeyError: 'c'
print(data.get("c")) # None -> No error when key is not present

# keys(): Used to get keys 
data = {"a":"apple","b":"banana"}
print(data)
print(data.keys())
for key in data.keys():
    print(key)
    
# values(): Used to get values
data = {"a":"apple","b":"banana"}
print(data)
print(data.values())
for value in data.values():
    print(value)
    
# items(): Used to get both keys & values 
data = {"a":"apple","b":"banana"}
print(data)
print(data.items())
# get individual items
for item in data.items():
    print(item)
    
# setdefault(): returns a value of key, if key is already present
# if key is not present, then adds the item and returns value 
data = {"a":"apple","b":"banana"}
print(data)
data.setdefault("b","blueberry")
out = data.setdefault("b","blueberry")
print(out)
print(data)

data = {"a":"apple","b":"banana"}
print(data)
out = data.setdefault("c","cherry")
print(out)
print(data)

# copy(): Create a copy 
data = {"a":"apple","b":"banana"}
print(data)
backup = data.copy()
print(backup)
