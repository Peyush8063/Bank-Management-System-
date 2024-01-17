import csv,os
from typing import List

class BankAccount:
    def __init__(self, account_number: int, name: str, account_type: str, balance: int):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.name}")
        print(f"Type of Account: {self.account_type}")
        print(f"Balance Amount: {self.balance}")

    def modify(self):
        print(f"\t Account Number: {self.account_number}")
        print("\t Modify Account Holder Name: ")
        self.name = input("\t ")
        print("\t Modify Type of Account: ")
        self.account_type = input("\t ")
        print("\t Modify Balance amount: ")
        self.balance = int(input("\t "))

def write_account(accounts: List[BankAccount]):
    with open("accounts.csv", "w", newline="") as csvfile:
        fieldnames = ["account_number", "name", "account_type", "balance"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for account in accounts:
            writer.writerow({
                "account_number": account.account_number,
                "name": account.name,
                "account_type": account.account_type,
                "balance": account.balance
            })

def delete_account(account_number: int, accounts: List[BankAccount]):
    accounts = [account for account in accounts if account.account_number != account_number]
    write_account(accounts)
    print("\t Record Deleted...")

def display_details(account_number: int):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    found = False
    with open("accounts.csv", "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["account_number"].strip() == str(account_number):
                account = BankAccount(int(row["account_number"]), row["name"].strip(), row["account_type"].strip(), int(row["balance"].strip()))
                account.display()
                found = True
                break
    if not found:
        print("\t Account number does not exist")
    else:
        print("\t Details displayed successfully")

    input("Press Enter to return to the main menu...")  # Wait for user input
    

def display_all():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    print("Bank Account Holder List")
    print("====================================================")
    print("A/c no.         NAME         TYPE         BALANCE")
    print("====================================================")
    with open("accounts.csv", "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"{row['account_number'].strip():<10} {row['name'].strip():<16} {row['account_type'].strip():<6} {row['balance'].strip():<6}")
    input("Press Enter to return to the main menu...")  # Wait for user input

def money_deposit_withdraw(account_number: int, option: int, accounts: List[BankAccount]):
    found = False
    amount = int(input("\t Enter the amount: "))
    for account in accounts:
        if account.account_number == account_number:
            if option == 1:
                account.deposit(amount)
            elif option == 2:
                if amount > account.balance:
                    print("\t Insufficient balance")
                else:
                    account.withdraw(amount)
            found = True
            print("\t Record Updated")
            break

    if found:
        write_account(accounts)
    else:
        print("\t Record Not Found")

def transfer_money(from_account_number: int, to_account_number: int, amount: int, accounts: List[BankAccount]):
    from_account = None
    to_account = None

    for account in accounts:
        if account.account_number == from_account_number:
            from_account = account
        elif account.account_number == to_account_number:
            to_account = account

    if from_account is None or to_account is None:
        print("\t One or both accounts not found.")
        return

    if amount > from_account.balance:
        print("\t Insufficient balance in the source account.")
        return

    from_account.withdraw(amount)
    to_account.deposit(amount)

    write_account(accounts)

    print(f"\t Transfer successful: {amount} transferred from Account {from_account_number} to Account {to_account_number}.")


def updation_bank_account(account_number: int, accounts: List[BankAccount]):
    found = False
    for account in accounts:
        if account.account_number == account_number:
            account.modify()
            write_account(accounts)
            print("\t Record Updated")
            found = True
            break
    if not found:
        print("\t Record Not Found")

