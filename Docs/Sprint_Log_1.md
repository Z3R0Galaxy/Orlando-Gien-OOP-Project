# Bank App Sprint Log: Sprint 1

## Sprint Goal
To build the object-oriented banking system with the ability to create accounts, deposit and withdraw funds, and save/load data persistently using CSV files.

---

## Tasks Completed

- Created `UserAccount` class with attributes:
  - `username` (str): Username chosen by user
  - `bank_number` (int): 8-digit bank account number
  - `balance` (float): Current account balance

- Implemented methods in `UserAccount`:
  - `deposit(amount)`: Adds a positive amount to the balance
  - `withdraw(amount)`: Removes amount if there is enough money, returns success status
  - `to_dict()`: Converts account data to dictionary for CSV saving
  - `from_dict(data)`: Class method to create a UserAccount object from dictionary data

- Created `BankDatabase` class with attributes:
  - `accounts` (dict): Maps usernames to their `UserAccount` instances

- Implemented methods in `BankDatabase`:
  - `load_accounts()`: Loads accounts from `bank.csv` into the `accounts` dictionary
  - `save_accounts()`: Writes current `accounts` data to `bank.csv`
  - `add_account(account)`: Adds a new `UserAccount` to `accounts` and saves it
  - `generate_bank_number()`: Generates an 8-digit bank number not already in use

- Built test script (`testing.py`) to:
  - Create a user account (`alex123`)
  - Test deposits and withdrawals with success and failure cases
  - Save accounts to CSV
  - Load accounts from CSV into a new `BankDatabase` instance
  - Verify loaded data matches original account details

---

## Resources used
- AI assistant (ChatGPT) used to:
    - Understand and Implement @classmethod and cls
    - provide examples on how to effectively test my code
- GitBook Module 220 for bulding the OOP app.

## Testing log

| Test Case             | Input                                                                 | Expected Outcome                            | Actual Outcome                            | Notes                            |
|-----------------------|-----------------------------------------------------------------------|---------------------------------------------|-------------------------------------------|----------------------------------|
| Account creation      | Create `UserAccount("alex123", 12345678, 1000.0)`                     | Correct attributes initialized              | Passed                                    | Account has correct values       |
| Deposit funds         | Call `deposit(500.0)`                                                 | Balance becomes `$1500.0`                   | Passed                                    | Balance increased by 500         |
| Withdraw funds        | Call `withdraw(300.0)`                                                | Balance becomes `$1200.0`                   | Passed                                    | Funds correctly withdrawn        |
| Withdraw too much     | Call `withdraw(5000.0)`                                               | Withdrawal denied, balance unchanged        | Passed                                    | Correctly prevented overdraft    |
| Save accounts         | Call `db.save_accounts()` with account added                          | `bank.csv` is created/updated               | Passed                                    | File written successfully        |
| Load accounts         | New `BankDatabase()` auto-loads `bank.csv`                            | Account data loaded into memory             | Passed                                    | Account found in new instance    |
| Verify loaded data    | Access account `alex123` from loaded DB and compare username/balance | Username = "alex123", balance = `$1200.0`   | Passed                                    | Data matches original account    |

---

## Reflections

- Class attributes and method signatures follow design requirements
- Tests cover both success and failure.
- CSV persistence implemented with Python’s `csv` module.
- Bank number generation makes sure the 8-digit numbers are unique across all accounts.

---

## Notes for next sprint
- Implement secure log in and account creation.
- Save and load log in and account information from the CSV file.