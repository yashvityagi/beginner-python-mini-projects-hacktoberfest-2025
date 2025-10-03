#!/usr/bin/env python3
"""
Test script for Expense Tracker CLI
This script tests the core functionality of the expense tracker.
"""

import sys
import os
import json
import tempfile
from datetime import datetime

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from expense_tracker import ExpenseTracker


def test_expense_tracker():
    """Test the core functionality of the ExpenseTracker class."""
    print("Testing Expense Tracker CLI...")
    print("-" * 50)
    
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
        temp_filename = temp_file.name
    
    try:
        # Initialize tracker with temporary file
        tracker = ExpenseTracker(temp_filename)
        
        print("1. Testing expense addition...")
        # Test adding expenses
        success1 = tracker.add_expense(25.50, "Lunch at cafe", "Food")
        success2 = tracker.add_expense(120.00, "Monthly bus pass", "Transportation", "2025-10-01")
        success3 = tracker.add_expense(15.99, "Movie ticket", "Entertainment")
        
        if success1 and success2 and success3:
            print("   ✓ Successfully added 3 expenses")
        else:
            print("   ✗ Failed to add expenses")
        
        print(f"   Total expenses in tracker: {len(tracker.expenses)}")
        
        print("\n2. Testing expense listing...")
        # Test listing expenses
        print("   All expenses:")
        tracker.list_expenses()
        
        print("\n   Food expenses only:")
        tracker.list_expenses(category="Food")
        
        print("\n3. Testing expense update...")
        # Test updating an expense
        if tracker.expenses:
            first_id = tracker.expenses[0]['id']
            success = tracker.update_expense(first_id, amount=30.00, description="Updated lunch expense")
            if success:
                print("   ✓ Successfully updated expense")
            else:
                print("   ✗ Failed to update expense")
        
        print("\n4. Testing summary generation...")
        # Test summary
        tracker.get_summary()
        
        print("\n5. Testing export functionality...")
        # Test export
        export_file = "test_expenses.csv"
        success = tracker.export_expenses(export_file)
        if success and os.path.exists(export_file):
            print("   ✓ Successfully exported expenses to CSV")
            # Clean up export file
            os.remove(export_file)
        else:
            print("   ✗ Failed to export expenses")
        
        print("\n6. Testing data persistence...")
        # Test data persistence by creating a new tracker with same file
        tracker2 = ExpenseTracker(temp_filename)
        if len(tracker2.expenses) == len(tracker.expenses):
            print("   ✓ Data persistence working correctly")
        else:
            print("   ✗ Data persistence failed")
        
        print("\n7. Testing expense deletion...")
        # Test deleting an expense
        if tracker.expenses:
            expense_to_delete = tracker.expenses[-1]['id']
            initial_count = len(tracker.expenses)
            success = tracker.delete_expense(expense_to_delete)
            if success and len(tracker.expenses) == initial_count - 1:
                print("   ✓ Successfully deleted expense")
            else:
                print("   ✗ Failed to delete expense")
        
        print("\n8. Testing error handling...")
        # Test error cases
        error_tests = [
            tracker.add_expense(-10, "Negative amount", "Food"),  # Should fail
            tracker.add_expense(10, "Invalid category", "InvalidCategory"),  # Should fail
            tracker.update_expense(999, amount=50),  # Should fail (invalid ID)
            tracker.delete_expense(999)  # Should fail (invalid ID)
        ]
        
        failed_as_expected = sum(1 for test in error_tests if not test)
        if failed_as_expected == len(error_tests):
            print("   ✓ Error handling working correctly")
        else:
            print("   ✗ Some error cases not handled properly")
        
        print("\n" + "=" * 50)
        print("TEST SUMMARY:")
        print(f"Final number of expenses: {len(tracker.expenses)}")
        print("All core functionality appears to be working!")
        
    except Exception as e:
        print(f"Error during testing: {e}")
    
    finally:
        # Clean up temporary file
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
    
    print("\nTest completed!")


if __name__ == "__main__":
    test_expense_tracker()