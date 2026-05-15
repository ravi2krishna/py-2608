# Private Means No Access Outside

class A:
    def __init__(self,a):
        self.__a = a # private double underscore __ 
        
obj = A(10)

# print(obj.a) # AttributeError: 'A' object has no attribute 'a'

# print(obj._A__a) # “You shouldn’t, but you can if you insist”

class CreditCard:
    def __init__(self,card_number,card_pin):
        self.__card_number = card_number # Private
        self.__card_pin = card_pin # Private 