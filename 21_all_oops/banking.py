# Implementing all OOP Principals 
# -> Inheritance
# -> Encapsulation
# -> Abstraction
# -> Polymorphism

class BankAccount:
    def __init__(self,account_no,holder_name,balance):
        self.account_no = account_no # not sensitive
        self.holder_name = holder_name # not sensitive
        self.__balance = balance # sensitive i.e used __ prefix making it private # Encapsulation
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            
    
# Implement Abstraction 
from abc import ABC, abstractmethod 

class Account(ABC):
    
    @abstractmethod
    def deposit(self,amount):
        pass 
    
    @abstractmethod
    def withdraw(self,amount):
        pass     
    
# Implement Inheritance
class SavingsAccount(Account):
    def __init__(self,balance):
        self.__balance = balance
    
    def deposit(self,amount):
        self.__balance += amount
        
    def withdraw(self, amount): # Method Overriding -> Polymorphism 
        if amount <= self.__balance:
            self.__balance -= amount
            
class CurrentAccount(Account):
    def __init__(self,balance,overdraft_limit):
        self.__balance = balance
        self.overdraft_limit = overdraft_limit
        
    def deposit(self,amount):
        self.__balance += amount
        
    def withdraw(self, amount): # Method Overriding -> Polymorphism 
        if amount <= self.__balance + self.overdraft_limit:
            self.__balance -= amount
        else:
            print("Overdraft Limit Exceeded")
            
savings = SavingsAccount()
