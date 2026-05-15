# Protected Access with Sub Classes

class A:
    def __init__(self,a):
        self._a = a # protected 
        
obj = A(10)

# print(obj.a) # AttributeError: 'A' object has no attribute 'a'
# With above we can say protected also cannot be accessed outside 

class B(A):
    def showA(self):
        a = A(10)
        print(a._a) # AttributeError: 'A' object has no attribute
    
obj = B(20)
obj.showA() # This confirms private data cannot be accessed in sub classes 

