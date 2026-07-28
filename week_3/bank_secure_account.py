class BankAccount:
    
    def __init__(self):
        self.__balance = 0 # Private variable or instance
        
    # Getter ie to get balance
    @property
    def balance(self):
        return self.__balance
    
    # Setter to set or modify the private data variable or instance
    @balance.setter
    def balance(self,amount):
        if(amount < 0):
            print("ERROR : Cannot set negative balance !!!")
        else:
            self.__balance = amount

acc = BankAccount()
print(acc.balance)
acc.balance = 1000
print(acc.balance)
acc.balance = -500
    
