#!/usr/bin/env python3
"""
Expense Tracker CLI
A comprehensive command-line application for tracking personal expenses
with features for adding, viewing, editing, and analyzing spending patterns.
"""

import json
import os
import sys
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import calendar


class ExpenseTracker:
    """
    A class to manage personal expenses with CLI interface.
    """
    
    def __init__(self, data_file: str = "expenses.json"):
        """
        Initialize the ExpenseTracker.
        
        Args:
            data_file: Path to the JSON file storing expense data
        """
        self.data_file = data_file
        self.expenses = self.load_expenses()
        self.categories = [
            "Food", "Transportation", "Entertainment", "Shopping", 
            "Bills", "Healthcare", "Education", "Travel", "Other"
        ]
    
    def load_expenses(self) -> List[Dict]:
        """
        Load expenses from the JSON file.
        
        Returns:
            List of expense dictionaries
        """
        if not os.path.exists(self.data_file):
            return []
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data.get('expenses', [])
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading expenses: {e}")
            print("Starting with empty expense list.")
            return []
    
    def save_expenses(self) -> bool:
        """
        Save expenses to the JSON file.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            data = {
                "expenses": self.expenses,
                "last_updated": datetime.now().isoformat()
            }
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            return True
        except IOError as e:
            print(f"Error saving expenses: {e}")
            return False
    
    def add_expense(self, amount: float, description: str, category: str, date: str = None) -> bool:
        """
        Add a new expense.
        
        Args:
            amount: Expense amount
            description: Description of the expense
            category: Category of the expense
            date: Date of expense (YYYY-MM-DD format), defaults to today
        
        Returns:
            True if successful, False otherwise
        """
        if amount <= 0:
            print("Error: Amount must be positive.")
            return False
        
        if category not in self.categories:
            print(f"Error: Invalid category. Choose from: {', '.join(self.categories)}")
            return False
        
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        else:
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Error: Invalid date format. Use YYYY-MM-DD.")
                return False
        
        expense = {
            "id": self.generate_id(),
            "amount": round(amount, 2),
            "description": description.strip(),
            "category": category,
            "date": date,
            "created_at": datetime.now().isoformat()
        }
        
        self.expenses.append(expense)
        if self.save_expenses():
            print(f"Expense added successfully! ID: {expense['id']}")
            return True
        return False
    
    def generate_id(self) -> int:
        """
        Generate a unique ID for new expenses.
        
        Returns:
            Unique integer ID
        """
        if not self.expenses:
            return 1
        return max(expense['id'] for expense in self.expenses) + 1
    
    def list_expenses(self, category: str = None, days: int = None) -> None:
        """
        List expenses with optional filtering.
        
        Args:
            category: Filter by category
            days: Show expenses from last N days
        """
        filtered_expenses = self.expenses.copy()
        
        # Filter by category
        if category:
            if category not in self.categories:
                print(f"Error: Invalid category. Choose from: {', '.join(self.categories)}")
                return
            filtered_expenses = [e for e in filtered_expenses if e['category'] == category]
        
        # Filter by date range
        if days:
            cutoff_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
            filtered_expenses = [e for e in filtered_expenses if e['date'] >= cutoff_date]
        
        if not filtered_expenses:
            print("No expenses found matching the criteria.")
            return
        
        # Sort by date (newest first)
        filtered_expenses.sort(key=lambda x: x['date'], reverse=True)
        
        # Display expenses
        print(f"\n{'ID':<4} {'Date':<12} {'Category':<15} {'Amount':<10} {'Description'}")
        print("-" * 70)
        
        total = 0
        for expense in filtered_expenses:
            print(f"{expense['id']:<4} {expense['date']:<12} {expense['category']:<15} "
                  f"${expense['amount']:<9.2f} {expense['description']}")
            total += expense['amount']
        
        print("-" * 70)
        print(f"Total: ${total:.2f}")
        print(f"Number of expenses: {len(filtered_expenses)}")
    
    def delete_expense(self, expense_id: int) -> bool:
        """
        Delete an expense by ID.
        
        Args:
            expense_id: ID of the expense to delete
        
        Returns:
            True if successful, False otherwise
        """
        for i, expense in enumerate(self.expenses):
            if expense['id'] == expense_id:
                deleted_expense = self.expenses.pop(i)
                if self.save_expenses():
                    print(f"Expense deleted: {deleted_expense['description']} (${deleted_expense['amount']:.2f})")
                    return True
                return False
        
        print(f"Error: No expense found with ID {expense_id}")
        return False
    
    def update_expense(self, expense_id: int, amount: float = None, 
                      description: str = None, category: str = None, date: str = None) -> bool:
        """
        Update an existing expense.
        
        Args:
            expense_id: ID of the expense to update
            amount: New amount (optional)
            description: New description (optional)
            category: New category (optional)
            date: New date (optional)
        
        Returns:
            True if successful, False otherwise
        """
        for expense in self.expenses:
            if expense['id'] == expense_id:
                if amount is not None:
                    if amount <= 0:
                        print("Error: Amount must be positive.")
                        return False
                    expense['amount'] = round(amount, 2)
                
                if description is not None:
                    expense['description'] = description.strip()
                
                if category is not None:
                    if category not in self.categories:
                        print(f"Error: Invalid category. Choose from: {', '.join(self.categories)}")
                        return False
                    expense['category'] = category
                
                if date is not None:
                    try:
                        datetime.strptime(date, "%Y-%m-%d")
                        expense['date'] = date
                    except ValueError:
                        print("Error: Invalid date format. Use YYYY-MM-DD.")
                        return False
                
                if self.save_expenses():
                    print(f"Expense updated successfully!")
                    return True
                return False
        
        print(f"Error: No expense found with ID {expense_id}")
        return False
    
    def get_summary(self, month: str = None) -> None:
        """
        Display expense summary by category.
        
        Args:
            month: Month in YYYY-MM format, defaults to current month
        """
        if month is None:
            month = datetime.now().strftime("%Y-%m")
        else:
            try:
                datetime.strptime(month, "%Y-%m")
            except ValueError:
                print("Error: Invalid month format. Use YYYY-MM.")
                return
        
        # Filter expenses by month
        month_expenses = [e for e in self.expenses if e['date'].startswith(month)]
        
        if not month_expenses:
            print(f"No expenses found for {month}")
            return
        
        # Calculate totals by category
        category_totals = {}
        total_amount = 0
        
        for expense in month_expenses:
            category = expense['category']
            amount = expense['amount']
            category_totals[category] = category_totals.get(category, 0) + amount
            total_amount += amount
        
        # Display summary
        month_name = datetime.strptime(month, "%Y-%m").strftime("%B %Y")
        print(f"\nExpense Summary for {month_name}")
        print("=" * 40)
        
        for category in sorted(category_totals.keys()):
            amount = category_totals[category]
            percentage = (amount / total_amount) * 100 if total_amount > 0 else 0
            print(f"{category:<15}: ${amount:>8.2f} ({percentage:>5.1f}%)")
        
        print("-" * 40)
        print(f"{'Total':<15}: ${total_amount:>8.2f}")
        print(f"Number of expenses: {len(month_expenses)}")
        
        # Find highest expense
        if month_expenses:
            highest = max(month_expenses, key=lambda x: x['amount'])
            print(f"\nHighest expense: ${highest['amount']:.2f} - {highest['description']} ({highest['category']})")
    
    def export_expenses(self, filename: str = None) -> bool:
        """
        Export expenses to CSV format.
        
        Args:
            filename: Output filename, defaults to expenses_YYYY-MM-DD.csv
        
        Returns:
            True if successful, False otherwise
        """
        if filename is None:
            filename = f"expenses_{datetime.now().strftime('%Y-%m-%d')}.csv"
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                # Write CSV header
                file.write("ID,Date,Category,Amount,Description\n")
                
                # Sort expenses by date
                sorted_expenses = sorted(self.expenses, key=lambda x: x['date'])
                
                # Write expense data
                for expense in sorted_expenses:
                    file.write(f"{expense['id']},{expense['date']},{expense['category']},"
                             f"{expense['amount']:.2f},\"{expense['description']}\"\n")
            
            print(f"Expenses exported to {filename}")
            return True
        except IOError as e:
            print(f"Error exporting expenses: {e}")
            return False
    
    def interactive_mode(self) -> None:
        """Run the expense tracker in interactive mode."""
        print("Expense Tracker CLI")
        print("Type 'help' for available commands or 'quit' to exit.")
        print("-" * 50)
        
        while True:
            try:
                command = input("\nexpense-tracker> ").strip().lower()
                
                if command in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break
                elif command == 'help':
                    self.show_help()
                elif command == 'add':
                    self.interactive_add()
                elif command == 'list':
                    self.interactive_list()
                elif command == 'delete':
                    self.interactive_delete()
                elif command == 'update':
                    self.interactive_update()
                elif command == 'summary':
                    self.interactive_summary()
                elif command == 'export':
                    self.export_expenses()
                elif command == 'categories':
                    print(f"Available categories: {', '.join(self.categories)}")
                elif command == '':
                    continue
                else:
                    print(f"Unknown command: {command}. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
    
    def show_help(self) -> None:
        """Display help information."""
        help_text = """
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
        """
        print(help_text)
    
    def interactive_add(self) -> None:
        """Interactive mode for adding expenses."""
        try:
            amount = float(input("Enter amount: $"))
            description = input("Enter description: ")
            
            print(f"Available categories: {', '.join(self.categories)}")
            category = input("Enter category: ")
            
            date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            date = date_input if date_input else None
            
            self.add_expense(amount, description, category, date)
        except ValueError:
            print("Error: Invalid amount entered.")
    
    def interactive_list(self) -> None:
        """Interactive mode for listing expenses."""
        category = input("Filter by category (or press Enter for all): ")
        category = category if category else None
        
        days_input = input("Show last N days (or press Enter for all): ")
        days = int(days_input) if days_input.isdigit() else None
        
        self.list_expenses(category, days)
    
    def interactive_delete(self) -> None:
        """Interactive mode for deleting expenses."""
        try:
            expense_id = int(input("Enter expense ID to delete: "))
            self.delete_expense(expense_id)
        except ValueError:
            print("Error: Invalid ID entered.")
    
    def interactive_update(self) -> None:
        """Interactive mode for updating expenses."""
        try:
            expense_id = int(input("Enter expense ID to update: "))
            
            # Find the expense to show current values
            expense = next((e for e in self.expenses if e['id'] == expense_id), None)
            if not expense:
                print(f"No expense found with ID {expense_id}")
                return
            
            print(f"Current expense: {expense['description']} - ${expense['amount']:.2f} ({expense['category']}) on {expense['date']}")
            print("Leave fields empty to keep current values:")
            
            amount_input = input(f"New amount (current: ${expense['amount']:.2f}): ")
            amount = float(amount_input) if amount_input else None
            
            description_input = input(f"New description (current: {expense['description']}): ")
            description = description_input if description_input else None
            
            category_input = input(f"New category (current: {expense['category']}): ")
            category = category_input if category_input else None
            
            date_input = input(f"New date (current: {expense['date']}): ")
            date = date_input if date_input else None
            
            self.update_expense(expense_id, amount, description, category, date)
        except ValueError:
            print("Error: Invalid input.")
    
    def interactive_summary(self) -> None:
        """Interactive mode for showing summary."""
        month = input("Enter month (YYYY-MM) or press Enter for current month: ")
        month = month if month else None
        self.get_summary(month)


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Expense Tracker CLI - Track your personal expenses",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python expense_tracker.py                           # Interactive mode
  python expense_tracker.py add 25.50 "Lunch" Food   # Add expense
  python expense_tracker.py list                     # List all expenses
  python expense_tracker.py list --category Food     # List food expenses
  python expense_tracker.py summary                  # Show monthly summary
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('amount', type=float, help='Expense amount')
    add_parser.add_argument('description', help='Expense description')
    add_parser.add_argument('category', help='Expense category')
    add_parser.add_argument('--date', help='Date (YYYY-MM-DD), defaults to today')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List expenses')
    list_parser.add_argument('--category', help='Filter by category')
    list_parser.add_argument('--days', type=int, help='Show last N days')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('id', type=int, help='Expense ID to delete')
    
    # Update command
    update_parser = subparsers.add_parser('update', help='Update an expense')
    update_parser.add_argument('id', type=int, help='Expense ID to update')
    update_parser.add_argument('--amount', type=float, help='New amount')
    update_parser.add_argument('--description', help='New description')
    update_parser.add_argument('--category', help='New category')
    update_parser.add_argument('--date', help='New date (YYYY-MM-DD)')
    
    # Summary command
    summary_parser = subparsers.add_parser('summary', help='Show expense summary')
    summary_parser.add_argument('--month', help='Month (YYYY-MM), defaults to current month')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export expenses to CSV')
    export_parser.add_argument('--filename', help='Output filename')
    
    # Categories command
    subparsers.add_parser('categories', help='Show available categories')
    
    return parser


def main():
    """Main function to run the expense tracker."""
    parser = create_parser()
    args = parser.parse_args()
    
    tracker = ExpenseTracker()
    
    if args.command is None:
        # Interactive mode
        tracker.interactive_mode()
    elif args.command == 'add':
        tracker.add_expense(args.amount, args.description, args.category, args.date)
    elif args.command == 'list':
        tracker.list_expenses(args.category, args.days)
    elif args.command == 'delete':
        tracker.delete_expense(args.id)
    elif args.command == 'update':
        tracker.update_expense(args.id, args.amount, args.description, args.category, args.date)
    elif args.command == 'summary':
        tracker.get_summary(args.month)
    elif args.command == 'export':
        tracker.export_expenses(args.filename)
    elif args.command == 'categories':
        print(f"Available categories: {', '.join(tracker.categories)}")


if __name__ == "__main__":
    main()