# Private Access with Sub Classes

class A:
    def __init__(self,a):
        self.__a = a # private 
        
obj = A(10)

# print(obj.a) # AttributeError: 'A' object has no attribute 'a'

class B(A):
    def showA(self):
        a = A(10)
        print(a.__a) # AttributeError: 'A' object has no attribute
    
obj = B(20)
obj.showA() # This confirms private data cannot be accessed in sub classes 
