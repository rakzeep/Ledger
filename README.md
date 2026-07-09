# LEDGER

A desktop banking application built with Python, Tkinter, MySQL, and NumPy. The application provides a simple graphical interface that allows users to perform basic banking operations while securely storing account information in a MySQL database.

## Features

- View current account balance
- Deposit money into the account
- Withdraw money from the account
- Automatic account initialization on first run
- Persistent data storage using MySQL
- User-friendly graphical interface with Tkinter
- Prevent invalid transactions:
  - Negative deposits are rejected
  - Withdrawals exceeding the available balance are blocked
  - Negative withdrawal amounts are not allowed
- Real-time balance updates

## Built With

- Python 3
- Tkinter
- MySQL
- MySQL Connector/Python
- NumPy

## How It Works

When the application starts, it connects to a MySQL database and checks whether an account already exists. If no account is found, one is automatically created with a balance of $0.00.

Users can then interact with the application through four buttons:

1. Show Balance
2. Deposit
3. Withdraw
4. Exit

The account balance is retrieved from the database, updated after each successful transaction, and stored permanently for future sessions.

### Show Balance

Displays the current account balance stored in the database.

### Deposit

Users can enter an amount to add to their account balance. Any amount less than zero is considered invalid and will not be processed.

### Withdraw

Users can withdraw money from their account provided that:
- The withdrawal amount is greater than zero.
- The withdrawal amount does not exceed the available balance.

### Exit

Selecting the exit button closes the application and safely terminates the database connection.

## Example

```text
+---------------------------+
|      Banking Program      |
+---------------------------+

[ Show Balance ]

[ Deposit ]

[ Withdraw ]

[ Exit ]
```

## Getting Started

### Prerequisites

- Python 3 installed on your system
- MySQL Server installed and running
- A MySQL database named `bankdb`

### Running the Project

1. Clone this repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd banking-management-system
```

3. Install the required dependencies:

```bash
pip install mysql-connector-python numpy
```

4. Update your MySQL credentials in the source code:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="bankdb"
)
```

5. Run the application:

```bash
python main.py
```

## Project Structure

```text
banking-management-system/
├── main.py
└── README.md
```

## Future Improvements

- Transaction history
- Multiple user accounts
- User authentication
- Fund transfers
- Interest calculations
- Account creation and deletion
- Enhanced user interface
- Transaction analytics and reports

## About

This project was created to strengthen my understanding of Python GUI development, database integration, and event-driven programming. It combines Tkinter for the user interface, MySQL for persistent data storage, and NumPy for data handling, providing hands-on experience with building a functional desktop banking application.
