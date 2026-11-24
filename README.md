# Python Banking System

A simple console-based banking application developed using Python. The application allows users to check their account balance, deposit money and withdraw money while maintaining balance information between sessions.

## Features

- Check current account balance.
- Deposit money into the account.
- Withdraw money from the account.
- Prevent withdrawals exceeding the available balance.
- Validate user input and handle invalid entries.
- Save account balance to a local text file for data persistence.

## Technologies Used

- Python 3
- File handling
- Exception handling
- Conditional statements
- Loops and functions

## Requirements

- Python 3.10 or later

## How to Run

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Run the application:

   `py banking.py`

4. Follow the menu options displayed in the terminal.

## Menu Options

| Option | Function |
|---|---|
| 1 | Check Balance |
| 2 | Deposit Money |
| 3 | Withdraw Money |
| 4 | Exit |

## Data Storage

The application uses a local file named `balance.txt` to store the account balance.

The file is automatically created when a successful deposit or withdrawal occurs. It is excluded from the Git repository because it contains local application data.

## Input Validation

The application handles invalid numerical input, rejects non-positive transaction amounts and prevents withdrawals that exceed the available balance.

## Future Improvements

- Multiple user accounts.
- Account registration and login.
- Transaction history.
- Graphical user interface.
- Database integration.

## Author

Developed as part of my Python software development learning journey.
