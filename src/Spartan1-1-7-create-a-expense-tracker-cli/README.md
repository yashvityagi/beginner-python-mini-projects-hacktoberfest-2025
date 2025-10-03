# Expense Tracker CLI

A comprehensive command-line application for tracking personal expenses with features for adding, viewing, editing, and analyzing spending patterns. This production-ready tool helps you manage your finances efficiently through an intuitive CLI interface.

## Features

### Core Functionality
- **Add Expenses**: Record expenses with amount, description, category, and date
- **List Expenses**: View expenses with filtering options by category and date range
- **Update Expenses**: Modify existing expense records
- **Delete Expenses**: Remove unwanted expense entries
- **Expense Summary**: Analyze spending patterns by category and month
- **Data Export**: Export expense data to CSV format

### Advanced Features
- **Interactive Mode**: User-friendly command-line interface with guided prompts
- **Command-Line Mode**: Direct commands for automation and scripting
- **Data Persistence**: Automatic saving to JSON file with backup support
- **Category Management**: Predefined expense categories with validation
- **Date Filtering**: View expenses from specific time periods
- **Summary Analytics**: Monthly breakdowns with percentage analysis
- **Error Handling**: Robust error handling with user-friendly messages

## Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

### Setup

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd src/Spartan1-1-7-create-a-expense-tracker-cli
   ```

3. Make the script executable (optional):
   ```bash
   chmod +x expense_tracker.py
   ```

## Usage

### Interactive Mode (Recommended for beginners)

Run without arguments to enter interactive mode:

```bash
python expense_tracker.py
```

Interactive commands:
- `add` - Add a new expense with guided prompts
- `list` - List expenses with optional filtering
- `delete` - Delete an expense by ID
- `update` - Update an existing expense
- `summary` - Show monthly expense summary
- `export` - Export expenses to CSV
- `categories` - Show available categories
- `help` - Display help information
- `quit` - Exit the application

### Command-Line Mode (For advanced users)

#### Add an Expense
```bash
python expense_tracker.py add 25.50 "Lunch at restaurant" Food
python expense_tracker.py add 120.00 "Monthly bus pass" Transportation --date 2025-10-01
```

#### List Expenses
```bash
# List all expenses
python expense_tracker.py list

# List expenses from a specific category
python expense_tracker.py list --category Food

# List expenses from last 7 days
python expense_tracker.py list --days 7

# Combine filters
python expense_tracker.py list --category Food --days 30
```

#### Update an Expense
```bash
python expense_tracker.py update 1 --amount 30.00 --description "Dinner at restaurant"
python expense_tracker.py update 2 --category Entertainment
```

#### Delete an Expense
```bash
python expense_tracker.py delete 1
```

#### View Summary
```bash
# Current month summary
python expense_tracker.py summary

# Specific month summary
python expense_tracker.py summary --month 2025-09
```

#### Export Data
```bash
# Export with default filename
python expense_tracker.py export

# Export with custom filename
python expense_tracker.py export --filename my_expenses.csv
```

#### Show Categories
```bash
python expense_tracker.py categories
```

## Expense Categories

The application includes the following predefined categories:
- **Food**: Meals, groceries, dining out
- **Transportation**: Gas, public transport, parking
- **Entertainment**: Movies, games, hobbies
- **Shopping**: Clothing, electronics, general purchases
- **Bills**: Utilities, rent, subscriptions
- **Healthcare**: Medical expenses, insurance
- **Education**: Books, courses, training
- **Travel**: Vacations, business trips
- **Other**: Miscellaneous expenses

## Data Storage

- Expenses are stored in `expenses.json` in the same directory
- Automatic backup of data with timestamps
- Human-readable JSON format for easy data recovery
- Data includes expense ID, amount, description, category, date, and creation timestamp

## Sample Output

### Interactive Mode Welcome
```
Expense Tracker CLI
Type 'help' for available commands or 'quit' to exit.
--------------------------------------------------

expense-tracker> add
Enter amount: $25.50
Enter description: Lunch at cafe
Available categories: Food, Transportation, Entertainment, Shopping, Bills, Healthcare, Education, Travel, Other
Enter category: Food
Enter date (YYYY-MM-DD) or press Enter for today: 
Expense added successfully! ID: 1
```

### Expense List View
```
ID   Date         Category        Amount     Description
----------------------------------------------------------------------
3    2025-10-03   Food            $25.50     Lunch at cafe
2    2025-10-02   Transportation  $120.00    Monthly bus pass
1    2025-10-01   Entertainment   $15.99     Movie ticket
----------------------------------------------------------------------
Total: $161.49
Number of expenses: 3
```

### Monthly Summary
```
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

## Project Structure

```
Spartan1-1-7-create-a-expense-tracker-cli/
├── expense_tracker.py    # Main application file
├── requirements.txt      # Dependencies (none required)
├── README.md            # Project documentation
└── expenses.json        # Data file (created automatically)
```

## Code Features

### Object-Oriented Design
- Clean `ExpenseTracker` class with well-defined methods
- Separation of concerns with dedicated methods for each operation
- Proper encapsulation and data validation

### Error Handling
- Input validation for amounts, dates, and categories
- File I/O error handling with graceful degradation
- User-friendly error messages with guidance

### Data Validation
- Amount validation (must be positive)
- Date format validation (YYYY-MM-DD)
- Category validation against predefined list
- Automatic data type conversion and sanitization

### User Experience
- Both interactive and command-line interfaces
- Clear help system and command guidance
- Formatted output with proper alignment
- Progress feedback for all operations

### Production Features
- Comprehensive argument parsing with help text
- Automatic data persistence with error recovery
- Export functionality for data portability
- Extensible category system

## Advanced Usage

### Automation Scripts
You can create shell scripts to automate common tasks:

```bash
#!/bin/bash
# Daily expense script
python expense_tracker.py add "$1" "$2" "$3"
python expense_tracker.py summary
```

### Data Analysis
Export data and analyze with external tools:
```bash
python expense_tracker.py export --filename monthly_report.csv
# Import CSV into spreadsheet applications for advanced analysis
```

## Contributing

This project is part of Hacktoberfest 2025. Contributions are welcome! Please ensure:

1. Code follows Python best practices
2. New features include appropriate error handling
3. Documentation is updated for any changes
4. Maintain backward compatibility with existing data files

## Future Enhancements

Potential improvements for this project:
- Budget setting and tracking with alerts
- Recurring expense management
- Multi-currency support
- Graphical reports and charts
- Integration with bank APIs
- Mobile companion app
- Cloud synchronization
- Advanced search and filtering
- Expense splitting and sharing
- Receipt photo attachment

## License

This project is open source and available under the MIT License.

## Author

Created by Spartan1-1-7 for Hacktoberfest 2025.

## Technical Details

- **Language**: Python 3.6+
- **Dependencies**: None (uses standard library only)
- **Data Format**: JSON for human readability
- **CLI Framework**: argparse for robust command-line interface
- **Date Handling**: datetime module for proper date validation
- **Error Handling**: Comprehensive exception handling throughout