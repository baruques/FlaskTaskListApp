from flask import Flask, json, render_template, request
from task import Task

app = Flask(__name__)
tasks = ...

@app.post("/")
def add_task():
    data = json.loads(request.data)
    task = data.get("task")
    priority = data.get("priority", 0)
    new_task = Task(description=task, priority=priority)
    return f"Task added: {new_task}"

@app.get("/")
def index():
    return render_template("index.html")