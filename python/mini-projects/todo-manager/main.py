# ADVANCED TODO MANAGER - MINI PROJECT

tasks = []


def generate_id():
    return len(tasks) + 1


def task_exists(task_name):
    for task in tasks:
        if task["name"].lower() == task_name.lower():
            return True
    return False


def add_task():
    name = input("Enter task name: ").strip()

    if task_exists(name):
        print("⚠️ Task already exists. Duplicate not allowed.")
        return

    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    task = {
        "id": generate_id(),
        "name": name,
        "due": due_date,
        "status": "Pending"
    }

    tasks.append(task)
    print("✅ Task added successfully!")


def view_tasks():
    if not tasks:
        print("📭 No tasks available.")
        return

    print("\n--- YOUR TASKS ---")
    for task in tasks:
        print(
            f"[{task['id']}] {task['name']} | Due: {task['due']} | Status: {task['status']}")


def fix_task_ids():
    for index, task in enumerate(tasks):
        task["id"] = index + 1


def mark_completed():
    view_tasks()
    if not tasks:
        return

    task_id = int(input("Enter task ID to mark completed: "))

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            print("🎉 Task marked as completed!")
            return

    print("❌ Invalid task ID.")


def delete_task():
    view_tasks()
    if not tasks:
        return

    task_id = int(input("Enter task ID to delete: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            fix_task_ids()
            print("🗑️ Task deleted successfully!")
            return

    print("❌ Invalid task ID.")


def menu():
    while True:
        print("\n===== TODO MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting Todo Manager. Stay productive!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


menu()
