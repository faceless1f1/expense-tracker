# Expense Tracker CLI

A simple command-line expense tracker written in Python. This application allows you to add, list, summarize, delete expenses, set a budget, update expense IDs, and clear all expenses. It uses JSON files to persist data.

## Features

- **Add Expense:** Record an expense with an amount, description, and auto-assigned date.
- **List Expenses:** Display all recorded expenses.
- **Summary:** Get the total expense amount (optionally filtered by month).
- **Delete Expense:** Remove an expense by its ID.
- **Budget Management:** Set and display a budget.
- **Update IDs:** Refresh the IDs in the expense records.
- **Clear Expenses:** Remove all expenses.

## Requirements

- Python 3.x

No external packages are required—this project uses only Python's standard library.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd expense-tracker
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Activate on Windows:
   venv\Scripts\activate
   # Activate on macOS/Linux:
   source venv/bin/activate
   ```

## Usage

The application is operated via command-line subcommands. Below are some examples:

### Add an Expense

```bash
python expense-tracker.py add --amount 20.50 --description "Lunch"
```

*Expected output:*
```
Expense added successfully.
```
If the total expenses exceed the set budget, a warning will be printed.

### List All Expenses

```bash
python expense-tracker.py list
```

*Expected output:*
```
ID:     Amount:     Description:    Date:
1       20.5        Lunch           2025-03-20
...
```

### Show Expense Summary

- **For all expenses:**
```bash
python expense-tracker.py summary
```
- **For a specific month (e.g., March):**
```bash
python expense-tracker.py summary --month 3
```

*Expected output:*
```
Total expenses: 20.5
```
or
```
Total expenses for month 3: 20.5
```

### Delete an Expense

```bash
python expense-tracker.py delete --id 1
```

*Expected output:*
```
Expense with ID 1 has been deleted.
```

### Clear All Expenses

```bash
python expense-tracker.py clear
```

*Expected output:*
```
All expenses have been deleted.
```

### Set Budget

```bash
python expense-tracker.py set-budget --amount 500
```

*Expected output:*
```
Budget set successfully.
```

### Show Budget

```bash
python expense-tracker.py budget
```

*Expected output:*
```
Budget: 500.0
```

### Update IDs in data.json

```bash
python expense-tracker.py update
```

*Expected output:*
```
IDs updated successfully.
```

## Code Overview

- **Data Persistence:**  
  - `data.json` stores expense records as a list of dictionaries.
  - `budget.json` stores the budget as a dictionary.

- **Expense Record Structure:**
  ```json
  {
      "id": 1,
      "amount": 20.50,
      "description": "Lunch",
      "date": "2025-03-20"
  }
  ```

- **Budget Structure:**
  ```json
  {
      "amount": 500.0
  }
  ```

- **Command-line Parsing:**  
  The project uses Python's `argparse` with subparsers to handle different commands (`add`, `list`, `summary`, `delete`, `set-budget`, `budget`, `update`, and `clear`).

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have improvements.

## License

This project is open source and available under the [MIT License](LICENSE).
