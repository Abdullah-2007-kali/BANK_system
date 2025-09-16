import bank
import chechingaccount as ca

bank_1 = bank.Bank()

class OptimerCheckingAccount:
    def __init__(self):
        self.account_number = None

    def account_Tayp(self, account_Tayp):
        if account_Tayp == "1":
            while True:
                account_number = input("enter account_number: ")
                mount = int(input("enter amount: "))
                checking_account = ca.ChechingAcount(account_number, mount)
                bank_1.add_account(checking_account)
                self.account_number = account_number
                print("exit=1 | loop=2")
                user_exit = input("enter exit or loop: ")
                if user_exit == "1":
                    break

        while True:
            print("deposit=1 | withdraw=2 | exit=3")
            operation = input("enter operation: ")
            if operation == "3":
                break
            elif operation == "1":
                mount_operation = int(input("enter amount: "))
                bank_1.deposit(self.account_number, mount_operation)
            elif operation == "2":
                mount_operation = int(input("enter amount: "))
                bank_1.withdraw(self.account_number, mount_operation)
