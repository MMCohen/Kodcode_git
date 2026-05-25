

def load_tasks(file_name: str) -> list:
    tasks_lst = []
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f.readline():
                task_id, task_status, task_description = line.split("|")
                temp_dict = {"id":task_id, "status": task_status, "description": task_description}
                tasks_lst.append(temp_dict)
    except FileNotFoundError as e:
        print(e)
    return tasks_lst


def save_tasks(file_name: str, tasks:list[dict]):
    with open(file_name, "a", encoding="utf-8") as f:
        for task in tasks:
            temp_line = f"{task["id"]} | {task["status"]} | {task["description"]}\n"
            f.write(temp_line)


