import csv
import random
from user_account import UserAccount

class BankDatabase:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def load_accounts(self):
        try:
            with open("bank.csv", mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    account = UserAccount.from_dict(row)
                    self.accounts[account.username] = account
        except FileNotFoundError:
            open("bank.csv", 'w').close()  # Create file if missing

    def save_accounts(self):
        with open("bank.csv", mode='w', newline='') as file:
            fieldnames = ['username', 'bank_number', 'balance']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for account in self.accounts.values():
                writer.writerow(account.to_dict())

    def add_account(self, account):
        self.accounts[account.username] = account
        self.save_accounts()

    def generate_bank_number(self):
        existing_numbers = {account.bank_number for account in self.accounts.values()}
        while True:
            number = random.randint(10_000_000, 99_999_999)
            if number not in existing_numbers:
                return number
            
    def authenticate(self, username, bank_number):
        account = self.accounts.get(username)
        if account and account.bank_number == bank_number:
            return account
        return None