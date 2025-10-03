# Simple Notes App with File Storage

A beginner-friendly Python application that allows users to create, read, update, and delete notes. All notes are persistently stored in a JSON file.

## Features

- Create new notes with titles and content
- List all saved notes
- View detailed information about a specific note
- Update existing notes
- Delete notes
- Persistent storage using JSON file
- Simple command-line interface
- Timestamp tracking for creation and updates

## How to Run

1. Make sure you have Python 3.x installed on your system
2. Clone this repository
3. Navigate to the project directory
4. Run the application:
   ```bash
   python notes_app.py
   ```

## Usage

The app provides a simple menu-driven interface with the following options:

1. Add a new note - Create a new note with a title and content
2. List all notes - See all your saved notes with their IDs and titles
3. View a note - See detailed information about a specific note
4. Update a note - Modify the title or content of an existing note
5. Delete a note - Remove a note from storage
6. Exit - Close the application

## Sample Output

```
=== Simple Notes App ===
1. Add a new note
2. List all notes
3. View a note
4. Update a note
5. Delete a note
6. Exit

Enter your choice (1-6): 1
Enter note title: Shopping List
Enter note content: 1. Milk
2. Bread
3. Eggs
Note added successfully with ID: 1

=== Simple Notes App ===
1. Add a new note
2. List all notes
3. View a note
4. Update a note
5. Delete a note
6. Exit

Enter your choice (1-6): 2
Your Notes:
1. Shopping List (Last updated: 2025-10-03 14:30:45)
```

## Implementation Details

- Uses Python's built-in `json` module for data persistence
- Implements a `NotesApp` class that handles all note operations
- Stores notes with metadata including creation and update timestamps
- Each note has a unique ID for easy reference
- Data is saved in a `notes.json` file in the same directory

## Project Structure

```
notes_app.py      # Main application file
notes.json        # Auto-generated storage file for notes
```

This is a beginner-friendly project that demonstrates:
- Basic Python programming concepts
- File handling
- JSON data format
- Object-oriented programming
- Command-line interface design
- Data persistence
