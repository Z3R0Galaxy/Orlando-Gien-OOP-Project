from user_account import UserAccount
from bank_database import BankDatabase

#Create a user account
alex = UserAccount("alex123", 12345678, 1000.0)
print("Account created:", alex.username == "alex123", alex.balance == 1000.0)

#Deposit funds
alex.deposit(500.0)
print("Deposit successful:", alex.balance == 1500.0)

#Withdraw funds
withdraw_success = alex.withdraw(300.0)
print("Withdraw successful:", withdraw_success, alex.balance == 1200.0)

#Withdraw too much
withdraw_fail = alex.withdraw(5000.0)
print("Withdraw failed as expected:", not withdraw_fail, alex.balance == 1200.0)

#Add account to BankDatabase and save
db = BankDatabase()
db.accounts[alex.username] = alex
db.save_accounts()
print("Account saved to CSV")

#Load accounts into a new database
db_loaded = BankDatabase()
loaded_account = db_loaded.accounts.get("alex123")
print("Account loaded from CSV:", loaded_account is not None)

#Loaded account data matches original
if loaded_account:
    print("Username match:", loaded_account.username == "alex123")
    print("Balance match:", loaded_account.balance == 1200.0)
