from tasklist import Tasklist

def main_menu():
    print("-Tasklist-")
    print(f"Tasks to complete: {len(tasklist)}")
    print("1. Display current task")
    print("2. Display all tasks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and quit")
    choice = get_int_range("Enter choice: ", 1, 6)
    return choice

def get_int_range(prompt, min_val, max_val):
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid number.")

def get_date():
    month = get_int_range("Enter month: ", 1, 12)
    day = get_int_range("Enter day: ", 1, 31)
    year = get_int_range("Enter year: ", 2000, 2100)
    return f"{month:02d}/{day:02d}/{year}"

def get_time():
    hour = get_int_range("Enter hour: ", 0, 23)
    minute = get_int_range("Enter minute: ", 0, 59)
    return f"{hour:02d}:{minute:02d}"

tasklist = Tasklist()

while True:
    choice = main_menu()
    if choice == 1:
        current_task = tasklist.get_current_task()
        if current_task:
            print("Current task is:")
            print(current_task)
        else:
            print("All tasks are complete.")
    elif choice == 2:
        print("-Tasklist-")
        for i, task in enumerate(tasklist, start=1):
            print(f"{i}. {task}")
    elif choice == 3:
        current_task = tasklist.mark_complete()
        if current_task:
            print("Marking current task as complete:")
            print(current_task)
            new_task = tasklist.get_current_task()
            if new_task:
                print("New current task is:")
                print(new_task)
            else:
                print("All tasks are complete.")
    elif choice == 4:
        desc = input("Enter a task: ")
        date = get_date()
        time = get_time()
        tasklist.add_task(desc, date, time)
        print("-Tasklist-")
        print("Task added.")
    elif choice == 5:
        date_to_search = get_date()
        print(f"Tasks due on {date_to_search}:")
        for task in tasklist:
            if task.date == date_to_search:
                print(task)
    elif choice == 6:
        print("Saving list...")
        tasklist.save_file()
        break
