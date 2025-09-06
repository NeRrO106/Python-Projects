import json
import datetime


class Note:
    def __init__(self, title, description, date = datetime.date.today()):
        self.title = title
        self.description = description
        self.date = date
    def __str__(self):
        return f"{self.title} - {self.description} on {self.date}"

class NoteManager:
    def __init__(self, filename = "notemanager.json"):
        self.notes=[]
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                file_content = file.read().strip()
                if not file_content:
                    self.notes = []
                    print("No data in file. Starting with an empty list.")
                else:
                    json_notes = json.loads(file_content)
                    self.notes = [Note(note["title"], note["description"], datetime.date.fromisoformat(note["date"])) for note in json_notes]
                    print("Notes data loaded...")
        except FileNotFoundError:
            print("No data file found. Starting with empty notes.")
        except json.JSONDecodeError:
            print("Invalid data in file. Starting with empty notes.")
            self.notes = []

    def save_data(self):
        with open(self.filename, "w") as file:
            json_notes = [{"title": note.title, "description": note.description, "date": note.date.isoformat()} for note in self.notes]
            json.dump(json_notes, file, indent=4)
        print("Note data saved...")

    def add_note(self, title, description):
        note = Note(title, description)
        self.notes.append(note)
        print(f"Note with title {title} was added successfully")

    def search_note(self, title):
        for note in self.notes:
            if title.lower() == note.title.lower():
                return note
        return None

    def edit_note(self, title):
        note = self.search_note(title)
        if note:
            print(f"Editing note: '{note}'")
            new_title = input(f"Enter new title (or press Enter to keep '{note.title}'): ") or note.title
            new_description = input(f"Enter new description (or press Enter to keep '{note.description}'): ") or note.description

            note.title = new_title
            note.description = new_description
            note.date = datetime.date.today()
            self.save_data()
            print(f"Note '{title}' has been updated.")
        else:
            print(f"Note with title '{title}' not found")
    def delete_note(self, title):
        note = self.search_note(title)
        if note:
            self.notes.remove(note)
            print(f"Note '{title}' was removed successfully")
        else:
            print(f"Note with title '{title}' was not found")
    def display_notes(self):
        if not self.notes:
            print("no notes available")
        for i, note in enumerate(self.notes, 1):
            print(f"{i}. {note}")

def main():
    manager = NoteManager()

    while True:
        print("\n--- Note Manager ---")
        print("1. Create Note")
        print("2. Edit Note")
        print("3. Delete Note")
        print("4. Display All Notes")
        print("5. Save")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            manager.add_note(title, content)
        elif choice == "2":
            old_title = input("Enter the title of the note to edit: ")
            manager.edit_note(old_title)
        elif choice == "3":
            title = input("Enter the title of the note to delete: ")
            manager.delete_note(title)
        elif choice == "4":
            manager.display_notes()
        elif choice == "5":
            manager.save_data()
        elif choice == "6":
            manager.save_data()
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
