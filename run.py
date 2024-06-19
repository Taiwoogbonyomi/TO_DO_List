"""Import relevant modules for the application"""

import datetime
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('To-Do List')


# This is an empty list to store tasks
tasks = []

def display_instructions():
    """
    Function to print out the to-do list instructions and menu,
    then wait for the user input before calling the appropriate
    function. 

    """
    print("""
    ===== To-Do List Instructions =====
    You can manage your tasks with the following options:
    1. Display to-do list : View all tasks currently in the list.
    2. Add a task : Enter a new task to add to your to-do list.
    3. Remove a task : Choose a task by its index to remove the task from your list.
    4. Verify saved tasks: Verify and print tasks saved on the to-do list.
    5. Quit : Exit the application.
    =====================================
    """)







def main():
    """
    Main function to run the to-do list application.
    """
    display_instructions()
    print("\U0001F4CB Welcome to the to-do list application \U0001F4CB")

    while True:
        print("\n === To-Do List Menu ===")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Verify saved tasks")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            verify_saved_tasks()
        elif choice == "5":
            print("Quitting application...")
            print("Goodbye \U0001F44B \U0001F44B")
            break
        else:
            print("\U0000274C Invalid choice, please enter a number from 1 to 5.")

# Run the main function to start the application
if __name__ == "__main__":
    main()