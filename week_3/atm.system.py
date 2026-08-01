from abc import ABC,abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def deduct_funds(self,amount):
        pass

class SavingsAccount(BankAccount):
    
    def __init__(self,initial_balance,pin):
        self.__pin = pin
        self.__balance = initial_balance
    
    @property    
    def pin(self):
        return "****"
    
    @property
    def balance(self):
        return self.__balance
    
    def deduct_funds(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
            return False

        if amount > self.__balance:
            print("INSUFFICIENT FUNDS!!!")
            return False
        
        self.__balance -= amount
        return True
    
    def verify_pin(self,entered_pin):
        return entered_pin == self.__pin 
    
class Screen:
    
    def welcome(self):
        print("-" * 50 ,"WELCOME TO THE ATM","-" * 50)
        
    """ Screen Display options like Pin , Balanace , Exit """
    
    def menu(self):
        print("1. BALANCE ")
        print("2. WITHDRAW ")
        print("3. EXIT")
        
class CashDispenser:
    
    def dispense(self,amount):
        if amount > 0 :
            print(f"Please take your cash : ₹{amount}")
        else:
            print("AMOUNT CANNOT BE NEGATIVE...")
        
class ATM:
    
    def __init__(self,bank_account_object):
        self.account = bank_account_object
        self.screen = Screen()
        self.cash_dispenser = CashDispenser()
        
    def start(self):
        self.screen.welcome()
        
        entered = input("Enter Pin: ")
        if not self.account.verify_pin(entered):
            print("WRONG PIN....!!!")
            return
        while True:
            self.screen.menu()
            choice = int(input("Choose option : "))
            if choice == 1 :
                print(f"Balance : "  , self.account.balance)
            elif choice == 2 :
                amount = int(input("Enter Amount : "))
                if self.account.deduct_funds(amount):
                    self.cash_dispenser.dispense(amount)
            elif choice == 3:
                break
            else :
                print("INVALID CHOICE TRY AGAIN!!!")
                

my_account = SavingsAccount(5000,"5555")
my_atm = ATM(my_account)
my_atm.start()
