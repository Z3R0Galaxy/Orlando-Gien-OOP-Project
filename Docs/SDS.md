# Software Design Specification (SDS)

## Project name  
Bank App

## Version  
v1.0 – Initial system design (covers all planned features across sprints)

## Overview  
The Bank App is a simple command-line program that lets users log in, create accounts, check balances, deposit, and withdraw money. It uses object-oriented design for clean structure and stores all data in a CSV file so information is saved between sessions. The goal is to keep the app functional, easy to use, and ready for future expansion.

## System architecture  
The program is built using an object-oriented structure to keep each part of the app modular, organised, and easy to expand. Each class is responsible for a specific aspect of the program:

- **`UserAccount`**: This class represents an individual user’s bank account. It stores the user’s `username`, `bank_number`, and `balance`, and includes methods for depositing and withdrawing money. It also supports conversion to and from dictionaries to allow easy saving and loading from CSV files.

- **`BankDatabase`**: This class manages the storage and retrieval of all user accounts. It handles reading and writing data to a CSV file, keeps a dictionary of `UserAccount` objects, and includes methods for adding new accounts, authenticating users, and generating unique bank numbers.

- **`BankApp`**: This is the main controller class that runs the program and manages user interaction through the command-line interface. It displays menus, guides users through login or account creation, and lets them perform actions like checking their balance, making deposits, or withdrawing money.

## Class descriptions  

### UserAccount

| Attribute       | Type    | Description                                               |
|-----------------|---------|-----------------------------------------------------------|
| `username`      | `str`   | The user's chosen name for the bank account               |
| `bank_number`   | `int`   | A unique identifier automatically generated for accounts  |
| `balance`       | `float` | The amount of money currently in the user's account       |

| Method              | Description                                        |
|---------------------|----------------------------------------------------|
| `deposit(amount)`   | Adds the specified amount to the account balance   |
| `withdraw(amount)`  | Deducts the specified amount from the balance if funds are sufficient |
| `to_dict()`        | Converts the account data to a dictionary format   |
| `from_dict(data)`  | Populates the account data from a dictionary       |

### BankDatabase

| Attribute | Type                  | Description                                              |
|-----------|-----------------------|----------------------------------------------------------|
| `accounts`| `dict[str, UserAccount]` | Stores all user accounts keyed by username               |

| Method                     | Description                                            |
|----------------------------|--------------------------------------------------------|
| `load_accounts()`          | Reads user data from `bank.csv` and loads into memory  |
| `save_accounts()`          | Writes user data back to `bank.csv`                     |
| `add_account(account)`     | Adds a new `UserAccount` to the database                |
| `authenticate(username, bank_number)` | Checks if credentials match an existing account   |
| `generate_bank_number()`   | Creates a new unique bank number for new accounts       |

### BankApp

| Attribute | Type    | Description                                             |
|-----------|---------|---------------------------------------------------------|
| `database`| `BankDatabase` | The database instance managing all user accounts     |
|`curren_user`| `UserAccount`|The user account that is currently logged in|

| Method                | Description                                            |
|-----------------------|--------------------------------------------------------|
| `run()`               | Starts the app and shows the main menu for users       |
| `login()`             | Lets a user log into their account                     |
| `create_account()`    | Allows a user to create a new account                  |
| `show_menu()`         | Shows options for logged-in users (view, deposit, etc) |
| `view_account()`      | Shows details of the logged-in user’s account          |
| `deposit()`           | Lets the user add money to their account               |
| `withdraw()`          | Lets the user take money out of their account          | 

## Assumptions and constraints  
**Functional constraints:**

- Users must have or create an account to use the app  
- Command-line interface only (no GUI or mouse interaction)  
- All interaction is through input prompts and printed messages  

**Technical constraints:**

- All data is saved and read from a `bank.csv` file  
- Only the standard Python library is used (no external packages)  
- All core features must follow object-oriented design  

## Planned features by sprint

### Sprint 1: Build the account system
**Goal:** Create the structure for managing accounts and saving data.

- Create `UserAccount` and `BankDatabase` classes
- Allow deposit and withdrawal funcitons
- Make sure all data can be saved and loaded from a CSV file
- Test these features with basic input manually

### Sprint 2: Add login and account creation
**Goal:** Let users log in securely or make a new account.

- Add functions to create a new account with a username in the `BankApp` class
- Ask user for confirmation when entering data
- Implement login that checks the CSV data for valid accounts
- Make sure the system loads the correct user after login
- Test login and signup with multiple accounts

### Sprint 3: Build the interface and user options
**Goal:** Let users interact with the app through a command-line menu.

- Set up the main `BankApp` class with a `run()` loop
- Display a menu of actions (view, deposit, withdraw, exit)
- Route each menu choice to the correct method
- Make sure balance changes are saved after each transaction
- Test the full flow with multiple user sessions 

## Extensibility  
The design makes the program easy to understand, test, and maintain. It also allows for future features to be added (like transaction history or password protection) without needing to rewrite the core structure.

### User Stories

| User Story ID | Story |
|---------------|-------|
| **US1** | As a user, I want to create a bank account with a username, an auto-generated bank number, and a starting balance. |
| **US2** | As a user, I want to log into my account using my username and bank number so I can access my money. |
| **US3** | As a user, I want to view my account details, including my username, bank number, and balance. |
| **US4** | As a user, I want to deposit money into my account so my balance increases. |
| **US5** | As a user, I want to withdraw money from my account, but only if I have enough funds. |
| **US6** | As a user, I want my account information to be saved in a file so that I can access it the next time I run the program. |

# Class Diagrams

## UserAccount

```
+--------------------------+
|      UserAccount         |
+--------------------------+
| - username: str          |
| - bank_number: str       |
| - balance: float         |
+--------------------------+
| + deposit(amount: float) |
| + withdraw(amount: float)|
| + to_dict()              |
| + from_dict(data: dict)  |
+--------------------------+
```

## BankDatabase

```
+---------------------------+
|      BankDatabase         |
+---------------------------+
| - accounts: dict          |
+---------------------------+
| + load_accounts()         |
| + save_accounts()         |
| + add_account()           |
| + generate_bank_number()  |
| + authenticate()          |
+---------------------------+
```

## BankApp

```
+------------------------------+
|          BankApp             |
+------------------------------+
| - db: BankDatabase           |
| - current_user: UserAccount  |
+------------------------------+
| + run()                      |
| + create_account()           |
| + login()                    |
| + view_account()             |
| + show_menu()                |
+------------------------------+
```

# Use Cases — Bank App

## Use Case 1: Create New Bank Account

- **Actor**: User  
- **Preconditions**:  
  - User is not currently logged in  
  - `bank.csv` file exists or is initialized  

- **Main Flow**:  
  1. User selects "Create Account" from the main menu  
  2. System prompts for a username  
  3. User enters a unique username  
  4. System generates a unique bank number  
  5. System creates a new `UserAccount` object  
  6. System adds the account to `BankDatabase` and saves to `bank.csv`  
  7. User is logged in automatically  

- **Postconditions**:  
  - A new user account is created and stored persistently  
  - User becomes the current active session  

---

## Use Case 2: Log In to Existing Account

- **Actor**: User  
- **Preconditions**:  
  - At least one account exists in `bank.csv`  

- **Main Flow**:  
  1. User selects "Log In" from the main menu  
  2. System prompts for username and bank number  
  3. User inputs credentials  
  4. System authenticates using `BankDatabase.authenticate()`  
  5. If correct, user is logged in and `current_user` is set  

- **Alternate Flow**:  
  - If credentials are invalid, system shows an error and asks to retry  

- **Postconditions**:  
  - User is logged in and can perform account actions  

---

## Use Case 3: Deposit Funds

- **Actor**: Logged-in User  
- **Preconditions**:  
  - User must be logged in  
  - Account must exist in `BankDatabase`  

- **Main Flow**:  
  1. User selects "Deposit" from the menu  
  2. System prompts for amount  
  3. User enters a positive float value  
  4. System calls `deposit(amount)` on `current_user`  
  5. Updated balance is saved to `bank.csv`  

- **Postconditions**:  
  - Account balance is increased  
  - Change is saved to persistent storage  

---

## Use Case 4: Withdraw Funds

- **Actor**: Logged-in User  
- **Preconditions**:  
  - User must be logged in  
  - Account must have sufficient funds  

- **Main Flow**:  
  1. User selects "Withdraw" from the menu  
  2. System prompts for amount  
  3. User enters a positive float value  
  4. System checks if balance is sufficient  
  5. If yes, calls `withdraw(amount)` on `current_user`  
  6. Updated balance is saved to `bank.csv`  

- **Alternate Flow**:  
  - If funds are insufficient, system shows error and cancels the transaction  

- **Postconditions**:  
  - If successful, balance is reduced and saved  
  - If not, balance remains unchanged  

---

## Resources used
- AI assistant (ChatGPT) used to:
    - Create User Stories and Cases
    - Format Class diagrams for Md
- GitBook Module 220 used for:
    - Formatting inspiration 