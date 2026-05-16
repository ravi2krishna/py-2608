# Method Overloading Traditional - Fails 

class MathsOps:
    
    def add(self,a,b):
        return a + b 
    
    def add(self,a,b,c):
        return a + b + c 

obj = MathsOps()
# print(obj.add(1,2)) # TypeError: MathsOps.add() missing 1 required positional argument: 'c'
print(obj.add(1,2,3))


class MathsOps:
    
    def add(self,*args):
        return sum(args)
    
obj = MathsOps()
print(obj.add(1,2)) 
print(obj.add(1,2,3))
print(obj.add(1,2,3,4))
print(obj.add(1,2,3,4,5))
        