# Creative-002
# Simple Notepad App Code
from datetime import datetime

FILENAME = "notes.txt"


def add_note():
    note = input("Write your note: ")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILENAME, "a") as f:
        f.write(f"[{now}] {note}\n")

    print("✅ Note saved!\n")


def view_notes():
    try:
        with open(FILENAME, "r") as f:
            print("\n📒 Your Notes:\n")
            print(f.read())
    except FileNotFoundError:
        print("No notes found yet.\n")


def main():
    while True:
        print("==== SIMPLE NOTEPAD APP ====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Choose option (1-3): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice\n")


main()
