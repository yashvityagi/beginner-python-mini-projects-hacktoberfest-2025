# Sample Output Examples

## Interactive Mode Welcome Screen
```
Expense Tracker CLI
Type 'help' for available commands or 'quit' to exit.
--------------------------------------------------

expense-tracker> help

Available Commands:
  add        - Add a new expense
  list       - List expenses (with optional filters)
  delete     - Delete an expense by ID
  update     - Update an existing expense
  summary    - Show expense summary by category
  export     - Export expenses to CSV
  categories - Show available categories
  help       - Show this help message
  quit       - Exit the application

expense-tracker> add
Enter amount: $25.50
Enter description: Lunch at cafe
Available categories: Food, Transportation, Entertainment, Shopping, Bills, Healthcare, Education, Travel, Other
Enter category: Food
Enter date (YYYY-MM-DD) or press Enter for today: 
Expense added successfully! ID: 1
```

## Command-Line Mode Examples

### Adding Expenses
```bash
$ python expense_tracker.py add 25.50 "Lunch at cafe" Food
Expense added successfully! ID: 1

$ python expense_tracker.py add 120.00 "Monthly bus pass" Transportation --date 2025-10-01
Expense added successfully! ID: 2

$ python expense_tracker.py add 15.99 "Movie ticket" Entertainment
Expense added successfully! ID: 3
```

### Listing Expenses
```bash
$ python expense_tracker.py list

ID   Date         Category        Amount     Description
----------------------------------------------------------------------
3    2025-10-03   Entertainment   $15.99     Movie ticket
1    2025-10-03   Food            $25.50     Lunch at cafe
2    2025-10-01   Transportation  $120.00    Monthly bus pass
----------------------------------------------------------------------
Total: $161.49
Number of expenses: 3
```

### Filtered Listing
```bash
$ python expense_tracker.py list --category Food

ID   Date         Category        Amount     Description
----------------------------------------------------------------------
1    2025-10-03   Food            $25.50     Lunch at cafe
----------------------------------------------------------------------
Total: $25.50
Number of expenses: 1

$ python expense_tracker.py list --days 2

ID   Date         Category        Amount     Description
----------------------------------------------------------------------
3    2025-10-03   Entertainment   $15.99     Movie ticket
1    2025-10-03   Food            $25.50     Lunch at cafe
----------------------------------------------------------------------
Total: $41.49
Number of expenses: 2
```

### Monthly Summary
```bash
$ python expense_tracker.py summary

Expense Summary for October 2025
========================================
Entertainment   :   $15.99 ( 9.9%)
Food           :   $25.50 (15.8%)
Transportation :  $120.00 (74.3%)
----------------------------------------
Total          :  $161.49
Number of expenses: 3

Highest expense: $120.00 - Monthly bus pass (Transportation)
```

### Updating Expenses
```bash
$ python expense_tracker.py update 1 --amount 30.00 --description "Dinner at restaurant"
Expense updated successfully!

$ python expense_tracker.py update 2 --category Bills
Expense updated successfully!
```

### Deleting Expenses
```bash
$ python expense_tracker.py delete 3
Expense deleted: Movie ticket ($15.99)
```

### Exporting Data
```bash
$ python expense_tracker.py export
Expenses exported to expenses_2025-10-03.csv

$ python expense_tracker.py export --filename my_expenses.csv
Expenses exported to my_expenses.csv
```

### Showing Categories
```bash
$ python expense_tracker.py categories
Available categories: Food, Transportation, Entertainment, Shopping, Bills, Healthcare, Education, Travel, Other
```

## Help Output
```bash
$ python expense_tracker.py --help
usage: expense_tracker.py [-h] {add,list,delete,update,summary,export,categories} ...

Expense Tracker CLI - Track your personal expenses

positional arguments:
  {add,list,delete,update,summary,export,categories}
                        Available commands
    add                 Add a new expense
    list                List expenses
    delete              Delete an expense
    update              Update an expense
    summary             Show expense summary
    export              Export expenses to CSV
    categories          Show available categories

optional arguments:
  -h, --help            show this help message and exit

Examples:
  python expense_tracker.py                           # Interactive mode
  python expense_tracker.py add 25.50 "Lunch" Food   # Add expense
  python expense_tracker.py list                     # List all expenses
  python expense_tracker.py list --category Food     # List food expenses
  python expense_tracker.py summary                  # Show monthly summary
```

## Error Handling Examples
```bash
$ python expense_tracker.py add -10 "Invalid amount" Food
Error: Amount must be positive.

$ python expense_tracker.py add 25 "Test" InvalidCategory
Error: Invalid category. Choose from: Food, Transportation, Entertainment, Shopping, Bills, Healthcare, Education, Travel, Other

$ python expense_tracker.py delete 999
Error: No expense found with ID 999

$ python expense_tracker.py add 25 "Test" Food --date 2025-13-45
Error: Invalid date format. Use YYYY-MM-DD.
```