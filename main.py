import os

todo_file = "todo.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(todo_file):
        return []
    with open(todo_file, "r") as f:
        return [line.strip() for line in f.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(todo_file, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Display menu
def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as done")
    print("5. Exit")

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Main app loop
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append("[ ] " + task)
            save_tasks(tasks)
            print("Task added.")
        elif choice == "3":
            show_tasks(tasks)
            task_no = int(input("Enter task number to remove: "))
            if 0 < task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        elif choice == "4":
            show_tasks(tasks)
            task_no = int(input("Enter task number to mark as done: "))
            if 0 < task_no <= len(tasks):
                task = tasks[task_no - 1]
                if "[X]" in task:
                    print("Task already marked as done.")
                else:
                    tasks[task_no - 1] = task.replace("[ ]", "[X]")
                    save_tasks(tasks)
                    print("Task marked as done.")
            else:
                print("Invalid task number.")
        elif choice == "5":
            print("Exiting. Bye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
