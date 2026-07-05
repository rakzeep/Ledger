# Ledger

A simple command-line banking application built with Python. Ledger allows users to perform basic banking operations such as checking their balance, depositing funds, and withdrawing money through an interactive menu-driven interface.

## Features

- View current account balance
- Deposit money into the account
- Withdraw money from the account
- Prevent invalid transactions:
  - Negative deposits are rejected
  - Withdrawals exceeding the available balance are blocked
  - Negative withdrawal amounts are not allowed
- Easy-to-use menu system
- Runs continuously until the user chooses to exit

## Built With

- Python 3
- Standard Python libraries only

## How It Works

When the program starts, users are presented with a menu containing four options:

1. Show Balance
2. Deposit
3. Withdraw
4. Exit

The application keeps track of the account balance throughout the session and updates it after successful transactions.

### Deposit

Users can enter an amount to add to their balance. Any amount less than zero is considered invalid and will not be processed.

### Withdraw

Users can withdraw money from their account provided that:
- The withdrawal amount is greater than zero.
- The withdrawal amount does not exceed the available balance.

### Exit

Selecting the exit option closes the application and ends the session.

## Example

```text
************************
Banking Program
************************
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
************************
Enter your choice(1-4): 2
************************
Enter an amount to be deposited: 500
************************

Your balance is $500.00
```

## Getting Started

### Prerequisites

- Python 3 installed on your system

### Running the Project

1. Clone this repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd bank-project
```

3. Run the program:

```bash
python main.py
```

## Project Structure

```text
bank-project/
├── main.py
└── README.md
```

## Future Improvements

- Transaction history
- Multiple user accounts
- PIN-based authentication
- Saving account data using files or databases
- Fund transfers between accounts
- Interest calculations

## About

This project was created to practice Python fundamentals, including functions, loops, conditional statements, user input handling, and basic program organization. It serves as a beginner-friendly introduction to building interactive command-line applications.
