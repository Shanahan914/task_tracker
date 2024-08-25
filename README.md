# Task Tracker CLI

## Overview

**Task Tracker CLI** is a command-line tool that allows you to manage tasks easily. You can add, update, delete, and list tasks, as well as mark them as in-progress or done. The tool is designed to be simple yet powerful, making task management straightforward from the terminal.

## Features

- **Add Tasks**: Create new tasks with a description.
- **Update Tasks**: Modify the description of existing tasks.
- **Delete Tasks**: Remove tasks by their ID.
- **Mark Tasks as In-Progress or Done**: Update the status of tasks.
- **List Tasks**: View all tasks or filter them by their status (e.g., done, to-do, in-progress).
- **Aliases**: Use shorthand commands for common actions (e.g., `ls` for `list`, `del` for `delete`).

## Installation

To use the Task Tracker CLI, clone this repository and ensure you have Python 3 installed. No additional packages are required.

```bash
git clone https://github.com/yourusername/task-tracker-cli.git
cd task-tracker-cli
```
```
chmod +x task_tracker.py
```
To use in any directory:
```
export PATH="$PATH:/path/to/your/script"
```

## Actions

add <task_description>: Adds a new task with the given description.
  ```
  bash
  ./task_tracker.py add "Finish project documentation"
  ```
update <id> <new_description>: Updates the description of the task with the specified ID.
 ```
  ./task_tracker.py update 1 "Update project documentation"
```
delete <id>: Deletes the task with the specified ID.
  ```
  ./task_tracker.py delete 1
  ```
mark-in-progress <id>: Marks the task with the specified ID as in progress.
```
  ./task_tracker.py mark-in-progress 1
```
mark-done <id>: Marks the task with the specified ID as done.
```
./task_tracker.py mark-done 1
```
list: Lists all tasks with their current status.
```
./task_tracker.py list
```
list-done: Lists tasks with the status "done".
```
./task_tracker.py list-done
```
list-todo: Lists tasks with the status "todo".
```
./task_tracker.py list-todo
```
list-in-progress: Lists tasks with the status "in progress".
```
./task_tracker.py list-in-progress
```

## Data storage

### Example data structure

Key is the unique id for the task. 
```
{
  "1": {
    "description": "Finish project documentation",
    "status": "todo",
    "createdAt": "2024-08-24T17:37:41.161736",
    "updatedAt": "2024-08-24T17:37:41.161742"
  },
  "2": {
    "description": "Review project documentation",
    "status": "in progress",
    "createdAt": "2024-08-24T17:43:14.309285",
    "updatedAt": "2024-08-25T17:43:14.309295"
  }
}
```





