# Bank App Sprint Log: Sprint 3

## Sprint Goal
To let users deposit and withdraw money from their account inside the app, make sure changes are saved properly to the CSV file, display main menu in CLI. 

---

## Tasks Completed

- Added `run()` method in `BankApp`:
  - Starts the app and keeps it running until the user logs out
  - Calls login and shows the menu with options

- Added `deposit()` method in `BankApp`:
  - Asks the user to enter how much money to add
  - Updates the account balance
  - Saves the new balance to `bank.csv`

- Added `withdraw()` method in `BankApp`:
  - Asks the user how much money to take out
  - Only allows withdrawal if there is enough money
  - Updates the balance and saves to `bank.csv`

- Updated the main menu (`show_menu()`):
  - Added options for Deposit (2) and Withdraw (3)
  - Menu now includes:
    - View account
    - Deposit
    - Withdraw
    - Log out

- Created `main.py`
---

## Resources used
- ChatGPT used to:
  - Help build user input for deposit and withdraw
  - Add simple error checking
  - Update the menu with working options
- Reused code from earlier sprints to avoid repeating things

---

## Testing log

| Test Case             | Input                      | Expected Outcome                     | Actual Outcome  | Notes                         |
|-----------------------|----------------------------|--------------------------------------|------------------|-------------------------------|
| Deposit funds         | Deposit $100               | Balance increases by $100            | Passed           | CSV file also updated         |
| Withdraw too much     | Try to withdraw $9999      | Error shown, balance stays the same  | Passed           | No overdraft allowed          |
| Withdraw valid amount | Withdraw $50               | Balance decreases by $50             | Passed           | CSV file reflects new balance |
| View updated account  | Check account after actions| Shows correct new balance            | Passed           | Matches transaction history   |

---

## Reflections

- Transactions work well and save changes to the CSV right away
- Added clear error messages for invalid input or if balance is too low
---