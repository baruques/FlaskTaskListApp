from flask import Flask, json, render_template, request
from task.task import Task
from database.db import read_tasks
app = Flask(__name__)
tasks = read_tasks("")

@app.post("/task")
def add_task():
    data = json.loads(request.data)
    new_task = Task(data["description"], data["priority"], False)
    tasks.append(new_task)
    return f"Task added: {new_task.description}"

@app.get("/")
def index():
    return render_template("index.html")