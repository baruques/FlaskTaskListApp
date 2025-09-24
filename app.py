import logging
import json
from flask import Flask, render_template, request
from task.task import Task
from database.db import read_tasks, save_tasks_on_file
import signal
import sys

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
tasks = read_tasks("./database/db.txt")

@app.post("/task")
def add_task():
    data = json.loads(request.data)

    task = Task(data["description"], data["priority"], data["completed"])
    tasks[task.uuid.hex] = task
    return json.dumps({"uuid": task.uuid.hex})

@app.get("/task/<uuid>")
def get_a_task(uuid):
    return json.dumps(tasks[uuid].to_json())

@app.get("/tasks")
def get_list_of_task():
    response = []
    for task in tasks.values():
        response.append(task.to_json())
    return response

@app.put("/task/<uuid>")
def complete_task(uuid: str):
    task = tasks[uuid]
    task.complete()
    return "200"

@app.delete("/task/<uuid>")
def delete_task(uuid: str):
    del tasks[uuid]
    return "200"

@app.get("/")
def index():
    return render_template("index.html")


def signal_handler():
    print("Ctrl+C pressed... Exiting app.")
    save_tasks_on_file("./database/db.txt", tasks)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5300)