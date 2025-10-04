#Simple CLI To-Do List App

import json
import os

File = "tasks.json"

def load_task():
    if not os.path.exists(File):
        return []
    with open(File, 'r') as f:
        return json.load(f)

def save_task(tasks):
    with open(File, 'w') as f:
        json.dump(tasks, f, indent = 4)

def show_task(tasks):
    if not tasks:
        print("\nNo Tasks Yet")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "(Completed)" if task["done"] else "(Pending)"
            print(f"{i}.{task['task']}{status}")

def main():
    tasks = load_task()
    while True:
        print("\nOptions: 1.Add 2.Show 3.Done 4.Delete 5.Exit")
        choice = int(input("Enter Your Choice: "))

        if choice== 1:
            task = input("\nEnter new task: ").strip()
            tasks.append({"task": task, "done":False})
            save_task(tasks)
            print("Task added Successfully")

        elif choice == 2:
            show_task(tasks)

        elif choice == 3:
            show_task(tasks)
            num = int(input("\nEnter task number to mark as done: "))
            if 1<= num <=len(tasks):
                tasks[num-1]["done"] = True
                save_task(tasks)
                print("Marked as done")
            else:
                print("Invalid task number")

        elif choice == 4:
            show_task(tasks)
            num = int(input("Enter task number to DELETE: "))
            if 1<= num <=len(tasks):
                tasks.pop(num-1)
                save_task(tasks)
                print("Deleted the task")
            else:
                print("Invalid task number")

        elif choice == 5:
            print("Goodbye")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()