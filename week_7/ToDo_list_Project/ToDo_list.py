

def load_tasks(file_name: str) -> list:
    tasks_lst = []
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                task_id, task_status, task_description = line.strip().split("|")
                temp_dict = {"id":task_id, "status": task_status, "description": task_description}
                tasks_lst.append(temp_dict)
    except FileNotFoundError as e:
        print(e)
    return tasks_lst


def save_tasks(file_name: str, tasks:list[dict], mode = "a"):
    with open(file_name, mode, encoding="utf-8") as f:
        for task in tasks:
            temp_line = f"{task["id"]}|{task["status"]}|{task["description"]}\n"
            f.write(temp_line)


def add_task(file_name, description):
    old_tasks = load_tasks(file_name)
    next_id = int(old_tasks[-1]["id"]) + 1
    temp_line = f"{next_id}|pending|{description}\n"

    with open(file_name, "a", encoding="utf-8") as f:
        f.write(temp_line)

def complete_task(file_name, task_id):
    all_tasks = load_tasks(file_name)
    change_task = False
    for task in all_tasks:
        if task["id"] == task_id:
            task["status"] = "DONE"
            change_task = True
    if change_task:
        save_tasks(file_name, all_tasks, "w")
    else:
        print("id does not exist!")


def list_tasks(file_name):
    lst_tasks = load_tasks(file_name)
    for task in lst_tasks:
        line = f"{task["id"]} | {task["status"]} | {task["description"]}"
        print(line)


def main():
    FILENAME = "tasks.txt"
    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Show all tasks")
        print("2. add task")
        print("3. Mark Task as 'done'")
        print("4. Exit")

        user_choice = input("\nEnter your choice: ")

        match user_choice:
            case "1":
                list_tasks(FILENAME)
            case "2":
                task_description = input("add task description: ")
                add_task(FILENAME, task_description)
                print("adding task complete!")
            case "3":
                task_id = input("enter task id: ")
                complete_task(FILENAME, task_id)
            case "4":
                print("good by!")
                break
            case _:
                print("incorrect choice!\n please try again!")

if __name__ == "__main__":
    main()