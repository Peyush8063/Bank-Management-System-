import csv,os


from Logic import * 

if not os.path.isfile("accounts.csv"):
    with open("accounts.csv", "w", newline="") as csvfile:
        fieldnames = ["account_number", "name", "account_type", "balance"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

accounts = []
with open("accounts.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        account = BankAccount(int(row["account_number"]), row["name"], row["account_type"], int(row["balance"]))
        accounts.append(account)

while True:
    print("\t\t ---------------------------------------")
    print("\t\t | Welcome to the Bank Management System |")
    print("\t\t ---------------------------------------")
    print("\n\t --- Main Menu ---")
    print("\t 1. Create Account")
    print("\t 2. Deposit Money")
    print("\t 3. Withdraw Money")
    print("\t 4. Balance Enquiry")
    print("\t 5. All Account Holder List")
    print("\t 6. Close an Account")
    print("\t 7. Modify an Account")
    print("\t 8. Transfer Money")
    print("\t 9. Exit")
    print()

    choice = input("\t Enter your choice (1-8): ")

    if choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear') 
        account_number = int(input("\t Enter the account number: "))
        name = input("\t Enter the name of the account holder: ")
        account_type = input("\t Enter the type of the account (C/S): ")
        balance = int(input("\t Enter the initial amount: "))
        account = BankAccount(account_number, name, account_type, balance)
        accounts.append(account)
        write_account(accounts)
        print("\t Account Created!")
        input("\t Press Enter to return to the main menu...")  # Wait for user input

    elif choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear') 
        account_number = int(input("\t Enter the account number: "))
        money_deposit_withdraw(account_number, 1, accounts)
        print("\t Money Deposited!")
        input("\t Press Enter to return to the main menu...")  # Wait for user input


    elif choice == '3':
        os.system('cls' if os.name == 'nt' else 'clear') 
        account_number = int(input("\t Enter the account number: "))
        money_deposit_withdraw(account_number, 2, accounts)
        print("\t Money Withdrawn!")
        input("\t Press Enter to return to the main menu...")  # Wait for user input


    elif choice == '4':
        os.system('cls' if os.name == 'nt' else 'clear') 
        account_number = int(input("\t Enter the account number: "))
        display_details(account_number)

    elif choice == '5':
        display_all()

    elif choice == '6':
        os.system('cls' if os.name == 'nt' else 'clear') 
        account_number = int(input("\t Enter the account number: "))
        delete_account(account_number, accounts)
        input("\t Press Enter to return to the main menu...")  # Wait for user input

    elif choice == '7':
        os.system('cls' if os.name == 'nt' else 'clear') 
        account_number = int(input("\t Enter the account number: "))
        updation_bank_account(account_number, accounts)
        input("\t Press Enter to return to the main menu...")  # Wait for user input

    elif choice=='8':
        os.system('cls' if os.name == 'nt' else 'clear') 
        source_account_number = int(input("\t Enter the source account number: "))
        destination_account_number = int(input("\t Enter the destination account number: "))
        transfer_amount = int(input("\t Enter the amount to transfer: "))

        transfer_money(source_account_number, destination_account_number, transfer_amount, accounts)
        input("\t Press Enter to return to the main menu...")  # Wait for user input


    else:
        print("\t Thanks for using the Bank Management System")
        break
