
# TO-DO LIST MANAGER

tasks = [
    {"title": "Buy groceries", "done": False},
    {"title": "Finish Python assignment", "done": True},
    {"title": "Call Ali", "done": False}
]

while True:

    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    # CREATE: Add Task
    if choice == "1":

        title = input("Enter task name: ").strip()

        if title == "":
            print("Task can't be empty")

        else:
            tasks.append({
                "title": title,
                "done": False
            })

            print("Task added successfully!")

    # READ: View Tasks
    elif choice == "2":

        print("\n===== MY TO-DO LIST =====")

        if len(tasks) == 0:
            print("No tasks yet")

        else:
            for i, task in enumerate(tasks, start=1):

                if task["done"] == True:
                    status = "[x]"
                else:
                    status = "[ ]"

                print(f"{i}. {status} {task['title']}")

            done = sum(1 for task in tasks if task["done"])
            pending = len(tasks) - done

            print(f"\nDone: {done}   Pending: {pending}")

    # UPDATE: Mark Task as Done
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks available")

        else:
            print("\n===== MY TO-DO LIST =====")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['title']}")

            try:
                number = int(input("Enter task number: "))

                if 1 <= number <= len(tasks):

                    index = number - 1
                    tasks[index]["done"] = True

                    print("Marked as done:",
                          tasks[index]["title"])

                else:
                    print("Invalid task number")

            except ValueError:
                print("Please enter a valid number")

    # DELETE: Remove Task
    elif choice == "4":

        if len(tasks) == 0:
            print("No tasks available")

        else:
            print("\n===== MY TO-DO LIST =====")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['title']}")

            try:
                number = int(input("Enter task number: "))

                if 1 <= number <= len(tasks):

                    index = number - 1
                    deleted_task = tasks.pop(index)

                    print("Deleted:", deleted_task["title"])

                else:
                    print("Invalid task number")

            except ValueError:
                print("Please enter a valid number")

    # EXIT: Show Summary
    elif choice == "5":

        done = 0
        pending = 0

        for task in tasks:

            if task["done"] == True:
                done += 1
            else:
                pending += 1

        print("\n===== TASK SUMMARY =====")
        print("Done:", done)
        print("Pending:", pending)
        print("Goodbye!")

        break

    else:
        print("Invalid choice! Please try again.")
