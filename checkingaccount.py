import bankaccount
class ChechingAcount(bankaccount.BankAccount):
    def __init__(self,acount_number,inital_balance):
        self.acount_number=acount_number
        self.balance=inital_balance
    def deposit(self,amount):
        self.balance +=amount
        print(f"Deposited :{amount}| into account :{self.acount_number}")
    def withdraw(self,amount):
        if amount >= self.balance:
            print("no many !!")
        else:
            self.balance -= amount
            print(f"withdraw :{amount}| into account :{self.acount_number}")

    def get_blanace(self):
        return self.balance
