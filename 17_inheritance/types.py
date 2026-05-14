# Types Of Inheritance

# Without Inheritance
class Father:
    def house(self):
        print("Has House")
        
class Son: # No Inheritance 
    def car(self):
        print("Has Car")
        
son_obj = Son()
son_obj.car()
# son_obj.house() # AttributeError: 'Son' object has no attribute 'house'

print("=" * 50)

# With Inheritance
class Father:
    def house(self):
        print("Has House")
        
class Son(Father): # Single Level Inheritance
    def car(self):
        print("Has Car")
        
son_obj = Son()
son_obj.car()
son_obj.house()

print("=" * 50)

# Multi Level Inheritance: GrandParent -> Parent -> Child 
class GrandFather():
    def land(self):
        print("Has Land")
        
class Father(GrandFather):
    def house(self):
        print("Has House")

class Son(Father): # Multi Level Inheritance
    def car(self):
        print("Has Car")
        
son_obj = Son()
son_obj.car()
son_obj.house()
son_obj.land()

print("=" * 50)

# Multiple Inheritance: One Child -> Multiple Parents 
class GrandFather():
    def land(self):
        print("Has Land")
        
class Father(GrandFather):
    def house(self):
        print("Has House")
        
class Mother():
    def gold(self):
        print("Has Gold")

class Son(Father,Mother): # Multiple Inheritance
    def car(self):
        print("Has Car")
        
son_obj = Son()
son_obj.car()
son_obj.house()
son_obj.land()
son_obj.gold()

print("=" * 50)

# Hierarchical Inheritance: One Parent -> Multiple Child 
class GrandFather():
    def land(self):
        print("Has Land")
        
class Father(GrandFather):
    def house(self):
        print("Has House")
        
class Mother():
    def gold(self):
        print("Has Gold")

class Son(Father,Mother): 
    def car(self):
        print("Has Car")
        
class Daughter(Father):
    def business(self):
        print("Has Business")
        
son_obj = Son()
son_obj.car()
son_obj.house()
son_obj.land()
son_obj.gold()

daughter_object = Daughter()
daughter_object.house()
daughter_object.business()

print("=" * 50)

# Hybrid Inheritance: Combination Of Types Of Inheritance
class A:
    def a(self):
        print("A")
        
class B(A):
    def b(self):
        print("B")
        
class C(A):
    def c(self):
        print("C")
        
class D(B,C):
    def d(self):
        print("D")
        
obj_d = D()
obj_d.a()
obj_d.b()
obj_d.c()
obj_d.d()