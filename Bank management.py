"""
===========================================================
                BANK MANAGEMENT SYSTEM
===========================================================

README
------

Project Name:
Bank Management System

Problem Statement:
The Bank Management System is a simple console-based Python
application designed to manage basic banking operations.
It allows users to create bank accounts, deposit money,
withdraw money, check balance, transfer money and view
account details.

The main purpose of this project is to demonstrate the use
of Python basics such as:
- Variables
- Data types
- Lists and dictionaries
- Functions
- Loops
- Conditional statements
- User input
- Basic error handling

Features:
1. Create a new bank account
2. Display account details
3. Deposit money
4. Withdraw money
5. Check account balance
6. Transfer money
7. Close an account
8. Display all accounts
9. Exit the program

How to Run:
1. Install Python 3 on your computer.
2. Save this file as:
   bank_management_system.py
3. Open the terminal in the same folder.
4. Run:
   python bank_management_system.py

Note:
This is a console-based educational project.
The account data is stored temporarily while the program
is running. When the program is closed, the data will reset.

===========================================================
"""


# Dictionary to store all bank accounts
accounts = {}

# Starting account number
next_account_number = 1001


def create_account():
    global next_account_number

    print("\n========== CREATE ACCOUNT ==========")

    name = input("Enter account holder name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()

    if phone == "":
        print("Phone number cannot be empty.")
        return

    try:
        initial_deposit = float(input("Enter initial deposit: ₹"))

        if initial_deposit < 0:
            print("Deposit cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    account_number = next_account_number

    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "balance": initial_deposit
    }

    next_account_number += 1

    print("\nAccount created successfully!")
    print("Account Number:", account_number)
    print("Account Holder:", name)
    print("Initial Balance: ₹", format(initial_deposit, ".2f"))


def find_account():
    try:
        account_number = int(input("Enter account number: "))

        if account_number in accounts:
            return account_number
        else:
            print("Account not found.")
            return None

    except ValueError:
        print("Please enter a valid account number.")
        return None


def display_account():
    print("\n========== ACCOUNT DETAILS ==========")

    account_number = find_account()

    if account_number is None:
        return

    account = accounts[account_number]

    print("------------------------------------")
    print("Account Number :", account_number)
    print("Account Holder :", account["name"])
    print("Phone Number   :", account["phone"])
    print("Balance        : ₹", format(account["balance"], ".2f"))
    print("------------------------------------")


def deposit_money():
    print("\n========== DEPOSIT MONEY ==========")

    account_number = find_account()

    if account_number is None:
        return

    try:
        amount = float(input("Enter amount to deposit: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    accounts[account_number]["balance"] += amount

    print("\nMoney deposited successfully!")
    print("Deposited Amount: ₹", format(amount, ".2f"))
    print(
        "New Balance: ₹",
        format(accounts[account_number]["balance"], ".2f")
    )


def withdraw_money():
    print("\n========== WITHDRAW MONEY ==========")

    account_number = find_account()

    if account_number is None:
        return

    try:
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    current_balance = accounts[account_number]["balance"]

    if amount > current_balance:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] -= amount

    print("\nWithdrawal successful!")
    print("Withdrawn Amount: ₹", format(amount, ".2f"))
    print(
        "Remaining Balance: ₹",
        format(accounts[account_number]["balance"], ".2f")
    )


def check_balance():
    print("\n========== CHECK BALANCE ==========")

    account_number = find_account()

    if account_number is None:
        return

    balance = accounts[account_number]["balance"]

    print("Account Number:", account_number)
    print("Account Holder:", accounts[account_number]["name"])
    print("Current Balance: ₹", format(balance, ".2f"))


def transfer_money():
    print("\n========== TRANSFER MONEY ==========")

    print("\nEnter sender details:")
    sender = find_account()

    if sender is None:
        return

    print("\nEnter receiver details:")
    receiver = find_account()

    if receiver is None:
        return

    if sender == receiver:
        print("Sender and receiver cannot be the same account.")
        return

    try:
        amount = float(input("Enter amount to transfer: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount > accounts[sender]["balance"]:
        print("Insufficient balance in sender account.")
        return

    accounts[sender]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    print("\nTransfer successful!")
    print("Transferred Amount: ₹", format(amount, ".2f"))
    print("From Account:", sender)
    print("To Account:", receiver)


def close_account():
    print("\n========== CLOSE ACCOUNT ==========")

    account_number = find_account()

    if account_number is None:
        return

    account = accounts[account_number]

    print("\nAccount Holder:", account["name"])
    print("Balance: ₹", format(account["balance"], ".2f"))

    confirmation = input(
        "Are you sure you want to close this account? (yes/no): "
    ).lower()

    if confirmation == "yes":
        del accounts[account_number]
        print("Account closed successfully.")
    else:
        print("Account closing cancelled.")


def display_all_accounts():
    print("\n========== ALL ACCOUNTS ==========")

    if len(accounts) == 0:
        print("No accounts available.")
        return

    print("----------------------------------------------")
    print("Account No.     Name              Balance")
    print("----------------------------------------------")

    for account_number, account in accounts.items():
        print(
            str(account_number).ljust(15),
            account["name"].ljust(18),
            "₹" + format(account["balance"], ".2f")
        )

    print("----------------------------------------------")


def main_menu():
    while True:

        print("\n")
        print("==============================================")
        print("          BANK MANAGEMENT SYSTEM")
        print("==============================================")
        print("1. Create New Account")
        print("2. Display Account Details")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Transfer Money")
        print("7. Close Account")
        print("8. Display All Accounts")
        print("9. Exit")
        print("==============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            display_account()

        elif choice == "3":
            deposit_money()

        elif choice == "4":
            withdraw_money()

        elif choice == "5":
            check_balance()

        elif choice == "6":
            transfer_money()

        elif choice == "7":
            close_account()

        elif choice == "8":
            display_all_accounts()

        elif choice == "9":
            print("\nThank you for using Bank Management System!")
            print("Program closed successfully.")
            break

        else:
            print("\nInvalid choice. Please select 1-9.")


# Program starts here
if __name__ == "__main__":
    main_menu()