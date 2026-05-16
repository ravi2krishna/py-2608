# With Abstraction - Abstract Classes 

# Contract Like Behavior 

# Laptop Contract - Government said these are must features for building laptops 

# Concrete Classes 
from abc import ABC,abstractmethod
class Laptop(ABC): # To Achieve abstraction, Create a class that inherits from ABC, 
    
    # Abstract Methods 
    @abstractmethod
    def processor(self):
        pass
    
    @abstractmethod    
    def ram(self):
        pass
    
    @abstractmethod
    def hdd(self):
        pass 
    
    @abstractmethod    
    def nw(self):
        pass
     
# Implementations -> Companies who wants to manufacture laptops        
class Dell(Laptop):
    def processor(self):
        print("Dell")
        print("Laptop")
        print("Processor")
        print("Functionality")
        
    def ram(self):
        print("Dell")
        print("Laptop")
        print("RAM")
        print("Functionality")
    
    def hdd(self):
        print("Dell")
        print("Laptop")
        print("HDD")
        print("Functionality")
    
    # def nw(self):
    #     print("Dell")
    #     print("Laptop")
    #     print("NETWORK")
    #     print("Functionality")
        
class Lenovo(Laptop):
    def processor(self):
        print("Lenovo")
        print("Laptop")
        print("Processor")
        print("Functionality")
        
    def ram(self):
        print("Lenovo")
        print("Laptop")
        print("RAM")
        print("Functionality")
        
    def hdd(self):
        print("Lenovo")
        print("Laptop")
        print("HDD")
        print("Functionality")
        
    def nw(self):
        print("Lenovo")
        print("Laptop")
        print("NETWORK")
        print("Functionality")
        
# End Users 
print("="*50)
print("             Customers Buying Dell Laptop")
dell = Dell() # TypeError: Can't instantiate abstract class Dell without an implementation for abstract methods 'hdd', 'nw'
dell.processor()
dell.ram()
dell.hdd()
dell.nw()
print("="*50)

print("="*50)
print("             Customers Buying Lenovo Laptop")
lenovo = Lenovo()
lenovo.processor()
lenovo.ram()
lenovo.hdd()
lenovo.nw()
print("="*50)