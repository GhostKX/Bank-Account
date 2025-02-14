# Bank Account Management System

A **Python-based command-line application** for managing bank accounts using **SQLite**. This system allows users to **register accounts, make deposits, withdraw funds, check balances, calculate interest, and manage account details** efficiently.

## Features

### **Account Management**
- **Create a new bank account** with personal details (name, phone number, email, username).
- **Unique usernames** to ensure data integrity.
- **View account details** including balance.
- **Edit account information** such as name, phone number, email, and username.
- **Delete accounts** permanently.

### **Financial Transactions**
- **Deposit funds** into an account.
- **Withdraw funds** with balance verification.
- **View account balance** at any time.
- **Interest Calculation** based on different timeframes (12, 24, and 36 months with 1% interest rate).

### **Database Integration**
- Uses **SQLite** for persistent data storage.
- Ensures secure and reliable transaction handling.
- Prevents duplicate usernames and invalid data entries.

### **User-Friendly Interface**
- Interactive **command-line menu** for easy navigation.
- Input validation for **security and data accuracy**.

## Requirements

- **Python 3.x** or higher  
- **SQLite** (built-in with Python)  
- No external libraries required  

## How to Run

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using:

```bash
python PythonBankAccount.py
```

## Usage

The system provides the following options:

- **Create Account** – Register a new user with unique credentials.
- **Deposit Money** – Add funds to an account.
- **Withdraw Money** – Withdraw funds from an account (subject to sufficient balance).
- **View Balance** – Check the current balance of an account.
- **Calculate Interest** – Simulate interest earnings over different time periods.
- **Search Accounts** – Find users based on name or phone number.
- **Edit Account Details** – Update user information.
- **Delete Account** – Remove an account from the system.
- **Exit** – Close the program.



## Example Usage Scenario
```
**********************************************
Welcome to the Bank Account Management System!

Choose an option:
1 - Create an account
2 - Make a deposit
3 - Withdraw funds
4 - View balance
5 - Calculate interest
6 - Search for an account
7 - Manage account details
8 - Exit
::: 1

Enter Your Details:
First Name: John
Last Name: Doe
Phone Number: (+998) 123456789
Email Address: johndoe@email.com
Username: johndoe123

Account successfully created!
--------------------------------
Username: johndoe123
Balance: $0.00
--------------------------------
```

## Code Structure

### Database Schema

The system manages account details in an SQLite database table named `user_details`, which stores:

- **id** (Primary Key) – Auto-incremented account ID.
- **first_name** – Account holder's first name.
- **last_name** – Account holder's last name.
- **phone_number** – Contact number.
- **email_address** – Registered email.
- **username** – Unique username.
- **balance** – Current account balance.

### Core Functions

The system consists of well-structured functions to handle banking operations:

- **`registration_client()`** – Creates a new user account.
- **`make_deposit(username)`** – Deposits funds into an account.
- **`withdraw(username)`** – Withdraws funds after verifying the balance.
- **`get_username(username)`** – Retrieves account details.
- **`update_balance(username, new_balance)`** – Updates and stores the new balance.
- **`calculate()`** – Computes potential interest earnings.
- **`search(first_name, last_name, phone_number)`** – Searches for accounts by name or phone number.
- **`show_account(username)`** – Displays account details.
- **`edit_account()`** – Updates user details such as name, phone number, email, or username.
- **`delete_account(username)`** – Removes an account permanently.

## Security & Validation

- **Username uniqueness check** prevents duplicate accounts.
- **Email format validation** ensures valid entries.
- **Phone number verification** requires proper formatting.
- **Sufficient funds check** prevents overdrafts on withdrawals.


## Author

- Developed by **GhostKX**
- GitHub: **[GhostKX](https://github.com/GhostKX/Bank-Account)**
