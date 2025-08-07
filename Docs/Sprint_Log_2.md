# Bank App Sprint Log: Sprint 2

## Sprint Goal  
Let users create new accounts and log in to existing ones. Make sure account info is saved in the CSV file and users can only log in with the correct details.

---

## Tasks Completed

- Made a new class called `BankApp` with:
  - `database` (BankDatabase): holds all accounts
  - `current_user` (UserAccount): keeps track of who’s logged in

- Added these methods to `BankApp`:
  - `create_account()`:
    - Asks the user to type a username
    - Makes a unique 8-digit bank number using `generate_bank_number()`
    - Shows the details and asks the user to confirm
    - Creates the account and saves it with `add_account()`
  - `login()`:
    - Asks for username and bank number
    - Checks if they match using `authenticate()` from `BankDatabase`
    - If correct, logs the user in by setting `current_user`

- Added `authenticate(username, bank_number)` to `BankDatabase`:
  - Checks if the username exists
  - If it does, checks if the bank number matches
  - If both are right, returns the account. If not, returns nothing

- Made a simple test loop so users can:
  - Make a new account
  - Log in to their account
  - Quit the app

---

## Resources used

- AI assistant (ChatGPT) helped with:
  - Planning the login and signup features
  - Avoiding any extra methods not in the plan
- GitBook Module 220 for examples of OOP programs

---

## Testing log

| Test Case                | Input                                                       | What I Expected                          | What Actually Happened                  | Notes                                 |
|--------------------------|-------------------------------------------------------------|-------------------------------------------|------------------------------------------|---------------------------------------|
| Create new account       | Username: `orlando`, confirmed `yes`                        | New account made and saved                | Worked correctly                         | Unique bank number was given          |
| Duplicate username       | Tried `orlando` again                                       | Should give error                         | Worked correctly                         | Didn’t allow same name twice          |
| Cancel account creation  | Typed a name, then said `no`                                | Should cancel the process                 | Worked correctly                         | Didn’t save anything                   |
| Login with correct info  | Username and bank number were correct                       | Should log in                             | Worked correctly                         | Set `current_user`                     |
| Login with wrong number  | Username was right, number was wrong                        | Should fail login                         | Worked correctly                         | Stopped wrong login                    |
| Login with fake user     | Used name that doesn’t exist                                | Should fail login                         | Worked correctly                         | Stopped unknown user                   |
| CSV file test            | Restarted app, tried logging in with saved account          | Should still work                         | Worked correctly                         | Data was loaded from file             |

---

## Reflections

- The login and signup system works well and feels smooth  
- Everything is done using simple input and print statements  
- The bank number system makes sure no two users have the same ID  
- The code is still easy to read and follows the design  
- Testing showed that both good and bad inputs work as expected

---

## Notes for next sprint

- Build the `run()` method and the full menu for users  
- Let logged-in users see their balance, deposit, and withdraw money  
- Make sure all changes are saved to the CSV file  
- Stick exactly to the SDS plan with class and method names