from bank_database import BankDatabase
from user_account import UserAccount

class BankApp:
    def __init__(self):
        self.database = BankDatabase()
        self.current_user = None
    def create_account(self):
        print("\n=== Create New Account ===")
        username = input("Enter a username: ").strip()

        if username in self.database.accounts:
            print("That username is already taken. Please try again.")
            return

        bank_number = self.database.generate_bank_number()
        print(f"Your generated bank number is: {bank_number}")
        confirm = input("Confirm account creation? (yes/no): ").lower()

        if confirm == 'yes':
            new_account = UserAccount(username, bank_number)
            self.database.add_account(new_account)
            print(f"Account created for {username} with bank number {bank_number}")
        else:
            print("Account creation cancelled.")
    def login(self):
        print("\n=== Login ===")
        username = input("Username: ").strip()
        try:
            bank_number = int(input("Bank number: "))
        except ValueError:
            print("Invalid bank number format.")
            return

        account = self.database.authenticate(username, bank_number)
        if account:
            self.current_user = account
            print(f"Welcome back, {username}!")
        else:
            print("Login failed. Please check your details and try again.")

if __name__ == "__main__":
    app = BankApp()
    while True:
        print("\n--- Bank App ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            app.create_account()
        elif choice == '2':
            app.login()
        elif choice == '3':
            break
        else:
            print("Invalid option.")
