import os
from datetime import datetime

# File to store diary entries
diary_file = 'diary.txt'

def add_entry():
    entry = input("Write your entry: ")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(diary_file, 'a') as file:
        file.write(f"{timestamp}\n{entry}\n\n")
    print("Entry added successfully!")

def view_entries():
    if os.path.exists(diary_file):
        with open(diary_file, 'r') as file:
            content = file.read()
            if content:
                print("\nYour Diary Entries:")
                print(content)
            else:
                print("Your diary is empty.")
    else:
        print("No diary entries found.")

def delete_entries():
    if os.path.exists(diary_file):
        os.remove(diary_file)
        print("All diary entries deleted successfully!")
    else:
        print("No diary entries to delete.")

def main():
    while True:
        print("\nPersonal Diary Application")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Delete All Entries")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            delete_entries()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
