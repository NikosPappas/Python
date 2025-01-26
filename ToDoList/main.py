import json
import os
def menu():
    print(f"1. Insert task")
    print(f"2. List all task")
    print(f"3. Mark task as complete")
    print(f"4. Remove task")
    print(f"5. Exit")
tasks=[];
DATA_FILE="tasks.json"
def main():
    tasks=load_tasks()
    running=True
    while running:
        menu()
        choice=input("Enter your choice")
        match choice:
            case "1":
                add_task(tasks)
            case "2":
                list_task(tasks)
            case "3":
                mark_complete(tasks)
            case "4":
                remove_task(tasks)
            case "5":
                running=False
                save_tasks(tasks)
                print(f"Exiting To-Do List App. Goodbye!")
            case _:
                print(f"Invalid choice. Please try again.\n")
def add_task(tasks):
    description=input("Enter the description: ");
    task={"description":description,"completed":False}
    tasks.append(task)

def list_task(tasks):
    if not tasks:
        print(f"Your to-do-list is empty.")
        return
    for index,task in enumerate(tasks):
        status="[x]" if task["completed"] else "[ ]"
        print(f"{index+1}.{status} {task['description']}")
    print("")
def mark_complete(tasks):
    list_task(tasks)
    if not tasks:
        return
    try:
       task_number=int(input("Enter the number of the task to mark as complete: "))-1
       if 0<=task_number<len(tasks):
           tasks[task_number]["completed"]=True
           print(f"Task marked as complete.\n")
       else:
            print(f"Invalid task number.\n")
    except ValueError:
         print(f"Invalid task number format.\n");
def remove_task(tasks):
    list_task(tasks)
    if not tasks:
        return
    try:
        task_number=int(input("Enter the number of the task to remove: "))-1
        if 0<=task_number<len(tasks):
            remove_task=tasks.pop(task_number)
            print(f"Task '{remove_task['description']}' removed.\n")
        else:
            print(f"Invalid task number.\n")
    except:ValueError
    print("Invalid task number format.\n")
def save_tasks(tasks):
    with open(DATA_FILE,'w') as f:
        json.dump(tasks,f,indent=4)
def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE,'r') as f:
                return json.load(f)
        except json.JSONDecoderError:
            print("Error reading from file,will start empty")
            return []
    else:
        return []

if __name__=="__main__":
    print("Welcome to the To-Do List App!")
    main()
