import os
import json
from datetime import datetime

def addTask(tasks, description, due_date, priority):
    tasks.append({"description": description, "due_date": due_date, "priority": priority})

def viewTask(tasks):
    if not tasks:
        print("No tasks found")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['description']} - Due Date: {task['due_date']} - Priority: {task['priority']}")

def deleteTask(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        print("Task deleted permanently")
    else:
        print("Invalid Task Index")

def saveTask(tasks, filepath):
    try:
        with open(filepath, 'w') as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def loadTask(filepath):
    tasks = []
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                tasks = json.load(f)
        except Exception as e:
            print(f"Error loading tasks: {e}")
    return tasks

def searchTask(tasks, keyword):
    results = [task for task in tasks if keyword.lower() in task['description'].lower()]
    return results

def sortTasks(tasks, by):
    if by == 'date':
        tasks.sort(key=lambda x: datetime.strptime(x['due_date'], '%Y-%m-%d'))
    elif by == 'priority':
        tasks.sort(key=lambda x: x['priority'])

def main():
    tasks = []
    filepath = "tasks.json"
    tasks = loadTask(filepath)

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Task")
        print("3. Delete Task")
        print("4. Search Task")
        print("5. Sort Tasks by Due Date")
        print("6. Sort Tasks by Priority")
        print("7. Exit")
        choice = input("Enter your Choice (1/2/3/4/5/6/7): ")
        
        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            priority = input("Enter Priority (low/medium/high): ").lower()
            addTask(tasks, description, due_date, priority)
            saveTask(tasks, filepath)
        
        elif choice == "2":
            viewTask(tasks)
        
        elif choice == "3":
            viewTask(tasks)
            try:
                task_index = int(input("Enter the task index to delete: "))
                deleteTask(tasks, task_index)
                saveTask(tasks, filepath)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "4":
            keyword = input("Enter keyword to search for: ")
            results = searchTask(tasks, keyword)
            viewTask(results)
        
        elif choice == "5":
            sortTasks(tasks, 'date')
            viewTask(tasks)
        
        elif choice == "6":
            sortTasks(tasks, 'priority')
            viewTask(tasks)
        
        elif choice == "7":
            print("Exiting the program")
            break
        
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
