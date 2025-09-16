# 🏦 Mini Banking System (Python)

## 📌 Overview
This project is a simple **Banking System** implemented in Python using **Object-Oriented Programming (OOP)** and **Abstract Classes**.  
It simulates real-world banking operations such as:
- Creating **Checking** and **Savings** accounts.
- Depositing and withdrawing money.
- Adding interest for savings accounts.
- Transferring money between accounts.

The system is interactive via the terminal.

---

## 📂 Project Structure
.
├── main.py # Entry point of the project
├── bank.py # Bank class (manage accounts & transfers)
├── bankaccount.py # Abstract base class for accounts
├── chechingaccount.py # Checking account implementation
├── savingsaccount.py # Savings account implementation
├── optmer_ChechingAcount.py # Interactive Checking Account manager
├── optmer_savingsaccount.py # Interactive Savings Account manager


---

## ⚙️ Features
- **Authentication** (Sign in / Sign up).
- **Checking Account**:
  - Deposit & Withdraw.
- **Savings Account**:
  - Deposit & Withdraw.
  - Add Interest.
- **Bank Operations**:
  - Add accounts.
  - Transfer money between accounts.
  - Check balance.

---

## ▶️ How to Run
1. Clone this repository or copy the files.
2. Run the main program:

```bash
python main.py
Follow the interactive menu:

Sign in / Sign up.

Add account (Savings or Checking).

Perform transactions (deposit, withdraw, transfer).

Exit when done.

📝 Example Flow
Sign in :
=====================
Enter account: user1
Enter password: 123
WOO!
Sign UP:
Enter account: user1
Enter password: 123
hello!

transactions=1 | add account=2 | exit=0
Enter 1, 2 or 0: 2
Savingsaccount=2 | Checkingaccount=1
Enter account_Tayp: 1
enter account_number: 101
enter amount: 500
...
🔮 Future Improvements
Store account data in a database or file (instead of memory).

Add authentication system with encrypted passwords.

GUI using Tkinter or PyQt.

Unit tests for core banking logic.

👨‍💻 Author
Developed by Abdullah as a practice project for learning Python OOP and banking system simulation.
