"""Import relevant modules for the application"""

import datetime
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
spreadsheet = GSPREAD_CLIENT.open('To-Do List')


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


def load_tasks():
    """
    This function load tasks from the spreadsheet.
    """
    global tasks
    tasks = []
    sheet = spreadsheet.sheet1
    rows = sheet.get_all_records()
    for row in rows:
        task = {
            "description": row["Description"],
            "due_date": row["Due Date"],
            "due_time": row["Due Time"]
        }
        tasks.append(task)
    print(f"Loaded {len(tasks)} tasks from the file.")


def save_tasks():
    """
    Save tasks to the spreadsheet.
    """
    print(f"Saving {len(tasks)} tasks to the file.")
    sheet = spreadsheet.sheet1
    sheet.clear()
    sheet.append_row(["Description", "Due Date", "Due Time"])
    for task in tasks:
        sheet.append_row([task["description"], task["due_date"], task["due_time"]])
    print("Tasks saved successfully.")




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
    it also ensures that the due date and time is entered correctly
    while ensuring that the due date cannot be in the past.
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


def remove_task():
    """
    Function to remove a task from the to-do list,
    This function provides the user with a prompt
    text to confirm if the task should be removed.
    """
    display_tasks()
    if tasks:
        try:
            index = int(input("Enter the number of the task to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks[index]
                confirm = input(f"Are you sure you want to remove the task '{removed_task['description']}'? (yes/no): ").lower()
                if confirm == 'yes':
                    tasks.pop(index)
                    print(f"\U0001F4ED Task '{removed_task['description']}' removed successfully.")
                    save_tasks()
                else:
                    print("\U0000274C Task removal cancelled.")
            else:
                print("\U0000274C Invalid input.")
        except ValueError:
            print("\U0000274C Invalid input. Please enter a number.")
    else:
        print("\U0001F4ED Your to-do list is already empty.")


def verify_saved_tasks():
    """
    Verify and print tasks saved in the spreadsheet.
    """
    sheet = spreadsheet.sheet1
    rows = sheet.get_all_records()
    print("Saved tasks in the file:")
    for row in rows:
        print(f"Description: {row['Description']}, Due Date: {row['Due Date']}, Due Time: {row['Due Time']}")



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