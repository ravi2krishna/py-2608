# Nested Loops 

# Generate Math Tables 

# 1 X 1 - 1 X 2 - 1 X 3 - 1 X 4 - 1 X 5 - ........
# 2 X 1 - 2 X 2 - 2 X 3 - 2 X 4 - 2 X 5 - ........
# 3 X 1 - 3 X 2 - 3 X 3 - 3 X 4 - 3 X 5 - ........
# 4 X 1 - 4 X 2 - 4 X 3 - 4 X 4 - 4 X 5 - ........
# 5 X 1 - 5 X 2 - 5 X 3 - 5 X 4 - 5 X 5 - ........

for outer in range(1,6,1):
    print(outer)
for outer in range(1,6,1):
    print(outer)
    
print("=============")

for outer in range(1,6,1):
    print(outer)
    print("-------")
    for inner in range(1,6,1):
        print(inner)
        
print("=============")

for outer in range(1,6,1):
    for inner in range(1,6,1):
        print(f"{outer} X {inner} = {outer * inner}")
        
# Real World Use Case Of Nested Loops 
colors = ["black","red","white"]
sizes = ["uk-6","uk-7","uk-8","uk-9"]
for color in colors:
    for size in sizes:
        print(color +"----"+size)
        

# Generate Math Tables
outer = 1
while outer < 6:
    inner = 1
    while inner < 6:
        print(f"{outer} X {inner} = {outer * inner}")
        inner += 1
    outer += 1