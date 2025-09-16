import bankaccount
class SavingsAccount(bankaccount.BankAccount):
    def __init__(self, acount_number, inital_balance,interest_rate):
        self.acount_number = acount_number
        self.balance = inital_balance
        self.interest_rate=interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited :{amount}| into account :{self.acount_number}")

    def withdraw(self, amount):
        if amount >= self.balance:
            print("no many !!")
        else:
            self.balance -= amount
            print(f"withdraw :{amount}| into account :{self.acount_number}")

    def get_blanace(self):
        return self.balance
    def add_interest(self):
        interest= self.balance *(self.interest_rate)/100
        self.balance +=interest
        print(f"add_interest :{interest}| into account :{self.acount_number}")
