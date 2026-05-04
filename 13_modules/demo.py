# Inbuilt Modules 

# 1st Syntax 
# print(math.pi) # NameError: name 'math' is not defined. Did you forget to import 'math'?
import math 
print(math.pi) 
print(math.sqrt(25))

# 2nd Syntax 
from math import sqrt
print(sqrt(25))
# print(pi) # NameError: name 'pi' is not defined

# 2nd Syntax 
from math import sqrt,pi
print(sqrt(25))
print(pi) 