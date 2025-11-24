#task 1


#Anuja's to-do-list

import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
        
    except json.JSONDecodeError:
        print("Error reading tasks file. Starting with an empty list.")
        return []

def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
    except IOError as e:
        print(f"Error: Could not save tasks to file. {e}")

def view_tasks(tasks):
    """Prints the list of tasks to the console."""
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks):
        status = "[X]" if task['done'] else "[ ]"
        print(f"{i + 1}. {status} {task['task']}")
    print("------------------------\n")

def add_task(tasks):
    """Prompts the user to add a new task."""
    task_name = input("Enter the new task: ").strip() # Added .strip()
    if task_name:
        tasks.append({"task": task_name, "done": False})
        print(f"\nTask '{task_name}' added.")
        save_tasks(tasks)
    else:
        print("\nTask name cannot be empty.")

def mark_task_done(tasks):
    """Marks a specific task as completed."""
    view_tasks(tasks)
    if not tasks:
        return
        
    try:
        task_num_str = input("Enter the task number to mark as done: ")
        if not task_num_str:
            print("\nNo input provided.")
            return
        
        task_num = int(task_num_str)
        if 1 <= task_num <= len(tasks):
            if tasks[task_num - 1]['done']:
                print(f"\nTask {task_num} is already marked as done.")
            else:
                tasks[task_num - 1]['done'] = True
                print(f"\nTask {task_num} marked as done.")
                save_tasks(tasks)
        else:
            print("\nInvalid task number.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a specific task from the list."""
    view_tasks(tasks)
    if not tasks:
        return
        
    try:
        task_num_str = input("Enter the task number to delete: ")
        if not task_num_str:
            print("\nNo input provided.")
            return

        task_num = int(task_num_str)
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"\nTask '{removed_task['task']}' deleted.")
            save_tasks(tasks)
        else:
            print("\nInvalid task number.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

def main():
    """Main function to run the application loop."""
    tasks = load_tasks()
    
    while True:
        print("\n===== Python To-Do List Menu =====")
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nGoodbye! Your tasks are saved.")
            break
        else:
            print("\nInvalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()