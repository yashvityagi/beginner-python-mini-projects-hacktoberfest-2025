import os
import json
from datetime import datetime

class NotesApp:
    def __init__(self, storage_file="notes.json"):
        self.storage_file = storage_file
        self.notes = self.load_notes()

    def load_notes(self):
        """Load notes from the storage file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        return []

    def save_notes(self):
        """Save notes to the storage file."""
        with open(self.storage_file, 'w') as f:
            json.dump(self.notes, f, indent=2)

    def add_note(self, title, content):
        """Add a new note."""
        note = {
            'id': len(self.notes) + 1,
            'title': title,
            'content': content,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.notes.append(note)
        self.save_notes()
        return note['id']

    def get_all_notes(self):
        """Get all notes."""
        return self.notes

    def get_note(self, note_id):
        """Get a specific note by ID."""
        for note in self.notes:
            if note['id'] == note_id:
                return note
        return None

    def update_note(self, note_id, title=None, content=None):
        """Update an existing note."""
        for note in self.notes:
            if note['id'] == note_id:
                if title:
                    note['title'] = title
                if content:
                    note['content'] = content
                note['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_notes()
                return True
        return False

    def delete_note(self, note_id):
        """Delete a note by ID."""
        for i, note in enumerate(self.notes):
            if note['id'] == note_id:
                del self.notes[i]
                self.save_notes()
                return True
        return False

def main():
    app = NotesApp()
    
    while True:
        print("\n=== Simple Notes App ===")
        print("1. Add a new note")
        print("2. List all notes")
        print("3. View a note")
        print("4. Update a note")
        print("5. Delete a note")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            note_id = app.add_note(title, content)
            print(f"Note added successfully with ID: {note_id}")
            
        elif choice == '2':
            notes = app.get_all_notes()
            if not notes:
                print("No notes found!")
            else:
                print("\nYour Notes:")
                for note in notes:
                    print(f"{note['id']}. {note['title']} (Last updated: {note['updated_at']})")
                    
        elif choice == '3':
            note_id = int(input("Enter note ID to view: "))
            note = app.get_note(note_id)
            if note:
                print(f"\nTitle: {note['title']}")
                print(f"Content: {note['content']}")
                print(f"Created: {note['created_at']}")
                print(f"Last Updated: {note['updated_at']}")
            else:
                print("Note not found!")
                
        elif choice == '4':
            note_id = int(input("Enter note ID to update: "))
            title = input("Enter new title (press Enter to skip): ")
            content = input("Enter new content (press Enter to skip): ")
            if app.update_note(note_id, title or None, content or None):
                print("Note updated successfully!")
            else:
                print("Note not found!")
                
        elif choice == '5':
            note_id = int(input("Enter note ID to delete: "))
            if app.delete_note(note_id):
                print("Note deleted successfully!")
            else:
                print("Note not found!")
                
        elif choice == '6':
            print("Thank you for using Simple Notes App!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
