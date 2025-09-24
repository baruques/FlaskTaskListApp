from task.task import Task
from typing import List

def display_tasks(tasks: List[Task]) -> None:
    if len(tasks) == 0:
        print("No tasks to display.")

    for task in tasks:
        status = "✓" if task.completed else "✗"
        print(f"[{status}] {task.description} (Priority: {task.priority})")
    print(f"Total tasks: {len(tasks)}")