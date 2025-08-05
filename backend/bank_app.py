from bank_database import BankDatabase
from user_account import UserAccount

class BankApp:
    def __init__(self):
        self.database = BankDatabase()
        self.current_user = None

    def run(self):
        while True:
            if self.current_user:
                self.show_menu()
            else:
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
                    print("Invalid choice. Please try again.")

    def login(self):
        print("\n=== Log In ===")
        username = input("Enter your username: ")
        bank_number = input("Enter your 8-digit bank number: ")

        user = self.database.accounts.get(username)
        if user and str(user.bank_number) == bank_number:
            self.current_user = user
            print(f"\nWelcome back, {username}!")
        else:
            print("\nInvalid username or bank number.")

    def create_account(self):
        print("\n=== Create Account ===")
        username = input("Choose a username: ")

        if username in self.database.accounts:
            print("Username already taken.")
            return

        bank_number = self.database.generate_bank_number()
        account = UserAccount(username, bank_number, 0.0)
        self.database.add_account(account)
        print(f"Account created for {username} with bank number {bank_number}")

    def show_menu(self):
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
        print("\n=== Account Details ===")
        print(f"Username: {self.current_user.username}")
        print(f"Bank Number: {self.current_user.bank_number}")
        print(f"Balance: ${self.current_user.balance:.2f}")

    def deposit(self):
        print("\n=== Deposit ===")
        try:
            amount = float(input("Enter amount to deposit: "))
            self.current_user.deposit(amount)
            self.database.save_accounts()
            print(f"Deposited ${amount:.2f}")
        except ValueError:
            print("Invalid amount.")

    def withdraw(self):
        print("\n=== Withdraw ===")
        try:
            amount = float(input("Enter amount to withdraw: "))
            if self.current_user.withdraw(amount):
                self.database.save_accounts()
                print(f"Withdrew ${amount:.2f}")
            else:
                print("Not enough money.")
        except ValueError:
            print("Invalid amount.")