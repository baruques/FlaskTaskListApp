from task.task import Task
from typing import Dict


def read_tasks(filepath: str) -> Dict[str, Task]:
    tasks = {}

    try:
        with open(filepath, "r") as file:
            for line in file:
                uuid, priority, description, completed = line.strip().split(";")

                completed = completed.strip() == "True"
                task = Task(
                    description=description.strip(),
                    priority=int(priority.strip()),
                    completed=completed,
                    uuid=uuid,
                )
                tasks[task.uuid.hex] = task
    except FileNotFoundError:
        print(f"🚨 File not found: {filepath}")
        response = input("Wanna type another path? (y/n):").strip()
        if response == "y":
            filepath = input("Which?:").strip()
            return read_tasks(filepath)
        raise FileNotFoundError()

    except Exception as e:
        print(f"🚨 Failed to read file: {e}")
        response = input("Wanna try again? (y/n):").strip()
        if response == "y":
            return read_tasks(filepath)
    else:
        print(">>>✅ Tasks loaded successfully.<<<")
        return tasks


def save_tasks_on_file(filepath: str, tasks: Dict[str, Task]):
    print("dados:", len(tasks.values()))
    try:
        with open(filepath, "w") as file:
            for task in tasks.values():
                priority = task.priority
                description = task.description
                completed = task.completed
                uuid = task.uuid.hex

                file.write(f"{uuid}; {priority}; {description}; {completed}\n")
                print(f"Task saved successfully: {uuid}!")
    except Exception as e:
        print(f"🚨 Failed to write on file: {e}")
        response = input("Wanna try again? (y/n):").strip()
        if response == "y":
            save_tasks_on_file(filepath, tasks)