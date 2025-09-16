import bank
import optmer_savingsaccount
import optmer_ChechingAcount

if __name__ == "__main__":
    bank_1 = bank.Bank()
    optm_sav = optmer_savingsaccount.OptimerSavigsAccount()
    optm_Che = optmer_ChechingAcount.OptimerCheckingAccount()

    print("Sign in :")
    print("=====================")
    account_1 = input("Enter account: ")
    password = input("Enter password: ")

    print("WOO!")
    print("Sign UP:")
    account_1_2 = input("Enter account: ")
    password_1 = input("Enter password: ")

    if account_1_2 == account_1 and password_1 == password:
        print("hello!")

        while True:
            print("ntransactions=1 | add account=2 | exit=0")
            trans_account = input("Enter 1, 2 or 0: ")

            if trans_account == '2':
                print("Savingsaccount=2 | Checkingaccount=1")
                account_Tayp = input("Enter account_Tayp: ")
                optm_Che.account_Tayp(account_Tayp)
                optm_sav.account_Tayp(account_Tayp)
                optm_sav.optim()

            elif trans_account == '1':
                while True:
                    transfer_account = input("Transfer account: ")
                    receiving_account = input("Receiving account: ")
                    amount_x = float(input("Enter amount: "))
                    bank_1.transfer(transfer_account, receiving_account, amount_x)

                    print("exit=1 | loop=2")
                    user_exit = input("Enter exit or loop: ")
                    if user_exit == "1":
                        break

            elif trans_account == '0':
                print("Goodbye!")
                break

            else:
                print("Invalid choice, try again.")
    else:
        print("Error")
