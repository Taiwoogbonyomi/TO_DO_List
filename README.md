# **TO-DO LIST APPLICATION**
This is a simple command-line to-do list application that allows you to manage your tasks and store them in a Google Sheet using the gspread library. You can add, view, and remove tasks, with each task having a description, due date, and due time.

The program automatically syncs all inputs to Google Sheets to ensure storage of and access to the tasks inputed on the to-do list.

Visit the deployed application [here](https://to-do-l-d6f945e0296e.herokuapp.com/)
#

<img src="assets/readme/images/am-i-responsive.png" alt="Picture of the application across different devices">

#

# Table of Content

* [**Project**](<#project>)
    * [Site Users Goal](<#site-users-goal>)
    * [User Stories](<#user-stories>)
    * [Site Owners Goal](<#site-owners-goal>)

* [**User Experience (UX)**](<#user-experience-ux>)
    * 
    * [Flow chart](<#flow-chart>)
    * [Data Model](<#data-model>)

## Features
* [Welcome Screen and Instructions](#welcome-screen-and-instructions)
* [Display To-Do List](#display-to-do-list)
* [Add a Task](#add-a-task)
* [Remove a Task](#remove-a-task)
* [Verify Saved Tasks](#verify-saved-task)
* [Load and Save Tasks](#load-and-save-tasks)

* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Frameworks, Librarys & Software](<#frameworks-libraries--software>)
    * [Python Packages](<#python-packages>)

* [**Testing**](<#testing>)
  * [Code Validation](<#code-validation>)
  * [Additional Testing](<#additional-testing>)
  * [Known Bugs](<#known-bugs>)
* [Deployment](<#deployment>)
* [Credits](<#credits>)
* [Acknowledgements](<#acknowledgements>)

# **Project**

## Site Users Goal
The primary goal of users visiting the To-Do List Application site is to efficiently manage their tasks and stay organized.
- Users want to easily manage their tasks, including adding, viewing, and removing tasks.
- Users want to organize their tasks by due dates and times to prioritize their workload effectively.
- Users want their tasks to be saved and retrievable across sessions, ensuring no data is lost.
- Users want a simple and intuitive interface to manage their tasks without a steep learning curve.
 

## User Stories
1. Viewing Tasks
As a user, I want to view all my current tasks so that I can see what needs to be done.

* The application displays a list of all tasks.
* Each task includes a description, due date, and due time.
* The list is displayed when I select the option to view tasks from the menu.

2. Adding a Task
As a user, I want to add a new task to my to-do list so that I can keep track of new tasks I need to complete.

* I can enter a description, due date, and due time for the task.
* The application validates that the due date is not in the past.
* The new task is added to my list and saved to the Google Sheet.

3. Removing a Task
As a user, I want to remove a task from my to-do list so that I can keep my list updated with only relevant tasks.

* I can choose a task by its index number to remove it.
* The application asks for confirmation before removing the task.
* The task is removed from the list and the changes are saved to the Google Sheet.

4. Verifying Saved Tasks
As a user, I want to verify the tasks saved in the Google Sheet so that I can ensure my data is stored correctly.

* The application fetches and displays all tasks stored in the Google Sheet.
* Each task includes a description, due date, and due time.

5. Loading Tasks on Startup
As a user, I want the application to load my tasks from the Google Sheet when it starts so that I can see my to-do list without manually loading tasks.

* When the application starts, it automatically loads tasks from the Google Sheet.
* The tasks are available for viewing, adding, and removing.

6. Quitting the Application
As a user, I want to quit the application so that I can close it when I'm done using it.

* I can choose an option to quit the application.
* The application exits cleanly without errors.

## Site Owner's Goal
The goal of the site owners for the To-Do List Application is to provide a robust, user-friendly platform that meets the needs of users while maintaining operational efficiency and scalability.

[Back to top](<#table-of-content>)

# **User Experience**
## Flow Chart
[Lucid App](https://lucid.app/) was used in creating the flow chart for this application, the flow chart was created prior to starting the project as this give an insight into what the project entails which made writing the code easy.

<details><summary><b>Flow Chart</b></summary>

![Flow Chart]<img src="assets/readme/images/To-Do List App.png">
</details><br/>

[Back to top](<#table-of-content>)

## Data Model
To store all the tasks in the application, I used a [Google Sheet](https://www.google.com/sheets/about/). All the tasks inputed into the application are stored in the google sheet and can also be retrieved from the google sheet.

Each task in the to-do list has the following attributes:
* Description: A brief text describing the task.
* Due Date: The date by which the task is to be completed (in YYYY-MM-DD format).
* Due Time: The time by which the task is to be completed (in HH:MM format).

These attributes are represented in the Google Sheet and locally within the application.

<details><summary><b>Google Sheet</b></summary>

![Google Sheet]<img src="assets/readme/images/google-sheet.png">

The view only version of the google sheet can be viewed [here](https://docs.google.com/spreadsheets/d/1RTZ_kWXGWAtH2YPAVOANknrq1FwICjXvHEyGpnd7_HU/edit?gid=2026798872#gid=2026798872)

</details><br/>

[Back to top](<#table-of-content>)

### Typography
To ensure the readability and usability of the To-Do List application, the following typography guidelines can be adopted.
* Font: Monospaced (default terminal font)
* Style: ASCII Art for logo, bold text for headings
* Color: Default terminal color (often white on black)

[Back to top](<#table-of-content>)

## Features
### Welcome Screen and Instructions
- When the application starts, it diplays an ASCII art banner informing the users of what the application is, followed by the list of detailed instructions. 

<details><summary><b>Welcome Screen</b></summary>

<img src="assets/readme/images/welcome-screen.png">
</details><br/>


### Menu List
- The menu list option guides the users on how to use the application. It consists of 5 choices

<details><summary><b>Menu List</b></summary>

<img src="assets/readme/images/menu-list.png">
</details><br/>

### Load Task
- Loads tasks from a Google Sheet into the local application.
- Ensures that tasks are up-to-date and synchronized between the local list and the Google Sheet.

<details><summary><b>Load Task</b></summary>

<img src="assets/readme/images/load-task.png">
</details><br/>

### Display To-Do List
- Lists all tasks currently in the to-do list.
- Displays task details including description, due date, and due time.

### Add Task
- Allows users to add a new task to the to-do list.
- Prompts for task description, due date, and due time.
- Validates the input to ensure the due date and time are not in the past.
- Error messages inform users of incorrect inputs.
- Saves the new task to the Google Sheet.

<details><summary><b>Add Task</b></summary>

<img src="assets/readme/images/add-task.png">
</details><br/>

### Remove Task
- Enables users to remove a task by selecting its index from the list.
- Confirms task removal to prevent accidental deletions.
- Updates the Google Sheet to reflect the removal.


<details><summary><b>Remove Task</b></summary>

<img src="assets/readme/images/remove-task.png">
</details><br/>

### Verify Saved Task
- Reads and prints tasks currently saved in the Google Sheet.
- Provides a way to verify that tasks are correctly saved and synchronized.

<details><summary><b>Verify Saved Task</b></summary>

<img src="assets/readme/images/verify-saved-task.png">
</details><br/>

### Quit Application
- The quit application choice signifies the end of the program.

<details><summary><b>Quit Application</b></summary>

<img src="assets/readme/images/quit-application.png">
</details><br/>

### Future Features

#### Task priortization

* Allow users to assign priority levels (e.g., high, medium, low) to tasks.
* Display tasks sorted by priority to help users focus on the most important tasks first.

#### Task Categories

* Enable users to categorize tasks (e.g., work, personal, urgent).
* Filter and display tasks based on selected categories.

#### Search and Filter Task

* Implement a search feature to find tasks by keywords in the description.
* Add filtering options to view tasks by due date, due time, or priority

#### Task Completion and Progress Tracking

* Add the ability for users to mark tasks as complete.
* Track and display the percentage of completed tasks.
* Option to archive completed tasks for future reference.

#### Notifications and Reminders

* Implement email or SMS notifications to remind users of upcoming due dates and times.
* Provide in-app reminders and alerts for tasks nearing their due time.

## Technologies Used

### Languages

- [Python3](https://en.wikipedia.org/wiki/Python_(programming_language)). This provides functionality for the application.

Provided as part of Code Institute's [Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template): 
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

## Frameworks, Libraries & Software
- [Datetime](https://docs.python.org/3/library/datetime.html) - used to validate date and time inputs.
- [Google Cloud](https://cloud.google.com/) - used to generate the APIs required to connect the spreadsheets with the Python code.
- [GSpread](https://docs.gspread.org/en/v6.0.0/) - used to interact with the data in the linked sheet and used to store user input data.
- [GitHub](https://github.com/) - used to host and store and edit the project.
- [GitPod](https://gitpod.io/) - used for writing code.
- [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal in [Gitpod](https://www.gitpod.io) used to push changes to the GitHub repository. 
- [Heroku](https://dashboard.heroku.com/login) - used to host and deploy the finished project.
- [Lucidchart](https://www.lucidchart.com/pages/) - used to create the flowchart during project planning.
- [PEP8 online check](http://pep8online.com/) was used to validate the Python code.







