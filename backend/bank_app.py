from backend.bank_database import BankDatabase
from backend.user_account import UserAccount
import os

class BankApp:
    def __init__(self):
        self.database = BankDatabase()
        self.current_user = None

    def run(self):
        while True:
            if self.current_user:
                os.system("clear")
                self.show_menu()
            else:
                os.system('clear')
                print("\n=== Welcome to the Bank App ===")
                print("1. Log in")
                print("2. Create an account")
                print("3. Exit")
                choice = input("Choose an option: ")

                if choice == "1":
                    self.login()
                elif choice == "2":
                    self.create_account()
                elif choice == "3":
                    print("Goodbye!")
                    break
                else:
                    input("Invalid choice. Please press enter to try again.")

    def login(self):
        os.system("clear")
        print("\n=== Log In ===")
        username = input("Enter your username: ")
        bank_number = input("Enter your 8-digit bank number: ")

        user = self.database.accounts.get(username)
        if user and str(user.bank_number) == bank_number:
            self.current_user = user
            os.system("clear")
            print(f"\nWelcome back, {username}!")
            input("Press Enter to continue to menu")
        else:
            input("Invalid username or bank number. Please press Enter to try again.")

    def create_account(self):
        os.system("clear")
        print("\n=== Create Account ===")
        username = input("Choose a username: ")

        if username in self.database.accounts:
            print("Username already taken.")
            input("Press Enter to try agian")
            return

        bank_number = self.database.generate_bank_number()
        account = UserAccount(username, bank_number, 0.0)
        self.database.add_account(account)
        print(f"Account created for {username} with bank number {bank_number}")
        input("\nPress Enter to log in")

    def show_menu(self):
        os.system("clear")
        print(f"\n=== {self.current_user.username}'s Menu ===")
        print("1. View account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Log out")
        choice = input("Choose an option: ")

        if choice == "1":
            self.view_account()
        elif choice == "2":
            self.deposit()
        elif choice == "3":
            self.withdraw()
        elif choice == "4":
            print(f"Logged out from {self.current_user.username}'s account.")
            self.current_user = None
        else:
            print("Invalid choice.")

    def view_account(self):
        os.system("clear")
        print("\n=== Account Details ===")
        print(f"Username: {self.current_user.username}")
        print(f"Bank Number: {self.current_user.bank_number}")
        print(f"Balance: ${self.current_user.balance:.2f}")
        print("========================")
        input("\nPress Enter to return to menu")

    def deposit(self):
        os.system("clear")
        print("\n=== Deposit ===")
        try:
            amount = float(input("Enter amount to deposit: "))
            self.current_user.deposit(amount)
            self.database.save_accounts()
            print(f"Deposited ${amount:.2f}")
            print(f"Balance ${self.current_user.balance:.2f}")
            input("\nPress Enter to return to menu")
        except ValueError:
            print("Invalid amount.")
            input("\nPress Enter to return to try agian")
            self.deposit()

    def withdraw(self):
        os.system("clear")
        print("\n=== Withdraw ===")
        try:
            print(f"Current balance ${self.current_user.balance:.2f}")
            amount = float(input("Enter amount to withdraw: "))
            if self.current_user.withdraw(amount):
                self.database.save_accounts()
                print(f"Withdrew ${amount:.2f}")
                input("\nPress Enter to return to menu")
            else:
                print("Not enough money.")
                input("\nPress Enter to return to menu")
        except ValueError:
            print("Invalid amount.")
            input("\nPress Enter to try agian")
            self.withdraw()