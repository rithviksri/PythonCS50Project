# Project Title: Task Manager
# Name: Rithvik Srinivas
# GitHub Username: rithviksrinivas
# edX Username: rithviksrinivas
# City and Country: Winston-Salem, NC, USA
# Date: 07/06/2024



# Project Name: Task Manager
# Video Demo: [https://www.youtube.com/watch?v=Shx9HX4Jgbs]
# Description: Task Manager is a simple Python application that allows users to manage their tasks. Users can add, remove, and list tasks. The application saves tasks to a file and loads them on startup, ensuring persistence across sessions. At its core, Task Manager allows users to create, manage, and track tasks within a single interface. The primary goal is to provide a centralized platform where users can efficiently add new tasks, mark them as complete, remove obsolete entries, and view their entire task list at a glance. This functionality is essential for individuals seeking to prioritize and manage their workload effectively. Users can easily add new tasks to their list by entering a brief description of each task. Tasks are stored internally as dictionaries within a Python list, capturing details such as the task name and its completion status (whether done or pending). The application offers a clear and organized view of all tasks currently on the list. Each task is displayed with its corresponding status (completed or pending), enabling users to track their progress and identify tasks that require immediate attention. Once a task is finished, users have the option to mark it as complete. This feature allows for efficient task tracking and helps users stay motivated by visualizing their accomplishments over time. Tasks that are no longer relevant or necessary can be easily removed from the list. This feature ensures that the task management interface remains clutter-free and focused on current priorities. Task Manager employs JSON (JavaScript Object Notation) for data storage and retrieval. When users save their task list, the application converts the internal data structure into JSON format and writes it to a file named todo_list.json. This ensures that tasks are preserved between sessions, allowing users to seamlessly resume their task management activities upon restarting the application. The application features a simple command-line interface (CLI) where users interact by entering commands such as adding tasks, viewing the task list, marking tasks as complete, removing tasks, saving changes, and quitting the application. This user-friendly approach makes Task Manager accessible to users with varying levels of technical proficiency. Task Manager is implemented in Python, leveraging core language features and the JSON library for data serialization. The project.py file serves as the main entry point, housing the application's main function and auxiliary functions responsible for task management operations. Tests for these functions are encapsulated in the test_project.py file, ensuring the reliability and correctness of the application's core functionalities.

## Features
- Add tasks
- Remove tasks
- View tasks
- Mark tasks as complete
- Save and load tasks

# Files
- `project.py`: Contains the main function and task management functions.
- `test_project.py`: Contains tests for the task management functions.
- `requirements.txt`: To lists any external libraries required.

# Usage
1. Run `project.py` to start the application.
2. Use the menu to add, remove, mark as complete, or view tasks.
3. Use the save command to save tasks to a file.

# Testing
Run `python project.py` to execute the tests.
