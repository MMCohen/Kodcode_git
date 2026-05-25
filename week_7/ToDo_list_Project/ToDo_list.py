

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




