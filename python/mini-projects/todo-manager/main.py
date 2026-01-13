# ==============================
# ADVANCED TODO MANAGER (CLI)
# ==============================
# A menu-driven Todo Manager using
# functions, lists, dictionaries,
# and clean control flow.
# ==============================

# Stores all tasks as dictionaries
task_list = []


def generate_task_id():
    """
    Generates a unique task ID based on
    the current number of tasks.
    """
    return len(task_list) + 1


def task_exists(task_name):
    """
    Checks if a task with the same name
    already exists (case-insensitive).
    Prevents duplicate tasks.
    """
    for task in task_list:
        if task["name"].lower() == task_name.lower():
            return True
    return False


def add_task():
    """
    Adds a new task to the task list
    after validating duplication.
    """
    task_name = input("Enter task name: ").strip()

    if task_exists(task_name):
        print("⚠️ Task already exists. Duplicate not allowed.")
        return

    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    task = {
        "id": generate_task_id(),
        "name": task_name,
        "due_date": due_date,
        "status": "Pending"
    }

    task_list.append(task)
    print("✅ Task added successfully!")


def view_tasks():
    """
    Displays all tasks in a readable format.
    """
    if not task_list:
        print("📭 No tasks available.")
        return

    print("\n--- YOUR TASKS ---")
    for task in task_list:
        print(
            f"[{task['id']}] {task['name']} | Due: {task['due_date']} | Status: {task['status']}"
        )


def refresh_task_ids():
    """
    Reassigns task IDs after deletion
    to keep IDs sequential.
    """
    for index, task in enumerate(task_list):
        task["id"] = index + 1


def mark_task_completed():
    """
    Marks a selected task as completed.
    """
    view_tasks()
    if not task_list:
        return

    task_id = int(input("Enter task ID to mark completed: "))

    for task in task_list:
        if task["id"] == task_id:
            task["status"] = "Completed"
            print("🎉 Task marked as completed!")
            return

    print("❌ Invalid task ID.")


def delete_task():
    """
    Deletes a task based on task ID
    and refreshes remaining IDs.
    """
    view_tasks()
    if not task_list:
        return

    task_id = int(input("Enter task ID to delete: "))

    for task in task_list:
        if task["id"] == task_id:
            task_list.remove(task)
            refresh_task_ids()
            print("🗑️ Task deleted successfully!")
            return

    print("❌ Invalid task ID.")


def show_menu():
    """
    Main menu loop controlling
    user interaction.
    """
    while True:
        print("\n===== TODO MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting Todo Manager. Stay productive!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


# Program entry point
show_menu()
