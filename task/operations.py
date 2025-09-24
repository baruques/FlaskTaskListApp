from task.display import display_tasks
from task.task import Task
from typing import List


def add_task(tasks: List[Task]):
    description = input("Task description: ").strip()

    priority = input("What is this task priority? (1,2,3): ").strip()
    while priority not in ["1", "2", "3"]:
        print("Invalid priority. Please enter 1, 2, or 3.")
        priority = input("What is this task priority? (1,2,3): ").strip()

    task = Task(description=description, priority=priority)
    tasks.append(task)

    print("\n>>>Task successfully added<<<")


def remove_task(tasks: List[Task]):
    if len(tasks) == 0:
        print("\n>>>No tasks available<<<")

    display_tasks(tasks)
    index = int(input("Task number to remove: ")) - 1

    if 0 <= index < len(tasks):
        del tasks[index]

        print("\n>>>Task successfully removed<<<")
    else:
        print("\n>>>Invalid task number<<<")


def complete_task(tasks: List[Task]):
    if len(tasks) == 0:
        print("\n>>>No tasks available<<<")

    display_tasks(tasks)
    index = int(input("Task number to complete: ")) - 1

    if 0 <= index < len(tasks):
        tasks[index].complete()

        print("\n>>>✅ Task successfully completed<<<")
    else:
        print("\n>>>Invalid task number<<<")