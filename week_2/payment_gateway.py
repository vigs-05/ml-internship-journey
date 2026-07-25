from abc import ABC, abstractmethod
class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass
    
class CreditCard(Payment):
    
    def pay(self,amount):
        self.amount = amount
        print(f"Paid ₹{self.amount} via Credit Card")
        
class Cash(Payment):
    
    def pay(self, amount):
        self.amount = amount
        print(f"Paid ₹{self.amount} via Cash")
 
my_obj = Cash()
my_obj.pay(40000)
my_obj = CreditCard()
my_obj.pay(5000)
