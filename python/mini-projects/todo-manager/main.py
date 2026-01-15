# ==============================
# ADVANCED TODO MANAGER (CLI)
# ==============================
# A menu-driven Todo Manager using
# functions, lists, dictionaries,
# and clean control flow.
# Focused on clarity, safety, and UX.
#
# ------------------------------
# TEST SCENARIOS (THINKING FIRST)
# ------------------------------
# 1. Add a task with a unique name → should be added successfully
# 2. Add a task with a duplicate name → should be rejected
# 3. View tasks when task list is empty → should show "No tasks available"
# 4. Mark a task as completed using a valid ID → status should update
# 5. Enter non-numeric input for task ID → program should not crash
# 6. Delete a task and confirm deletion → task removed and IDs refreshed
# 7. Cancel deletion when asked → task list remains unchanged
#
# These scenarios help verify system behavior
# without writing automated test code.
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

    Test cases:
    - Adding a task with a new name
    - Adding a task with an existing name
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
    Uses symbols for quick status clarity.

    Test cases:
    - Viewing tasks when list is empty
    - Viewing tasks after additions
    """
    if not task_list:
        print("📭 No tasks available.")
        return

    print("\n--- YOUR TASKS ---")
    for task in task_list:
        status_icon = "✔️" if task["status"] == "Completed" else "⏳"
        print(
            f"[{task['id']}] {task['name']} | Due: {task['due_date']} | {status_icon} {task['status']}"
        )


def refresh_task_ids():
    """
    Reassigns task IDs after deletion
    to keep IDs sequential.

    Test case:
    - Delete a task and ensure IDs are updated correctly
    """
    for index, task in enumerate(task_list):
        task["id"] = index + 1


def get_valid_task_id(prompt):
    """
    Safely gets a numeric task ID from the user.
    Prevents crashes on invalid input.

    Test cases:
    - Enter letters instead of numbers
    - Enter numbers outside valid range
    """
    user_input = input(prompt).strip()
    if not user_input.isdigit():
        print("⚠️ Please enter a valid numeric task ID.")
        return None
    return int(user_input)


def mark_task_completed():
    """
    Marks a selected task as completed.

    Test cases:
    - Mark a valid task as completed
    - Enter invalid task ID
    """
    view_tasks()
    if not task_list:
        return

    task_id = get_valid_task_id("Enter task ID to mark completed: ")
    if task_id is None:
        return

    for task in task_list:
        if task["id"] == task_id:
            task["status"] = "Completed"
            print("🎉 Task marked as completed!")
            return

    print("❌ Invalid task ID.")


def delete_task():
    """
    Deletes a task after confirmation
    and refreshes remaining IDs.

    Test cases:
    - Confirm deletion with 'y'
    - Cancel deletion with 'n'
    - Enter invalid task ID
    """
    view_tasks()
    if not task_list:
        return

    task_id = get_valid_task_id("Enter task ID to delete: ")
    if task_id is None:
        return

    for task in task_list:
        if task["id"] == task_id:
            confirm = input(
                f"Are you sure you want to delete '{task['name']}'? (y/n): "
            ).strip().lower()

            if confirm == "y":
                task_list.remove(task)
                refresh_task_ids()
                print("🗑️ Task deleted successfully!")
            else:
                print("❎ Deletion cancelled.")
            return

    print("❌ Invalid task ID.")


def show_menu():
    """
    Main menu loop controlling
    user interaction.

    Test cases:
    - Invalid menu choice
    - Exit option
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
