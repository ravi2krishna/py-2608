# Without Abstraction - Concrete Classes 

# Contract Like Behavior 

# Laptop Contract - Government said these are must features for building laptops 

# Concrete Classes 
class Laptop:
    
    # Concrete Methods 
    def processor(self):
        print("Laptop")
        print("Processor")
        print("Functionality")
        
    def ram(self):
        print("Laptop")
        print("RAM")
        print("Functionality")
    
    def hdd(self):
        print("Laptop")
        print("HDD")
        print("Functionality")
        
    def nw(self):
        print("Laptop")
        print("NETWORK")
        print("Functionality")
     
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
        
class Lenovo(Laptop):
    def hdd(self):
        print("Dell")
        print("Laptop")
        print("HDD")
        print("Functionality")
        
    def nw(self):
        print("Dell")
        print("Laptop")
        print("NETWORK")
        print("Functionality")
        
# End Users 
print("="*50)
print("             Customers Buying Dell Laptop")
dell = Dell()
dell.processor()
dell.ram()
print("="*50)

print("="*50)
print("             Customers Buying Lenovo Laptop")
lenovo = Lenovo()
dell.hdd()
dell.nw()
print("="*50)