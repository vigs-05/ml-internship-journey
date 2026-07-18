class Account:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no
        
    # debit method
    def get_debit(self,debit_amount):
        self.debit_amount = debit_amount
        if (self.debit_amount<self.balance):
            self.balance = self.balance - self.debit_amount
            print("AMOUNT OF",self.debit_amount,"IS DEBITED AND REMAINING BALANCE IS",self.balance)  
        else:
            print("NOT SUFFICIENT BALANCE")
    
    #credit method
    def get_credit(self,credit_amount):
        self.credit_amount = credit_amount
        self.balance = self.balance + self.credit_amount
        print("AMOUNT OF",self.credit_amount,"IS CREDITED AND NEW BALANCE IS", self.balance)
    
    # printing balance
    def get_balance(self):
        print("ACCOUNT BALANCE IS",self.balance)
        
customer1 = Account(10000,1234)
customer2 = Account(1000,1264)
customer3 = Account(10000,1234)

customer1.get_debit(5000)
customer1.get_credit(6000)
customer1.get_balance()

        
        
        