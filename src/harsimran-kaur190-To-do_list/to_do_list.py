import json,os

menu_list=["Show tasks","Add tasks","Mark tasks as completed","Delete a task","Edit a task","Show tasks by status (Pending/Completed)","Clear all completed tasks","Exit"]  

def menu():
    print("TO-DO LIST".center(62,"-"))
    for i,task in enumerate(menu_list):
        print(f"{i+1}. {task}")

# File where tasks will be stored
file_name="todo_list.json"

def open_access():
    '''Loads tasks from the JSON file if it exists, else returns an empty list.'''
    if os.path.exists(file_name):
            with open(file_name,"r") as f:
                return json.load(f)
    else:
        return []

def save_task(data):
    '''Save all tasks to the JSON file with indentation'''
    with open(file_name,"w") as f:
        json.dump(data,f,indent=4)

def show_task():
    '''Show all tasks with their status.'''
    try:
        data=open_access()
        if data:
           for i,task in enumerate(data):
                 print(f"{i+1}. {task['task']} [{task['status']}]")
        else:
            print("No task to show.")
    except json.JSONDecodeError:
        print("Task file is corrupted.")

def add_task():
    """
    Prompt the user to add a new task with 'pending' status.
    The task description must not be empty.
    """
    try:
        while True:
            task_to_add=input("Enter the task you want to add: ").strip()
            if task_to_add:
                file_existed_before = os.path.exists(file_name)# check before opening or saving
                tasks_list=open_access()
                tasks_list.append({'task':task_to_add,'status':"pending"})# load current tasks (empty list if file missing)
                save_task(tasks_list)#save updated tasks
                if not file_existed_before:
                    print(f'''NO file found. Therefore,a new json file named "{file_name}" has been created.''')
                    break
                else: 
                    print("Task has been added successfully.")
                    break
            else:
                print("Task cannot be empty.")
                continue
    except json.JSONDecodeError:
        print("Task file is corrupted.")

def mark_completed():
    '''Mark a user-selected task as completed.'''
    try:
        loaded_data=open_access()
        if loaded_data:
            for i,tasks in enumerate(loaded_data):
                    print(f"{i+1}. {tasks['task']} [{tasks['status']}]")
            while True:
                try:
                    complete=int(input("Enter the task you want to mark as completed:")) 
                    if complete in range(1,len(loaded_data)+1):
                            loaded_data[complete-1]['status']="completed"
                            save_task(loaded_data)
                            print("Task has been marked completed successfully.")
                            break
                    else:
                        print("Enter a number")
                        continue
                except ValueError:
                    print(f"Enter a number")  
                    continue              
        else:
            print("No task found to mark as completed.")
    except json.JSONDecodeError:
        print("Task file is corrupted.")

def clear_completed():
    '''Remove all tasks marked as 'completed'.'''
    try:
        data=open_access()
        if data:
            # Filter out only non-completed tasks
            updated_data=[task for task in data if task['status']!="completed"]
            save_task(updated_data)
            print("Removed all the tasks completed.")     
        else:
             print("Nothing found.")
    except json.JSONDecodeError:
        print("Task file is corrupted.")

def show_by_status():
    try:
        data=open_access()
        if data:
                # Sorting to show pending tasks before completed ones
                data.sort(key=lambda x: x['status'].lower())
                for i,task in enumerate(data): 
                    print(f"{i+1}.{task['task']} {[task['status']]}")
        else:
            print("No file found...")
    except json.JSONDecodeError:
        print("Task file is corrupted.")

def delete_task():
    '''Delete a user-selected task from the list'''
    try:
        loaded_data=open_access()
        if loaded_data:
            for i,tasks in enumerate(loaded_data):
                print(f"{i+1}. {tasks['task']} [{tasks['status']}]")
            while True:
                    try:
                        delete_data=int(input("Enter the task you want to delete: "))
                        if delete_data in range(1,len(loaded_data)+1):
                            confirm=input("Do you really want to delete this task?(Yes/No): ").strip().lower()
                            if confirm=="yes":
                                del loaded_data[delete_data-1]
                                save_task(loaded_data)
                                print(f"Task deleted successfully.")
                                break
                            else:
                                print("Task has not been deleted.")
                                break
                        else:
                            print("Enter a number.")
                            continue
                    except ValueError:
                        print("Enter a number.")
                        continue            
        else:
            print("Nothing found...")
    except json.JSONDecodeError:
        print("Task file is corrupted.")

def edit():
    '''Edit the description of a selected task.'''
    try:
        loaded_data=open_access()
        if loaded_data:
                for i,tasks in enumerate(loaded_data):
                    print(f"{i+1}. {tasks['task']} [{tasks['status']}]")
                while True:
                        try:
                            to_be_edited=int(input("Enter the task you want to edit: "))
                            if to_be_edited in range(1,len(loaded_data)+1):
                                    new_task=input("Enter the new task: ")
                                    if new_task:
                                        loaded_data[to_be_edited-1]['task']=new_task
                                        save_task(loaded_data)
                                        print(f"Task successfully edited.")
                                        break
                                    else:
                                        print("New task cannot be empty.")
                                        continue
                            else:
                                if len(loaded_data)+1 !=1:
                                    print(f"Enter a number from 1 to {len(loaded_data)+1}")
                                    continue
                                else:
                                    print("Enter 1 to select the only task available.")
                                continue
                        except ValueError:
                            print("Enter a number.")
                            continue 
        else:
            print("Nothing found...")
    except json.JSONDecodeError:
        print("Task file is corrupted.")

def main():
    while True:
        try:
            menu()
            user_choice=int(input(f"Enter your choice (1 to {len(menu_list)}):"))
            if user_choice in range(1,len(menu_list)+1):
                if user_choice==1:
                    show_task()
                elif user_choice==2:
                    add_task()
                elif user_choice==3:
                    mark_completed()
                elif user_choice==4:
                    delete_task()
                elif user_choice==5:
                    edit()
                elif user_choice==6:
                    show_by_status()
                elif user_choice==7:
                    clear_completed()
                else:
                    print("Goodbye!!!")
                    break
            else:
                print(f"Please enter a number from 1 to {len(menu_list)}")
                continue
        except ValueError:
            print(f"Please enter a number from 1 to {len(menu_list)}")
            continue

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program. Goodbye!") 