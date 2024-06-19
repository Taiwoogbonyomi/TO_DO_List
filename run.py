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


def display_tasks():
    """
    This function displays the tasks added by the user
    to the to-do list. The due date and time is also displayed 
    which shows the user the tasks in order of their priority.
    """
    if not tasks:
        print("\U0001F4ED Your to-do list is empty.")
    else:
        print("\U0001F4CB Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['description']} - Due: {task['due_date']} {task['due_time']}")


def add_task():
    """
    This function allows a user to add a task to the to-do list,
    it also ensures that the due date and time is while ensuring 
    that the due date cannot be in the past.
    """
    description = input("Enter task description: ").strip()
    if not description:
        print("\U0000274C Task description cannot be empty. Please enter a valid description.")
        return

    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ")
        due_time = input("Enter due time (HH:MM): ")
        try:
            due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            due_time_obj = datetime.datetime.strptime(due_time, "%H:%M").time()
            if due_date_obj < datetime.date.today():
                print("\U0000274C Due date cannot be in the past. Please enter a valid date.")
                continue
            break
        except ValueError:
            print("\U0000274C Invalid date or time format. Please try again.")

    task = {
        "description": description,
        "due_date": due_date,
        "due_time": due_time
    }

    tasks.append(task)
    print(f"\U00002705 Task '{description}' added to your to-do list.")
    save_tasks()




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