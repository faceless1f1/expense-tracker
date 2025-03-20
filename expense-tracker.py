import json
import argparse
from datetime import datetime
import os

DATA_FILE = "data.json"

def load_data():
    """Load data from the JSON file or initialize with an empty list if needed."""
    if not os.path.exists(DATA_FILE):
        # Create the file with an empty list if it doesn't exist
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
        return []
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            # Ensure the loaded data is a list; if not, return an empty list
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
      print(f"Warning: {DATA_FILE} contains invalid JSON. Resetting data.")
      return []

def load_budget():
    """Load budget from the JSON file or initialize with a default value."""
    if not os.path.exists("budget.json"):
        return {"amount": 0.0}  # Default budget

    try:
        with open("budget.json", "r") as f:
            budget = json.load(f)
            if isinstance(budget, dict) and "amount" in budget:
                return budget
            else:
                return {"amount": 0.0}  # Reset to default if malformed
    except json.JSONDecodeError:
        print("Warning: budget.json contains invalid JSON. Resetting budget.")
        return {"amount": 0.0}


def save_data(data):
    """Save the list data to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def save_budget(budget):
    """Save the budget to the JSON file."""
    with open("budget.json", "w") as f:
        json.dump(budget, f, indent=4)

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add expense command
    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount of the expense")
    add_parser.add_argument("--description", type=str, required=True, help="Description of the expense")

    # List expenses command
    subparsers.add_parser("list", help="List all expenses")

    # Summary command
    summary_parser = subparsers.add_parser("summary", help="Show summary of expenses")
    summary_parser.add_argument("--month", type=int, help="Month for which to show summary")

    # Delete expense command
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, required=True, help="ID of the expense to delete")

    # Set Budget command
    set_budget_parser = subparsers.add_parser("set-budget", help="Set a budget")
    set_budget_parser.add_argument("--amount", type=float, required=True, help="Amount of the budget")

    # Show Budget command
    budget_parser = subparsers.add_parser("budget", help="Show budget")

    # Update ids in data.json command
    update_ids_parser = subparsers.add_parser("update", help="Update ids in data.json")

    # Clear expenses command
    clear_parser = subparsers.add_parser("clear", help="Clear all expenses")

    args = parser.parse_args()

    data = load_data()
    budget = load_budget()

    if args.command == "add":
        new_id = max((exp["id"] for exp in data), default=0) + 1
        expense = {
            "id": new_id,
            "amount": args.amount,
            "description": args.description,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        data.append(expense)
        save_data(data)
        print("Expense added successfully.")
        total = sum(exp["amount"] for exp in data)
        if total > budget["amount"]:
            print("You have exceeded your budget!")

    elif args.command == "list":
        if not data:
            print("No expenses found.")
        else:
            print("ID:\tAmount:\tDescription:\tDate:")
            for expense in data:
                print(f"{expense['id']}\t{expense['amount']}\t{expense['description']}\t{expense['date']}")

    elif args.command == "summary":
        if not data:
            print("No expenses to summarize.")
        else:
            if args.month:
                if args.month and (args.month < 1 or args.month > 12):
                  print("Invalid month. Please enter a value between 1 and 12.")
                else:
                  filtered = [exp for exp in data if datetime.strptime(exp["date"], "%Y-%m-%d").month == args.month]
                  total = sum(exp["amount"] for exp in filtered)
                  print(f"Total expenses for month {args.month}: {total}")
            else:
                total = sum(exp["amount"] for exp in data)
                print(f"Total expenses: {total}")


    elif args.command == "delete":
        expense_to_delete = None
        for exp in data:
            if exp["id"] == args.id:
                expense_to_delete = exp
                break
        if expense_to_delete:
            data.remove(expense_to_delete)
            save_data(data)
            print(f"Expense with ID {args.id} has been deleted.")
        else:
            print(f"No expense found with ID {args.id}.")

    elif args.command == "clear":
        data.clear()
        save_data(data)
        print("All expenses have been deleted.")

    elif args.command == "set-budget":
        load_budget()
        budget["amount"] = args.amount
        save_budget(budget)
        print("Budget set successfully.")

    elif args.command == "budget":
        load_budget()
        print(f"Budget: {budget['amount']}")

    elif args.command == "update":
        for idx, exp in enumerate(data, start=1):
          exp["id"] = idx
        save_data(data)
        print("IDs updated successfully.")

if __name__ == "__main__":
    main()
