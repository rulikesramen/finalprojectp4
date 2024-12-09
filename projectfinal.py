# Helper function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task, status in tasks.items():
            print(f"{task}: {'Completed' if status else 'Pending'}")

# Function to add a task to the list
def add_task(tasks):
    task_name = input("Enter the task name: ")
    tasks[task_name] = False  # Default is False (Pending)

# Function to mark a task as completed
def complete_task(tasks):
    task_name = input("Enter the task name to mark as completed: ")
    if task_name in tasks:
        tasks[task_name] = True
        print(f"Task '{task_name}' marked as completed.")
    else:
        print("Task not found.")

# Function to delete a task
def delete_task(tasks):
    task_name = input("Enter the task name to delete: ")
    if task_name in tasks:
        del tasks[task_name]
        print(f"Task '{task_name}' deleted.")
    else:
        print("Task not found.")

# Main function to control the flow of the to-do list
def main():
    tasks = {}  # Data structure (dictionary)
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            complete_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            print("Exiting To-Do List App.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
main()
