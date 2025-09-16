import bankaccount
class Bank:
    def __init__(self):
        self.accounts=[]
    def add_account(self,account:bankaccount.BankAccount):
        self.accounts.append(account)

    def deposit(self,acount_number,amount):
        for account in self.accounts:
            if account.acount_number ==acount_number:
                account.deposit(amount)
                break
    def withdraw(self,acount_number,amount):
        for account in self.accounts:
            if account.acount_number ==acount_number:
                account.withdraw(amount)
                break
    def get_blanace(self,acount_number):
        for account in self.accounts:
            if account.acount_number ==acount_number:
                return account.get_blanace()
            return None
