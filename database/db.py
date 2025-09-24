from task import task
from task.task import Task
from typing import Dict

def read_tasks(filepath: str) -> Dict[str, Task]:
    tasks = {}

    try:
        with open(filepath, "r") as file:
            for line in file:
                uuid, description, priority, completed = line.strip().split(";")

                completed = completed.strip().lower() == "true"
                new_task = Task(
                    description=description.strip(),
                    priority=int(priority.strip()),
                    completed=completed,
                    uuid=uuid.strip(),
                )
                tasks[task.uuid.hex] = new_task
    except FileNotFoundError:
        print("File not found. Want to input a new file path? (y/n):")
        user_input = input().strip().lower()
        if user_input == "y":
            new_path = input("Enter new file path: ").strip()
            return read_tasks(new_path)
        raise FileNotFoundError()
    except Exception as e:
        print(f"Error reading tasks from {filepath}: {e}")
        answer = input("Wanna try again? (y/n): ").strip().lower()
        if answer == "y":
            return read_tasks(filepath)
    else:
        print("Loaded no tasks.")
        return tasks
    
def write_tasks(filepath: str, tasks: Dict[str, Task]) -> None:
    try:
        with open(filepath, "w") as file:
            for task in tasks.values():
                line = f"{task.id}; {task.priority}; {task.description}; {task.completed}\n"
                file.write(line)
    except Exception as e:
        print(f"Error writing tasks to {filepath}: {e}")
        raise e
